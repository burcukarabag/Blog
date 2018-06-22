from django.contrib import admin

# Register your models here.

from .models import Post

#from post.models import Post

class PostAdmin(admin.ModelAdmin): #admin modeli oluşturduk.

    list_display = ['title', 'publishing_date']

    list_display_links = ['publishing_date'] #bu listedekilere tıklayınca postların detay sayfasına ulaşabiliriz.

    list_filter = ['publishing_date'] #tarih alanına göre filtreleme ekledik

    search_fields = ["title", 'publishing_date'] #arama alanına yazılan kelimeler title veya published date ile eşleşince kayıt gelecek akrşımıza

    list_editable = ['title']


    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)
