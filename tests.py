import unittest


class TestDBMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(cls).setUpClass()




    def setUp(self):
        self.tags = {'html': 1, 'head': 1, 'meta': 13, 'base': 1, 'link': 7, 'title': 1, 'script': 7, 'body': 1,
                     'div': 31, 'a': 5, 'h1': 1, 'b': 1, 'span': 1, 'form': 1, 'dl': 2, 'dd': 2, 'input': 3, 'i': 1,
                     'img': 2}
        self.conn = create_connection()
        self.cursor = self.conn.cursor()
        self.testdb = db(self.conn)
        self.insert_tags = pickle.dumps(self.tags, 2)


    def tearDown(self):
        pass

    def testInsert(self):
        site_name, url, now = 'vk', 'https://vk.com', '2019-04-25'
        # pickle.loads(tags[-1][-1]


        self.testdb.save(site_name, url, now, self.insert_tags)
        self.cursor.execute(f"SELECT tags FROM tagtable WHERE url = '{url}' \
         AND name = '{site_name}' AND checkdate = '{now}'")
        self.result = self.cursor.fetchall()
        self.assertDictEqual(self.tags, pickle.loads(self.result[-1][-1]))