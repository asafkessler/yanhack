from random import shuffle
import os
import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LinearRegression
from business_logic_layer.ellipse import Ellipse
from business_logic_layer.ellipse_actions import best_time_for_ellipse
from business_logic_layer.ellipse_actions import generate_ellipse
from business_logic_layer.ellipse_time import EllipseTime


def predict_time_and_latency_of_clear_area(lat1, lon1, lat2, lon2):
    if os.path.isfile("clf_end.joblib") and os.path.isfile("clf_start.joblib"):
        print('-' * 15, 'models already exists' + '-' * 15)
        return

    # get the entire data
    ellipses = generate_ellipse(lat1, lon1, lat2, lon2, 1)
    print('-' * 15, 'finished generating ellipsis' + '-' * 15)
    # random sort it
    shuffle(ellipses)

    # for all calculate: when enter and for how long
    y = []
    for ellipse in ellipses:
        y.append(best_time_for_ellipse(ellipse))

    print('-' * 15, 'finished labeling' + '-' * 15)

    # devide to 80  20
    last_index = int(len(ellipses) * 0.8)
    train = pd.DataFrame(e.get_data() for e in ellipses[:last_index])
    test = pd.DataFrame(e.get_data() for e in ellipses[last_index:])

    # train the data with 2 models (2 outputs)
    clf = LinearRegression(fit_intercept=True, normalize=True, copy_X=True, n_jobs=5)
    y_start = [n.start for n in y]
    y_end = [n.end for n in y]

    # predict the output
    clf.fit(train, y_start[:last_index])
    print('-' * 15, 'finished fitting start module' + '-' * 15)

    dump(clf, 'clf_start.joblib')
    print('-' * 15, 'finished saving start module' + '-' * 15)

    p_start = clf.predict(test)
    print('-' * 15, 'finished predicting start module' + '-' * 15)

    clf.fit(train, y_end[:last_index])
    print('-' * 15, 'finished fitting end module' + '-' * 15)

    dump(clf, 'clf_end.joblib')
    print('-' * 15, 'finished saving end module' + '-' * 15)

    p_end = clf.predict(test)
    print('-' * 15, 'finished predicting end module' + '-' * 15)

    # calculate how right i was
    success = 0
    for index in range(0, len(p_start)):
        success += (EllipseTime(p_start[index], p_end[index])).__eq__(y[last_index + index])

    print('success rate: ', 100 * success / (len(y) - last_index), ' %')


def predict_new_ellipse(ellipse):
    clf_start = load('clf_start.joblib')
    clf_end = load('clf_end.joblib')

    return EllipseTime(clf_start.predict([ellipse.get_data()]), clf_end.predict([ellipse.get_data()]))


# good area of cover
predict_time_and_latency_of_clear_area(29, 31, 35, 37)
predict_new_ellipse(Ellipse(1,1,1))