import urllib.request

url = 'https://www.yahoo.co.jp/'
conn = urllib.request.urlopen(url)
print(conn.status)
print('-' * 30)
for key, value in conn.getheaders():
    print(key, value)

url = 'https://httpbin.org'
conn = urllib.request.urlopen(url)
print(conn.read().decode('utf-8'))
