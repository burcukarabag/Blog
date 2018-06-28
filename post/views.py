# -*- coding: utf-8 -*-


from django.shortcuts import render, Http404, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

#request parametresi sitemizi ziyaret eden kullanıcıların yaptıkları istekleri temsil ediyor
#fonksiyonumuzun view olabilmesi için en az bir tane arguman alması gerekiyor

def post_index(request):

    posts = Post.objects.all()

    return render(request, 'post/index.html', {'posts' : posts})

def post_detail(request, id):

    post = get_object_or_404(Post, id=id)
    context = {
        'post' : post,
    }
    return render(request, 'post/detail.html', context)

def post_create(request):

    if not request.user.is_authenticated():

        return Http404
    """if request.method == "POST":
        print(request.POST)

    title = request.POST.get('title')
    content = request.POST.get('content')

    Post.objects.create(title='title', content='content')

     #####

    if request.method == "POST":
        #formdan geen bilgileri kaydet
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

    else:
        #formu kullanıcıya göster
        form = PostForm() """

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        """HttpResponseRedirectin içine oluşturulan postun detay adresini
        vermemiz lazım. Yani oraya yönlenmesi lazım. Save metodu eklediği veya 
        güncellediği nesneyi geri döndüren bir metottur. Geri dönen nesneyi post
        adlı değişkende tutalım. Postun adresini get absolute un içine yazıyoruz."""

        post = form.save()
        messages.success(request, 'Başarılı bir şekilde oluşturuldu.')

        #mesaj sadece 1 kere görünür. postu yenileyince mesaj silinir.

        return HttpResponseRedirect(post.get_absolute_url())


    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)

def post_update(request, id):
    if not request.user.is_authenticated():
        return Http404

    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None,  instance=post)

    #bu formu getirdiğimiz post bilgilerine göre doldurmak istiyoruz

    if form.is_valid():
        form.save()
        messages.success(request, 'Başarılı bir şekilde oluşturuldu.', extra_tags='mesaj-basarili ')

        return HttpResponseRedirect(post.get_absolute_url())
        #burada post nesnesini getirmeye gerek yok çünkü yukarıda zaten çağırdık

    context = {
        'form': form,
    }

    return render(request, 'post/form.html', context)

def post_delete(request, id):
    if not request.user.is_authenticated():
        return Http404

    post = get_object_or_404(Post, id=id)
    post.delete()

    #post silinirken detay sayfası da silinecek. bu yüzden yönlendirme index sayfasına olmalı

    return redirect('post:index')

    #HttpResponseRedirect i ekleme ve güncelleme işlemlerinde işlem tamamlandığında amaç ilgili postun
    #detay sayfasına yöndlendirmek olduğu için kullandık. get_absolute_url vererek ilgli
    #postun detay sayfasına gidileceğini belirttik.
    #redirect ise çok daha basit bir metottur
    #silinen bir eşyin detay sayfası olmayacağı için basit bir şekilde index sayfasına yönlendirdik.
