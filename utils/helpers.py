from models import models


def resolve_sub_county(data):
    for e in data:
        sub_county = models.SubCounties.query.get(e['sub_county'])
        e['sub_county'] = {
            'name': sub_county.__dict__['name'],
            'id': sub_county.__dict__['id']
        }
    return data
