import hashlib
import urllib

import httplib2
import simplejson

__all__ = ['APIError', 'API']

class APIError(Exception):
    pass

class API:
    def __init__(self, app_key, server='www.eventbrite.com/', cache=None):
        self.app_key = app_key
        self.server = server
        self.http = httplib2.Http(cache)
		

    def call(self, method, **args):
        "Call the Eventful API's METHOD with ARGS."
        # Build up the request
       
        args['app_key'] = self.app_key   
        args = urllib.urlencode(args)
        url = "http://%sjson%s/?%s" % (self.server, method,args)
        print url
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
