

#import matplotlib.pyplot as plt
#get_ipython().run_line_magic('matplotlib', 'inline')



import cv2 



from imageai.Detection import ObjectDetection
import os
#from IPython.core.getipython import get_ipython

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "media/resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "media/dog_cycle.jpeg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )



img = cv2.imread('imagenew.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

#plt.imshow(img_rgb)


