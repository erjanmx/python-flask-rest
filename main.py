# -*- coding: utf-8 -*-
from flask import Flask
from time import sleep
app = Flask(__name__)


def is_prime(n):
    """
    Проверка числа на его простоту
    :param n:
    :return:
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route("/")
def welcome():
    return "Welcome to simple rest server<br>" \
           "usage<br>" \
           "/prime/&lt;n&gt; - calculates the n-th prime number (<a target='_blank' href='/prime/55'>example</a>)<br>" \
           "/factor/&lt;n&gt; - factorizes n (<a target='_blank' href='/factor/55'>example</a>)<br>" \
           "/ping/&lt;host&gt;/&lt;n&gt; - pings given host n-times " \
           "(<a target='_blank' href='/ping/google.com/5'>example</a>)<br>"


@app.route("/prime/<n>")
def prime(n):
    """
    Нахождение n-го простого числаа
    :param n:
    :return:
    """
    k = 1
    res = ""
    primes = 0
    while primes < int(n) + 1:
        if is_prime(k):
            primes += 1
            res = str(k)
        k += 1
    return res


@app.route("/factor/<n>")
def factor(n):
    """
    Разложение на простые множители
    :param n:
    :return:
    """
    a = int(n)
    res = []
    i = 2
    while is_prime(a) == 0:
        if is_prime(i) == 1 and a % i == 0:
            a = int(a / i)
            res.append(i)
            i = 2
        i += 1
    res.append(a)
    return ', '.join(str(i) for i in res)


@app.route("/ping/<host>/<n>")
def ping(host, n):
    """
    Пинг заданного сервера n - раз
    :param host:
    :param n:
    :return:
    """
    import os
    import platform
    success = 0
    for i in range(int(n)):
        ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        if os.system("ping " + ping_str + " " + host) == 0:
            success += 1
        sleep(1)
    return "{} ping succeeded {} out of {}".format(host, success, n)


if __name__ == "__main__":
    app.run(threaded=True)