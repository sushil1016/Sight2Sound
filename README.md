#Sight2Sound

##An Assistive Video-to-Audio Captioning Tool for the Visually Impaired

Project Workflow Summary

Utilized a pre-trained ResNet-50 model as the visual feature extractor by removing its final classification layer.
Extracted deep feature vectors from 8,000 images of the Flickr8k dataset using the modified ResNet-50 architecture.
Parsed and cleaned the Flickr8k caption dataset to generate multiple captions per image, followed by building a vocabulary based on word frequency.
Encoded captions into numerical sequences, including special tokens (e.g., START and END) to indicate sentence boundaries.
Created a paired training dataset consisting of image features and their corresponding encoded captions.
Designed a decoder using stacked LSTM layers to learn temporal patterns in the caption sequences.
Trained the image captioning model on the generated dataset and evaluated its performance on unseen test images to verify generalization.
Objective:

Image Captioning : Image Captioning is the process of generating textual description of an image. It uses both Natural Language Processing and Computer Vision to generate the captions. The dataset will be in the form [image → captions]. The dataset consists of input images and their corresponding output captions.

Encoder

The Convolutional Neural Network(CNN) can be thought of as an encoder. The input image is given to CNN to extract the features. The last hidden state of the CNN is connected to the Decoder.

Decoder

The Decoder is a Recurrent Neural Network(RNN) which does language modelling up to the word level. The first time step receives the encoded output from the encoder and also the vector.

Read the pickle or token file (https://www.kaggle.com/waelboussbat/flickr8ksau) {filename: Flickr8k.token.txt => set_0.pkl} and convert the data into the correct format which could be used for ML model.

Pickle file contains the image id and the text associated with the image.

Eg: '319847657_2c40e14113.jpg#0\tA girl in a purple shirt hold a pillow . Each image can have multiple captions.

319847657_2c40e14113.jpg -> image name
#0 -> Caption ID
\t -> separator between Image name and Image Caption A girl in a purple shirt hold a pillow . -> Image Caption
Corresponding image wrt image name can be found in the image dataset folder. Image dataset Folder : https://www.kaggle.com/waelboussbat/flickr8ksau/ Images folder can be extracted from above location

Use Pretrained Resnet-50 model trained on ImageNet dataset (available publicly on google) for image feature extraction.

Take a random image from google and generate caption for that image.

🔁 Example Process Image of cat on couch → ResNet50 gives 2048 features → “START” word is fed → Model predicts: “A” Then: “A cat” → model predicts: “sitting” Then: “A cat sitting” → model predicts: “on” ... until it says: “END”