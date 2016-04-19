def request(context, flow):
  if(flow.request.headers["Cookie"]) :
    print("flag cookie: %s" % (flow.request.headers["Cookie"]))

def response(context, flow):
  if(flow.response.headers["Set-Cookie"]) :
    print("response flag cookie: %s" % (flow.response.headers["Set-Cookie"]))
