from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from django.template import loader
from django.contrib.auth import logout
from .models import Picture, Rectangle, Tag

PICTURES_PER_PAGE = 5

def create_miniature(picture):
    width = 100
    height = 100
    rectangles = picture.rectangles.all()
    svg = f'<svg width="{width}" height="{height}">'
    for rect in rectangles:
        scaled_width = (rect.width / picture.size_x) * width
        scaled_height = (rect.height / picture.size_y) * height
        scaled_x = (rect.x / picture.size_x) * width
        scaled_y = (rect.y / picture.size_y) * height
        svg += f'<rect x="{scaled_x}" y="{scaled_y}" width="{scaled_width}" height="{scaled_height}" fill="{rect.color}"/>'
    svg += '</svg>'
    return svg

def index(request):
    page_num = int(request.GET.get('page_num', 1))
    sort = request.GET.get('sort', 'asc')
    tags = request.GET.get('tags', '')
    tags_list = tags.split(',')

    pictures = Picture.objects.all()

    if tags != '':
        for tag in tags_list:
            pictures = pictures.filter(tags__name__contains=tag)

    if sort == 'asc':
        pictures = pictures.order_by('pub_date')
    elif sort == 'desc':
        pictures = pictures.order_by('-pub_date')

    total_pictures = Picture.objects.count()
    pictures = pictures[PICTURES_PER_PAGE * (page_num - 1):PICTURES_PER_PAGE * page_num]
    page_buttons = []

    for i in range(1, (total_pictures // PICTURES_PER_PAGE) + 2):
        page_buttons.append(i)

    miniatures = [create_miniature(picture) for picture in pictures]

    context = {
        "pictures": zip(pictures, miniatures), 
        "page_num": page_num, 
        "page_buttons": page_buttons} 

    return render(request, "index.html", context)

def logged_in(request):
    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

def pic_view(request, pic_id):
    picture = Picture.objects.get(pk=pic_id)
    return render(request, "picture.html", {"picture": picture})

def pic_clear(request, pic_id):
    picture = Picture.objects.get(pk=pic_id)
    picture.rectangles.clear()
    return redirect('/pic/' + str(pic_id) + '/')

def pic_add_rect(request, pic_id):
    picture = Picture.objects.get(pk=pic_id)
    width = int(request.POST['width'])
    height = int(request.POST['height'])
    color = request.POST['color']
    x = int(request.POST['x'])
    y = int(request.POST['y'])
    rect = Rectangle(width=width, height=height, color=color, x=x, y=y)
    rect.save()
    picture.rectangles.add(rect)
    return redirect('/pic/' + str(pic_id) + '/')
