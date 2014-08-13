import hashlib
import urllib

import httplib2
import simplejson

__all__ = ['APIError', 'API']

class APIError(Exception):
    pass

class API:
    def __init__(self, sig_id, sig, server='api.meetup.com', cache=None):
        """Create a new meetup API client instance.
If you don't have an application key, you can request one:
    http://api.meetup.com/keys/"""
        
        self.sig = sig
        self.sig_id = sig_id
        self.server = server
        self.http = httplib2.Http(cache)
		

    def call(self, method, lat, lon, **args):
        "Call the Eventful API's METHOD with ARGS."
        # Build up the request
       
        args['sig'] = self.sig
        args['sig_id'] = self.sig_id       
        args = urllib.urlencode(args)
        url = "http://%s/%s&lat=%s&page=%s&lon=%s&sig_id=%s&sig=%s" % (self.server, method, lat, 20,lon, self.sig_id ,self.sig)
        #print url
        # Make the request
        response, content = self.http.request(url, "GET")

        # Handle the response
        status = int(response['status'])
        if status == 200:
            try:
                return simplejson.loads(content)
            except ValueError:
                raise APIError("Unable to parse API response!")
        elif status == 404:
            raise APIError("Method not found: %s" % method)
        else:
            raise APIError("Non-200 HTTP response status: %s" % response['status'])
