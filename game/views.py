from django.http import HttpResponse

def index(request):
    line0 = '<hr>'
    line1 = '<h1 style="font-size: 100px; color: pink; text-align:center">McKenna·Grace</h1>'
    line2 = '<hr>'
    line3 = '<img width=1000px src="https://img1.baidu.com/it/u=398310624,119349209&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500">'
    line4 = '<hr>'
    line5 = '<a style="font-size:50px; text-decoration: none; padding-left: 250px;" href="/play/" >--> Annabelle Comes Home <-- </a>'

    return HttpResponse(line0 + line1 + line2 + line3 + line4 + line5)

def play(request):
    line0 = '<hr>'
    line1 = '<h1 style="font-size: 100px; color: brown; text-align:center">Annabelle Comes Home</h1>'
    line2 = '<hr>'
    line3 = '<img width=1000px src="https://nimg.ws.126.net/?url=http%3A%2F%2Fcrawl.ws.126.net%2F792c71f6b6b8c923ab8706c6b91c9f48.jpg&thumbnail=660x2147483647&quality=80&type=jpg">'
    line4 = '<hr>'
    line5 = '<a style="font-size:50px; text-decoration: none; padding-left:400px;" href="/"> --> EXIT <-- </a>'

    return HttpResponse(line0 + line1 + line2 + line3 + line4 + line5)
