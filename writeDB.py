from flask import Flask, request
import pymysql

app = Flask(__name__)


@app.route('/register', methods=['POST'])
def writeData(FormRequest):
    course_name = FormRequest["course_name"]
    course_name = course_name.replace(" ", "_")
    sql_q = "INSERT INTO `users1_table`("
    sql_q += "FirstName, LastName, user_email,"
    if FormRequest["user_phone"] != None:
        sql_q += "user_phone, "
    sql_q += course_name + ") VALUES (N'"
    sql_q += FormRequest["FirstName"]+"',N'" + \
        FormRequest["LastName"]+"','"+FormRequest["user_email"]+"','"
    if FormRequest["user_phone"] != None:
        sql_q += FormRequest["user_phone"]
    sql_q += "',1);"

    my_conncetion = pymysql.connect(
        host='c58793.sgvps.net', user='uuxcegdmba9et', password='cbgf66yt2plw', db='dbu285dkqs78on')

    a = my_conncetion.cursor()
    try:
        a.execute(sql_q)
    except:
        print("ERROR writing to user's table failed")
    my_conncetion.commit()

    return
