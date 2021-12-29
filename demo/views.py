from django.shortcuts import render
from rest_framework.response import Response
from demo.serializers import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
import csv,json,requests
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}
	tasks=task.objects.all().values()
	return Response({'Book List':tasks})
@api_view(['GET'])
def tasklist(request):
    tasks=task.objects.all()
    serializers=taskserializer(tasks,many=True)
    return Response(serializers.data)
@api_view(['POST'])
def taskcreate(request):
	tasks=task.objects.all()
	#serializers=taskserializer(tasks,many=True)
	serializer=taskserializer(data=request.data,many=isinstance(request.data,list))
	if serializer.is_valid():
		serializer.save()
		""" export part started """
		data=requests.get("http://127.0.0.1:8000")
		Data=json.loads(data.content)
		testdata=Data["Book List"]
		file=open('s1.csv','w')
		csv_writer=csv.writer(file)
		count=0
		for test in testdata:
			if count==0:
				header=test.keys()
				csv_writer.writerow(header)
				count+=1
			csv_writer.writerow(test.values())
		file.close()
		""" export part ended """
	return Response(serializer.data)
@api_view(['GET'])
def tasksid(request,pk):
	tasks=task.objects.get(id=pk)
	serializer=taskserializer(tasks,many=False)
	return Response(serializer.data)
@api_view(['POST'])
def taskupdate(request,pk):
	tasks=task.objects.get(id=pk)
	serializershow=taskserializer(tasks)
	serializer=taskserializer(instance=tasks,data=request.data)
	if serializer.is_valid():
		serializer.save()
		Response(serializer.data,serializershow)
@api_view(['GET'])
def taskid(request,title):#title is used to pass the title in the url
	tasks=task.objects.get(title=title)#pass the title in the parameter
	serializers=titleserializer(tasks)
	return Response(serializers.data)