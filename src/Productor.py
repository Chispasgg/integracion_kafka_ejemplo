'''
Created on 16 may. 2018

@author: pgg
'''
from kafka.producer.kafka import KafkaProducer
import datetime
import time

if __name__ == '__main__':
    print('productor de kafka')
    topic = 'pgg_test'
	ip = 'localhost:9092'
    producer = KafkaProducer(bootstrap_servers=ip)
    time.sleep(0.01)
    for x in range(10):
        m = str.encode(str(datetime.datetime.now()))
        a = producer.send(topic, m)
        time.sleep(0.01)
        print(str(x) + ' - ' + str(a.is_done))
    print('se fini')
