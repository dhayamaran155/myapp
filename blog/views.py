from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
# Create your views here.
# static demo data
# posts = [

#         {'id':1,'title':'Post 1','content':'Content of Post 1'},
#         {'id':2,'title':'Post 2','content':'Content of Post 2'},
#         {'id':3,'title':'Post 3','content':'Content of Post 3'},
#         {'id':4,'title':'Post 4','content':'Content of Post 4'}
#     ]
def index(request):
    blog_title="Latest posts"
    # getting data from post model

    all_posts=Post.objects.all()

    #paginator
    paginator = Paginator(all_posts,5)
    page_number= request.GET.get('page')
    page_obj= paginator.get_page(page_number)



    return render(request,'blog/index.html',{'blog_title':blog_title,'page_obj':page_obj})

def detail(request,slug):
    #  static data
    # post = next((item for item in posts if item['id']==int(post_id)),None)
    try:
        #getting data from post id
        post=Post.objects.get(slug=slug)
        related_posts=Post.objects.filter(category=post.category).exclude(pk=post.id)



    except Post.DoesNotExist:
        raise Http404("Post Does not Exist")
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')
    return render(request,'blog/detail.html',{'post':post,'related_posts':related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("this is the new url")