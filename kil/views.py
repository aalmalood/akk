from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponseRedirect
from .models import Agency,Offers,Customer
from .forms import reqForm

Agency_list = Agency.objects.all()
of_list = Offers.objects.all()
def index(request):
    
    template = loader.get_template('kil/index.html')
    context = {
        'Agency_list': Agency_list,
        'of_list': of_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, ag_name ):
	
    try:
        ag = Agency.objects.get(pk=ag_name)
    except Agency.DoesNotExist:
        raise Http404("Agency does not exist")
    
    context = {
        'ag': ag,
        'of_list': of_list,
    }
    return render(request, 'kil/detail.html', context)

def results(request, ag_name):
    response = "You're looking at the results of ag %s."
    return HttpResponse(response % ag_name)

def vote(request, ag_name):
    return HttpResponse("You're voting on ag %s." % ag_name)


def customerinfo(request):
        if request.method == 'POST':
            if request.POST.get('phone') and request.POST.get('nppl'):
                cust=Post()
                cust.phone= request.POST.get('phone')
                cust.request= request.POST.get('request')
                cust.nppl= request.POST.get('nppl')
                cust.name= request.POST.get('name')
                cust.offer= request.POST.get('offer')

                cust.save()
                
                return render(request, 'customerinfo.html')  

        else:
                return render(request,'customerinfo.html')

def offer(request, of_id ):
	
    try:
        off = Offers.objects.get(pk=of_id)
    except Offers.DoesNotExist:
        raise Http404("Offer does not exist")
    
    context = {
        'off': off,
        'Agency_list': Agency_list,
        'of_list': of_list,
    }
    return render(request, 'kil/offer.html', context)


def requestt(self ,request): 	
    form = reqForm(request,POST)
    if form.is_valid():
    	form.save()
    context ={
    	'off': off,
    }
    return render(request, self.template_name , arg)