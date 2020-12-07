"""
Djangoには独自コマンドを作ってmanage.pyのコマンドとして実行することができる。
バックアップ用のバッチを作成。
"""
import csv
import datetime
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from diary.models import Post


class Command(BaseCommand):
    help = "Backup Post data."

    def handle(self, *args, **options):
        date = datetime.date.today().strftime("%Y%m%d")
        # 保存ファイルの相対パス
        file_path = settings.BACKUP_PATH + 'post_' + date + '.csv'
        # 保存ディレクトリがなければ作成
        os.makedirs(settings.BACKUP_PATH, exist_ok=True)

        # バックアップファイル作成
        with open(file_path, 'w') as file:
            writer = csv.writer(file)
            # ヘッダーの書き込み
            header = [field.name for field in Post._meta.fields]
            writer.writerow(header)

            # Postテーブル全データ取得
            posts = Post.objects.all()
            # データ部分の書き込み
            for post in posts:
                writer.writerow([
                    str(post.id),
                    str(post.category),
                    # str(post.tags),
                    str(post.title),
                    str(post.description),
                    str(post.content),
                    str(post.created_at),
                    str(post.updated_at),
                    str(post.published_at),
                    str(post.is_public),
                    str(post.image),
                ])

            # 保存ディレクトリのファイルリスト取得
            files = os.listdir(settings.BACKUP_PATH)
            # ファイルが設定数以上（30）あったら一番古いファイル削除 ※settings.pyに記入してある。
            if len(files) >= settings.NUM_SAVED_BACKUP:
                files.sort()
                os.remove(settings.BACKUP_PATH + files[0])
