from controllers.users import UsersController
from controllers.locations import LocationsController
from controllers.sub_counties import ListCreateSubCounties, RetrieveUpdateDeleteSubCounties
from controllers.sub_locations import SubLocationsController
from controllers.wards import ListCreateWards,RetrieveUpdateDeleteWard
from controllers.villages import VillageController

controllers = [
    [UsersController, '/users'],
    [ListCreateSubCounties, '/sub-counties'],
    [RetrieveUpdateDeleteSubCounties, '/sub-counties/<int:pk>'],
    [ListCreateWards, '/wards'],
    [RetrieveUpdateDeleteWard, '/wards/<int:pk>'],
    [LocationsController, '/locations'],
    [SubLocationsController, '/sub-locations'],
    [VillageController, '/villages']
]


def resources(api):
    for each in controllers:
        api.add_resource(each[0], each[1])
    return api


