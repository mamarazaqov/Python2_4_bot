import sqlite3
class Database:
    def __init__(self,baza_manzil):
        self.baza = baza_manzil


    @property
    def connection(self):
        return sqlite3.connect(self.baza)
    def execute(self,sql:str,paratmetrs: tuple=None,fetchone=False,fetchall=False,commit=False):
        if not paratmetrs:
            paratmetrs= ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql,paratmetrs)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return  data


    @staticmethod
    def format_args(sql,paratmetrs: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in paratmetrs
        ])
        return  sql,tuple(paratmetrs.values())

    def add_user(self,id:int,name:str,email:str = None,language: str = 'uz'):

        sql = """
            INSERT INTO users(id, Name, email, language) VALUES(?, ?, ?, ?)
            """
        self.execute(sql,paratmetrs=(id,name,email,language), commit=True)

    def selecet_all_user(self):
        sql = """"
        SELECT * FROM users 
        """
        return self.execute(sql,fetchall=True)
    def select_user(self, **kwargs):

        sql = "SELECT * FROM users WHERE "
        sql, paratmetrs = self.format_args(sql, kwargs)
        return sql.execute(sql, paratmetrs=paratmetrs,fetchone=True)

    def count_user(self):
        return self.execute("SELECT COUNT(*) FROM users;",fetchone=True)

    def delet_users(self):
        self.execute("DELETE FROM users WHERE TRUE",commit=True)


    def user_sanash(self):
        return self.execute("SELECT COUNT(*) FROM users;", fetchone=True)


    def user_qoshish(self, ism:str,tg_id = int,fam:str = None,username:str=None):

        sql = """
            INSERT INTO users(ism,fam,tg_id,username) VALUES(?, ?, ?, ?)
            """
        self.execute(sql,paratmetrs=(ism,fam,tg_id,username), commit=True)
    def selecet_XAMMA_user(self):
        sql = """
           SELECT * FROM users 
           """
        return self.execute(sql,fetchall=True)
    def selecet_barcha_menu(self):
        sql = """
           SELECT * FROM menu 
           """
        return self.execute(sql,fetchall=True)

    def select_maxsulotlar(self, **kwargs):

        sql = "SELECT * FROM maxsulotlar WHERE "
        sql, paratmetrs = self.format_args(sql, kwargs)
        return self.execute(sql, paratmetrs=paratmetrs, fetchall=True)
    def selecet_barcha_maxsulotlar(self):
        sql = """
           SELECT * FROM maxsulotlar 
           """
        return self.execute(sql,fetchall=True)

    def select_maxsulot(self, **kwargs):

        sql = "SELECT * FROM maxsulotlar WHERE "
        sql, paratmetrs = self.format_args(sql, kwargs)
        return self.execute(sql, paratmetrs=paratmetrs, fetchone=True)

    # 2
    def selecet_barcha_menu1(self):
        sql = """
           SELECT * FROM menus 
           """
        return self.execute(sql,fetchall=True)

def logger(statement):
    print(f"""
    ----------------------------------------------------
    Executing:
    {statement}
    ----------------------------------------------------
""")