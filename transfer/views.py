from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from transfer.serializer import FilelistSerializer
# Create your views here.
class TransferViewset(viewsets.ViewSet):
    def create(self,request):
        try:
            print(request.data)
            serilalizer=FilelistSerializer(data=request.data)
            if serilalizer.is_valid():
                serilalizer.save()
                return Response({'message':'created sucessfully','data':serilalizer.data},status=status.HTTP_201_CREATED)
            return Response({'message':'something went wrong'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

