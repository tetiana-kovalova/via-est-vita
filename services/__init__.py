import requests

from settings import Settings


class RestApi(object):

    @classmethod
    def get(cls, group, mode, data):
        uri = (Settings.MAPBOX
               + group + '/v5/mapbox/'
               + mode + '/'
               + data + '?access_token='
               + Settings.ACCESS_TOKEN).replace(',', '%2C').replace(';', '%3B')

        response = requests.get(uri)
        assert response.status_code == 200, 'Invalid request or service not available'

        return response.json()

    @classmethod
    def retrieve_directions(cls, mode, data):
        return cls.get('directions', mode, data)
