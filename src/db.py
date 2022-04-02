"""
@version:1.0
@author: endaqa
@file db.py
@time 2022/4/1 16:50
"""
import pymysql
import pymysql.cursors

db_conf = {"host": '119.91.135.29',
           # "name": 'zujuan_paper',
           "name": 'zhiyuan_sd',
           "user": 'root',
           "password": 'rYa+wq10dFTWzYz8FeZgsWRygyKfLKULSRdKfRnEgSk=',
           "charset": 'utf8mb4',
           "port": 3306}


# from sqlalchemy import create_engine


class DataBase:
    def __init__(self,):

        self._db = None
        self._cursor = None
        self._engine = None

        self._db = pymysql.connect(host=db_conf['host'], user=db_conf['user'],
                                   password=db_conf['password'],
                                   db=db_conf['name'], charset=db_conf['charset'],
                                   port=db_conf['port'], autocommit=True)

    def get_engine(self):
        return self._engine

    def get_cursor(self, cursor_type=1):
        """
        返回游标
        :param cursor_type:
        :return: 返回一个可用数据库游标来操作数据库，返回类型由cursor_type的值决定
        """

        if cursor_type == 1:
            self._cursor = self._db.cursor(pymysql.cursors.DictCursor)
        elif cursor_type == 2:
            self._cursor = self._db.cursor()
        elif cursor_type == 3:
            self._cursor = self._db.cursor(pymysql.cursors.SSDictCursor)
        else:
            self._cursor = self._db.cursor(pymysql.cursors.SSCursor)

        return self._cursor

    def close(self):
        if self._cursor:
            self._cursor.close()
        if self._db:
            self._db.commit()
            self._db.close()
