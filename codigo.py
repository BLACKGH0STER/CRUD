from flask import Flask, render_template, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')

app.config['MYSQL_HOST']='162.241.62.85'; 
app.config['MYSQL_USER']='funda471_clases';	
app.config['MYSQL_PASSWORD']='Clases2023*';	
app.config['MYSQL_DB']='funda471_clases';		
mysql = MySQL(app)                                                          

if __name__=='__main__':
	#link = mysql.connection.cursor()
	#       link.execute(SELECT * FROM tabla)
	#result = link.fetchall()
	app.run(port=5000, debug=True) 