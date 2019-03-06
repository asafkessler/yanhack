import os
from random import shuffle

import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LinearRegression

from business_logic_layer.ellipse import Ellipse
from business_logic_layer.ellipse_actions import generate_ellipse
from business_logic_layer.ellipse_actions import number_of_planes_in_ellipse


def get_ellipsis():
    if os.path.isfile("ellipsis.csv"):
        pprint('loaded exist ellipsis')
        return pd.read_csv("ellipsis.csv")
    ellipses = generate_ellipse()
    # random sort it
    shuffle(ellipses)
    pprint('finished generating ellipsis')
    df = pd.DataFrame(e.get_data() for e in ellipses[:])
    df.to_csv("ellipsis.csv")
    pprint('ellipsis saved as csv')
    return df


def build_model():
    if os.path.isfile("clf_end.joblib") and os.path.isfile("clf_start.joblib"):
        pprint('models already exists')
        return

    # get the entire data
    ellipses = get_ellipsis()

    # for all calculate: when enter and for how long
    y = []
    for ellipse in ellipses:
        y.append(number_of_planes_in_ellipse(ellipse))

    pprint('finished labeling')

    # divide to 80  20
    last_index = int(len(ellipses) * 0.8)
    train = ellipses.iloc[:last_index]
    test = ellipses.iloc[last_index:]

    # train the data with 2 models (2 outputs)
    clf = LinearRegression(fit_intercept=True, normalize=True, copy_X=True, n_jobs=5)

    # predict the output
    clf.fit(train, y[:last_index])
    pprint('finished fitting module')

    dump(clf, 'clf.joblib')
    pprint('finished saving module')

    p = clf.predict(test)
    pprint('finished predicting module')

    # calculate how right i was
    success = 0
    for index in range(0, len(p)):
        success += (p[index] == (y[last_index + index]))

    print('success rate: ', 100 * success / (len(y) - last_index), ' %')


def pprint(to_print):
    print('-' * 15, to_print + '-' * 15)


def predict_new_ellipse(cx, cy, w, h, angle):
    clf = load('clf.joblib')
    ellipses = expand_ellipse(cx, cy, w, h, angle)
    return clf.predict(ellipses)


def expand_ellipse(cx, cy, w, h, angle):
    from business_logic_layer.ellipse_actions import MINUTES_DELTA

    minutes = [m for m in range(0, 1440, MINUTES_DELTA)]
    ellipses = []
    for m in minutes:
        ellipses.append(Ellipse(cx, cy, w, h, angle, m))
    ellipses = [e.get_data() for e in ellipses]

    return pd.DataFrame(ellipses, index=False)


# good area of cover
build_model()

p = predict_new_ellipse(1, 1, 10, 20, 0)
print(p)
