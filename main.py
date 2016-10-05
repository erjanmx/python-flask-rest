# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from time import sleep
app = Flask(__name__)


def is_prime(n):
    """
    Проверка числа на его простоту
    """
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route("/")
def welcome():
    return "Welcome to the simple rest server<br>" \
           "usage<br>" \
           "/prime/&lt;n&gt; - calculates the n-th prime number (<a target='_blank' href='/prime/55'>example</a>)<br>" \
           "/factor/&lt;n&gt; - factorizes n (<a target='_blank' href='/factor/55'>example</a>)<br>" \
           "/ping/&lt;host&gt;/&lt;n&gt; - pings given host n-times " \
           "(<a target='_blank' href='/ping/google.com/5'>example</a>)<br>"


@app.route("/prime/<int:n>")
def prime(n):
    """
    Нахождение n-го простого числаа
    """
    k = 1
    res = ""
    primes = 0
    while primes < n + 1:
        if is_prime(k):
            primes += 1
            res = str(k)
        k += 1
    return jsonify({'n': res})


@app.route("/factor/<int:n>")
def factor(n):
    """
    Разложение на простые множители
    """
    res = []
    i = 2
    while not is_prime(n):
        if is_prime(i) and n % i == 0:
            n = int(n / i)
            res.append(i)
            i = 2
        else:
            i += 1
    res.append(n)

    return jsonify(res)


@app.route("/ping/<host>/<int:n>")
def ping(host, n):
    """
    Пинг заданного сервера n раз
    """
    import os
    import platform
    success = 0
    for i in range(n):
        ping_str = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        if os.system("ping " + ping_str + " " + host) == 0:
            success += 1
        sleep(1)
    res = {'hostname': host, 'packages': {'sent': n, 'received': success}}
    return jsonify(res)


if __name__ == "__main__":
    app.run(threaded=True)