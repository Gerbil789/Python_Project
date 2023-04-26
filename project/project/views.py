from django.shortcuts import redirect, render
from .models import Image, Author, Tag
from .forms import UploadForm, CreateUserForm, EditUserForm
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db.models import Q


from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def edit_user(request):
    user = request.user
    author = Author.objects.get(user=user)
    form = EditUserForm(instance=author)

    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            
            return redirect('user' , id=user.id)
        
    context = {'form': form}
    return render(request, 'users/edit_user.html', context)

@login_required(login_url='login')
def user(request, id):
    user = get_object_or_404(User, pk=id)
    author = Author.objects.get(user=user)
    images = Image.objects.filter(author=user)

    context = {'author': author, 'images': images}
    if user is not None:
        return render(request, 'users/user.html', context)
    else:
        raise Http404('user not found')
  
    


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                Author.objects.create(user=user)
                return redirect('login')

    context = {'form':form}
    return render(request, 'users/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    #search_query = request.GET.get('search', '') # Get the search query from the request
    #images = Image.objects.filter(title__icontains=search_query) # Filter the images based on the search query
    search_query = request.GET.get('search', '')
    images = Image.objects.filter(
        Q(title__icontains=search_query) | Q(tags__name__icontains=search_query)
    )

    author = None
    if request.user.is_authenticated:
        author = Author.objects.get(user=request.user)


    context = {
        'images': images,
        'user': request.user,
        'author': author,
    }
    return render(request, 'home/home.html', context)

def image(request, id):
    image = Image.objects.get(pk=id)
    if image is not None:
        return render(request, 'images/image.html', {'image': image})
    else:
        raise Http404('Image not found')
    
@login_required(login_url='login')
def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = request.user
            #image.tags = form.cleaned_data['tags']
            form.save()
        return redirect('home')
    return render(request, 'images/upload.html', {'form': UploadForm})