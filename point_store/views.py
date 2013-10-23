import json
from django.http import HttpResponse
from django.contrib.gis.geos import Point, Polygon
from point_store.models import *
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
'''
class DataPoint(models.Model):
    #localization
    position = models.PointField()
    speed = models.FloatField()
    accuracy = models.FloatField()
    altitude = models.FloatField()
    time = models.DateTimeField()
    #wifi
    frequency = models.IntegerField()
    level = models.IntegerField()
    ssid = models.CharField(max_length=300)
    bssid = models.CharField(max_length=300)
    capabilities = models.TextField()'''

def geoj(res, full=False):
    r = {}
    r['type']="Feature"
    r['geometry'] = json.loads(res.position.json)
    r['properties']={}
    r['properties']['id'] = res.id
    if full:
        pass
    return r

def to_json(res):
    r = {}
    r['position'] = json.loads(res.position.json)
    r['speed'] = res.speed
    r['accuracy']= res.accuracy
    r['altitude'] = res.altitude
    r['time'] = str(res.time)
    
    r['frequency'] = res.frequency
    r['level'] = res.level
    r['ssid'] = res.ssid
    r['bssid'] = res.bssid
    r['capabilities'] = res.capabilities
    return r

@csrf_exempt
def push(request):
    data = request.REQUEST.get('point', "{}")
    data = json.loads(data)
    ldata = data['location']
    loc = Point(ldata['lon'],ldata['lat'])
    speed = ldata['speed']
    accuracy = ldata['accuracy']
    altitude = ldata['altitude']
    time = datetime.fromtimestamp(ldata['time']/1000)
    
    ret = 0
    for scan in data['scan_data']:
        dp = DataPoint()
        dp.position = loc
        dp.speed = speed
        dp.accuracy = accuracy
        dp.altitude = altitude
        dp.time = time
        
        dp.frequency = scan['frequency']
        dp.level = scan['level']
        dp.ssid = scan['SSID']
        dp.bssid = scan['BSSID']
        dp.capabilities = scan['capabilities']
        dp.save()
        ret += 1 
    return HttpResponse(json.dumps({'inserted':ret}))

from django.shortcuts import render_to_response


def points(request):
    BB = request.REQUEST.get('BB')
    ret = DataPoint.objects.filter(position__contained=Polygon.from_bbox([float(bb) for bb in BB.split(',')]))
    return HttpResponse(json.dumps({'type':'FeatureCollection', 'features':[geoj(r) for r in ret]}))


def point(request):
    id = request.REQUEST.get('id')
    ret = DataPoint.objects.get(id=id)
    return HttpResponse(json.dumps(to_json(ret)))





def index(request):
    return render_to_response('index.html')


def proxy(request, path):
    import httplib2
    conn = httplib2.Http()
    url = path
    if request.method == 'GET':
        url_ending = '%s?%s' % (url, request.GET.urlencode())
        url = "http://" + url_ending
        response, content = conn.request(url, request.method)
    elif request.method == 'POST':
        url = "http://" + url
        data = request.POST.urlencode()
        response, content = conn.request(url, request.method, data)
    return HttpResponse(content, status = int(response['status']), mimetype = response['content-type'])
    