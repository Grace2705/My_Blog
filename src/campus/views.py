from django.shortcuts import render, redirect
from .models import Post, AddComment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'

def RegisterView(request):
	if request.user.is_authenticated:
		return redirect('blog')
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('blog')
		else:
			messages.error(request, 'Correct the errors below')
	else:
		form = RegisterForm()

	return render(request, 'register.html', {'form': form})



def LoginView(request):
    if request.user.is_authenticated:
        return redirect('blog')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('blog')
                else:
                    messages.error(request, "Invalid username or password.")

        context = {}
        return render(request, "registration/login.html", context)

def LogoutView(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('registration/login')

class BlogView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    paginate_by = 4
    template_name = 'blog.html'


class Blogdetailview(DetailView):
    model = Post
    template_name = 'post_detail.html'

class Blogcreateview(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class AddCommentview(CreateView):
    model = AddComment
    template_name = 'add_comment.html'
    fields = ['name', 'body']

class Blogupdateview(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields =['title', 'body']

    def test_func(self):
        obj = self.get_object()

        return obj.author == self.request.user


class Blogdeleteview(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()

        return obj.author == self.request.user