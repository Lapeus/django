from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.
def index(request):
    r = requests.get('http://www.pathofexile.com/api/public-stash-tabs?id=6715219-6940400-6501061-7710885-6962087')
    rJson = r.json()
    change_id = rJson['next_change_id']
    # get the latest stashes
    count_changeIds = 1
    for i in range(100):
        r = requests.get('http://www.pathofexile.com/api/public-stash-tabs?id=' + change_id)
        change_id = r.json()['next_change_id']
        count_changeIds += 1
    
    
    
#    stashes = rJson['stashes']
    return HttpResponse(change_id)