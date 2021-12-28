import mysql.connector


# Local
db = mysql.connector.connect(
    host='localhost',
    user='dev',
    password='Lp12345678',
    database='metronomo_db'
)

# Hosting
# db = mysql.connector.connect(
#     host='luispelaez.mysql.pythonanywhere-services.com/',
#     user='luispelaez',
#     password='Lp12345678',
#     database='luispelaez$metronomo_db'
# )
class Cancion:

    # def __init__(self):
    #     self.user = 'luispelaez'
    #     self.password = 'Lp12345678'
    #     self.host = 'luispelaez.mysql.pythonanywhere-services.com'
    #     self.database = 'luispelaez$metronomo_db'
    
    def __init__(self):
        self.user = 'dev'
        self.password = 'Lp12345678'
        self.host = 'localhost'
        self.database = 'metronomo_db'

    def connection(self):
        db = mysql.connector.connect(
             host= self.host,
             user=self.user,
             password=self.password,
             database=self.database
        )

        return db, db.cursor(dictionary=True)


    def select(self):
        db, cursor = self.connection()
        sql = 'select * from Cancion ORDER BY cancion ASC'
        cursor.execute(sql)
        res = cursor.fetchall()
        return res

    def add(self, cancion, bpm, compas):
        db, cursor = self.connection()
        sql = "insert into Cancion(cancion, bpm, compas) values (%s, %s, %s)"
        values = (cancion, bpm, compas)
        cursor.execute(sql, values)
        db.commit()

    def edit_page(self, id):
        db, cursor = self.connection()
        sql = f"select * from Cancion where id = {id}"
        cursor.execute(sql)
        res = cursor.fetchone()
        return res

    def edit(self, id, cancion, bpm, compas):
        db, cursor = self.connection()
        sql = f"update Cancion set cancion=%s, bpm=%s, compas=%s where id = {id}"
        values = (cancion, bpm, compas)
        cursor.execute(sql, values)
        db.commit()

    def delete(self, id):
        db, cursor = self.connection()
        sql = f'delete from Cancion where id={id}'
        cursor.execute(sql)
        db.commit()
