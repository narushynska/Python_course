import sys
from cStringIO import StringIO

class Logger():
    def __init__(self, argument):
        self.log_file = argument

    def __call__(self, fn):
        def captured(*args, **kwargs):
            backup = sys.stdout

            sys.stdout = StringIO()
            res = fn(*args, **kwargs)
            out = sys.stdout.getvalue()

            sys.stdout.close()
            sys.stdout = backup

            log = open(self.log_file, 'a+')
            log.write(out)
            log.close()
            return res

        return captured
