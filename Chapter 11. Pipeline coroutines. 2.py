'''2. Implement a producer-consumer pipeline where the values squared by the producer
are dispatched to two consumers, one at a time. The first value should be sent to
consumer 1, the second value to consumer 2, third value to consumer 1 again, and
so on. Closing the producer should force the consumers to print a list with the
numbers that each one obtained.'''


def producer(consumers):
    print('Producer is ready')
    try:
        while True:
            val = yield
            for consumer in consumers:
                consumer.send(val*val)
    except GeneratorExit:
        for consumer in consumers:
            consumer.close()


def consumer(name, counter):
    print(f'{name} ready')
    result = []
    try:
        while True:
            val = yield
            result.append(val)
    except GeneratorExit:
        print(f'{name} closed, the values are {result[counter::2]}')


con1 = consumer('Consumer 1', 0)
con2 = consumer('Consumer 2', 1)
prod = producer([con1, con2])

next(prod)
next(con1)
next(con2)

prod.send(1)
prod.send(2)
prod.send(3)
prod.send(4)
prod.send(5)
prod.send(6)
