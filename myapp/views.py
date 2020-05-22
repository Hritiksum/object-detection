#!/usr/bin/python
# -*- coding: utf-8 -*-
def warn(*args, **kwargs):
    pass

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from .models import *




def upload(request):
    default="/media/dog_cycle.jpeg"
    import requests
    arr=[]
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs=FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
        #f = open("media/"+uploaded_file.name, "r")
        #print(f.read())
        #storage=[]
        #num=0
        import cv2 
        from imageai.Detection import ObjectDetection
        import os
        #from IPython.core.getipython import get_ipython

        execution_path = os.getcwd()

        detector = ObjectDetection()
        detector.setModelTypeAsRetinaNet()
        detector.setModelPath( os.path.join(execution_path , "media/resnet50_coco_best_v2.0.1.h5"))
        detector.loadModel()

        #detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "/content/drive/My Drive/minor2final/dog_cycle.jpeg"), output_image_path=os.path.join("/content/drive/My Drive/minor2final" , "imagenew.jpg"))

        detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "media/"+uploaded_file.name), output_image_path=os.path.join(execution_path , "static/"+"1"+uploaded_file.name))
        
        for eachObject in detections:
            #print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
            arr.append(str(eachObject["name"]) +  " : " + str(eachObject["percentage_probability"]))
        print (arr)


        #img = cv2.imread('imagenew.jpg')
        #img_rgb = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        #plt.imshow(img_rgb)



        default="/static/"+"1"+uploaded_file.name


       
            
    return render(request,'upload.html',{'result':arr,'f5':default})



def error_404_view(request, exception):
    return render(request,'404.html')

def index(request):
    try:
        return render(request, 'index.html')
    except:
        return render(request, '404.html')

