import input_output as io
import regression
import utils

files = ["./data/v1_world-happiness-report-2017.csv",
         "./data/v2_world-happiness-report-2017.csv",
         "./data/v3_world-happiness-report-2017.csv"]

my_data_set = io.read_csv(files[1], ['Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score'])
io.plot_histogram(my_data_set, 'Economy..GDP.per.Capita.')
io.plot_histogram(my_data_set, 'Freedom')
io.plot_histogram(my_data_set, 'Happiness.Score')
io.plot_2_traits(my_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score')
io.plot_2_traits(my_data_set, 'Freedom', 'Happiness.Score')
io.plot_3_traits(my_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score')

training_data_set, validation_data_set = utils.split_training_validation(my_data_set, 0.8)
io.plot_training_validation_3_traits(training_data_set, validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom'
                                     , 'Happiness.Score')

regressors = regression.solve_linear_regression_mine(training_data_set, ['Economy..GDP.per.Capita.', 'Freedom'],
                                                          ['Happiness.Score'])
if regressors is None:
    print("Error: Determinant is 0 - can't apply method\n")
else:
    my_regressor = regressors[0]
    print(str(my_regressor))
    io.plot_my_regression_3_traits_line(training_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score',
                                        my_regressor)
    io.plot_my_regression_3_traits_line(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score',
                                        my_regressor)
    io.plot_my_regression_3_traits_points(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score',
                                          my_regressor)
    io.print_error_3_traits(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score', my_regressor)
"""
files = ["./data/v1_world-happiness-report-2017.csv",
         "./data/v2_world-happiness-report-2017.csv",
         "./data/v3_world-happiness-report-2017.csv"]

my_data_set = io.read_csv(files[2],['Economy..GDP.per.Capita.','Happiness.Score'])
io.plot_histogram(my_data_set, 'Economy..GDP.per.Capita.')
io.plot_histogram(my_data_set, 'Happiness.Score')
io.plot_2_traits(my_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score')

training_data_set, validation_data_set = utils.split_training_validation(my_data_set, 0.8)
io.plot_training_validation_2_traits(training_data_set, validation_data_set, 'Economy..GDP.per.Capita.'
                                     , 'Happiness.Score')

regressors = regression.solve_linear_regression_libraries(training_data_set, ['Economy..GDP.per.Capita.'],
                                                          ['Happiness.Score'])

my_regressor = regressors[0]
print(str(my_regressor))
io.plot_my_regression_2_traits_line(training_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score', my_regressor)
io.plot_my_regression_2_traits_line(validation_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score', my_regressor)
io.plot_my_regression_2_traits_points(validation_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score', my_regressor)
io.print_error_2_traits(validation_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score', my_regressor)
"""""
