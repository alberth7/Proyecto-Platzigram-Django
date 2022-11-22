#Django
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Utilities
from datetime import datetime


# Create your views here.

posts = [
    {
        'title': 'Group Music kpop',
        'user':{
            'name': 'Jennie Kim',
            'picture': 'http://pm1.narvii.com/6903/c99bd7de0c5fe0c4a1da306080b75688745e2c95r1-1000-1500v2_uhq.jpg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1036',
    },
    {
        'title': 'Group Music kpop',
        'user':{
            'name': 'Jisoo ',
            'picture': 'https://0.soompi.io/wp-content/uploads/2021/07/07193649/jisoo-3.jpeg',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=903',
    },
    {
        'title': 'Group Music kpop',
        'user':{
            'name': 'Rose',
            'picture': 'https://www.publimetro.com.mx/resizer/bqFHQdiltpVqaoO6u4v8J5RW5co=/800x0/filters:format(png):quality(70)/cloudfront-us-east-1.images.arcpublishing.com/metroworldnews/RHP76QC6UJF5NN52BOPJBTS2WM.png',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=883',
    }
]

# def list_post(request):
#     content = []
#     for post in posts:
#         content.append(""" 
#             <p><strong>{name}</strong></p>
#             <p><small>{user} - <i>{timestamp}</i></small></p>
#             <figure><img src="{picture}"/></figure>
#         """.format(**post))
    
#     return HttpResponse('<br>'.join(content))

@login_required
def list_post(request):
    '''List exist post'''
    return render(request, 'posts/feed.html',{'posts':posts})


