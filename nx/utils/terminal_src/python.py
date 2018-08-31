import inspect
from contextlib import redirect_stdout
import io


class Python(object):
    def __init__(self, logging):
        self.TILED_DOUBLE = 1
        self.logger = logging

    def cleanup_code(self, content):
        """
        Clean up the code
        """
        # remove `foo`
        return content.strip('` \n')

    def get_syntax_error(self, e):
        if e.text is None:
            return '{0.__class__.__name__}: {0}'.format(e)
        return '{0.text}{1:>{0.offset}}\n{2}: {0}'.format(e, '^', type(e).__name__)

    def repl(self, raw_code):
        variables = {
            'by': 'PuffDip',
            'message': '',
            '_': None,
        }
        cleaned = self.cleanup_code(raw_code)
        if cleaned in ('quit', 'exit', 'exit()'):
            pass # TODO quit terminal

        executor = exec

        # if there are no new lines this is protentional a one liner
        if cleaned.count('\n') == 0:
            try:
                code = compile(cleaned, '<repl session>', 'eval')
            except SyntaxError:
                pass
            else:
                executor = eval

        if executor is exec:
            try:
                code = compile(cleaned, '<repl session>', 'exec')
            except SyntaxError as e:
                return str(self.get_syntax_error(e))

        variables['message'] = raw_code
        fmt = None
        stdout = io.StringIO()
        try:
            with redirect_stdout(stdout):
                result = executor(code, variables)
                if inspect.iscode(result):
                    result = result
        except Exception as e:
            value = stdout.getvalue()
            return str(value)
        else:
            value = stdout.getvalue()
            if result is not None:
                fmt = '{}{}'.format(value, result)
                variables['_'] = result
            elif value:
                fmt = value

        if fmt is not None:
            return str(fmt)
