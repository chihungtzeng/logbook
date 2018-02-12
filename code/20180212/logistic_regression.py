# -*- coding: utf-8 -*-
"""
Toy example of logistic regression. The data are drawn from
https://en.wikipedia.org/wiki/Logistic_regression.
"""
from __future__ import print_function
import numpy as np
from sklearn.linear_model import LogisticRegression

# 20 data points, one is study hours, the other is exam results (0: fail, 1:
# pass)
HOURS = [0.50, 0.75, 1.00, 1.25, 1.50,
         1.75, 1.75, 2.00, 2.25, 2.50,
         2.75, 3.00, 3.25, 3.50, 4.00,
         4.25, 4.50, 4.75, 5.00, 5.50]
EXAM_RESULTS = [0, 0, 0, 0, 0,
                0, 1, 0, 1, 0,
                1, 0, 1, 0, 1,
                1, 1, 1, 1, 1]


def main():
    """
    Train model
    """
    logreg = LogisticRegression()
    train_x = np.array(HOURS)
    train_x = train_x.reshape(-1, 1)
    train_y = np.array(EXAM_RESULTS)
#    train_y = train_y.reshape(-1, 1)
    logreg.fit(train_x, train_y)
    print("logreg score: {}".format(logreg.score(train_x, train_y)))

    # predicting a student who study x hours
    for x in xrange(0, 10):
        prob = logreg.predict_proba(x)
        does_pass = logreg.predict(x)
        print("hour: {}, pass prob: {} result: {}".format(x, prob, does_pass))

if __name__ == "__main__":
    main()
