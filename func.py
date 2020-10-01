from bs4 import BeautifulSoup
import re


def marathon(html):
    value = "-"
    soup = BeautifulSoup(html, "html.parser")
    result = soup.find('div', text = re.compile('Тотал сетов'), attrs = {'class' : 'name-field'})
    if result:
        koef = result.parent.parent.parent.parent.parent.select_one('span[data-selection-key*="Total_Sets.Under_2.5"]')
        if koef:
            value = koef.text.strip()
            
    return str(value).strip()

def betcity(html):
    value = "-"
    soup = BeautifulSoup(html, "html.parser")
    result = soup.find('span', text = re.compile('Тотал по сетам'))
    if result:
        koef = re.findall( r"\d\.\d{1,4}", str(result.parent.parent))
        if koef:
            if len(koef) > 2: 
                value = koef[1]

    return str(value).strip()

def ligastavok(html):
    value = "-"
    soup = BeautifulSoup(html, "html.parser")
    result = soup.find('span', text = re.compile('Тотал сетов'))
    if result:
        res = re.findall(r"\d\,\d{1,4}", str(result.parent.select_one('div[title*="мен"]')))
        if res:
            value = res[0]

    return str(value).replace(",", ".").strip()
    

def xbet(html):
    value = "-"
    soup = BeautifulSoup(html, "html.parser")
    result = soup.find(text = re.compile('Тотал по сетам точный'))
    if result:
        # import pdb;pdb.set_trace()
        res = re.findall(r"\d\.\d{1,4}", str(result.parent.parent.find(text=re.compile('^2\n')).parent.parent ) )
        if res:
            value = res[0]

    return str(value).strip()

func_dict = {
    "1xstavka" : xbet,
    "betcity":betcity,
    "marathon":marathon,
    "ligastavok":ligastavok
}