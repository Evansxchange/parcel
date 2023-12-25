from django.shortcuts import render, HttpResponse
from . models import ShippingInfo
from django. contrib import messages
from .pdf import render_to_pdf
from django.views.generic import View

# Create your views here.

def home(request):
  return render(request, 'home.html',  {'nav' : 'home'})

def about(request):
  return render(request, 'about.html',  {'nav' : 'about'})

def contact(request):
  return render(request, 'contact.html',  {'nav' : 'contact'})

def ocean(request):
  return render(request, 'ocean.html',  {'nav' : 'ocean'})

def land(request):
  return render(request, 'land.html',  {'nav' : 'land'})

def air(request):
  return render(request, 'flight.html',  {'nav' : 'air'})

def track(request):
  if 'q' in request.GET:
    q = request.GET['q']
    data = ShippingInfo.objects.filter(waybillNumber=q)
    if ShippingInfo.objects.filter(waybillNumber=q):
      messages.info(request, f"The tracking code you entered is correct")
    else:
      messages.info(request, f"The tracking code you entered is incorrect")

  else: 
   data = ShippingInfo.objects.none()
   messages.warning(request, f"Enter a valid tracking number")
  context = {
    "data" : data,
    "nav" : "track"
  }
  return render(request, 'track.html', context)

class GeneratePdf(View):
  def get(self, request, id, *args, **kwargs):
     data = ShippingInfo.objects.get(id=id)
     context = {
        'data': data
      }
     pdf = render_to_pdf('pdf.html', context)
     return HttpResponse(pdf, content_type='application/pdf')


