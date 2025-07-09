from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {'movies': ['green book', 'mafia', 'the intouchables'],}
    return render(request, 'movies/index.html', context)

def about(req):
    return render(req, 'movies/about.html',{})