#Import library using
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import json
from utils import checkPhone
#Image processs
class Animal():
    def __init__(self):
        self.model = load_model("best_model.h5")
        self.label = ['antelope', 'bat', 'beaver', 'bobcat', 'buffalo', 'chihuahua', 'chimpanzee', 'collie', 'dalmatian',
                 'german+shepherd', 'grizzly+bear',
                 'hippopotamus', 'horse', 'killer+whale', 'mole', 'moose', 'mouse', 'otter', 'ox', 'persian+cat',
                 'raccoon', 'rat',
                 'rhinoceros', 'seal', 'siamese+cat', 'spider+monkey', 'squirrel', 'walrus', 'weasel', 'wolf']
    def predict_test(self,filename):
        self.label.sort()
        img = tf.keras.preprocessing.image.load_img(filename, target_size=(256, 256))
        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, 0)  # Create batch axis
        logit = self.model.predict(img_array)
        # score = model.predict_proba(img_array)
        scoreList = tf.sigmoid(logit)
        idx = np.argmax(tf.constant(logit), axis=-1)[0]
        score = scoreList[0][label]
        # score_arr = tf.argmax(lb, -1)
        idx = np.argmax(lb, axis=-1)[0]
        return self.label[idx],float(np.array(score))

#NLP process
class PostBuy():
    def __init__(self,stopwordWeight=0.2,animalDict="dict.json",phonedict="phone.json"):
        self.mark = "!,./()?@#^&*-_<>"
        self.stopwordWeight = stopwordWeight
        self.animalDict = json.load(open(animalDict,encoding="utf-8"))
        self.phoneDict = json.load(open(phonedict,encoding="utf-8"))
    
    #preprocess sentence
    def preprocess(self,sentence):
        sentence = sentence.lower()
        tmp = ""
        for i in range(len(sentence)):
            if (sentence[i] in self.mark):
                tmp+=""
            else:
                tmp += sentence[i]
        return tmp
    
    #tokenizer sentence
    def tokenizer(self,sentence):
        tokenList = sentence.split(" ")
        return tokenList

    #calculate probability of being negative
    def calculateProbabity(self,sentence):
        tokenList = self.tokenizer(sentence)
        sentenceWeight = 0
        awareWeight = 0
        for token in tokenList:
            if token in self.animalDict.keys():
                awareWeight+=self.animalDict[token]
                sentenceWeight+=self.animalDict[token]
            else:
                sentenceWeight+=self.stopwordWeight
        awarenessProbability = awareWeight/sentenceWeight
        return awarenessProbability
    
    #extract phone number
    def extractPhoneNumber(self,phoneNumber):
        try:
            s1 = "0123456789"
            res= ""
            i =0
            s = phoneNumber  
            while (i<len(s)):
                if s[i] not in s1:
                    tmp =""
                    j = i
                    while(True):        
                        if (tmp in self.phoneDict.keys()):
                            num = int(self.phoneDict[tmp])
                            tmp = ""
                            res+=str(num)
                            i = j
                            break
                        tmp+=s[j]
                        j+=1
                else:
                    res+=s[i]
                    i+=1
            return res
        except:
            return phoneNumber

    def trackPhoneNumber(self,caption):
        tokenList = self.tokenizer(caption)
        out = []
        for token in tokenList:
            if checkPhone(token):
                out.append(token)
        return out

    #predict probability
    def predict(self,caption):
        captionProccessed = self.preprocess(caption)
        tokenList = self.tokenizer(captionProccessed)
        probability = self.calculateProbabity(tokenList)
        return probability
    


