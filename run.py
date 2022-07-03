from flask import Flask
from flask_restful import Resource, Api
from db_con import db
#from resources.user import Users, Home
from resources.user import *
from resources.admin import *
import os
#from dotenv import load_dotenv
#load_dotenv()

app=Flask(__name__)
#Use for plain joining api with mysql
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:akashmukherjee@localhost/student'
#Use for mysql container with local machine mysql
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:akashmukherjee@akash-mysql/student'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:{}@{}/{}".format(os.getenv('MYSQL_ROOT_PASSWORD'),os.getenv('HOST_NAME'),os.getenv('DB_NAME'))
print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

api = Api(app)
api.add_resource(User, '/')
api.add_resource(Login, '/login')
api.add_resource(Authentication, '/auth')
api.add_resource(Admin, '/admin')


if __name__== "__main__":
    
    app.run(debug=True, host="0.0.0.0", port="5001", use_reloader=True)
    #print(app)
