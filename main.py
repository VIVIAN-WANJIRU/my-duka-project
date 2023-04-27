
from flask import Flask, render_template
import psycopg2

app=Flask(__name__)
try:
    conn = psycopg2.connect("dbname='myduka' user='postgres' host='localhost'port='5433' password='12345'")
    print("Database Connected Successfully")
except Exception as e:
    print ("I am unable to connect to the database", e)

@app.route("/")
def home():
    username = "VIVI K"
    return render_template("index.html", username=username)

@app.route("/products")
def products():

    products = [
        (1,"omo",40,50,100),
        (2,"bread",50,60,200),
        (3,"milk",60,65,150)
        
    ]
cur = conn.cursor()
cur.execute("""my-duka""")
rows = cur.fetchall()
print(rows)


    #
    #for i in products:
        #total = total + i[3]

   # return render_template("products.html", products=products)
app.run()
