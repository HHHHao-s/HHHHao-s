import os
import json
from multiprocessing.dummy import Pool as pl
import tkinter.filedialog
from multiprocessing.dummy import Pool
import requests
from lxml import html

etree = html.etree

class Main():
    def __init__(self) -> None:
        self.headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
        ,'upgrade-insecure-requests': '1'
        ,'cookie': '_ga=GA1.2.210270941.1585231709; lang_set=zh; __tea_sdk__ssid=d7862ddc-7e11-4cd9-ab8a-46a28c5c2b1a; tt_webid=6973632808560379406; passport_csrf_token_default=079117db0687e7f73268db7b9d7c0ffa; passport_csrf_token=079117db0687e7f73268db7b9d7c0ffa; passport_auth_status=6f7c999465d344789168ea1e64fc10ab%2C; passport_auth_status_ss=6f7c999465d344789168ea1e64fc10ab%2C; n_mh=RQqalLvHWCqPHJh_AOQ7RxKA_KdARY-CzU2BtwYZb7s; MONITOR_WEB_ID=0a016a3d-2d10-489e-abf7-1ec8934c6709; MONITOR_WEB_ID=0a016a3d-2d10-489e-abf7-1ec8934c6709; mobile_set=no; s_v_web_id=kpxeeik4_4VhguPdy_0A27_4d9g_BNy0_BaQ2H3o4C5O2; mobile_set=no; PHPSESSID=5c7bc7d3fee6a09e1c1a5b420c1bbc67; _csrf_token=5124e04562f6afb08391b02ac29ce577; Hm_lvt_330d168f9714e3aa16c5661e62c00232=1623675422,1623722416,1623736959; Hm_lpvt_330d168f9714e3aa16c5661e62c00232=1623736974'
        }
        self.urls = []
        
            
    def geturl(self,url):
        try:
            a = json.loads(requests.get(url,headers=self.headers).text)
            for y in a['data']['items']:
                for x in y['item_detail']['image_list']:
                    self.urls.append(x['path'].split('/')[-1].split('~')[0])
            
        except:
            pass
        
    
    def download(self,id):
        name = id + '.png'
        try:
            url = 'https://p9-bcy.byteimg.com/img/banciyuan/{}~tplv-banciyuan-w650.image'.format(id)
            p = requests.get(url)
            f = open(name,'wb')
            f.write(p.content)
            f.close()
            print(name)
        except:
            pass
        
if __name__ == '__main__':
    os.chdir(tkinter.filedialog.askdirectory())
    flag = 1
    while flag:
        for i in range(10):
            m = Main()# 492 -->jk, 416 --> 汉服 
            m.geturl('https://www.bcy.net/apiv3/common/circleFeed?circle_id=492&since=rec:2&sort_type=1&grid_type=10&_signature=W.26YAAgEBG3wcFSaMcYhVv9unAADs5')
            pool = Pool()
            pool.map(m.download,m.urls)
        try:
            flag = int(input('是否继续(0/1):'))
        except:
            pass
    pool.close()
    pool.join()
    
    
    
    
    