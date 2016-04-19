import Cookie
import os.path

def request(context, flow):
  print flow.request.headers
  if os.path.isfile("tmp_cookie.txt") :
    with open('tmp_cookie.txt', 'r') as f:
      cookie_name = f.read()
    print "COOKIE NAME IS %s" % cookie_name
    if "Cookie" in flow.request.headers :
      cookie = Cookie.SimpleCookie(flow.request.headers["Cookie"])
      if cookie[cookie_name] and cookie[cookie_name].value :
        print "request cookie is: %s" % cookie[cookie_name].value
        with open('tmp_cookie_value.txt', 'w+') as f:
          f.write(cookie[cookie_name].value)
  else :
    print "No specific cookie need to investigate"
