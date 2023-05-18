import requests
from django.http import HttpResponse
import re
from bs4 import BeautifulSoup


def proxy_view(request):

    if 'id' in request.GET:
        return proxy_view_news(request)

    url = f'https://news.ycombinator.com{request.path}'
    response = requests.get(url)
    return HttpResponse(response.text)

def proxy_view_news(request):
    item_id = request.GET['id']
    url = f'https://news.ycombinator.com/item?id={item_id}'
    response = requests.get(url)
    content_type = response.headers.get('content-type', 'text/html')
    response_text = response.text
    text = modify_html(response_text)
    return HttpResponse(text, content_type=content_type)


def modify_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all(text=re.compile(r'\b\w{6}\b')):
        modified_text = re.sub(r'\b\w{6}\b', lambda match: match.group(0) + '™', tag.string)
        tag.string.replace_with(modified_text)
    return str(soup)
