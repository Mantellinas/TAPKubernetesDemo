from BeanstalkdQueue import *
import os 

BTALK_IP   = "BTALK_IP"

if __name__ == '__main__':
    env_var    = os.environ
    if BTALK_IP not in env_var:
        print("YOU NEED TO SPECIFY THE IP ADDRESS OF THE BEANSTALK SERVER")
        exit(1)
    ip_address = os.environ[BTALK_IP]
    port = 11300
    
    beanstalkd = BeanstalkdQueue(ip_address, port)
    file1 = open('redditTitle.txt', 'r')
    Lines = file1.readlines()

    for line in Lines:
        print(line)
        beanstalkd.putInQueue(str(line))
