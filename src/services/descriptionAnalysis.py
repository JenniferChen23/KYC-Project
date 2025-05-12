import pickle

# 第三步：載入模型
import tensorflow as tf
import numpy as np
import os

# 第四步：定義必要常數與預處理函數
MAXLEN = 120  # 與你訓練模型時使用的 MAXLEN 一致
# 第三步：載入模型與 tokenizer（從檔案）
# 計算專案根目錄（src 的上一層）
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 正確取得 tokenizer.pickle 路徑
tokenizer_path = os.path.join(BASE_DIR, 'models', 'tokenizer.pickle')
with open(tokenizer_path, 'rb') as handle:
    tokenizer = pickle.load(handle)

model_path = os.path.join(BASE_DIR, 'models', 'model.h5')

# 載入模型
model = tf.keras.models.load_model(model_path)

def seq_and_pad(sentences, tokenizer, padding, maxlen):
    sequences = tokenizer.texts_to_sequences(sentences)
    padded_sequences = tf.keras.utils.pad_sequences(sequences, maxlen=maxlen, padding=padding)
    return padded_sequences

def predict_startup_success(text):
    padded_input = seq_and_pad([text], tokenizer, padding='post', maxlen=MAXLEN)
    prediction = model.predict(padded_input)
    print("兩個類別的機率",prediction)
    pred_class = np.argmax(prediction, axis=-1)[0]
    result = "Predict Live" if pred_class == 1 else "Risky"
    print("預測結果:", result)
    return result
