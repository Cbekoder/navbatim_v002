from django.shortcuts import render
from .models import *

def home(request):
    # content = {
    #     "softwares" : softwares.objects.all()
    # }
    # print(softwares.objects.all().values("photo"))
    return render(request, 'index.html')

def categories(request):
    categories = Category.objects.all()
    services = Service.objects.all()

    tabs = [
        {'label': 'Home',
         'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>',
         'url': '/',
         'active': True
         },
        {'label': 'Tanlov',
         'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>',
         'url': '/selection/',
         'active': False},
        {'label': 'Katalog',
         'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>',
         'url': '/catalog/',
         'active': False},
        {'label': 'Kelishuvlar',
         'icon': None,
         'url': '/deal/',
         'active': False},
        {'label': 'Xaritadan',
         'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>',
         'url': '/map/',
         'active': False},
        {'label': 'Sevimli',
         'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>',
         'url': '/favorite/',
         'active': False},
        {'label': 'Mening navbatlarim',
         'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>',
         'url': '/my-appointment/',
         'active': False},
    ]

    context = {
        'categories': categories,
        'services': services,
        'tabs': tabs,
    }

    return render(request, 'catalog.html', context)


# def catalog(request):
#     categories = Category.objects.all()
#     services = Service.objects.all()
#
#     tabs = [
#         {'label': 'Home',
#          'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>',
#          'url': '/',
#          'active': False
#          },
#         {'label': 'Tanlov',
#          'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>',
#          'url': '/selection/',
#          'active': False},
#         {'label': 'Katalog',
#          'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>',
#          'url': '/catalog/',
#          'active': True},
#         {'label': 'Kelishuvlar',
#          'icon': None,
#          'url': '/deal/',
#          'active': False},
#         {'label': 'Xaritadan',
#          'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>',
#          'url': '/map/',
#          'active': False},
#         {'label': 'Sevimli',
#          'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>',
#          'url': '/favorite/',
#          'active': False},
#         {'label': 'Mening navbatlarim',
#          'icon': '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>',
#          'url': '/my-appointment/',
#          'active': False},
#     ]
#
#     context = {
#         'categories': categories,
#         'services': services,
#         'tabs': tabs,
#     }
#
#     return render(request, 'catalog.html', context)

def product_details(request):
    return render(request, 'product-details.html')

def contact(request):
    return render(request, 'contact.html')