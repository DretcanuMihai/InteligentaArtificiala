import pandas
import performance_metrics as pm
import input_output as io

flowers_data = pandas.read_csv("./data/flowers.csv")
sport_data = pandas.read_csv("./data/sport.csv")

# multi-target regression error
targets = io.get_predicted_correct(sport_data)
io.print_regression_errors(targets)
print("MultiClass with MonteCarlo distance:")
print(pm.regression_multi_target_error2(pm.zip_targets(targets),lambda a,b:sum(abs(a[i]-b[i]) for i in range(len(a)))))

# multi-label performance metrics
# targets = io.get_predicted_correct(flowers_data)
# io.print_classification_results(targets[0], ["Daisy", "Tulip", "Rose"])
# print(pm.zip_targets(targets))

# loss
# targets = io.get_predicted_correct(sport_data)
# print(pm.logarithmic_loss(pm.zip_targets(targets)))
# print(pm.logarithmic_loss(pm.transform_sigmoid(pm.zip_targets(targets))))
# print(pm.logarithmic_loss(pm.transform_softmax(pm.zip_targets(targets))))
# print(pm.logarithmic_loss(pm.transform_softmax(pm.transform_sigmoid(pm.zip_targets(targets)))))

# binary loss
# realOutputs =[[1,0], [1,0], [0,1], [0,1], [1,0], [0,1]]
# computedOutputs = [ [0.7, 0.3], [0.2, 0.8], [0.4, 0.6], [0.9, 0.1], [0.7, 0.3], [0.4, 0.6]]
# zipped_targets={'names':[None,None],'data':{'predicted':computedOutputs,'expected':realOutputs}}
# print(pm.logarithmic_loss(zipped_targets))

# multi-class loss
# realOutputs = [[1, 0, 0], [0, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [1, 0, 0]]
# computedOutputs = [[5, 4, 1], [-3, 24, 2], [4, 7, 3], [3, 3, 3], [10, 0, 2], [3, 6, 2]]
# zipped_targets={'names':[None,None,None],'data':{'predicted':computedOutputs,'expected':realOutputs}}
# print(pm.logarithmic_loss(pm.transform_softmax(zipped_targets)))

# multi-class loss
# realOutputs = [[1, 0, 1], [0, 1, 0], [0, 1, 1], [1, 1, 1], [1, 1, 0], [0, 1, 0]]
# computedOutputs = [[5, 4, 1], [-3, 24, 2], [4, 7, 3], [3, 3, 3], [10, 0, 2], [3, 6, 2]]
# zipped_targets = {'names': [None, None, None], 'data': {'predicted': computedOutputs, 'expected': realOutputs}}
# print(pm.logarithmic_loss(pm.transform_sigmoid(zipped_targets)))
