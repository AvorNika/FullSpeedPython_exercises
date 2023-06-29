'''1. Implement a producer-consumer pipeline where the values squared by the producer
are sent to two consumers. One should store and print the minimum value sent so
far and the other the maximum value.'''


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


def consumer(name, charact, func):
    print(f'{name} ready')
    result = []
    try:
        while True:
            val = yield
            result.append(val)
            print(f'{name} consists {charact}: {func(result)}')
    except GeneratorExit:
        print(f'{name} closed')


con1 = consumer('Consumer 1', 'minimum value', min)
con2 = consumer('Consumer 2', 'maximum value', max)
prod = producer([con1, con2])

next(prod)
next(con1)
next(con2)

prod.send(1)
prod.send(8)
prod.send(25)
