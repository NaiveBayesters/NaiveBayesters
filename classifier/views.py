from django.shortcuts import HttpResponse, render, get_object_or_404, HttpResponseRedirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from .models import Classifier
from .machine_learning import get_training_data
from .forms import ClassifierForm


# Create your views here.

def loggedin(request):
    userid = request.user.id
    return HttpResponseRedirect('/classifier/profile/{}'.format(userid))
    # return render(request, 'profile.html', {'username': request.user.username})

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
            userid = request.user.id
            classifier.save()
            return HttpResponseRedirect('/classifier/profile/{}'.format(userid))
    else:
        form = ClassifierForm()

    return render(request, 'create.html', {'form': form})

def prediction(request):
    if request.method == 'POST':
        context = {}
        context['test'] = request.POST['test']
        context['testing'] = get_training_data(context['test'])
        return render(request,'prediction.html', context)
    else:
        return render(request,'prediction.html')


def classifier_detail_view(request, id):
    classifier = get_object_or_404(Classifier, pk=id)
    return render(request, 'classifier/detail.html', {'classifier': classifier})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            userid = request.user.id
            return HttpResponseRedirect('/classifier/profile/{}'.format(userid))

    else:
        form = UserCreationForm()
        
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
    return render(request, 'registration/registration_complete.html')
