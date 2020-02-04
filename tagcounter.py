import sys, sqlite3, requests, datetime, pickle
from collections import defaultdict
from html.parser import HTMLParser

# Create table for recording requests result
conn = sqlite3.connect("homework.db")
cursor = conn.cursor()
try:
    cursor.execute("""CREATE  TABLE IF NOT EXISTS tagtable (name VARCHAR(20), url VARCHAR(50),
                    checkdate DATE, tags BLOB)""")
except Exception as e:
    print(e)
finally:
    conn.commit()


# Define class for working with db
class db(object):
    def __init__(self, conn):
        self.conn = conn
        self.inner_cursor = conn.cursor()

    def save(self, site_name, url, now, tags):
        self.sql = f"INSERT INTO tagtable VALUES('{site_name}','{url}','{now}', ?)"
        self.inner_cursor.execute(self.sql, (tags,))
        self.conn.commit()

    def load(self, url):
        self.url = url
        self.sql = f"SELECT DISTINCT * FROM tagtable WHERE url = '{url}';"
        self.inner_cursor.execute(self.sql)
        return self.inner_cursor.fetchall()

    def show(self, result):
        self.tags = pickle.loads(result[-1][-1])
        print("SITE: ", result[0][0])
        print("URL: ", result[0][1])
        print("DATE: ", result[0][2])
        print("TAGS: \n", dict(self.tags))


# Custom exception type for http response, we need only html
class FormatException(Exception):
    def __init__(self, contype):
        self.message = f"Inappropriate format {contype}, text/html; is expected"


# HTML parser for counting tags
class parser(HTMLParser):
    tagdict = defaultdict(int)

    def handle_starttag(self, tag, attr):
        self.tagdict[tag] += 1


# Function for making http get request
def load_html(url: str):
    """

    :param url:
    :return:
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        contype = response.headers['Content-Type']
        print(type(contype))
        if 'text/html' not in contype:
            raise FormatException(contype)
        if 'utf-8' not in contype:
            response.encoding = 'utf-8'
        return (response.text)
    except FormatException as format_err:
        print(format_err.message)
    except Exception as e:
        print('An error occurs while http request: {}'.format(sys.exc_info()[0]))


# Parse arguments
arg_message = 'use it in this way:\nmain.py --get/view url'
method = sys.argv[1]
arg_len = len(sys.argv)
if arg_len > 3 or arg_len < 3:
    print('incorrect number of arguments,', arg_message)
    exit(0)
if method != '--get' and method != '--view':
    print('incorrect method,', arg_message)
    exit(0)
url = sys.argv[2]
# Create object of db class
dbquery = db(conn)

if method == '--get':
    page = load_html(url)
    myparser = parser()
    myparser.feed(page)
    # Define variable for db queries
    site_name = url.split('.')[-2].split(':')[1].replace('/', '')
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    tags = pickle.dumps(myparser.tagdict, 2)
    # save result to db
    dbquery.save(site_name, url, now, tags)
    # load result from db
    result = dbquery.load(url)
    # show result from db
    dbquery.show(result)
if method == '--view':
    try:
        result = dbquery.load(url)
        dbquery.show(result)
    except IndexError as e:
        print('{}\nThere is no such data in DB, you need to use --get instead'.format(sys.exc_info()[0]))
