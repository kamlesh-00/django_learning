from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hey! Atlast you reached here.")

def detail(request, question_id):
    return HttpResponse("You are looking at question number %s" % question_id)

def results(request, question_id):
    response = "You are looking at result of question %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s" % question_id)
