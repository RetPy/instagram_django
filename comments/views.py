from django.shortcuts import render, redirect
from .models import *
from .forms import CommentForm

def update_comm(request, id):
    comment = Comment.objects.get(id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'tags/update_comm.html', {'form':form})

def delete_comm(request, id):
    if request.method == 'POST':
        comment = Comment.objects.get(id=id)
        comment.delete()
        return redirect('home')
    return render(request, 'tags/delete_comm.html')