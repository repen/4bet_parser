import os, zipfile
import urllib.request

APP_DIR = os.getcwd()

def download_url(url, save_path):
    with urllib.request.urlopen(url) as dl_file:
        with open(save_path, 'wb') as out_file:
            out_file.write(dl_file.read())

def unzip(path):
    with zipfile.ZipFile(path, 'r') as zip_ref:
        zip_ref.extractall( APP_DIR )


cmd1 = "pip install selenium"
cmd2 = "pip install openpyxl"
cmd3 = "pip install bs4"
cmds = [cmd1, cmd2, cmd3]


for x in cmds:
    os.system(x)

# os.system("python test.py")
# 
# url = "https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_win32.zip"
url = "https://chromedriver.storage.googleapis.com/85.0.4183.87/chromedriver_linux64.zip"
zip_webdriver = os.path.join(APP_DIR, "chromedriver.zip" )
download_url( url, zip_webdriver )
unzip( zip_webdriver )
os.chmod(os.path.join(APP_DIR, "chromedriver"), 0o775)
# os.chmod(os.path.join(APP_DIR, "chromedriver.exe"), 0o775)