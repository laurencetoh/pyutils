import datetime
import os
import sys


def get_timestamp_str():
    """Gets the timestamp string YYYYmmDD_HHMMSS
    :return: string
    """
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')


def print_to_file(filename):
    """Redirects print function to a file
    :param filename: filename
    """
    sys.stdout = open(filename, 'w')


def print_disable():
    """Disables the print function"""
    sys.stdout = open(os.devnull, 'w')


def print_enable():
    """Enables back the print function"""
    sys.stdout = sys.__stdout__


if __name__ == '__main__':
    print('This will print')

    # print_disable()
    print_to_file('print_log.txt')
    print("This won't")

    print_enable()
    print("This will too")
