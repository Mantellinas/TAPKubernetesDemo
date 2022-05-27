from pystalkd.Beanstalkd import Connection 

class BeanstalkdQueue:
    def __init__(self, ip_address, port):
        self.beanstalk = Connection(host = ip_address, port = port)

    def getFromQueue(self):
        job = self.beanstalk.reserve(10) # wait 10 second after the queue is empty and then self-kill
        if job is not None:
            result = job.body
            job.delete()
            return result
        else:
            return None