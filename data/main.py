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
        'tnx_id': fake.uuid4(),
        'prd_name': random.choice([
            'laptop',
            'smartphone',
            'tablet',
            'smartwatch',
            'headphone',
            'speaker'
        ]),
        'prd_id': random.choice([
            'product-1',
            'product-2',
            'product-3',
            'product-4',
            'product-5',
            'product-6'
        ]),
        'prd_category': random.choice([
            'electronics',
            'fashion',
            'home',
            'sports',
            'beauty',
            'health'
        ]),
        'prd_price': round(random.uniform(100, 1000), 2),
        'prd_quantity': random.randint(1, 10),
        'prd_brand': random.choice([
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
        'customer_id': user['username'],
        'tnx_date': fake.date_time_between(start_date='-1y', end_date='now').isoformat(),
        'payment_method': random.choice([
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
        'bootstrap.servers': 'localhost:9092',
    })
    curr_time = datetime.now()
    while (datetime.now() - curr_time).seconds < 120:
        try:
            tnx = generate_sales_transaction()
            tnx['total_amount'] = tnx['prd_price'] * tnx['prd_quantity']

            producer.produce(
                topic=topic,
                key=tnx['tnx_id'],
                value=json.dumps(tnx),
                on_delivery=delivery_report
            )

            producer.poll(0)
            time.sleep(5)
        except BufferError as e:
            print('Buffer full, waiting for free space on the queue...')
            time.sleep(1)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
