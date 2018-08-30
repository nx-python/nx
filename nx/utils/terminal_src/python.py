from io import StringIO
import traceback
import sys

class Python(object):
    def __init__(self, logging):
        self.TILED_DOUBLE = 1
        self.logger = logging

    def execute(self, code):
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_output = sys.stdout = StringIO()
        redirected_error = sys.stderr = StringIO()

        ns_globals = {}
        ns_locals = {}
        out, err, exc = None, None, None

        try:
            exec(code, ns_globals, ns_locals)
        except:
            exc = traceback.format_exc()

        out = redirected_output.getvalue()
        err = redirected_error.getvalue()

        # reset outputs to the original values
        sys.stdout = old_stdout
        sys.stderr = old_stderr

        return out, err, exc
