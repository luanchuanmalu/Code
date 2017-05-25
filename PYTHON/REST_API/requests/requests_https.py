
import requests

r = requests.get('https://api.github.com/events')
print r.json()
print r.headers
print r.headers['Content-Type']
print r.headers.get('content-type')

def requests_method():
    url = 'https://api.github.com/some/endpoint'
    payload = {'some': 'data'}
    r = requests.post(url, data=json.dumps(payload))
    print r.json()

    requests.get(‘https://github.com/timeline.json’) #GET请求
    requests.post(“http://httpbin.org/post”) #POST请求
    requests.put(“http://httpbin.org/put”) #PUT请求
    requests.delete(“http://httpbin.org/delete”) #DELETE请求
    requests.head(“http://httpbin.org/get”) #HEAD请求
    requests.options(“http://httpbin.org/get”) #OPTIONS请求

    #https的证书问题  解决放方法
    ret = requests.get(url, verify="/tmp/ssl/52.77.252.184.crt") #指定证书信任
    ret = requests.get(url, verify=False) #不验证证书
    #解决方法2：
    #设置环境变量 REQUESTS_CA_BUNDLE:
    #export REQUESTS_CA_BUNDLE=/tmp/ssl/52.77.252.184.crt
