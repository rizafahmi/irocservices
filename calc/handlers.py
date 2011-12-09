from piston.handler import BaseHandler

class CalcHandler(BaseHandler):
  def read(self, request, expression):
    return eval(expression)
