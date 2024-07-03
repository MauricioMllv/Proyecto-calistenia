import requests
from django.shortcuts import render
from .models import Slider

def home(request):
    sliders = Slider.objects.all().order_by('order')
    
    access_token = 'IGQWRQd2ZApWUJVczhuM3lOMl9ndHFDbWF0R2hIQ1daWFVPRUl0aE5xTWdlcXUzOEtiUFJyOVVLakYxV19ZANE1jYk4xWHIybnUxSUVmUkRyVG9ZAQ2ozd0RINjI5dFA3anRwTWFrcjhJWHNhUGI1cDVHM3pFQnVlQWcZD'
    limit = 6
    url = f'https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,permalink,thumbnail_url,timestamp&limit={limit}&access_token={access_token}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', [])
    else:
        posts = []

    context = {
        'sliders': sliders,
        'posts': posts,
    }

    return render(request, 'home/home.html', context)


# import requests
# from django.shortcuts import render
# from .models import Slider

# def home(request):
#     sliders = Slider.objects.all().order_by('order')
#     return render(request, 'home/home.html', {'sliders': sliders})

# def instagram_feed(request):
#     access_token = 'IGQWROMElIX2MzaUhCTmhmeDVuNEtqdlFGaTBSRlJYM3JXSVllWFdfVW50bXFMTFAzT09NRXVTbFZAjUDR5Nk1CN0pGRUhVekRBZAWVFX2NEeENqMG9FM3NpM2dkOVg4empfUW1XdUg2SWMzMkxFbjVVQUZAua1NXVXcZD'
#     url = f'https://graph.instagram.com/me/media?fields=id,caption,media_type,media_url,permalink,thumbnail_url,timestamp&access_token={access_token}'

#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         posts = data.get('data', [])
#     else:
#         posts = []

#     return render(request, 'home/home.html', {'posts': posts})
