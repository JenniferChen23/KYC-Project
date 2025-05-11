import pickle
from models import model
from models import tokenziser
# 第三步：載入模型
import tensorflow as tf
import numpy as np


# 第四步：定義必要常數與預處理函數
MAXLEN = 120  # 與你訓練模型時使用的 MAXLEN 一致

def seq_and_pad(sentences, tokenizer, padding, maxlen):
    sequences = tokenizer.texts_to_sequences(sentences)
    padded_sequences = tf.keras.utils.pad_sequences(sequences, maxlen=maxlen, padding=padding)
    return padded_sequences

def predict_startup_success(text):
    padded_input = seq_and_pad([text], tokenizer, padding='post', maxlen=MAXLEN)
    prediction = model.predict(padded_input)
    print("兩個類別的機率",prediction)
    pred_class = np.argmax(prediction, axis=-1)[0]
    result = "✅ 成功" if pred_class == 1 else "❌ 失敗"
    print("預測結果:", result)
