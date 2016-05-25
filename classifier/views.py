from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from .models import Classifier

# Create your views here.

def loggedin(request):
    return render_to_response('registration/loggedin.html', {'username': request.user.username})

def home(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html', {'username': request.user.username})

def train(request):
    return render(request, 'create.html')

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
