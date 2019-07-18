# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 17:06:03 2019

@author: Administrator
"""
import numpy as np
'''
def mediannum(listvalue):
    ave=listvalue.sum()/len(listvalue)
    presult=[]
    nresult=[]
    for i in listvalue:
        result=i-ave
        if result>=0:
            presult.append(i)
        else:
            nresult.append(i)
    
    if len(nresult) or len(nresult)
 '''
def medianBlur(img, kernel, padding_way):
     img_width=img.shape[1]
     img_height=img.shape[0]
     pad_rsize=kernel.shape[0]//2#先行后列
     pad_csize=kernel.shape[1]//2
     if pad_rsize !=pad_csize:
          raise ValueError('The kernelsize is invalid!')
     padding_image=np.zeros([img_height+pad_rsize,img_width+pad_rsize])
     if padding_way=="Zeros":
         padding_image[pad_rsize:pad_rsize+img_height,pad_csize:pad_csize+img_width]=img
     if padding_way=="REPLICA":
         padding_image[:pad_rsize,pad_csize:pad_csize+img_width]=img[0]
         padding_image[-pad_rsize:,pad_csize:pad_csize+img_width]=img[-1]
         padding_image[pad_rsize:,:pad_csize]=img[:,0:1]
         padding_image[pad_rsize:,pad_csize+img_width:]=img[:,-1:]
     wind_img=np.ones([kernel.shape[0],kernel.shape[1]])
     for j in range(img_width):
         for i in range(img_height):
             wind_img=wind_img*padding_image[i:i+kernel.shape[0],j:j+kernel.shape[1]]
             list_wind=wind_img.flatten()
             #medianvalue=mediannum(list_wind)
             img[i,j]=list_wind.sort()[kernel.shape[0]//2+1]
     return img
             
             
     
