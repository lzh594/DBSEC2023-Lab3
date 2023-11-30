from django.http import JsonResponse


# Create your views here.
def index(request):
    # return render(request, 'index.html')
    return JsonResponse({"para1": "Test"})
