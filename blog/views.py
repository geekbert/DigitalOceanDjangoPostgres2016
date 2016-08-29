from django.shortcuts import render
from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """Return the last five published questions."""
        return Blog.objects.all()
	#return Blog.objects.order_by('Title')[:15]

#def index(request):
#    return render_to_response('index.html', {
#        'categories': Category.objects.all(),
#        'posts': Blog.objects.all()[:5]
#    })


class DetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/detail.html'


def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
