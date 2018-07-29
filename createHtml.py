import requests
from lxml import etree
import re
import execjs

def get_id(url):
    pattern = r'/vol\d+-(\d+)/'
    reg = re.search(pattern, url)
    
    id = reg.groups()[0]
    print(id)
    return int(id)

def getHua(url):
    r = requests.get(url)
    # print(r.text)
    html = etree.HTML(r.text)
    content = html.xpath('//ul/li/a/@href')
    print(content)
    pattern = r'/vol\d+-(\d+)/'
    huaurl_list = []
    for c in content:
        reg = re.match(pattern, c)
        if reg:
            id = reg.groups()[0]
            huaurl = 'http://m.1kkk.com' + c
            # print(c, id)
            huaurl_list.append(huaurl)
    huaurl_list.sort(key=get_id)
    return huaurl_list       

if __name__ == "__main__":
    # url = 'http://www.1kkk.com/manhua3744/'
    # url = 'http://www.1kkk.com/manhua3745/'
    # url = 'http://www.1kkk.com/manhua3746/'
    # url = 'http://www.1kkk.com/manhua3747/'
    # url = 'http://www.1kkk.com/manhua3748/'
    # url = 'http://www.1kkk.com/manhua3754/'
    # url = 'http://www.1kkk.com/manhua7235/'
    # url = 'http://www.1kkk.com/manhua2690/'
    # url = 'http://www.1kkk.com/manhua2455/'
    url = 'http://www.1kkk.com/manhua2706/'
    huaurl_list = getHua(url)
    print(huaurl_list)
    ß
    for index,huaurl in enumerate(huaurl_list):
        r = requests.get(huaurl)
        
        pattern = 'eval(.*)'
        reg = re.search(pattern,r.text)
        text = reg.groups()[0]
        newImg = execjs.eval(text)
        pattern = r'\'(.*?)\''
        img_list = re.findall(pattern, newImg)
        
        with open('神兵玄奇F.html', 'a') as f:
            f.write('<h6 ><a href = "{}">第{}章<a></h6>\n'.format(huaurl, index+1))
        for img in img_list:
            text = '<img src="{}"/>'.format(img)
            with open('神兵玄奇F.html', 'a') as f:
                f.write(text+'\n')
    
        