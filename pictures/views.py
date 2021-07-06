from django.shortcuts import render
from .models import Image,Location

# Create your views here.
def pictures(request):
    pics = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'photos.html',{'pics':pics,'locations':locations})

def locations(request,location):
    locations = Image.filterimageByLocation(location)
    return render(request,'locations.html',{'locations':locations})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_pictures = Image.searchImage(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
