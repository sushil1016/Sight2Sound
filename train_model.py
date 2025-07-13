Model predicts: “A”
from tensorflow.keras.models import Model
modele = Model(inputs = incept_model.input,outputs = last) #Gives the output from the second last layer, not the final prediction layer.
"""# **Modelling**
3. Model after training will be used of predictions
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import LSTM
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.layers import Dense, Flatten,Input, Convolution2D, Dropout, LSTM, TimeDistributed, Embedding, Bidirectional, Activation, RepeatVector,Concatenate
from tensorflow.keras.models import Sequential, Model
#     language_model.add(LSTM(params[1], return_sequences=True))
# #     x = LSTM(128, return_sequences=True)(conca)
# #     x = LSTM(512, return_sequences=False)(x)
#     x = LSTM(params[2], activation="relu", return_sequences=True, kernel_regularizer=regularizers.l1(0.01), bias_regularizer=regularizers.l1(0.01))(conca)
#     x = LSTM(params[3], activation="relu", return_sequences=True, kernel_regularizer=regularizers.l1(0.01), bias_regularizer=regularizers.l1(0.01))(x)
#     x = LSTM(params[4], activation="relu", return_sequences=True, kernel_regularizer=regularizers.l1(0.01), bias_regularizer=regularizers.l1(0.01))(x)
#     x = LSTM(params[5], activation="relu", return_sequences=True, kernel_regularizer=regularizers.l1(0.01), bias_regularizer=regularizers.l1(0.01))(x)
#     x = LSTM(params[6], activation="relu", return_sequences=False, kernel_regularizer=regularizers.l1(0.01), bias_regularizer=regularizers.l1(0.01))(x)
#     model = Model(inputs=[image_model.input, language_model.input], outputs = out)
#     history = model.fit([X, y_in], y_out, batch_size=params[8], epochs=params[9], validation_split=0.2)
# pd.DataFrame(h1.history).plot(figsize=(4,4), xlabel='Model Loss')
# pd.DataFrame(h2.history).plot(figsize=(4,4), xlabel='Model Loss')
# pd.DataFrame(h3.history).plot(figsize=(4,4), xlabel='Model Loss')
# pd.DataFrame(h4.history).plot(figsize=(4,4), xlabel='Model Loss')
# pd.DataFrame(h5.history).plot(figsize=(4,4), xlabel='Model Loss')
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, RepeatVector, TimeDistributed, Concatenate, Activation
text_lstm = LSTM(256, return_sequences=True)(text_embedded)
x = LSTM(128, return_sequences=True)(merged)
x = LSTM(512, return_sequences=False)(x)
model = Model(inputs=[image_input, text_input], outputs=output)
"""**Model Training**"""
model.fit([X, y_in], y_out, batch_size=512, epochs=30, initial_epoch=3)
"""**Automatic Video-to-Text Captioning using Key Frame Extraction and Image Captioning Model**