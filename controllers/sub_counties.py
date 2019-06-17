from flask import request, jsonify
from flask_restful import Resource
from models import models, database
from schemas import schemas


class ListCreateSubCounties(Resource):
    def get(self):
        all_sub_counties = models.SubCounties.query.all()
        result = schemas.sub_counties_schema.dump(all_sub_counties)
        return jsonify(result.data)

    def post(self):
        name = request.get_json()['name']
        db = database.db
        new_sub_county = models.SubCounties(name)
        db.session.add(new_sub_county)
        db.session.commit()
        return schemas.sub_county_schema.jsonify(new_sub_county)


class RetrieveUpdateDeleteSubCounties(Resource):
    def get(self, pk):
        sub_county = models.SubCounties.query.get(pk)
        return schemas.sub_county_schema.jsonify(sub_county)

    def put(self, pk):
        sub_county = models.SubCounties.query.get(pk)
        name = request.get_json()['name']
        sub_county.name = name
        db = database.db
        db.session.commit()
        return schemas.sub_county_schema.jsonify(sub_county)

    def delete(self, pk):
        sub_county = models.SubCounties.query.get(pk)
        db = database.db
        db.session.delete(sub_county)
        db.session.commit()
        return {'message': 'delete method successful', 'id': pk}
