items = []
def hget(path):
    if path == "/items":
        return {"status": "OK", "data": items}
    return {"status": "ERROR", "message": "Unknown GET path"}

def hpost(path, payload):
    if path == "/items":
        items.append(payload)
        return {"status": "CREATED", "data": payload}
    return {"status": "ERROR", "message": "Unknown POST path"}

def router(req):
    method = req.get("method")
    path = req.get("endpoint")
    data = req.get("data", {})
    if method == "GET":
        return hget(path)
    elif method == "POST":
        return hpost(path, data)
    return {"status": "ERROR", "message": "Invalid HTTP verb"}
