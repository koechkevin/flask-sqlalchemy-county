from urls import resources
from models import database
from flask_restful import Api


app = database.app
api = Api(app=app, prefix='/api/v1')
resources(api)

if __name__ == '__main__':
    app.run(debug=True)
