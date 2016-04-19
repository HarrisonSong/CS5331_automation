import Cookie
import json
import os.path

def request(context, flow):
  print flow.request.headers
  if os.path.isfile("tmp_cookie.txt") :
    with open('tmp_cookie.txt', 'r') as f:
      cookie_name = f.read()
    print "COOKIE NAME IS %s" % cookie_name
    if "Cookie" in flow.request.headers :
      cookie = Cookie.SimpleCookie(flow.request.headers["Cookie"])
      print "request cookie is: %s" % cookie[cookie_name].value
      cookie[cookie_name].set(cookie_name, "12345", "12345")
      print "update request cookie is: %s" % cookie.output()
      flow.request.headers["Cookie"] = cookie.output().replace("Set-Cookie:", "").strip()
      print("final updated request cookie: %s" % (flow.request.headers["Cookie"]))
  else :
    print "No specific cookie need to investigate"

def response(context, flow):
  print flow.response.headers
  if "Set-Cookie" in flow.response.headers :
    print("response flag cookie: %s" % (flow.response.headers["Set-Cookie"]))
