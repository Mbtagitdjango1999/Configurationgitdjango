from .base import *
from .services import *
from decouple import config
from .packages import *

DEBUG= DEBUG= config('DEBUG',cast=bool,default=True)