from flask_restful import Resource


class UsersController(Resource):
    def get(self):
        return {
            "message": 'get users successful'
        }

    def post(self):
        return {
            'message': 'post method successful'
        }

    def put(self):
        return {
            'message': 'put method successful'
        }

    def delete(self):
        return {
            'message': 'delete method successful'
        }
