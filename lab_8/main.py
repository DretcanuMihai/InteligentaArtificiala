from sklearn.datasets import load_linnerud

import input_output as io
import regression
import utils

value = 3

# univariate

if value == 1:
    files = ["./data/2017.csv",
             "./data/v1_world-happiness-report-2017.csv",
             "./data/v2_world-happiness-report-2017.csv",
             "./data/v3_world-happiness-report-2017.csv"]

    my_data_set = io.read_csv(files[0], ['Economy..GDP.per.Capita.', 'Happiness.Score'])
    io.plot_histogram(my_data_set, 'Economy..GDP.per.Capita.')
    io.plot_histogram(my_data_set, 'Happiness.Score')
    io.plot_2_traits(my_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score')

    training_data_set, validation_data_set = utils.split_training_validation(my_data_set, 0.8)
    io.plot_training_validation_2_traits(training_data_set, validation_data_set, 'Economy..GDP.per.Capita.'
                                         , 'Happiness.Score')

    regressors = regression.solve_linear_regression_mine(training_data_set, ['Economy..GDP.per.Capita.'],
                                                         ['Happiness.Score'])

    my_regressor = regressors[0]
    print(str(my_regressor))
    io.plot_my_regression_2_traits_line(training_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score', my_regressor)
    io.plot_my_regression_2_traits_line(validation_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score',
                                        my_regressor)
    io.plot_my_regression_2_traits_points(validation_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score',
                                          my_regressor)
    io.print_error_2_traits(validation_data_set, 'Economy..GDP.per.Capita.', 'Happiness.Score', my_regressor)

# multivariate
if value == 2:
    files = ["./data/2017.csv",
             "./data/v1_world-happiness-report-2017.csv",
             "./data/v2_world-happiness-report-2017.csv",
             "./data/v3_world-happiness-report-2017.csv"]

    my_data_set = io.read_csv(files[0], ['Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score'])

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
    my_regressor = regressors[0]
    print(str(my_regressor))
    io.plot_my_regression_3_traits_line(training_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score',
                                        my_regressor)
    io.plot_my_regression_3_traits_line(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score',
                                        my_regressor)
    io.plot_my_regression_3_traits_points(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score',
                                          my_regressor)
    io.print_error_3_traits(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score', my_regressor)

# multivariate multitarget independent
if value == 3:
    files = ["./data/2017.csv",
             "./data/v1_world-happiness-report-2017.csv",
             "./data/v2_world-happiness-report-2017.csv",
             "./data/v3_world-happiness-report-2017.csv"]
    third_trait = 'Trust..Government.Corruption.'

    my_data_set = io.read_csv(files[0], ['Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score', third_trait])
    io.plot_histogram(my_data_set, 'Economy..GDP.per.Capita.')
    io.plot_histogram(my_data_set, 'Freedom')
    io.plot_histogram(my_data_set, 'Happiness.Score')
    io.plot_histogram(my_data_set, third_trait)
    io.plot_3_traits(my_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score')
    io.plot_3_traits(my_data_set, 'Economy..GDP.per.Capita.', 'Freedom', third_trait)

    training_data_set, validation_data_set = utils.split_training_validation(my_data_set, 0.8)
    io.plot_training_validation_3_traits(training_data_set, validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom'
                                         , 'Happiness.Score')
    io.plot_training_validation_3_traits(training_data_set, validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom'
                                         , third_trait)

    regressors = regression.solve_linear_regression_mine(training_data_set, ['Economy..GDP.per.Capita.', 'Freedom'],
                                                         ['Happiness.Score', third_trait])
    print(str(regressors[0]))
    print(str(regressors[1]))
    io.plot_my_regression_3_traits_line(training_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score',
                                        regressors[0])
    io.plot_my_regression_3_traits_line(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score',
                                        regressors[0])
    io.plot_my_regression_3_traits_points(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score',
                                          regressors[0])
    io.plot_my_regression_3_traits_line(training_data_set, 'Economy..GDP.per.Capita.', 'Freedom', third_trait,
                                        regressors[1])
    io.plot_my_regression_3_traits_line(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', third_trait,
                                        regressors[1])
    io.plot_my_regression_3_traits_points(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', third_trait,
                                          regressors[1])
    io.print_error_4_traits(validation_data_set, 'Economy..GDP.per.Capita.', 'Freedom', 'Happiness.Score', third_trait,
                            regressors)

# multivariate multitarget dependent
if value == 4:
    files = ["./data/2017.csv",
             "./data/v1_world-happiness-report-2017.csv",
             "./data/v2_world-happiness-report-2017.csv",
             "./data/v3_world-happiness-report-2017.csv"]
    third_trait = 'Generosity'

    my_data_set = io.read_csv(files[0], ['Economy..GDP.per.Capita.', 'Happiness.Score', third_trait])
    io.plot_histogram(my_data_set, 'Economy..GDP.per.Capita.')
    io.plot_histogram(my_data_set, 'Happiness.Score')
    io.plot_histogram(my_data_set, third_trait)
    io.plot_2_traits(my_data_set, 'Economy..GDP.per.Capita.', third_trait)
    io.plot_3_traits(my_data_set, 'Economy..GDP.per.Capita.', third_trait, 'Happiness.Score')

    training_data_set, validation_data_set = utils.split_training_validation(my_data_set, 0.8)
    io.plot_training_validation_2_traits(training_data_set, validation_data_set, 'Economy..GDP.per.Capita.',
                                         third_trait)
    io.plot_training_validation_3_traits(training_data_set, validation_data_set, 'Economy..GDP.per.Capita.', third_trait
                                         , 'Happiness.Score')

    regressors = regression.solve_linear_regression_mine_dependent(training_data_set,
                                                                   ['Economy..GDP.per.Capita.'],
                                                                   [third_trait, 'Happiness.Score'])
    print(str(regressors[0]))
    print(str(regressors[1]))
    io.plot_my_regression_2_traits_line(training_data_set, 'Economy..GDP.per.Capita.', third_trait,
                                        regressors[0])
    io.plot_my_regression_2_traits_points(training_data_set, 'Economy..GDP.per.Capita.', third_trait,
                                          regressors[0])
    io.plot_my_regression_3_traits_line(training_data_set, 'Economy..GDP.per.Capita.', third_trait, 'Happiness.Score',
                                        regressors[1])
    io.plot_my_regression_3_traits_points(training_data_set, 'Economy..GDP.per.Capita.', third_trait,
                                          'Happiness.Score',
                                          regressors[1])
    io.plot_my_regression_2_traits_line(validation_data_set, 'Economy..GDP.per.Capita.', third_trait,
                                        regressors[0])
    io.plot_my_regression_2_traits_points(validation_data_set, 'Economy..GDP.per.Capita.', third_trait,
                                          regressors[0])
    io.plot_my_regression_3_traits_line(validation_data_set, 'Economy..GDP.per.Capita.', third_trait, 'Happiness.Score',
                                        regressors[1])
    io.plot_my_regression_3_traits_points(validation_data_set, 'Economy..GDP.per.Capita.', third_trait,
                                          'Happiness.Score',
                                          regressors[1])
    io.print_error_2_traits(validation_data_set, 'Economy..GDP.per.Capita.', third_trait, regressors[0])
    io.print_error_3_traits(validation_data_set, 'Economy..GDP.per.Capita.', third_trait, 'Happiness.Score',
                            regressors[1])

# multivariate multitarget dependent
if value == 5:

    my_data_set,input_traits,output_traits = io.read_sk()

    training_data_set, validation_data_set = utils.split_training_validation(my_data_set, 0.8)
    regressors = regression.solve_linear_regression_mine_dependent(training_data_set,
                                                                   input_traits,
                                                                   output_traits)
    print(str(regressors[0]))
    print(str(regressors[1]))
    print(str(regressors[2]))
