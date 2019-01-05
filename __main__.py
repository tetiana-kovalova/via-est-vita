from constants import Mode
from services import RestApi

print('Via est vita!\n')

walking_duration = RestApi.retrieve_directions(Mode.WALKING, '-73.989,40.733;-74,40.733')['routes'][0]['duration']
cycling_duration = RestApi.retrieve_directions(Mode.CYCLING, '-73.989,40.733;-74,40.733')['routes'][0]['duration']
driving_duration = RestApi.retrieve_directions(Mode.DRIVING, '-73.989,40.733;-74,40.733')['routes'][0]['duration']

print(f'Duration by foot: {walking_duration}\n'
      f'Duration by bike: {cycling_duration}\n'
      f'Duration by car: {driving_duration}')
