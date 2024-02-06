from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from .CommentSerialaizer import ItemSerializer,CommentSerialaizerOut
from .models import Comment,Product

@api_view(["GET"])
def FirstGet(request):
    if request.method == "GET":
        return Response({"message":"My first get request"})

@api_view(["POST"])
def FirstPost(request):
    if request.method == "POST":
        data = request.data
        print(data)
        return Response({"message":"My first post request"})

@api_view(["POST"])
def Zapros(request):
    if request.method == "POST":
        aloowedLevel = ["B3","B4"]
        comment = Comment(**ItemSerializer(data=JSONParser().parse(io.BytesIO(request.body))).data)
        return Response(comment.status)
        # data = request.data
        # print(data)
        # if int(data["age"]) >= 25 and data["angl"] in aloowedLevel:
        #     return Response({"message":f"{data["name"]} подходит"})
        # else:
        #     return Response({"massage":f"{data["name"]} не подходит"})
@api_view(["POST"])
def SecondPost(request):
    comment = Comment.object.get()
    serialaize = CommentSerialaizerOut(Comment)
    json = JSONRenderer().render(serialaize.data)
    return Response(json)

@api_view(["POST"])
def Receive(request):
    if request.method == "POST":
        product = Product(**ItemSerializer(data=JSONParser().parse(io.BytesIO(request.body))).data)
        return Response(product)

@api_view(["POST"])
def MainPost(request):

    serialaize = CommentSerialaizerOut(Product)
    json = JSONRenderer().render(serialaize.data)
    return Response(json)

