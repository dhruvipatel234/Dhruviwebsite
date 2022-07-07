
from flask import Flask, render_template ,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Sanskar@localhost:81/system'
db = SQLAlchemy(app)



if __name__=="__main__":
    app.run(debug=True)
