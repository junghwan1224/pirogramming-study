from .common import *

# common.py 에 있는 내용을 오버라이드 한다.

BASE_DIR = os.path.dirname(BASE_DIR )

DEBUG = False
ALLOWED_HOSTS = ['13.124.168.61']

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
