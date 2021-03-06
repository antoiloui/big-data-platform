#!/usr/bin/env python
import pika


credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/',credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
