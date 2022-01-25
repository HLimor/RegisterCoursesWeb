from cgitb import text
import email
from email.message import EmailMessage
from tkinter.tix import INTEGER
import pymysql


class fetchData:
    def build_users_table(rows_data):

        sql_q = "CREATE TABLE IF NOT EXISTS `users1_table`( `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,`FirstName` varchar(45) NOT NULL,`LastName` varchar(45) NOT NULL,`user_email` TEXT NOT NULL, `user_phone` INTEGER NULL,"
        for item in rows_data:
            course_name = item[1]
            course_name = course_name.replace(" ", "_")
            sql_q += "`"+course_name+"`" + " TEXT NULL , "

        sql_q += ' PRIMARY KEY (`id`),KEY `id` (`id`));'

        my_conncetion = pymysql.connect(
            host='c58793.sgvps.net', user='uuxcegdmba9et', password='cbgf66yt2plw', db='dbu285dkqs78on')

        a = my_conncetion.cursor()
        mssg = ""
        try:
            mssg = a.execute(sql_q)
        except:
            print("ERROR building user's table ", mssg)

    def fetch_data():
        my_conncetion = pymysql.connect(
            host='c58793.sgvps.net', user='uuxcegdmba9et', password='cbgf66yt2plw', db='dbu285dkqs78on')

        a = my_conncetion.cursor()

        sql_q = 'SELECT * from `track_name`;'

        a.execute(sql_q)

        all_data = a.fetchall()
        sql_q = 'SELECT COUNT(*) from `users1_table`;'
        try:
            num_rows = a.execute(sql_q)
        except:
            print("Building new user's")
            fetchData.build_users_table(all_data)

        return all_data
