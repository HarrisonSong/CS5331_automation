def request(context, flow):
	print("flag cookie: %s" % (flow.request.headers["Cookie"]))
