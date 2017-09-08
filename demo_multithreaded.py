from __future__ import print_function
import threading
import socket
import sys
import time
import requests

urls = ['https://www.chegg.com/tutors/Computer-Science-online-tutoring/',
        'https://www.chegg.com/tutors/Programming-online-tutoring/',
        'https://www.chegg.com/tutors/Electrical-Engineering-online-tutoring/',
        'https://www.chegg.com/tutors/Mechanical-Engineering-online-tutoring/',
        'https://www.chegg.com/tutors/Python-Programming-online-tutoring/',
        'https://www.chegg.com/tutors/Java-Programming-online-tutoring/',
        'https://www.chegg.com/tutors/HTML-Programming-online-tutoring/',
        'https://www.chegg.com/tutors/C++-Programming-online-tutoring/',
        'https://www.chegg.com/tutors/C-Sharp-Programming-online-tutoring/',
        'https://www.chegg.com/tutors/C-Programming-online-tutoring/',
        'https://www.chegg.com/tutors/Algebra-online-tutoring/',
        'https://www.chegg.com/tutors/Calculus-online-tutoring/',
        'https://www.chegg.com/tutors/Trigonometry-online-tutoring/',
        'https://www.chegg.com/tutors/Statistics-online-tutoring/',
        'https://www.chegg.com/tutors/Geometry-online-tutoring/',
        'https://www.chegg.com/tutors/Chemistry-online-tutoring/',
        'https://www.chegg.com/tutors/Physics-online-tutoring/',
        'https://www.chegg.com/tutors/Accounting-online-tutoring/',
        'https://www.chegg.com/tutors/Economics-online-tutoring/',
        'https://www.chegg.com/tutors/Finance-online-tutoring/']

def do_fetch(url):
    i = 10**6
    while i > 0:
        i -= 1 # Deliberately slow code

def worker():
    while True:
        try:
            do_fetch(urls.pop())
        except IndexError:
            break # Done.

def fetch_multithraded():
    threads = []
    for _ in range(10):
        t = threading.Thread(target=worker)
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()


if __name__ == '__main__':
    start_time = time.time()
    fetch_multithraded()
    print(time.time() - start_time)
