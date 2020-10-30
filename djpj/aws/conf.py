import os

# add: AWS S3
AWS_ACCESS_KEY_ID       = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY   = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_LOCATION         = 'media'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'djpj.aws.utils.S3Boto3Storage'
MEDIA_URL            = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL       = None
AWS_QUERYSTRING_AUTH  = False # URLからクエリパラメータを削除
AWS_PRELOAD_METADATA  = True # これをTrueにしたほうがファイル変更のチェックが速くなる
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # キャッシュの有効期限（最長期間）= 1日
}
