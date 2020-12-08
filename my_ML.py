import cv2
import numpy as np
import matplotlib.pyplot as plt

url1='/home/subhankar/subhankar_110118084.jpeg'
url='/home/subhankar/plane.jpeg'
image=cv2.imread(url,cv2.IMREAD_GRAYSCALE)
#plt.imshow(image)
#plt.show()
image_BGR=cv2.imread(url,cv2.IMREAD_COLOR)

image_RGB=cv2.cvtColor(image_BGR,cv2.COLOR_BGR2RGB)
#Resize image
image_size=cv2.resize(image_RGB,(100,100))
#Bluring Image
image_blur=cv2.blur(image_RGB,(100,100))
#Kernel of the image
kernel=np.array([[0,-1,0],
						[-1,5,-1],
						[0,-1,0]])
#print(kernel)
print("Hello")
#Enhance contrast
image_kernel=cv2.filter2D(image,-1,kernel)
image_yuv=cv2.cvtColor(image_BGR,cv2.COLOR_BGR2YUV)
image_yuv[:,:,0] = cv2.equalizeHist(image_yuv[:,:,0])
image_enhance_contrast=cv2.cvtColor(image_yuv,cv2.COLOR_YUV2BGR)

 #Differentiating the colors in image

image_HSV=cv2.cvtColor(image_BGR,cv2.COLOR_BGR2HSV)
lower_blue=np.array([50,100,50])
upper_blue=np.array([130,255,255])
mask=cv2.inRange(image_HSV,lower_blue,upper_blue)
image_bgr_mask=cv2.bitwise_and(image_BGR,image_BGR,mask=mask)
image_rbg_mask=cv2.cvtColor(image_bgr_mask,cv2.COLOR_BGR2RGB)

#image Binaryrization

max_value=255
max_neighbor=99
subtract_from_mean=10
image_binarization=cv2.adaptiveThreshold(image,max_value,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,max_neighbor,subtract_from_mean)

#Remove Background
#rectangle=(0,56,256,150)
#mask=np.zeros(image_RGB.shape[:2],np.uint8)
#bgd_model=np.zeros((1,65),np.float64)
#fgd_model=np.zeros((1,65),np.uint8)
##cv2.grabCut(image_RGB,mask,rectangle,bgd_model,fgd_model,5,cv2.GC_INIT_WITH_RECT)
#mask_2=np.where((mask==2) | (mask==0),0,1).astype('uint8')
##image_rgb_nobg=img_RGB * mask_2[:,:,np.newaxis]

#Detecting Edges

median_intensity=np.median(image)
lower_threshold=int(max(0,(1.0-0.33)*median_intensity))
upper_threshold=int(max(255,(1.0+0.33)*median_intensity))
image_Canny=cv2.Canny(image,lower_threshold,upper_threshold)

#Detecting Corners

image=np.float32(image)

block_size=2
aperture=29
free_parameter=0.04

detector_response=cv2.cornerHarris(image,block_size,aperture,free_parameter)
detector_response=cv2.dilate(detector_response,None)

threshold=0.02
image_BGR[detector_response > detector_response.max()*threshold]=[255,255,255]

image_gray=cv2.cvtColor(image_BGR,cv2.COLOR_BGR2GRAY)

 #good Features to Track
corners_to_detect=10
min_quality_score=0.05
min_distance=25

corners=cv2.goodFeaturesToTrack(image,corners_to_detect,min_quality_score,min_distance)
corners=np.float32(corners)

for corner in corners:
    x,y=corner[0]
    cv2.circle(image_BGR,(x,y),25,(255,255,255),-1)

image_gray=cv2.cvtColor(image_BGR,cv2.COLOR_BGR2GRAY)

#ploting the image

plt.imshow(image_gray,cmap="gray"),plt.xticks([]),plt.yticks([])
plt.show()


