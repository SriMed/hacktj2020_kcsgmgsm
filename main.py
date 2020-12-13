import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import pandas as pd
import pickle

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'd068d24aec2b4fc588d971b320d52c2f',
}

params = urllib.parse.urlencode({})

def get_storm_event_ids():
    try:
        conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
        conn.request("GET", "/snowiq/v1/historical-storms?%s" % params, "{body}", headers)
        response = conn.getresponse()
        storm_event_data = json.loads(response.read())
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    storm_event_ids = []
    for elem in storm_event_data:
        storm_event_ids.append(elem['stormEventId'])
    # print(storm_event_ids, len(storm_event_ids))

    data = []
    data_X = []
    data_y = []
    for elem in storm_event_data:
      try:
        conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
        conn.request("GET", "/snowiq/v1/historical-storms/" + str(elem['stormEventId']) +"/details?%s" % params, "{body}", headers)
        response = conn.getresponse()
        storm_info = json.loads(response.read())
        data.append([elem['stormEventId'], storm_info['eventName'], storm_info['predictedPrecipitation'], storm_info['predictedDuration'], storm_info['totalSnowfall'], storm_info['totalMilesPlowed'], storm_info['totalTimePlowed'], storm_info['totalAmountOfSaltUsed']])
        data_X.append([storm_info['predictedPrecipitation'], storm_info['predictedDuration']])
        data_y.append(storm_info['totalAmountOfSaltUsed'])
        conn.close()
      except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return data, data_X, data_y

data, data_X, data_y = get_storm_event_ids()
# df = pd.DataFrame(data, columns = ["Storm ID","Event Name","Predicted Precipitation","Predicted Duration","Total Snowfall","Total Miles Plowed","Total Time Plowed", "Total Salt Used"])
# print(df)
pickle.dump((data_X,data_y), open('data.p', 'wb'))
