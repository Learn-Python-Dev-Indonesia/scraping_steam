
import requests
from bs4 import BeautifulSoup

url = 'https://indeed.com/jobs?'
params = {
    'q': 'python developer',
    'l': 'Jakarta',
    'from': 'searchOnHP',
    'vjk': 'b287232987f71d31',
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}
res = requests.get(url, params=params, headers=headers)
print(res.status_code)
