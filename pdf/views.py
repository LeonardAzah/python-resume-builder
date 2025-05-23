
from django.shortcuts import render
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

from .models import Profile
# Create your views here.

def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name',"")
        email = request.POST.get('email', "")
        summary = request.POST.get('summary', "")
        degree = request.POST.get('degree', "")
        university = request.POST.get('university', "")
        skills = request.POST.get('skills', "")
        phone = request.POST.get('phone', "")
        school = request.POST.get('previous_work', "")
        previous_work = request.POST.get('previous_work', "")

        profile = Profile(name=name, email=email, summary=summary, degree=degree, university=university, skills=skills, school=school, phone=phone,
                          previous_work=previous_work)
        profile.save()
    return render(request, 'pdf/accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({"user_profile":user_profile})
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8',
    }
    pdf = pdfkit.from_string(html,False, options)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = 'resume.pdf'


    return response

def lists(request):
    profile = Profile.objects.all()
    return render(request, 'pdf/profile.html', {'profile':profile})