import re

from piston.handler import BaseHandler
# from piston.utils import rc, throttle

from irocservices.cori.models import *

class CoriHandler(BaseHandler):
    allowed_method = ('GET')
    fields = ('name', 'email', 'url', 'detail')
    #model = eval('otComment'+str(id_table))

    def read(self, request, id_table, id_news):
        comment = eval('OtComment'+str(id_table)+'.objects.filter(id_content=id_news)')
        return comment

class CoriCountHandler(BaseHandler):
    allowed_method = ('GET')
    fields = ()

    def read(self, request, id_table, id_news):
        count = eval('OtComment'+str(id_table)+'.objects.filter(id_content=id_news).count()')
        print count
        return count