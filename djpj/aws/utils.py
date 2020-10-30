from storages.backends.s3boto3 import S3Boto3Storage

# 同一ファイル名の画像がアップロードされたら上書きせずに適当にリネーム
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False
