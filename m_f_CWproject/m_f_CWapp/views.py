from django.http import HttpResponse
from django.shortcuts import render
from .forms import NewBlogPost


# Create your views here.

# sends form to index.HTML, also checks validation and saves to database.
def index(request):
    newForm = NewBlogPost()

    if request.method == "POST":
        print("GRABBED!!!!")
        newForm = NewBlogPost(request.POST)
        if newForm.is_valid():
            newForm.save()
        else:
            print('GTFOH with that nonsense!!')

    return render(request, 'm_f_CWapp/index.html', {'form': newForm})



