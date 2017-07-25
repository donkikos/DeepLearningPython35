#import sys
#sys.stdout = open('file', 'w')
#print 'test'

import mnist_loader
import network as network
import time

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
net = network.Network([784, 30, 10])
start = time.time()
print(start)
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
end = time.time()
print(end)
print(end - start)