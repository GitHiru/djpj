"""djpj URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #edit
from django.conf import settings #add:media
from django.conf.urls.static import static #add:media
# from django.contrib.staticfiles.urls import static #add:開発モード時静的ファイルを配信
from .feeds import LatestPostsFeed #add:feed(rss)
from django.contrib.sitemaps.views import sitemap #add:sitemap
from .sitemaps import DiaryPostSitemap, StaticViewSitemap #add:sitemap

#add:sitemap
sitemaps = {
    'diary': DiaryPostSitemap,
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')), #add:app
    path('latest/feed/', LatestPostsFeed()), #add:feed(rss)
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'), #add:sitemap
]

#add:media
# https://docs.djangoproject.com/ja/2.2/howto/static-files/#serving-files-uploaded-by-a-user-during-development
if not settings.DEBUG: # =True
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
