import urllib.request

url = 'http://www.yahoo.co.jp/'
ua = 'Mozilla/5.0 (Macintosh; Intel MacOS X 10_12_3) '\
     'AppleWebkit/537.36 (KHTML, like Gecko) '\
     'Chrome/55.0.2883.95 Safari/537.36 '

req = urllib.request.Request(url, headers={'User-Agent': ua})
try:
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body)
except urllib.error.HTTPError as ERR:
    print(ERR.code)
except urllib.error.URLError as ERR:
    print(ERR.reason)