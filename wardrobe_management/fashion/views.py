# views.py in 'fashion' app
# views.py in 'fashion' app
from django.shortcuts import render, redirect, get_object_or_404
from .models import FashionBlog
from .forms import FashionBlogForm
from django.contrib.auth.decorators import login_required

# View to list all fashion blogs
def blog_list(request):
    blogs = FashionBlog.objects.all()
    return render(request, 'fashion/blog_list.html', {'blogs': blogs})

# View to display a single blog post
def blog_detail(request, id):
    blog = get_object_or_404(FashionBlog, id=id)
    return render(request, 'fashion/blog_detail.html', {'blog': blog})

# View to create a new blog post

def create_blog(request):
    if request.method == 'POST':
        form = FashionBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Set the current user as the author
            blog.save()
            return redirect('blog_list')
    else:
        form = FashionBlogForm()
    return render(request, 'fashion/blog_form.html', {'form': form})

# View to update an existing blog post

def update_blog(request, id):
    blog = get_object_or_404(FashionBlog, id=id)
    if request.method == 'POST':
        form = FashionBlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', id=blog.id)
    else:
        form = FashionBlogForm(instance=blog)
    return render(request, 'fashion/blog_form.html', {'form': form})


def delete_blog(request, id):
    blog = get_object_or_404(FashionBlog, id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'fashion/blog_confirm_delete.html', {'blog': blog})
