* Utilized a pre-trained **ResNet-50** model as the visual feature extractor by removing its final classification layer.
* Created a paired **training dataset** consisting of image features and their corresponding encoded captions.
The Convolutional Neural Network(CNN) can be thought of as an encoder. The input image is given to CNN to extract the features. The last hidden state of the CNN is connected to the Decoder.
* Use Pretrained Resnet-50 model trained on ImageNet dataset (available publicly on google) for image feature extraction.
ResNet50 gives 2048 features →
"""# **ResNet50 Pretrained Model**
1. Using ResNet50 Model to extract image features
2. Create ResNet50 instacnce
3. Create keras Model using ResNet50
4. Extract feature from images
from tensorflow.keras.applications import ResNet50
# incept_model = ResNet50(include_top=True)
incept_model = ResNet50(weights='imagenet',
"""##### Extract image features"""
from tensorflow.keras.applications.resnet50 import preprocess_input
images_features = {}
    img_data = preprocess_input(img_data) #Preprocesses the image (like normalizing pixel values) to match the format ResNet50 was trained on.
    cnn_feature = incept_model.predict(img_data,verbose=0) #Feeds the image into the pretrained ResNet50 model.
    images_features[i.split('/')[-1]] = cnn_feature #Stores the feature vector in the dictionary using the image filename as the key.
len(images_features)
from tensorflow.keras.applications.resnet50 import preprocess_input
def extract_features_from_images(image_dir, image_keys, limit=5000):
    features = {}
        img_data = preprocess_input(img_data)
        features[img_name] = incept_model.predict(img_data, verbose=0)
    return features
mscoco_features = extract_features_from_images(mscoco_images_dir, mscoco_captions.keys(), limit=5000)
"""Filter the captions to match only the images for which feature vectors are created so far"""
# Now filter based on available image features
    if img_name in images_features:
2. Generate X & y data set using image features & caption dictionary (Preparing the training data for the decoder model (LSTM) by creating input-output pairs from given dataset.)
X, y_in, y_out = generator(images_features, captions_dict)
image_input = Input(shape=(2048,), name="image_input")  # Input vector for image features from 2nd last layer of ResNet50
test_feature = incept_model.predict(getImage(test_img_path))
    prediction = np.argmax(model.predict([test_feature, encoded]))
3	Preprocess each frame and extract features using ResNet50
    img = preprocess_input(img)
    test_feature = incept_model.predict(getImage_from_frame(frame)).reshape(1, 2048)  # shape depends on your model
        prediction = np.argmax(model.predict([test_feature, encoded]))