from flask import request, jsonify
from flask_restful import Resource
from models import models, database
from schemas import schemas
from utils import helpers


class ListCreateWards(Resource):
    def get(self):
        all_wards = database.db.session.query(models.Wards)
        result = schemas.wards.dump(all_wards)
        data = helpers.resolve_sub_county(result.data)
        return jsonify(data)

    def post(self):
        name = request.get_json()['name']
        sub_county = request.get_json()['sub_county']
        db = database.db
        new_ward = models.Wards(name, sub_county)
        db.session.add(new_ward)
        db.session.commit()
        return schemas.ward.jsonify(new_ward)


class RetrieveUpdateDeleteWard(Resource):
    def get(self, pk):
        ward = models.Wards.query.get(pk)
        return schemas.ward.jsonify(ward)

    def put(self, pk):
        ward = models.Wards.query.get(pk)
        name = request.get_json()['name']
        sub_county = request.get_json()['sub_county']
        ward.name = name
        ward.sub_county = sub_county
        db = database.db
        db.session.commit()
        return schemas.ward.jsonify(sub_county)

    def delete(self, pk):
        ward = models.Wards.query.get(pk)
        db = database.db
        db.session.delete(ward)
        db.session.commit()
        return {'message': 'delete method successful', 'id': pk}
