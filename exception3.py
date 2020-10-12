class HTTPError(Exception):
    def __init__(self,msg,code):
        super(HTTPError, self).__init__()
        self.message=msg
        self.code=code


def upload():
    "Code to upload data to server via HTTP"
    response = 404
    if response!=200:
        if response == 404:
            raise HTTPError("File Not Found",response)
        elif response == 500:
            raise HTTPError("Server Error",response)

try:
    upload()
except HTTPError as err:
    print("Message:",err.message)
    print("Code:",err.code)