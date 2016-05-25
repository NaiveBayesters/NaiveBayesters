from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from .models import Classifier
from .machine_learning import get_training_data, what_is_the_text
from .forms import ClassifierForm


# Create your views here.

def loggedin(request):
    return render(request, 'registration/loggedin.html', {'username': request.user.username})

def home(request):
    return render(request, 'home.html')

def profile(request, id):
    owner = User.objects.get(id=id)
    classifier = Classifier.objects.all().filter(owner=owner)
    return render(request, 'profile.html', {'username': request.user.username, 'classifier': classifier})

def train(request):
    if request.method == 'POST':
        form = ClassifierForm(request.POST)
        if form.is_valid():
            classifier = form.save(commit=False)
            classifier.owner = request.user
            classifier.save()
            return HttpResponseRedirect('/classifier/home/')
    else:
        form = ClassifierForm()

    return render(request, 'create.html', {'form': form})

def classifier_detail_view(request, id):
    classifier = get_object_or_404(Classifier, pk=id)
    return render(request, 'classifier/detail.html', {'classifier': classifier})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')
