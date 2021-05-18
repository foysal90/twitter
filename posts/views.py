from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Post
from .forms import PostForm 
# from .forms import UpdateForm 
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.all()[:20]

    return render(request, 'posts.html', 
                  {'posts': posts}) 
def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')
    
def edit(request, post_id):
     post = Post.objects.get(id = post_id)
     print(post)
     if request.method == 'POST':
         form = PostForm(request.POST, request.FILES, instance=post)
         if form.is_valid():
             form.save()
             return HttpResponseRedirect('/')
         else:
             return HttpResponseRedirect(form.errors.as_json())
     else:
    # Show editting screen
        form = PostForm
        return render(request, 'edit.html',
        {'post': post, 'form': form})


def postLikeAdd(request,post_id):
  
    post = Post.objects.get(id = post_id)
  
    new_like_count = post.like_count + 1
    post.like_count = new_like_count
  
    print(post.like_count)
    post.save()

    return HttpResponseRedirect('/')  

    
# def postLikeAdd(request,post_id):
  
#    post = Post.objects.get(id = post_id)
  
#    new_like_count = post.like_count - 1
#    post.like_count = new_like_count
  
#    print(post.like_count)
#    post.save()

#    return HttpResponseRedirect('/')  





# def postLikeAdd(request, post_id):
  
#   post = Post.objects.get(id = post_id)
# ​
  
#   new_like_count = post.like_count + 1
#   post.like_count = new_like_count
# ​
 
#   post.save()
# ​
#   return JsonResponse({'result': 'successful'})





# def likeCount(request, post_id):
#     post = Post.objects.get(id = post_id)
#     new_like_count = post.like_count + 1
#     post.like_count = new_like_count
#     post.save()
    



# def like_post(request):
#     liked = False
#     if request.method == 'GET':
#         post_id = request.GET['post_id']
#         post = Post.objects.get(id=int(post_id))
#         if request.session.get('has_liked_'+post_id, liked):
#             print("unlike")
#             if post.likes > 0:
#                 likes = post.likes - 1
#                 try:
#                     del request.session['has_liked_'+post_id]
#                 except KeyError:
#                     print("keyerror")
#         else:
#             print("like")
#             request.session['has_liked_'+post_id] = True
#             new_like_count = post.like_count + 1
#     post.like_count = new_like_count
#     post.save()
#     return HttpResponse(likes, liked)    
     


    
                