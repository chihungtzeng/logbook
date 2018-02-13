# -*- coding: utf-8 -*-
"""
Play with logistic regression. The data and code are from
https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8
"""
from __future__ import print_function
import pandas
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
# import matplotlib.pyplot as plt
# import numpy as np


def __read_data_from_csv():
    data = pandas.read_csv("banking.csv", header=0)
    # data = data.drop("poutcome", 1)
    return data.dropna()  # # pylint: disable=no-member


def __examine_data(data):
    # print(data.shape)
    # print(data.columns)
    print(data.head())
    # print(data["y"].value_counts())
    # print(data.groupby("job").mean())

    # This will show:
    # y                 0     1
    # job
    # admin.         9070  1352
    # blue-collar    8616   638
    # ...
    table = pandas.crosstab(data.job, data.y)
    print(table)
    # Futhur process table:
    # y                     0         1
    # job
    # admin.         0.870274  0.129726
    # blue-collar    0.931057  0.068943

    print(table.div(table.sum(1).astype(float), axis=0))

    return None


def __create_dummy_variables(data):
    """
    Create columns like "martital_divorce", "marital_married",... with column
    values either 0 or 1, and then append the columns to |data|.
    """
    # deliberately use non-numerical fields to do logistic regression.
    # cat_vars = ["job", "marital", "education", "housing", "loan"]
    cat_vars = ["job", "marital", "education", "default", "housing",
                "loan", "contact", "month", "day_of_week", "poutcome"]
    for var in cat_vars:
        cat_list = pandas.get_dummies(data[var], prefix=var)
        data = data.join(cat_list)
    # Remove the origin vars related to dummy variables
    columns_all = data.columns.values.tolist()
    keeps = [_ for _ in columns_all if _ not in cat_vars]

    # We need to return the modified data to make the change effective
    return data[keeps]


def __select_features(data, num_features):
    columns = data.columns.values.tolist()
    _y = ["y"]
    _x = [_ for _ in columns if _ not in _y]
    data_x = data[_x]
    data_y = data[_y].values.ravel()

    logreg = LogisticRegression()
    rfe = RFE(logreg, num_features)

    rfe.fit(data_x, data_y)

    ret = []
    for index, support in enumerate(rfe.support_):
        # print(u"{} -- support: {} ranking: {}".format(
        # _x[index], support, rfe.ranking_[index]))
        if support:
            ret.append(_x[index])
    return ret


def __train_logistic_regression(data):
    for num_features in xrange(1, 7):
        features = __select_features(data, num_features)
        print(features)

        train_x, test_x, train_y, test_y = train_test_split(
            data[features], data[["y"]], test_size=0.3, random_state=7)
        logreg = LogisticRegression()
        logreg.fit(train_x, train_y)
        print(("Accuracy of logistic regression classifier on test set: "
               "{:.2f}".format(logreg.score(test_x, test_y))))


def main():
    """
    Prog entry.
    """
    data = __read_data_from_csv()
#    __examine_data(data)
    data = __create_dummy_variables(data)
    __train_logistic_regression(data)

if __name__ == "__main__":
    main()
