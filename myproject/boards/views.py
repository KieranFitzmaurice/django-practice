from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post

# Create your views here.
def home(request):

    boards = Board.objects.all()
    return render(request,'home.html',{'boards': boards})

    #boards = Board.objects.all()
    #board_names = list()

    #for board in boards:
    #    board_names.append(board.name)

    #response_html = '<br>'.join(board_names)

    #return(HttpResponse(response_html))

def board_topics(request,post_id):
    board = get_object_or_404(Board,id=post_id)
    return render(request,'topics.html',{'board': board})

def new_topic(request, post_id):
    board = get_object_or_404(Board, id=post_id)

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', post_id=board.id)  # TODO: redirect to the created topic page

    return render(request, 'new_topic.html', {'board': board})
