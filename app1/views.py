from cmath import e

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .models import *
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import viewsets
from .CustomeResponse import CustomeResponse


# **************************************************************** serializers.py ************************************************************ #

#**************************************************************** views.py ************************************************************ #
#**************************************************************** insert_view ************************************************************ #
# from requests import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# from app1.CustomeResponse import CustomeResponse
# from app1.serializers import *


@api_view(['Post'])
def inserttodolistview(request):
    serializer=todolistserilizers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(CustomeResponse("Inserted Successfully", status.HTTP_200_OK, False))
    return Response(CustomeResponse("Invalid Data", status=status.HTTP_400_BAD_REQUEST))

#**************************************************************** update_view ************************************************************ #

@api_view(['POST'])
def updatetodolistview(request,pk):
    todolist = tbl_todolist.objects.get(pk=pk)  # to fetch the all data
    # countryname=request.data['countryname']
    serializer = todolistupdateserilizers(instance=todolist, data=request.data)  # converts in json
    if serializer.is_valid():
        serializer.save()
        return Response(CustomeResponse("Data Updated Successfully", status=status.HTTP_200_OK))
    return Response(CustomeResponse("Invalid Data", status=status.HTTP_400_BAD_REQUEST))

# ************************************************************ delete_view ************************************************************ #

@api_view(['DELETE'])
def deletetodolistview(request,pk):
    try:
        todolist = tbl_todolist.objects.get(pk=pk)  # to fetch the all data
        x = todolist.delete()
        # print(len(x))
        if len(x) != 0:
            # print(len(x))
            # return Response(status=status.HTTP_204_NO_CONTENT)
            return Response(CustomeResponse("Data Deleted Successfully", status=status.HTTP_200_OK))
        return Response(CustomeResponse("Data Not Found", status=status.HTTP_204_NO_CONTENT))
    except Exception as e:
        return Response(CustomeResponse("Data Not Found", status=status.HTTP_204_NO_CONTENT))

# ************************************************************ search_by_id_view ************************************************************ #

@api_view(['Get'])
def searchtodolistbyidview(request,pk):
    todolist = tbl_todolist.objects.filter(pk=pk)   # to fetch the all data
    if len(todolist)!=0:
        serializer = todolistserilizers(todolist, many=True)  # converts in json
        return Response(CustomeResponse(serializer.data, status.HTTP_200_OK, False))
    return Response(CustomeResponse("Data Not Found", status=status.HTTP_404_NOT_FOUND))

# ************************************************************ search_view ************************************************************ #

@api_view(['Get'])
def searchtodolistview(request):
    todolist = tbl_todolist.objects.all()  # to fetch the all data
    if len(todolist)!=0:
        serializer = todolistserilizers(todolist, many=True)  # converts in json
        return Response(CustomeResponse(serializer.data, status.HTTP_200_OK, False))
    return Response(CustomeResponse("Data Not Found", status=status.HTTP_404_NOT_FOUND))
