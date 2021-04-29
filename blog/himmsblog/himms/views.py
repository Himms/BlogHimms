from django.shortcuts import render, redirect
from .models import Post
from .models import Comment
from .forms import NewUserForm
from .form_post import CommentForm
from django.contrib.auth import login
from django.contrib import messages 


def frontpage(request):
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {'posts':posts})

def post_detail(request, slug):
	post = Post.objects.get(slug=slug)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', slug=post.slug)
	else:
		form = CommentForm()


	return render(request, 'blog/post_detail.html', {'post':post, 'form': form})



def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("himms:frontpage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="blog/register.html", context={"register_form":form})
