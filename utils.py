import tensorflow as tf
from tensorflow.keras.models import load_model

def calculate_prob(logits):
    return tf.nn.sigmoid(logits)

def checkPhone(phoneNumber):
    check = 0
    s ="0123456789"
    for i in range(len(phoneNumber)):
        if phoneNumber[i] in s:
            check = 1
    return check