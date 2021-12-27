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

cursor = db.cursor(dictionary=True)

class Cancion:
    
    def select(self):
        sql = 'select * from Cancion ORDER BY cancion ASC'
        cursor.execute(sql)
        res = cursor.fetchall()
        return res

    def add(self, cancion, bpm):
        sql = "insert into Cancion(cancion, bpm) values (%s, %s)"
        values = (cancion, bpm)
        cursor.execute(sql, values)
        db.commit()

    def edit_page(self, id):
        sql = f"select * from Cancion where id = {id}"
        cursor.execute(sql)
        res = cursor.fetchone()
        return res

    def edit(self, id, cancion, bpm):
        sql = f"update Cancion set cancion=%s, bpm=%s where id = {id}"
        values = (cancion, bpm)
        cursor.execute(sql, values)
        db.commit()

    def delete(self, id):
        sql = f'delete from Cancion where id={id}'
        cursor.execute(sql)
        db.commit()
