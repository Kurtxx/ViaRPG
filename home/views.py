from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):

    context = {
    }

    return render(request, 'game/home.html', context)


def about(request):
    return render(request, 'game/about.html', {'title': 'About'})
