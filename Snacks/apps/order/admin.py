import xadmin
from .models import *

# Register your models here.
xadmin.site.register(OrderGoods)
xadmin.site.register(OrderInfo)
