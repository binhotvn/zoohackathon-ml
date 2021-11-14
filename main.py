from flask import Flask,request,redirect, url_for, send_from_directory,Response,jsonify
import tensorflow as tf
# import Pillow
from tensorflow.keras.models import load_model
import numpy as np
import urllib.request
from AnimalPred import Animal,PostBuy
from utils import calculate_prob

#init class for Image and Text-processing
animal = Animal()
postProcess = PostBuy()

url = "30.102.5.4" # server url

#main script
def detectAnimal():
    try:
        while True:
            #get data from media
            rev = request.get(url)
            mediaRequest = rev["media"]
            mediaType = mediaRequest["type"] 
            urlList = mediaRequest["media"]

            #get data from Post
            postRequest = rev["post"]
            caption = postRequest["caption"]
            comment = postRequest["comment"]
            violate = PostBuy.calculateProbabity(caption)
            phone = PostBuy.extractPhoneNumber(PostBuy.trackPhoneNumber(caption))

            labelList = []
            scoreList = []
            violate = []

            #get Url Images
            if mediaType == "image":
                for imgUrl in range(len(urlList)):
                    dir_dst = "./database/"+str(imgUrl.split("/")[-1])
                    urllib.request.urlretrieve(imgUrl,dir_dst)
                    label , score = Animal.predict_test(dir_dst)
                    labelList.append(label)
                    scoreList.append(score)

            #define response
                response = dict()
                response["animal"]= labelList
                response["score"] = score[0]
                response["evaluate"] = violate
                response["phone"] = phone
            
            #post request
            ret = request.post("")
            res = {"statusCode":200,
                "message":"UPDATED"}
                
        # return when disconnect server
        return {"errorCode":-1,
                "status":"Finish mission"}
    except:
        return {"errorCode":0,
                "status":"Server Shutdown"}

if __name__=="__main__":
    detectAnimal()



