'''
Created on 16 may. 2018

@author: pgg
'''
from kafka.consumer.group import KafkaConsumer

if __name__ == '__main__':
    topic = 'pgg_test'
    print('consumidor de kafka para el topic: ' + str(topic))
	ip = 'localhost:9092'
    consumer = KafkaConsumer(bootstrap_servers=ip, auto_offset_reset='earliest')
    consumer.subscribe([topic])
    for msg in consumer:
        print(msg)
    print('se fini')
