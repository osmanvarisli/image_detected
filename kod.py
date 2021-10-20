# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 09:06:36 2021

@author: Osman VARIŞLI 
"""

import cv2
import numpy as np
import time

images=['semsiye.png','yuvarlak.png','ucgen.png','yildiz.png','kelle.png','kelle2.png']

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.5

main_image = cv2.imread('resim.jpg')
for image_ in images:
    
    image_png = cv2.imread(image_)
    w, h = image_png.shape[:-1]
    result = cv2.matchTemplate(main_image, image_png , cv2.TM_CCOEFF_NORMED)
    
    threshold = .6
    loc = np.where(result >= threshold) 
    for pt in zip(*loc[::-1]): 
        cv2.rectangle(main_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        cv2.putText(main_image, image_[:-4], (pt[0] , pt[1] + h+20), font, 
                   fontScale, (0, 255, 255), 1, cv2.LINE_AA)  
        
        if image_ in ['semsiye.png','yuvarlak.png','ucgen.png','yildiz.png']: break

    cv2.destroyAllWindows()
    cv2.imshow(image_, main_image)
    initial_time = time.time()
    cv2.waitKey(3000)
    final_time = time.time()  
        
        

cv2.waitKey(0)