import mnist_loader
import network as network
import network_mat as network_mat
import datetime

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
net = network.Network([784, 30, 10])
start = datetime.datetime.now()
print(start)
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
end = datetime.datetime.now()
print(end)
duration1 = end - start
print(duration1)

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
net = network_mat.Network([784, 30, 10])
start = datetime.datetime.now()
print(start)
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
end = datetime.datetime.now()
print(end)
duration2 = end - start
print(duration2)

print(duration1 / duration2)