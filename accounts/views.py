from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Profile

# Create your views here.
def get_profiles_list(request):
  objects = Profile.objects.all() # get all data from DB
  nick = request.GET.get('nickname')
  
  if nick:# get needed data frim DB
    objects = objects.filter(nickname__icontains=nick)
  
  iterator = (f'{obj.nickname} - {obj.login}' for obj in objects)
  #result = '<br>'.join(str(obj) for obj in objects)
  result = '<br>'.join(iterator)
  return HttpResponse(result)
