"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'year':datetime.now().year,
        }
    )

def residential(request):
    """Renders the residential page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/residential.html',
        {
            'year':datetime.now().year,
        }
    )

def commercial(request):
    """Renders the commercial page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/commercial.html',
        {
            'year': datetime.now().year,
        }
    )

def inprogress(request):
    """Renders the commercial page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/inprogress.html',
        {
            'year': datetime.now().year,
        }
    )

def sanangelo(request):
    """Renders the commercial page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/inprogress/sanangelo.html',
        {
            'year': datetime.now().year,
        }
    )