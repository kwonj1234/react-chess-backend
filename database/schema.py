import sqlite3
import os

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'chess.db')

# Initalize schema
def schema(dbpath = DBPATH):
    """ Creates brand new database for react-chess """

    with sqlite3.connect(dbpath) as connection:
        c = connection.cursor()

        # If the table already exists, drop it. This function is 
        for table in ["user", "match", "moves"]:
            c.execute(f"""DROP TABLE IF EXISTS {table}""")

        # Create user table. Users will have a unique id(pk), username, 
        # hash
        sql = """CREATE TABLE user (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(21)
            hash VARCHAR(256)
        );"""

        # Create match table. Every match has a unique id (pk) and the pk 
        # for the user playing the white pieces and the user playing the 
        # black pieces are recorded.
        sql = """CREATE TABLE match (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            white INTEGER,
            black INTEGER,
            FOREIGN KEY (white) REFERENCES user(pk),
            FOREIGN KEY (black) REFERENCES user(pk)
        );"""

        # Create moves tables. This will record every move ever played and 
        # correlate it with the match it belongs to
        sql = """CREATE TABLE moves (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            moveNum INTEGER,
            white VARCHAR(8),
            black VARCHAR(8),
            match_pk INTEGER,
            FOREIGN KEY (match_pk) REFERENCES match(pk)
        );"""

if __name__ == "__main__":
    schema()