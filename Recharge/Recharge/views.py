from django.http import HttpResponse
def Home_page(request):
    print("Home Page Requested")
    return HttpResponse("<h1 >Recharge Plan</h1>")