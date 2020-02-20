import sys, sqlite3, requests, datetime, pickle, argparse, tkinter as tk
from collections import defaultdict
from html.parser import HTMLParser


def create_connection(storage=None):
    # Create table for recording requests result
    if storage == None:
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()
    else:
        conn = sqlite3.connect(f"{storage}.db")
        cursor = conn.cursor()
    try:
        cursor.execute("""CREATE  TABLE IF NOT EXISTS tagtable (name VARCHAR(20), url VARCHAR(50),
                        checkdate DATE, tags BLOB)""")
    except Exception as e:
        print(e)
    finally:
        conn.commit()
    return conn


# define class for working with db
class db(object):
    def __init__(self, conn):
        self.conn = conn
        self.inner_cursor = conn.cursor()

    def save(self, site_name, url, now, tags):
        sql = f"INSERT INTO tagtable VALUES('{site_name}','{url}','{now}', ?)"
        self.inner_cursor.execute(sql, (tags,))
        self.conn.commit()

    def load(self, url):
        sql = f"SELECT DISTINCT * FROM tagtable WHERE url = '{url}';"
        self.inner_cursor.execute(sql)
        return self.inner_cursor.fetchall()

    def show(self, result):
        tags = pickle.loads(result[-1][-1])
        print("SITE: ", result[0][0])
        print("URL: ", result[0][1])
        print("DATE: ", result[0][2])
        print("TAGS: \n", dict(tags))

# class for graphical interface
class Interface(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

 #       self.get = tk.Button(self, text="get", fg="green", command=getPage(url))
 #       self.view = tk.Button(self, text="view", fg="green", command=viewPage(url))

        self.quit = tk.Button(self, text="leave", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


# Custom exception type for http response, we need only html
class FormatException(Exception):
    def __init__(self, contype):
        self.message = f"Inappropriate format {contype}, text/html; is expected"


# HTML parser for counting tags
class parser(HTMLParser):
    tagdict = defaultdict(int)

    def handle_starttag(self, tag, attr):
        self.tagdict[tag] += 1

def getPage(url):
    # load and parse page
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

def viewPage(url):
    try:
        result = dbquery.load(url)
        dbquery.show(result)
    except IndexError as e:
        print('{}\nThere is no such data in DB, you need to use --get instead'.format(sys.exc_info()[0]))


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

arg_len = len(sys.argv)
if arg_len == 1:
    root = tk.Tk()
    app = Interface(master=root)
    app.mainloop()
elif arg_len > 3:
    print('incorrect number of arguments,', arg_message)
    exit(0)
elif arg_len == 3:
    method = sys.argv[1]
    if method != '--get' and method != '--view':
        print('incorrect method,', arg_message)
        exit(0)
    # define url
    url = sys.argv[2]
    # create connection to db
    conn = create_connection('homework')
    # create object of db class
    dbquery = db(conn)

    if method == '--get':
        getPage(url)


    if method == '--view':
        viewPage(url)
else:
    pass
