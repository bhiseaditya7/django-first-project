from django.shortcuts import render,HttpResponse
from .models import IceCream 
from django.views.decorators.csrf import csrf_protect
#from home import models as IceCream


# Create your views here.
def index(request):
    context={
        "variable1":"Aditya is great",
        "variable2":"Benz is great"
    }
    #return HttpResponse("this is homepage")
    ##if request.method =="POST":
    #    fullname:request.POST("fullname") 
    #    email:request.POST("email")
    #    phone=request.POST("phone")
    #    message=request.POST("message")
    #    Ice=IceCream(fullname=fullname, email=email, phone=phone, message=message)
    #    Ice.save()



    

    return render(request,'index.html',context)

def about(request):
    #return HttpResponse("this is about")
    return render(request,'about.html')

def services(request):
    #return HttpResponse("this is services")
    return render(request,'services.html')

@csrf_protect
def contact(request):
    #return HttpResponse("this is contact page")
    if request.method =="POST":
        fullname=request.POST["fullname"] 
        email=request.POST["email"]
        phone=request.POST["phone"]
        message=request.POST["message"]
        IceC=IceCream(fullname=fullname, email=email, phone=phone, message=message)
        IceC.save()

    return render(request,'contact.html')

"""@login_required
def tags(request):
    all_tags = Tag.objects.all()
    context = base_context(request)
    if request.method == 'POST':
        if 'status_check' in request.POST:
            status = request.GET('status')
            tag = request.GET('tag')
            user = request.user
            tag_status, created = TagStatus.objects.get_or_create(status=len(status), tag=tag, user=user).save()

            response = simplejson.dumps({"status": "Successfully changed status"})
        else:
            response = simplejson.dumps({"status": "Error"})
            return HttpResponse (response, mimetype='application/json')
    context['all_tags'] = all_tags
    return render_to_response('tags/tag.html', context, context_instance=RequestContext(request))    
"""