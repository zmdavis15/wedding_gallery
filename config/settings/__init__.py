from config.settings.base import *

try:
    from config.settings.local import *
except:
    from config.settings.prod import *
