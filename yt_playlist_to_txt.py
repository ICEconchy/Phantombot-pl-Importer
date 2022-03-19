from urllib import request
from time import sleep
import sys
import math
import json

def get_api_data(token, playlist, page, data, amount):
	raw_data = request.urlopen(request.Request('https://www.googleapis.com/youtube/v3/playlistItems?playlistId={0}&key={1}&part=snippet&maxResults=50{2}'.format(playlist, token, page))).read()
	json_data = json.loads(raw_data.decode('utf-8'))

	if 'error' in json_data:
		print('Error while getting information from the API:', str(json_data['error']['message']))
		return None

	items = json_data['items']
	total = int(json_data['pageInfo']['totalResults'])

	# Add URLs to the array.
	for item in items:
		amount += 1
		data.append('https://youtu.be/' + item['snippet']['resourceId']['videoId'])
		sys.stdout.write('Importing {0}% complete... \r'.format(str(math.floor((amount / total) * 100))))
		sys.stdout.flush()

	# If there's another page, keep going but sleep for a few milliseconds.
	if 'nextPageToken' in json_data:
		# Sleep for 50ms.
		sleep(0.05)
		# Get the data.
		get_api_data(token, playlist, ('&pageToken=' + json_data['nextPageToken']), data, amount)

	return True


def main():
	#You can define your YouTube API key as a string with ''.
	API_TOKEN = None
	# You can define you playlist ID here as a string with ''.
	PLAYLIST = None
	# Data we get from YouTube.
	data = []

	# If token isn't set, as for one.
	while API_TOKEN == None:
		print('Please enter you YouTube API token: ', end='')
		API_TOKEN = input()

	# If playlist isn't set, as for one.
	while PLAYLIST == None:
		print('Please enter the playlist ID you want to import: ', end='')
		PLAYLIST = input()

	# Call the API and get all the songs.
	result = get_api_data(API_TOKEN, PLAYLIST, '', data, 0)

	if result == None:
		print('Something went wrong while getting data. Press any key to exit...')
		input()
	else:
		# File location here.
		file = open('playlist.txt', 'w')
		# Write the data.
		file.write('\n'.join(data))
		# Close the file.
		file.close()

		print('Done! Press any key to exit...')
		# Remove this if you want to script to auto exit.
		input()

main()
