from logger import log_event

class APIResponseError(Exception):
    def _init_(self, info, status_code=None):
        super()._init_(info)
        self.status_code = status_code
        log_event("ERROR", f"APIResponseError: {info}", exception_code="API_RESPONSE_ERROR")

class APIClient:
    def _init_(self, base_url):
        self.base_url = base_url

    def request(self, endpoint, method="GET"):
        if method not in ["GET","POST","PUT","PATCH","DELETE"]:
            raise APIResponseError(f"Unsupported method {method}")
        response_status = 200
        if response_status >= 400:
            raise APIResponseError("Unexpected HTTP status", status_code=response_status)
        return {"status": response_status, "data": {}}
