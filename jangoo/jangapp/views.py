from django.shortcuts import render, get_object_or_404
from .models import posts


# Create your views here.
def index(request):
    post = (
        posts.objects.all()
    )  # where post is a query set ( let's say a list of instances/records )
    return render(request, "posts/index.html", {"content": post})

def about(request, id):
    data = posts.objects.get(id=id)
    return render(request, "posts/nextpg.html", {"context": data})
