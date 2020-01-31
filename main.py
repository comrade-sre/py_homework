import sys, sqlite3, requests
# Custom exception type for http response, we need only html
class FormatException(Exception):
    def __init__(self, contype):
        self.message = f"Inapropriate format {contype}, text/html; is expected"

# Function for making http get request
def load_html(url: str):
    """

    :param url:
    :return:
    """
    try:
        response = requests.get(url)
        contype =  response.headers['Content-Type'].split(';')
        if contype[0] != 'text/html':
            raise FormatException(contype)
        if contype[1] != 'utf-8':
            response.encoding = 'utf-8'
        return (response.text)
    except FormatException as format_err:
        print(format_err.message)
    except Exception as e:
        print('An error occurs while http request: {}'.format(sys.exc_info()[0]))


def parse_html(page):
    """

    :param page:
    :return:
    """
    pass

arg_message = 'use it in this way:\nmain.py --get/view url'
method = sys.argv[1]
arg_len = len(sys.argv)
if arg_len > 3 or  arg_len < 3:
    print('incorrect number of arguments,', arg_message)
    exit(0)
if sys.argv[1] != '--get':
    print('incorrect method,', arg_message)
    exit(0)
url = sys.argv[2]
print(load_html(url))

