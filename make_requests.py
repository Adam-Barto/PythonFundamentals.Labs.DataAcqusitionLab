from urllib import request
import json


token = 'ByIYbVDPnRpUdoaCtYcUtRAarxTZpOCS' # Yeah this is a bad idea to post this sorta stuff on Github.
file_save_location = 'outputfiles' # This is made to store the files
num = 0
offset = 1
limit = 1 # should have kept this small
amount = 39

for i in range(amount):
    url_string = f'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?offset={offset}&limit={limit}'
    the_request = request.Request(url_string, headers={'token': token})
    with request.urlopen(the_request) as f:
        the_json = json.loads(f.read())
        with open(file_save_location + f'/locations_{num}.json', 'w') as f:
            json.dump(the_json, f)
        num += 1
        offset += 1000

