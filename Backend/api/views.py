from django.http import JsonResponse

def api_home(request):
    data = {
        'message': 'Welcome to the home page!'
    }
    return JsonResponse(data)
