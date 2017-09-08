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
    requests.get(url)
    print('fetched %s' % url)

def fetch_sequential():
    for url in urls:
        do_fetch(url)

if __name__ == '__main__':
    start_time = time.time()
    fetch_sequential()
    print(time.time() - start_time)
