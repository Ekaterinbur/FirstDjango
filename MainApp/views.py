from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
    }  

items = [
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
    {"id": 7, "name": "Картофель фри" ,"quantity":0},
    {"id": 8, "name": "Кепка" ,"quantity":124},
    ]

# def home(request): -- Домашняя страница ---проба -- day_1
#     text = """
#     <h1> "Изучаем django" </h1>
#     <strong> Автор </strong>:  <i> Буравкова Е.И. </i>
#     """
#     return HttpResponse (text)

def home(request): ## day_2 
    context ={
        "name": "Иванов Иван Иванович",
        "email": "my_mail@mail.ru"
    }
    return render (request, "index.html",context)

def about(request):
    text = f"""
    <header>
        <a href = "/"> Home </a> / <a href = "/items"> Items </a> / <a href = "/about"> About </a>
    </header> 
    <br>
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Фамилия: <b>{author["Фамилия"]}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse (text)

def get_item(request,item_id: int):
    item = next ((item for item in items if item ["id"] == item_id), None)
    if item :
        context ={
            "item": item
        }
        return render (request, "item_page.html", context)
    return HttpResponseNotFound (f'Item with id = {item_id} not found.')

def get_items(request):
    # result = f"<h2> Cписок товаров </h2> <ol>" --- day_1 
    # for item in items:
    #     result += f""" <li><a href="/item/{item ["id"]}"> {item ["name"]} </a></li>"""
    # result += "</ol>"
    # return HttpResponse (result)
    context = { 
        "items": items
    }
    return render (request, "items_list.html",context)

