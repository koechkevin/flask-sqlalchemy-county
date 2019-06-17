from models.database import ma


class SubCountiesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


class WardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'sub_county')


class LocationsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'ward')


class SubLocationsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'location')


class VillageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'sub_location')


sub_counties_schema = SubCountiesSchema(many=True, strict=True)
sub_county_schema = SubCountiesSchema(strict=True)

ward = WardSchema(strict=True)
wards = WardSchema(many=True, strict=True)

location = LocationsSchema(strict=True)
locations = LocationsSchema(strict=True, many=True)

sub_location = SubLocationsSchema(strict=True)
sub_locations = SubLocationsSchema(strict=True, many=True)

village = VillageSchema(strict=True)
villages = VillageSchema(many=True, strict=True)
