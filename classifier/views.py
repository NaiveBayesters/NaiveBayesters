from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Classifier

# Create your views here.
def register(request):
    return render(request, 'classifier/home.html')

def profile(request):
    return render(request, 'classifier/profile.html')

def train(request):
    return render(request, 'classifier/create.html')

def classifier_detail_view(request, id):
    classifier = get_object_or_404(Classifier, pk=id)
    return render(request, 'classifier/detail.html', {'classifier': classifier})
