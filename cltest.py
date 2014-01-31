#!/usr/bin/env python
import urllib.request
import urllib.parse

user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25"
check_url = 'http://wo.yao.cl/register.php'
alphabeta = [chr(x+ord('a')) for x in range(26)]
digi = [chr(x+ord('0')) for x in range(10)]

begin_code = ['92b7040**dbbc19c']

def BuildReq(url,data):
    req = urllib.request.Request(url,data)
    req.add_header('User-Agent',user_agent)
    return req

def BuildCode(begin_code,end):
    codes = []
    for code in begin_code:
        for letter in alphabeta:
            codes.append(code[0:end]+letter+code[end+1:])
        for data in digi:
            codes.append(code[0:end]+data+code[end+1:])
    return codes
def CheckCode(code):
    data =  {
             'reginvcode' : code,
             'action' : 'reginvcodeck'
             }
    data = urllib.parse.urlencode(data)
    data = data.encode('utf-8')
    req = BuildReq(check_url,data)
    resp = urllib.request.urlopen(req).read()
    
    if "retmsg_invcode('1')" in resp.decode('utf-8'):
        return 0
    else:
        print('OK!')
        return 1
   

if __name__ == '__main__':
    fp = open('code.txt','a')
    end = [7,8]
    num = len(end)
    
    codes = begin_code
    for i in range(num):
        codes = BuildCode(codes,end[i])
    i = 0
    for code in codes:
        result = CheckCode(code)
        if result == 1:
            fp.write(code)
            print(code,'ok')
        i += 1
        print(i,'Codes checked!')

    



