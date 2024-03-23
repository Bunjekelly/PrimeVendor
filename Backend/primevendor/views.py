from django.http import HttpResponse

def home(request):
    content = "<h1>Welcome to the home page!</h1>"
    return HttpResponse(content)