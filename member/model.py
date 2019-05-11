import sqlite3
import os

class MemberDAO:

    def __init__(self):
        self._conn = sqlite3.connect('sqlite.db')

    @staticmethod
    def db_path():
        path = os.getcwd()
        basename = os.path.basename(os.getcwd())
        if(basename=='member'):
            db_path = path.replace(basename, '')
        else:
            db_path = basename
        print('db 경로'+ db_path)
        return db_path

    def create(self):
        sql = """
            CREATE TABLE IF NOT EXISTS Persons (
                userid varchar(10) primary key,
                password varchar(10),
                name varchar(10),
                phone varchar(15),
                address varchar(10),
                regdate date default current_timestamp 
            );
        """
        print('쿼리 체크: {} '.format(sql))
        self._conn.execute(sql)
        self._conn.commit()

    def insert_one(self, userid, password, name, phone, address):
        sql = """
                   INSERT INTO Persons (
                   userid, password, name, phone, address)
                    VALUES (
                    ?, ?, ?, ?, ?); 
                """
        self._conn.execute(sql, userid, password, name, phone, address)
        self._conn.commit()

    def insert_many(self):
        data = [('lee', '1', '이순신', '010-1234-5678', '사당'),
                ('hong', '1', '홍길동', '010-2345-4121', '강남'),
                ('Kang', '1', '강감찬', '010-5555-6666', '부산')]
        sql = """
           INSERT INTO Persons (
           userid, password, name, phone, address)
            VALUES (
            ?, ?, ?, ?, ?); 
        """
        self._conn.executemany(sql, data)
        self._conn.commit()

    def fetch_one(self, userid) -> object:
        sql = """
                    SELECT * FROM Persons WHERE userid LIKE ?;
                """
        cursor = self._conn.execute(sql, userid)
        row = cursor.fetchone()
        return row

    def fetch_all(self) -> object:
        sql = """
            SELECT * FROM Persons;
        """
        cursor = self._conn.execute(sql)
        rows = cursor.fetchall()
        return rows

    def count_all(self) -> object:
        sql = """
                   SELECT COUNT(*) FROM Persons;
               """
        cursor = self._conn.execute(sql)
        row = cursor.fetchone()
        return row

    def update(self, userid, password):
        sql = """
            UPDATE Persons
            SET password = ?
            WHERE userid = ?;
        """
        self._conn.execute(sql, password, userid)
        self._conn.commit()

    def remove(self, userid):
        sql = """
            DELETE FROM Persons WHERE userid=? ;
        """
        self._conn.execute(sql, userid)
        self._conn.commit()

    def login(self, userid, password):
        sql = """
            SELECT * FROM Persons
            WHERE userid LIKE ?
                AND password LIKE ?
        """
        data = [userid, password]
        cursor = self._conn.execute(sql, data)
        row = cursor.fetchone()
        print('로그인한 회원정보 {}'.format(row))
        return row

