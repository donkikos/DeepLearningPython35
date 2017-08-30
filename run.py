import mnist_loader
import network2
import datetime

folder_to_save = './runs/run2/'

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)

start = datetime.datetime.now()
print(start)

net = network2.Network([784, 30, 10],
    cost=network2.CrossEntropyCost,
    use_momentum=True)
net.large_weight_initializer()
evaluation_cost, evaluation_accuracy, \
    training_cost, training_accuracy = net.SGD(training_data, 30, 10, 0.5,
    lmbda = 5,
    mu = 0.5,
    evaluation_data=validation_data,
    monitor_evaluation_accuracy=True,
    monitor_evaluation_cost=True,
    monitor_training_accuracy=True,
    monitor_training_cost=True)

end = datetime.datetime.now()
print(end)

duration1 = end - start
print(duration1)

### Saving results
print("Saving training results...")
import numpy as np

# evaluation_cost
fid = open(folder_to_save + 'evaluation_cost.dat', 'w')
np.array(evaluation_cost).tofile(fid," ")
fid.close()

# evaluation_accuracy
fid = open(folder_to_save + 'evaluation_accuracy.dat', 'w')
np.array(evaluation_accuracy).tofile(fid," ")
fid.close()

# training_cost
fid = open(folder_to_save + 'training_cost.dat', 'w')
np.array(training_cost).tofile(fid," ")
fid.close()

# training_accuracy
fid = open(folder_to_save + 'training_accuracy.dat', 'w')
np.array(training_accuracy).tofile(fid," ")
fid.close()

print("Done.")