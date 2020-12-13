import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import pickle

headers = {'Ocp-Apim-Subscription-Key': 'd068d24aec2b4fc588d971b320d52c2f'}
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


    data, data_X, data_y = [], [], []
    for elem in storm_event_data:
      try:
        conn = http.client.HTTPSConnection('hacktj2020api.eastbanctech.com')
        conn.request("GET", "/snowiq/v1/historical-storms/" + str(elem['stormEventId']) + "/depots?%s" % params, "{body}", headers)
        response = conn.getresponse()
        storm_info = json.loads(response.read())

        for depot in storm_info:
            # data_X.append([elem['predictedPrecipitation'],  depot['totalSnowfall'], depot['totalMilesPlowed']])
            data_X.append([elem['predictedPrecipitation'], depot['totalMilesPlowed']])
            data_y.append(depot['totalAmountOfSaltUsed'])

        conn.close()
      except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    return data, data_X, data_y

data, data_X, data_y = get_storm_event_ids()
# print(data_X, data_y)
pickle.dump((data_X,data_y), open('data.p', 'wb'))
print("Finished & pickled data")
