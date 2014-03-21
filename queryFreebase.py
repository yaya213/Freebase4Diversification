import json
import urllib

def query(query_string):
	service_url = 'https://www.googleapis.com/freebase/v1/search'
	params = {
       	'query': query_string,
        'key': 'AIzaSyByQFSydeBulZx9nhgdu5zqUWtdvwi-x9A',
		'limit': 200
	}
	url = service_url + '?' + urllib.urlencode(params)
	response = json.loads(urllib.urlopen(url).read())
	rank_list = []
	for result in response['result']:
		rank_list.append(result['mid'])
	return rank_list
