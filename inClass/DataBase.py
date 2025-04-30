import sqlite3

class sqlBase:
    def __init__(self, path: str) -> None:
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()

    def customOp(self, func):
        return func(self.cur)

    def stringOp(self, sql: str):
        return self.cur.execute(sql)
    
    def finished(self):
        self.conn.commit()
        self.conn.close()       

def main(func):
    conn = sqlite3.connect("contact.db")

    cur = conn.cursor()

    func()

    conn.commit()
    conn.close()


def performOp (cur):
    #perform operations
    sql = """ operations """
    cur.execute(sql)


if __name__ == "__main__":
    main(performOp)