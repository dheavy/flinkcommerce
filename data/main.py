import json
import random
from datetime import datetime
import time

from faker import Faker
from confluent_kafka import SerializingProducer

fake = Faker()

def generate_sales_transaction():
    user = fake.simple_profile()
    return {
        'transactionId': fake.uuid4(),
        'productName': random.choice([
            'laptop',
            'smartphone',
            'tablet',
            'smartwatch',
            'headphone',
            'speaker'
        ]),
        'productId': random.choice([
            'product-1',
            'product-2',
            'product-3',
            'product-4',
            'product-5',
            'product-6'
        ]),
        'productCategory': random.choice([
            'electronics',
            'fashion',
            'home',
            'sports',
            'beauty',
            'health'
        ]),
        'productPrice': round(random.uniform(100, 1000), 2),
        'productQuantity': random.randint(1, 10),
        'productBrand': random.choice([
            'apple',
            'samsung',
            'xiaomi',
            'huawei',
            'sony',
        ]),
        'currency': random.choice([
            'USD',
            'EUR',
        ]),
        'customerId': user['username'],
        'transactionDate': fake.date_time_between(start_date='-1y', end_date='now').isoformat(),
        'paymentMethod': random.choice([
            'credit_card',
            'debit_card',
            'paypal',
        ]),
    }

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def main():
    topic = 'sales_transactions'
    producer = SerializingProducer({
        'bootstrap.servers': 'broker:9092',
    })
    curr_time = datetime.now()
    while (datetime.now() - curr_time).seconds < 120:
        try:
            tnx = generate_sales_transaction()
            tnx['totalAmount'] = tnx['productPrice'] * tnx['productQuantity']

            producer.produce(
                topic=topic,
                key=tnx['transactionId'],
                value=json.dumps(tnx),
                on_delivery=delivery_report
            )

            producer.poll(0)
            time.sleep(2)
        except BufferError as e:
            print('Buffer full, waiting for free space on the queue...')
            time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
