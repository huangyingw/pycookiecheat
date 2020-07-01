from pycookiecheat import chrome_cookies
import requests

url = 'https://api.imvu.com/login/me/'

# Uses Chrome's default cookies filepath by default
cookies = chrome_cookies(
    url, cookie_file='/Users/huangyingw/Library/Application Support/Google/Chrome/Default/Cookies')
r = requests.get(url, cookies=cookies)
print('r --> %s' % r)
