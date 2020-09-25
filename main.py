from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, re, os, configparser
from tools import log as lo, save_csv, write
from func import func_dict
from datetime import datetime
from selenium.webdriver.common.keys import Keys

config = configparser.ConfigParser()
config.read('s.conf')

args_urls = config['urls']
URLS = [ x for x in args_urls.values() ]

args_site = config['conf']
TIMEOUT  = int( args_site['timeout'] )
HEADLESS = int( args_site['headless'] )


log = lo("main", "main.log")
PATH = os.getcwd()

def chrome_browser():
    co = Options()
    userAgent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
    co.add_argument('user-agent={}'.format(userAgent))
    if HEADLESS:
        co.add_argument('--headless')
    co.add_argument('--no-sandbox')
    co.add_argument('--disable-dev-shm-usage')
    co.add_argument("--mute-audio")
    # disable infobars
    co.add_argument('--disable-infobars')

    co.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    chrome_prefs = {}
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}
    co.add_experimental_option("prefs", chrome_prefs)
    chrome_path = os.path.join(PATH, "chromedriver")
    driver = webdriver.Chrome(chrome_path, chrome_options=co)
    return driver

driver = chrome_browser()

def _main():

    names = list(map( lambda x : re.findall(r"https:\/\/(?:www\.)?(.*?)\/", x)[0], URLS ))
    ctime = datetime.now().strftime("%Y-%m-%d_%H_%M")
    NAME = "Tennis-" + ctime + ".xlsx"
    FULL_PATH = os.path.join(PATH, "data" ,NAME)
    write( FULL_PATH, names )

    log.info("Chrome browser opening")
    driver.get( URLS[0] )


    for url in URLS:
        driver.execute_script("window.open('{}');".format( url ))
        time.sleep(2.5)


    driver.switch_to.window(driver.window_handles[0])
    driver.close()

    for e,tab in enumerate(driver.window_handles):

        driver.switch_to.window(tab)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        time.sleep(4)
        log.info("%d to go", len(driver.window_handles) - e)


    log.info("Start!!!")
    time.sleep(10)
    while True:
        temp = []
        for tab in driver.window_handles:

            driver.switch_to.window(tab)
            html = driver.page_source
            domain = driver.execute_script("return window.location.hostname")

            for key, func in func_dict.items():
                if key in domain:
                    result = func(html)
                    temp.append(  result )
                    log.info("Domain: %s Result: %s", domain , result)
        write( FULL_PATH ,temp )
        log.info("====== Sleep: %s ======", TIMEOUT)
        time.sleep(TIMEOUT)

def main():
    try:
        _main()
    except KeyboardInterrupt:
        driver.quit()


if __name__ == '__main__':
    main()