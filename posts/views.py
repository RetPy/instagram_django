from django.forms.models import inlineformset_factory
from django.shortcuts import render,redirect
from posts.models import *
from comments.models import Comment
from tags.models import Tag
from posts.forms import PostForm,PostImageForm
from django.contrib.auth.models import User
from django.db.models import Q

def home(request):
    if 'key_word' in request.GET:
        key = request.GET.get('words')
        posts = Post.objects.filter(Q(owner__icontains=key))
    else:
        posts = Post.objects.all()
        if request.method == 'POST':
            if 'like' in request.POST:
                like_post = request.POST.get('like')
                id_post = Post.objects.get(id=like_post)
                try:
                    like = Like.objects.get(user_like=request.user, post_like=id_post)
                    like.delete()
                except:
                    Like.objects.create(user_like = request.user, post_like=id_post)
            if 'comment' in request.POST:
                post_id = request.POST.get('post_id')
                post = Post.objects.get(id=post_id)
                text = request.POST.get('comm')
                Comment.objects.create(user=request.user, post=post, text=text)
            return redirect('home')
        return render(request,'posts/index.html',{'posts':posts})

def create(request):
    form = PostForm(request.POST, None)
    PostImageFormSet = inlineformset_factory(Post,PostImage,form=PostImageForm,extra=1)
    if request.method == 'POST':
        if form.is_valid():
            post = Post()
            post.text = form.cleaned_data['text']
            post.owner = request.user
            post.save()
            tags = form.cleaned_data['tag']
            for tag in tags.split(' '):
                obj, created = Tag.objects.get_or_create(title = tag)
                post.tag.add(obj)
            formset = PostImageFormSet(request.POST, request.FILES, instance=post)
            if formset.is_valid():
                formset.save()
            return redirect('home')
    formset=PostImageFormSet()
    return render(request,'posts/create.html',locals())

def detail(request,id):
    post = Post.objects.get(id=id)
    return render(request,'posts/detail.html',{'post':post})

def update(request,id):
    post = Post.objects.get(id=id)
    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post.text = form.cleaned_data['text']
            post.image = form.cleaned_data['image']
            post.save()
            return redirect('home')
    else:
        form=PostForm()
    return render(request,'posts/update.html',{'form':form})

def delete(request,id):
    if request.method =='POST':
        post = Post.objects.get(id=id)
        post.delete()
        return redirect('home')
    return render(request,'posts/delete.html')

def get_profile(request,id):
    profile = User.objects.get(id=id)
    return render(request,'profile.html',{'profile':profile})

