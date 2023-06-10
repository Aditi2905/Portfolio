from django.shortcuts import render, HttpResponse

# Create your views here.
def Aditi(request):
    #return HttpResponse("This is the homepage")
    context = {'name': 'Aditi', 'course': 'Django'}
    return render(request, 'Aditi.html', context)

def project(request):
    #return HttpResponse("This is the project")
    return render(request, 'project.html')

def about(request):
    #return HttpResponse("This is the about")
    return render(request, 'about.html')

def contact(request):
    #return HttpResponse("This is the contact")
    return render(request, 'contact.html')

def main(request):
    #return HttpResponse("This is the contact")
    return render(request, 'main.html')


