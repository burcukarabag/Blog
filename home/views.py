from django.shortcuts import render, HttpResponse



#ilk parametre request. ikincisinde servis edeceğimiz html dosyasının adını.
#bu html dosyası, settingte ayarladığımız template klasörüyle aynı yerde olmalı. templatesin yolunu belirtmiştik
def home_view(request):
    if request.user.is_authenticated():
        context = {
            'isim' : 'Burcu'
        }

    else:
        context = {
            'isim' : ''
        }
    return render(request, 'home.html', context)


