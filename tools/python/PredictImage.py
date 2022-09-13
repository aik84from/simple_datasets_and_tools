import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions


class PredictImage:
    def __init__(self):
        self.model = ResNet50(weights='imagenet')

    def predict(self, filename):
        img = image.load_img(filename, target_size=(224, 224))
        data = np.expand_dims(image.img_to_array(img), axis=0)
        return decode_predictions(self.model.predict(preprocess_input(data)), top=5)[0]

