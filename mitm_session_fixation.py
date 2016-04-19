def request(context, flow):
  if(flow.request.headers["Cookie"]) :
    print("flag cookie: %s" % (flow.request.headers["Cookie"]))
  flow.request.headers["Cookie"] = "12345"
  if(flow.request.headers["Cookie"]) :
    print("updated flag cookie: %s" % (flow.request.headers["Cookie"]))

def response(context, flow):
  if(flow.request.headers["Set-Cookie"]) :
    print("response flag cookie: %s" % (flow.response.headers["Set-Cookie"]))
