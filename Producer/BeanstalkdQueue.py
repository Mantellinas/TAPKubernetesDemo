from   pystalkd.Beanstalkd import Connection
import time

class BeanstalkdQueue:
    def __init__(self, ip_address, port):
        self.beanstalk = Connection(host = ip_address, port = port)
    
    def putInQueue(self,doc_id):
        while self.beanstalk.stats()['current-jobs-ready'] > 100000:
            time.sleep(0.5)
        self.beanstalk.put(doc_id)