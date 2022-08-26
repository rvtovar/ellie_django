from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

from .models import Question

# Create your views here.


def index(request):
    latest__questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest__questions': latest__questions}
    return render(request, 'polls/index.html', context)


def results(request, question_id):
    response = "Your looking at the results of question %s"
    return HttpResponse(response % question_id)


def detail(request, question_id):
    response = 'Your looking at question %s'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    response = 'Your voting on question %s'
    return HttpResponse(response % question_id)
