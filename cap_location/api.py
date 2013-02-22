from tastypie.resources import ModelResource
from location.models import Location

import urllib
import urllib2

import operator

from django.utils import simplejson as json

from django.conf import settings

from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """ 
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    mi = 3959 * c 
    return mi  

class DealerResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        allowed_methods = ['get']

    def __init__(self, *args, **kwargs):
        self.dest_lat = None
        self.dest_lng = None
        super(DealerResource,self).__init__(*args, **kwargs)

    def create_response(self, request, data, **kwargs):
        data["objects"] = sorted(data["objects"], key = lambda k: k.data["distance"])   

        data["curr_lat"] = self.dest_lat
        data["curr_lng"] = self.dest_lng

        data["objects"] = data["objects"][:25]
        return super(DealerResource, self).create_response(request, data, **kwargs)

    def dispatch(self, request_type, request, **kwargs):

        address = request.GET.get("daddress", None)

        lat = request.GET.get("currlat", None)
        lng = request.GET.get("currlng", None)

        if address:
            address = urllib.quote_plus(address)

            url = "http://maps.googleapis.com/maps/api/geocode/json?address={0}&sensor=true".format(address)

            data = urllib2.urlopen(url)

            j = json.load(data)

            dest_lat = j["results"][0]["geometry"]["location"]["lat"]
            dest_lng = j["results"][0]["geometry"]["location"]["lng"]

            self.dest_lat = float(dest_lat)
            self.dest_lng = float(dest_lng)

        elif lat and lng:

            self.dest_lat = float(lat)
            self.dest_lng = float(lng)

        return super(DealerResource, self).dispatch(request_type, request, **kwargs)

    def dehydrate(self, bundle):
        request = bundle.request

        lat1 = 0 if not bundle.data["lat"] else float(bundle.data["lat"])
        lng1 = 0 if not bundle.data["lng"] else float(bundle.data["lng"])

        bundle.data["distance"] = int(haversine(lng1, lat1, self.dest_lng, self.dest_lat))

        return bundle


