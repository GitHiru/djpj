from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from diary.models import Post


class DiaryPostSitemap(Sitemap):
    """
    ブログ記事のサイトマップ
    🔗https://www.sitemaps.org/ja/protocol.html
    """
    changefreq = "never"
    priority   = 0.8

    def items(self):
        return Post.objects.filter(is_public=True)

    def location(self, obj):
        return reverse('diary:post_detail', args=[obj.pk])

    def lastmod(self, obj):
        return obj.published_at


class StaticViewSitemap(Sitemap):
    """
    静的ページのサイトマップ
    """
    changefreq = "daily"
    priority   = 0.5

    def items(self):
        return ['diary:index', 'diary:category_list', 'diary:tag_list']

    def location(self, item):
        return reverse(item)
