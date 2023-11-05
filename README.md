# Predicting mobile games' success using deep learning <br/><br/> ![Screenshot](data/GPLogo.png "Google Play Logo")

This repository contains a comprehensive project that develops a predictive model capable of predicting mobile games' success based on the data scraped from Google Play Store.

* The project was made in April 2022 and published in August 2023.

**Aim of the Project:**
The aim of this study is to preprocess near real-life data, conduct explanatory data analysis on the data set, and build a predictive model that will predict the success measure of a mobile game. 

Moreover, acknowledging the fact that much simpler models may be used for data that is mostly tabular and has a low amount of instances to learn deep representations, it is intended to use additional unstructured data like text and images to gain hands-on experience in implementing various neural network architectures via TensorFlow.

**Data Summary:**
Data contains information about games that were scraped from Google Play Store. It contains different types of data like numerical, categorical (nominal & ordinal), text, and image.

* Find raw data at **data/data_raw.csv**
* Find preprocessed data at **data/data_pp.csv**
* Find image data at **data/icon_png**


**Data Description:**
| Column Name          | Description |
| -----------          | ----------- |
| Name                 | Name of the game | 
| Number of Rating     | Total number of ratings |
| Genre                | Genre of the game |
| Rating               | Rating of the game |
| Price                | Price of the game ($) |
| Description          | Description of the game |
| Updated              | Last update date |
| Size                 | Size of the game (MB) |
| Installs             | Total installs up to a current day (not continuous) |
| Current Version      | Current version of the game |
| Requires Android     | Required min Android version |
| Content Rating	     | Targeted audience |
| Offered By	         | Developer of the game |
| Interactive Elements | Additional feature of the game|
| In-app Products      | Premium services within the app |

**Success measure (Target Variable):**
Instead of taking **Rating** or **Installs** as one target variable a combination of those two variables is created. Rating is multiplied by a log base of 10 Installs. Log base 10 is taken because there is an excessive gap between the Installs and the range of those two measures needs to be close.

---

# Walkthrough

In every Jupyter Notebook file, operations and motivations are explained in detail.

1. Find the scraper at **1. Scraper.ipynb**
* Data is scraped from [Google Play Official Website](https://play.google.com/) by using the BeautifulSoup module.
2. Find the preprocessing and explanatory data analysis steps at **2. Preprocess EDA.ipynb**
* Since there are many HTML elements, data is preprocessed and manipulated before feeding it to models. 
* Also preprocessed data are visualized and some of the features' descriptive statistics are observed to gain insights.
3. Find the NLP MODEL at **3.1. NLP_Model.ipynb**
* Text data is preprocessed, normalized, tokenized, and then trained on LSTM and Dense layers. Trained model is saved to be used in next Notebook.

(The original author of this notebook is my good fellow Ahmet Arif Turkmen who has excellent skills in NLP. However, I altered the architecture of the model that enables pre-training on the text with Descriptions and used the embedding of a pre-trained model in the training of Feed Forward Neural Network with tabular features which ended up increasing the model's performance)

4. Find the Final Models at **3.2. Final Models.ipynb**
* With benchmarks of different algorithms like KNN and Random Forrest, neural network models are trained and evaluated in the same training-test sets.
