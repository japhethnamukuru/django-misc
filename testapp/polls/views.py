# from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question as q

def index(request):
    latest_question_list = q.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # output = ', '.join([question.question_text for question in latest_question_list])
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You are looking at question {}".format(question_id))

def results(request, question_id):
    response = "You are looking at the results of question{}".format(question_id)
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("Your are voting on question {}".format(question_id))