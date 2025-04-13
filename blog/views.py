from django.shortcuts import render, redirect, get_object_or_404

from blog.models import Post
from .forms import AutorForm, CategoriaForm, PostForm
from django.db.models import Q

def buscar_post(request):
    query = request.GET.get("q")
    resultados = []

    if query:
        resultados = Post.objects.filter(
            Q(titulo__icontains=query) |
            Q(contenido__icontains=query) |
            Q(categoria__nombre__icontains=query)
        ).distinct()

    return render(request, "blog/buscar_post.html", {"resultados": resultados, "query": query})


def inicio(request):
    return render(request, 'blog/inicio.html')

def nuevo_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_autor')
    else:
        form = AutorForm()
    return render(request, 'blog/nuevo_autor.html', {'form': form})

def nueva_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nueva_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'blog/nueva_categoria.html', {'form': form})

def nuevo_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_post')
    else:
        form = PostForm()
    return render(request, 'blog/nuevo_post.html', {'form': form})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detalle_post.html', {'post': post})

