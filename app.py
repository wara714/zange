# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import *

app = Flask(__name__)
@app.route('/',methods=["GET","POST"])

def hello():
    if request.method == "GET":
        return render_template("index.html") 
    else:
        try:
            text=format(str(request.form["zange"])) + "\n"
            print(text)
            f = open("data.txt","a")
            f.write(text)
            f.close()
            return render_template("index.html")
        except:
            print("error")
            return render_template("index.html")
            
if __name__ == "__main__":
    app.run()
