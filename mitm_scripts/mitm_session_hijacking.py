import os.path

def request(context, flow):
  print flow.request.headers
  if os.path.isfile("tmp_cookie.txt") :
    with open('tmp_cookie.txt', 'r') as f:
      cookie_name = f.read()
    print "COOKIE NAME IS %s" % cookie_name
    if "Cookie" in flow.request.headers :
      print "request cookie content is: %s" % flow.request.headers["Cookie"]
      with open('tmp_cookie_value.txt', 'w+') as f:
        f.write(flow.request.headers["Cookie"])
  else :
    print "No specific cookie need to investigate"
