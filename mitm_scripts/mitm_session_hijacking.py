def request(context, flow):
  if(flow.request.headers["Cookie"]) :
    print("flag cookie: %s" % (flow.request.headers["Cookie"]))
