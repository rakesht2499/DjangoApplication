from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from login.models import log


# Create your views here.
class loginpage(TemplateView):
    template_name = 'loginpage.html'


def data(request):
    user = str(request.POST['UserName'])
    password = str(request.POST['Password'])
    try:
        t = log.objects.get(studentcode = user)
        if(str(t.dob) == password):
            return render(request,'loggedinpage.html',{'code': t.studentcode , 'name': t.studentname ,
                                                       'admin': t.adminno , 'class' : t.classname ,
                                                       'section': t.section , 'result' : t.result,
                                                       'pass': t.result == "PASS"})
        else:
            return render(request, 'loginpage.html', {'login_fail': True})
    except:
        return render(request, 'loginpage.html', {'login_fail': True})
