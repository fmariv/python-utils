# -*- coding: utf-8 -*-

import time
from math import floor


"""

***************************************************************************
    timeit function
    ---------------
    Autor:          Andreas Jung
    Link:           https://www.zopyx.de/andreas-jung/contents/a-python-decorator-for-measuring-the-execution-time-of-methods
    Edited by:      Fran Martín
    Date:           20200309
***************************************************************************


"""


def timeit(method):
    """
    Calculate the time it takes for a specific function to run
    :param method: function to monitorize
    :return: time taked for code to run
    """

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print "\nMetode - %r | Temps d'execucio - %2.2f sec" % \
              (method.__name__, te-ts)
        return result

    return timed


"""

***************************************************************************
    Useful Python Snippets
    ---------------
    Autor:          Mikhail Raevskiy
    Link:           https://medium.com/swlh/top-useful-python-snippets-that-save-time-38958f256822
    Edited by:      Fran Martín
    Date:           20201008
***************************************************************************


"""


def check_all_unique(lst):
    """
    Check if there are duplicate items in the given list
    :param lst: list where to check the duplicate items
    :return: existance of duplicate items
    """
    return len(lst) == len(set(lst))


def merge_dictionaries(a, b):
    """
    Combine two dictionaries
    :param a: first dict
    :param b: second dict
    :return:
    """
    return {**a, **b}
