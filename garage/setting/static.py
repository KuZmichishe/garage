import os
from easy_thumbnails.conf import Settings as thumbnail_settings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

IMAGE_CROPPING_THUMB_SIZE = (300, 300)

THUMBNAIL_PROCESSORS = (
                           'image_cropping.thumbnail_processors.crop_corners',
                       ) + thumbnail_settings.THUMBNAIL_PROCESSORS