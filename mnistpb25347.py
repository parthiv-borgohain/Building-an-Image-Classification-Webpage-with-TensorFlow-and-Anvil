import keras

model = keras.models.load_model("final_CNN_model.h5")
import numpy as np
import pandas as pd
import anvil.media
import tensorflow as tf
import matplotlib.pyplot as plt
import anvil.server
anvil.server.connect("server_PAAPP5OGEDBF7EFHR6TKXQUD-SHHV56YP2W6MJFAL")


@anvil.server.callable
def get_result(file):
    with anvil.media.TempFile(file) as filename2:
      try:
        df = pd.read_csv(filename2,header=None)
        image_matrix = np.array(df)
        dim = image_matrix.shape
        image_tensor = image_matrix.reshape((1,dim[0],dim[1],1))
        predprob = model.predict(image_tensor)[0,:]
        return np.argmax(predprob), np.flipud(image_matrix)
      except:
        return "Error","Error"
anvil.server.wait_forever()