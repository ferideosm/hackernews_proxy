
from proxy.views import proxy_view, proxy_view_news
from django.urls import path, re_path

# urlpatterns = [
#     path('', proxy_view, name='proxy'),
# ]

urlpatterns = [
    re_path(r'^', proxy_view, name='proxy'),
]