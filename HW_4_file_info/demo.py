import os
import sys
from config import get_dict_config

PROPERTIES = get_dict_config('Extensions')


def filtering(file_name, input_extensions):
    for ext in input_extensions:
        try:
            extens = PROPERTIES[ext]
        except KeyError:
            print 'Incorrect extension {ext}'.format(ext=ext)
            extens = ''
        if file_name.endswith(tuple(extens)):
            return '{f} is {ext} file'.format(f=file_name, ext=ext)


def main():
    path = os.path.split(os.path.abspath(os.path.realpath(sys.argv[0])))[0]
    input_extensions = sys.argv[1:]
    for root, dirs, files in os.walk(path):
        for file_name in files:
            filt = filtering(file_name, input_extensions)
            if filt:
                print filt


if __name__ == '__main__':
    main()
