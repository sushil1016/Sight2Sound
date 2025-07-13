* Extracted deep feature vectors from **8,000 images** of the **Flickr8k** dataset using the modified ResNet-50 architecture.
* Parsed and cleaned the **Flickr8k caption dataset** to generate multiple captions per image, followed by building a vocabulary based on word frequency.
Read the pickle or token file  (https://www.kaggle.com/waelboussbat/flickr8ksau) {***filename***: Flickr8k.token.txt => set_0.pkl} and convert the data into the correct format which could be used for ML model.
import kagglehub
path = kagglehub.dataset_download("adityajn105/flickr8k")
coco_path = kagglehub.dataset_download("arunmohan003/coco2017-dataset")
    data = json.load(f)
It reads caption data from the Flickr8k dataset and converts it into a Python dictionary, then saves it as a .pkl (pickle) file for later use.
input_txt_path = "/content/Flickr8k.token.txt"
    captions_dict = pickle.load(f)
    captions = pickle.load(f)