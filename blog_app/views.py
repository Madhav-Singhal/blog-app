from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, AddComment
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User, auth


# Create your views here.




def register(request, id=None):
    if request.method == 'POST':
        val1 = request.POST['first_name']
        val2 = request.POST['last_name']
        val3 = request.POST['username']
        val4 = request.POST['password']
        val5 = request.POST['confirm']

        if val4 == val5:
            if User.objects.filter(username=val3).exists():
                if id:
                    return render(request, 'register.html', {'id':id})

              
                
                return render(request, 'register.html')
            else:


                user = User.objects.create_user(username = val3, password = val4, first_name = val1, last_name = val2)
                user.save()
                auth.login(request, user)
                if id:
                    return redirect("blog_app:detail", id)
                # pk = user.instance.pk
                return redirect("blog_app:user_list")

        else:
            if id:
                return redirect('blog_app:register', id)

            return redirect('blog_app:register')

    else:
        if id:
            return render(request, 'register.html', {'id':id})

        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def user_list(request):
    if not request.user.is_authenticated:
        return redirect('blog_app:login')

    obj = Post.objects.filter(author = request.user)
  

    return render(request, 'user_list.html', {'obj':obj})

def login(request, id=None):
    if request.method == 'POST':


        val3 = request.POST['username']
        val4 = request.POST['password']

        user = auth.authenticate(username=val3, password=val4)

        if user is not None:
            auth.login(request, user)
            # id=request.user.id
            if id:
                return redirect('blog_app:detail', id)

            
            return redirect('blog_app:user_list')
        else:
            if id:

                return redirect('blog_app:login', id)
            return redirect('blog_app:login')

    else:
        if id:
            return render(request, 'login.html', {'id':id})

        return render(request, 'login.html')




def list(request):
    
    object = Post.objects.all()
    
    return render(request, 'base.html', {'obj': object})


def create(request):

    form = PostForm
    if request.method == "POST":
        my_form = PostForm(request.POST or None, request.FILES or None )

        if my_form.is_valid():

            obj = my_form.save(commit = False)
            # x = request.POST.get('img')
            # print(x)
            obj.author = request.user
            obj.save()

            return redirect("blog_app:user_list")

    return render(request, 'create.html', {'form': form})




def detail(request, id):

    object = Post.objects.get(pk = id)
    # print(object.img)
    comments = AddComment.objects.all().filter(post_id=id, reply=None)
    # comments = AddComment.objects.all().filter(post=id), c
    form = CommentForm
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('blog_app:login', id)
        form = CommentForm(request.POST or None )
        if form.is_valid():
            # obj = form.save(commit=False)get('comment')
            form.save(commit=False)
            content = request.POST.get('comment')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = AddComment.objects.get(id=reply_id)

            comment = AddComment.objects.create(user_id=request.user, post_id=object, comment = content, reply = comment_qs)
            # comment.save()
            # obj.author = request.user
            comment.save()
            

            return redirect("blog_app:detail", id)

    # return render(request, 'detail.html', {'obj':object, 'form':form})
    return render(request, 'detail.html', {'obj': object, 'comments':comments, 'form':form})


def edit(request, id):

    
    update_obj = get_object_or_404(Post, id = id)
    form = PostForm(request.POST or None, request.FILES or None, instance = update_obj)
    if form.is_valid():
        
        form.save()
        
        return redirect("blog_app:user_list")
    context = {
        'form': form
    }
    return render(request, 'edit.html', context)



def delete(request, id):

    object = Post.objects.get(pk = id)
    object.delete()
    return redirect("blog_app:user_list")



    



