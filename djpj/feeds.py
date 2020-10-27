from django.contrib.syndication.views import Feed
from django.urls import reverse
from diary.models import Post


class LatestPostsFeed(Feed):
    title = "djpj 最新ブログ記事"
    link = "/"
    description = "djpj のブログ記事に関する最新情報。"

    def items(self):
        return Post.objects.order_by('-published_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('diary:post_detail', args=[item.pk])
