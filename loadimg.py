import requests
import re
import time

referurl = ''
index = 0
with open('./神兵玄奇F.html', 'r') as f:
    for i in f:
        
        reg = re.search('src="(.*)"', i)
        if reg:
            
            imgurl = reg.groups()[0]
            headers = {
                'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36',
                'Referer' : referurl
            }
            # print(headers)
            name_reg = re.search(r'\/([^/]+.jpg)\?',imgurl)
            if name_reg:
                name = name_reg.groups()[0]
                
                img_path = './shenbingxuanqiF/'+str(index)+ "_" +name
                
                while True:
                    try:
                        print(img_path)
                        r = requests.get(imgurl,headers=headers)
                        break
                    except:
                        continue

                with open(img_path, 'wb') as ir:
                    ir.write(r.content)
                with open('./神兵玄奇FF.html', 'a') as f1:
                    text = '<img src="{}"/>'.format(img_path)
                    f1.write('{}\n'.format(text))
                # break
        else:
            with open('./神兵玄奇FF.html', 'a') as f1:
                f1.write(i)
            # print(i)
            index += 1
            referurl = re.search('href\s?=\s?"(.*)"',i).groups()[0]
            print(referurl)