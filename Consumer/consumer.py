from ipaddress import ip_address
from BeanstalkdQueue import *
import nltk
import os
from time import sleep
from nltk.sentiment.vader import SentimentIntensityAnalyzer

BTALK_IP   = "BTALK_IP"

if __name__ == '__main__':
    env_var    = os.environ
    sid = SentimentIntensityAnalyzer()

    if BTALK_IP not in env_var:
        print("YOU NEED TO SPECIFY THE IP ADDRESS OF THE BEANSTALK SERVER")
        exit(1)

    ip_address = os.environ[BTALK_IP]
    port = 11300

    beanstalkd = BeanstalkdQueue(ip_address, port)
    
    while True:
        text = beanstalkd.getFromQueue()
        if text is None:
            break
        sleep(10)
        print(text)
        print(sid.polarity_scores(text))
        