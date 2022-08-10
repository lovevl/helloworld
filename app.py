
from sanic import Sanic, response
from sanic.response import json as json_
import json
from urllib import parse



app = Sanic("pdd_main")
app.config.PROXIES_COUNT = 1
app.config.REAL_IP_HEADER = 'x-real-ip'
# nest_asyncio.apply()

@app.route("/")
async def getIndex(request):
  print(request.ip)
  return  json_(dict(status=200))

# 用户被t下线展示的网页。
@app.route("/notifylogout")
async def test(request):
  username = ""
  if request.query_string:
    resultArr = parse.unquote(request.query_string)
    for datastr in resultArr.split('&'):
      arr = datastr.split("=")
      if arr[0] == 'user':
        username = f"用户：{arr[1]}"
        break
  htmls = """ 
        <p>Hello World</p>
        <p>非常抱歉，你已被t下线，请重试登录。%s</p>
        """ % username
  return response.html(htmls)


if __name__ == '__main__':
  app.run('0.0.0.0',443)


