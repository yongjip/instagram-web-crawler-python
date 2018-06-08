import time 
import requests
import operator
import urllib
import httplib, base64

_url = 'https://api.projectoxford.ai/vision/v1.0/analyses'
_key = ''

_maxNumRetries = 10

def processRequest( json, data, headers, params = None ): 
    retries = 0
    result = None

    while True:

        response = requests.request( 'post', _url, json = json, headers = headers, params = params )

        if response.status_code == 429: 

            print "Message: %s" % ( response.json()['error']['message'] )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print 'Error: failed after retrying!'
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print "Error code: %d" % ( response.status_code )
            print "Message: %s" % ( response.json())

        break
        
    return result


def requestAPI(urlImage):
    # URL direction to image
    #f = urllib.urlopen(urlImage)
    #myfile = f.read()
    
    # Computer Vision parameters
    params = { 'visualFeatures' : 'Tags,Categories,Description,Faces'} 

    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = _key
    headers['Content-Type'] = 'application/json' 
    
    json = {"url":urlImage}
    #data = myfile
    
    result = processRequest( json, headers, params )
 
    return result



def pythonSample(urlImage):
    headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': _key,
    }

    params = urllib.urlencode({
        # Request parameters
        'visualFeatures': 'Faces',
        'language': 'en',
    })

    body = {"url":urlImage}
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    
    return (data)
