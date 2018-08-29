import urllib.parse
import urllib.request

class Utils(object):
    def __str__(self):
        return "Our screen objects will be created here"

    def __init__(self):
        pass

    def export(self, cli_history):
        """
        Export CLI history to hastebin
        :return: hastebin url
        """
        # If there is nothing to copy
        if len(cli_history) <= 0:
            # Return None
            return "Nothing to export"
        else:
            # API Pastebin
            url = "http://pastebin.com/api/api_post.php"

            # Reverse the content of the list
            # This way the last event will be the first
            tmp_cli = cli_history[::]
            tmp_cli.reverse()
            data = "\n".join(tmp_cli)


            values = {'api_option': 'paste',
                      'api_dev_key': '12527a93ee3ee6540683fed9704be9f0',
                      'api_paste_code': data,
                      'api_paste_private': '0',
                      'api_paste_name': None,
                      'api_paste_format': 'python', }

            data = urllib.parse.urlencode(values)
            data = data.encode('utf-8')
            req = urllib.request.Request(url, data)
            t = urllib.request.Request(url, data)
            with urllib.request.urlopen(req) as response:
                the_page = response.read().decode()
            return str(the_page)
