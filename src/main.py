# Main script file for running toggl-ml
from export import export
from preprocess import preprocess
from learn import learn
from analyse import analyse


# Instructions: Run all script files from the top level directory, calling...
#   $ python src/<SCRIPT>.py


# Module variable definitions:
#   since:          Starting date for exporting time entries
#   until:          Ending date for exporting time entries
#   size_train:     Percentage size of the training data set (0.0 - 1.0)
#   size_test:      Percentage size of the testing data set (0.0 - 1.0)
#   size_validate:  Percentage size of the validation data set (0.0 - 1.0)
#   days:           Number of days to split data training bundles into
#   sets:           Number of datasets to generate and train on
#   bundle:         Plot the given bundle's value

# NOTE: The three size variables must sum to 1.0, else an error is thrown


# Run probability classifiers on time entry data from Toggl account
def main(since, until, size_train, size_test, size_validate,
         days, sets, bundle):
    print('\nMAIN:')

    # Export all data from Toggl account
    # export(since, until)

    # Partition data into three separate sets
    preprocess(size_train, size_test, size_validate)
    
    # Run learning model on the training data set, printing outcomes
    learn(days, sets)

    # Show visual results of learning model of training data
    analyse(bundle)

    print('\nFINISHED MAIN\n')


# DEBUG
if __name__ == '__main__':
    main('2018-01-01', '2018-12-31', 0.6, 0.2, 0.2, 7, 100, 0)
