import http.client, urllib.request, urllib.parse, urllib.error, base64, json

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
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # jdata = json.loads(data)
    # print(jdata)
    # storm_event_ids = set()
    # for elem in jdata:
    #   storm_event_ids.add(elem['stormEventId'])
    # print(storm_event_ids)
    # return storm_event_ids

get_storm_event_ids()