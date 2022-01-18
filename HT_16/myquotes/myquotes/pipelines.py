# -*- coding: utf-8 -*-
# Define your item pipelines here

import sqlite3                                                    # import to work with the database sqlite3


class SaveToDataBasePipeLine(object):
    """
    A class for creating and updating the sqlite3
    database and loading our scraper into the database
    """
    def __init__(self):
        """
        Initialize variables to connect to and
        work with the database, using the __init__ method
        """
        self.con = sqlite3.connect('news.db')
        self.cur = self.con.cursor()
        self.create_or_update_table()

    def create_or_update_table(self):
        """
        Create a table in the database and delete the data of our scraper
        before a new load to overwrite the data in the database,
        using special commands of the sqlite3 library
        """
        self.cur.execute("""CREATE TABLE IF NOT EXISTS news(
        date TEXT,
        title TEXT,
        text TEXT,
        tegs TEXT,
        url TEXT 
        )""")

        self.cur.execute("""DELETE FROM news""")

    def process_item(self, item, spider):
        """
        Load our scraper data as an object with the type key-value
        into the database and save the changes with the commit,
        using special commands of the sqlite3 library

        :return our object with scraper data as a key-value
        """
        self.cur.execute("""INSERT INTO news VALUES (?, ?, ?, ?, ?)""",
                         (item['date'], item['title'], item['text'], item['tegs'], item['url']))
        self.con.commit()
        return item



#print(help(SaveToDataBasePipeLine()))                                # uncomment to review the documentation
