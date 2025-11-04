from locust import User, task, between
from xmlrpc.client import ServerProxy, Fault
import time

class XmlRpcClient(ServerProxy):
    """
    XmlRpcClient is a wrapper around the standard library's ServerProxy.
    It proxies any function calls and fires the *request* event when they finish,
    so that the calls get recorded in Locust.
    """

    def __init__(self, host, request_event):
        super().__init__(host)
        self._request_event = request_event

    def __getattr__(self, name):
        func = ServerProxy.__getattr__(self, name)

        def wrapper(*args, **kwargs):
            request_meta = {
                "request_type": "xmlrpc",
                "name": name,
                "start_time": time.time(),
                "response_length": 0,  # calculating this for an xmlrpc.client response would be too hard
                "response": None,
                "context": {},  # see HttpUser if you actually want to implement contexts
                "exception": None,
            }
            start_perf_counter = time.perf_counter()
            try:
                request_meta["response"] = func(*args, **kwargs)
            except Fault as e:
                request_meta["exception"] = e
            request_meta["response_time"] = (time.perf_counter() - start_perf_counter) * 1000
            self._request_event.fire(**request_meta)  # This is what makes the request actually get logged in Locust
            return request_meta["response"]

        return wrapper

class XmlRpcUser(User):
    """
    A minimal Locust user class that provides an XmlRpcClient to its subclasses
    """

    abstract = True  # dont instantiate this as an actual user when running Locust

    def __init__(self, environment):
        super().__init__(environment)
        self.client = XmlRpcClient(self.host, request_event=environment.events.request)

# HttpUser: It adds a client attribute which is used to make HTTP requests
class UploadLargeFileUser1(XmlRpcUser):
    host = "http://127.0.0.1:8881/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(5, 6)
    @task(1)
    def upload_large_file(self):
        self.client.upload_large_file()
        print("Upload large file completed")

class UploadLargeFileUser2(XmlRpcUser):
    host = "http://127.0.0.1:8882/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(5, 6)
    @task(1)
    def upload_large_file(self):
        self.client.upload_large_file()
        print("Upload large file completed")

class UploadLargeFileUser3(XmlRpcUser):
    host = "http://127.0.0.1:8883/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(5, 6)
    @task(1)
    def upload_large_file(self):
        self.client.upload_large_file()
        print("Upload large file completed")

class UploadLargeFileUser4(XmlRpcUser):
    host = "http://127.0.0.1:8884/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(5, 6)
    @task(1)
    def upload_large_file(self):
        self.client.upload_large_file()
        print("Upload large file completed")

class UploadSmallFileUser1(XmlRpcUser):
    host = "http://127.0.0.1:8885/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(1, 2)
    @task(1)
    def upload_small_file(self):
        self.client.upload_small_file()
        print("Upload small file completed")

class UploadSmallFileUser2(XmlRpcUser):
    host = "http://127.0.0.1:8886/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(1, 2)
    @task(1)
    def upload_small_file(self):
        self.client.upload_small_file()
        print("Upload small file completed")

class UploadSmallFileUser3(XmlRpcUser):
    host = "http://127.0.0.1:8887/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(1, 2)
    @task(1)
    def upload_small_file(self):
        self.client.upload_small_file()
        print("Upload small file completed")

class UploadSmallFileUser4(XmlRpcUser):
    host = "http://127.0.0.1:8888/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(1, 2)
    @task(1)
    def upload_small_file(self):
        self.client.upload_small_file()
        print("Upload small file completed")

class DownloadLargeFileUser1(XmlRpcUser):
    host = "http://127.0.0.1:8889/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(5, 6)
    @task(1)
    def download_large_file(self):
        self.client.download_large_file()
        print("Download large file completed")

class DownloadLargeFileUser2(XmlRpcUser):
    host = "http://127.0.0.1:8890/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(5, 6)
    @task(1)
    def download_large_file(self):
        self.client.download_large_file()
        print("Download large file completed")

class DownloadLargeFileUser3(XmlRpcUser):
    host = "http://127.0.0.1:8891/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(5, 6)
    @task(1)
    def download_large_file(self):
        self.client.download_large_file()
        print("Download large file completed")

class DownloadLargeFileUser4(XmlRpcUser):
    host = "http://127.0.0.1:8892/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(5, 6)
    @task(1)
    def download_large_file(self):
        self.client.download_large_file()
        print("Download large file completed")

class DownloadSmallFileUser1(XmlRpcUser):
    host = "http://127.0.0.1:8893/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(1, 2)
    @task(1)
    def download_small_file(self):
        self.client.download_small_file()
        print("Download small file completed")

class DownloadSmallFileUser2(XmlRpcUser):
    host = "http://127.0.0.1:8894/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(1, 2)
    @task(1)
    def download_small_file(self):
        self.client.download_small_file()
        print("Download small file completed")

class DownloadSmallFileUser3(XmlRpcUser):
    host = "http://127.0.0.1:8895/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(1, 2)
    @task(1)
    def download_small_file(self):
        self.client.download_small_file()
        print("Download small file completed")

class DownloadSmallFileUser4(XmlRpcUser):
    host = "http://127.0.0.1:8896/"
    
    # make simulated users wait between x & x secs after each task is executed
    wait_time = between(1, 2)
    @task(1)
    def download_small_file(self):
        self.client.download_small_file()
        print("Download small file completed")

