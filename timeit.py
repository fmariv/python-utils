# -*- coding: utf-8 -*-

"""

***************************************************************************
    timeit.py
    ---------------
    Autor:          Andreas Jung
    Link:           https://www.zopyx.de/andreas-jung/contents/a-python-decorator-for-measuring-the-execution-time-of-methods
    Editat per:     Fran Martín
    Data:           20200309
***************************************************************************


Funció per a calcular el temps que triga en executar-se una funció
"""


import time                                                

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print "\nMetode - %r | Temps d'execucio - %2.2f sec" % \
              (method.__name__, te-ts)
        return result

    return timed