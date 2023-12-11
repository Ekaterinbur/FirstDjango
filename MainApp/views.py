from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

author = {
    "Имя": "Иван",
    "Фамилия": "Иванов"
}

def home(request):
    text = """
    <h1> "Изучаем django" </h1>
    <strong> Автор </strong>:  <i> Буравкова Е.И. </i>
    """
    return HttpResponse (text)


def about(request):
    text = f"""


    Имя: <b> {author ["Имя"]} </b> <br>
    Фамилия: <b> {author ["Фамилия"]} </b> <br>

    
    """
    return HttpResponse (text)
