import logging

# logging.debug('It is a debug message')	# it will not be printed
# logging.info('It is an info message')	# not printed
# logging.warning('OOPs!!! It is a warning')	# it will be print because it is default level
# logging.error('Oops !! an error message')	# will be printed 
# logging.critical('Oh!!!! it is a critical message')	# will be printed

# logging.basicConfig(level=logging.INFO)
# # logging.info('This is an info message.This will get logged.')
#
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('This message is to indicate that Admin has just logged in')
#
# import os
# list = os.listdir()
#
# for i in list:
#     print(i)

import statistics

a = [1,2,3,4,5]
print(statistics.mean(a))
print(statistics.harmonic_mean(a))
print(statistics.median(a))
print(statistics.median_grouped(a))
print(statistics.median_high(a))
print(statistics.median_low(a))
print(statistics.mode(a))
print(statistics.pstdev(a))
print(statistics.stdev(a))
print(statistics.pvariance(a))
print(statistics.variance(a))

