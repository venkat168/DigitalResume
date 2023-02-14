from django.shortcuts import render

# Create your views here.
from myapp.models import Profile


def accept(request):
    if request.method=='POST':
        name = request.POST.get('name','')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        school = request.POST.get('school', '')
        diploma = request.POST.get('diploma','')
        degree = request.POST.get('degree', '')
        skill = request.POST.get('skill', '')
        about_you = request.POST.get('about_you', '')

        profile=Profile(name=name,phone=phone,email=email,school=school, diploma=diploma, degree=degree, skill=skill, about_you=about_you)
        profile.save()
    return render(request,'accept.html')

def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    return render(request,'resume.html',{'user_profile'})