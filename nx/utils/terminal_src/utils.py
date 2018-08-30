import urllib.parse
import urllib.request
import datetime

class Utils(object):
    def __str__(self):
        return "Our screen objects will be created here"

    def __init__(self, logging):
        self.logger = logging

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
            url = "http://dpaste.com/api/v2/"

            # Reverse the content of the list
            # This way the last event will be the first
            tmp_cli = cli_history[::]
            # tmp_cli.reverse() # Reverse is disabled because its unreadable
            data = "\n".join(tmp_cli)

            values = {'content': data,
                      'syntax': 'python',
                      'title': 'PyNX Terminal',
                      'expiry_days': 365,
                      }
            try:
                data = urllib.parse.urlencode(values)
                data = data.encode('utf-8')
                req = urllib.request.Request(url, data)
                t = urllib.request.Request(url, data)
                with urllib.request.urlopen(req) as response:
                    the_page = response.read().decode()
                self.logger.info("Around {} you exported the following url: {}".format(datetime.datetime.now(), the_page))
                return str(the_page)
            except Exception as e:
                self.logger.error(e)
                return str(e)

    def import_url(self, url):
        self.logger.info("Around {} you imported the following url: {}".format(datetime.datetime.now(), url))
        if url.startswith("http://dpaste.com/"):
            try:
                response = urllib.request.urlopen(url)
                html = response.read().decode()
                return str(html)
            except Exception as e:
                self.logger.error(e)
                return str(e)
        else:
            self.logger.info("Could not connect to website")
            return "Invalid import link"

