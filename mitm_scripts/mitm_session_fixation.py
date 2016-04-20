import Cookie
import os.path

def request(context, flow):
  print "request header is %s" % flow.request.headers

def response(context, flow):
  print "response header is %s" % flow.response.headers
  if os.path.isfile("tmp_cookie.txt") :
    with open('tmp_cookie.txt', 'r') as f:
      cookie_name = f.read()
    print "COOKIE NAME IS %s" % cookie_name
    if "Set-Cookie" in flow.response.headers :
      cookie = Cookie.SimpleCookie(flow.response.headers["Set-Cookie"])
      cookie[cookie_name] = "123"
      print "updated response cookie is: %s" % cookie.output()
      flow.response.headers["Set-Cookie"] = cookie.output().replace("Set-Cookie:", "").strip()
    print("final updated response header: %s" % (flow.response.headers))
  else :
    print "No specific cookie need to investigate"
  if "Cookie" in flow.response.headers :
    print("response cookie: %s" % (flow.response.headers["Cookie"]))
