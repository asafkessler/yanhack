from random import shuffle

import pandas as pd
from sklearn.linear_model import LinearRegression

from business_logic_layer.ellipse_actions import best_time_for_ellipse
from business_logic_layer.ellipse_actions import generate_ellipse
from business_logic_layer.ellipse_time import EllipseTime


def predict_time_and_latency_of_clear_area():
    # get the entire data
    ellipses = generate_ellipse(1, 0)
    # random sort it
    shuffle(ellipses)

    # for all calculate: when enter and for how long
    y = []
    for ellipse in ellipses:
        y.append(best_time_for_ellipse(ellipse))

    # devide to 80  20
    last_index = int(len(ellipses) * 0.8)
    train = pd.DataFrame(ellipses[:last_index])
    test = pd.DataFrame(ellipses[last_index:])

    # train the data with 2 models (2 outputs)
    lr = LinearRegression(fit_intercept=True, normalize=True, copy_X=True, n_jobs=5)
    y_start = [n.start for n in y]
    y_end = [n.end for n in y]

    # predict the output
    lr.fit(train, y_start[:last_index])
    p_start = lr.predict(test)

    lr.fit(train, y_end[:last_index])
    p_end = lr.predict(test)

    # calculate how right i was
    p = [EllipseTime(start, end) for start in p_start for end in p_end]
    results = [1 if x.__eq__(_p) else 0 for _p in p for x in y[last_index:]]
    print(100 * sum(results) / len(results), ' %')

    # return best polygon time
    return p

predict_time_and_latency_of_clear_area(3)
