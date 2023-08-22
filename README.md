# Predicting mobile games' success using deep learning ![Screenshot](data/GPLogo.png "Google Play Logo")

This repository contains a comprehensive project that develops a predictive model capable of forecasting mobile games' success based on the data scraped from Google Play Store.

Additionally, this project utilizes deep learning through the use of TensorFlow.

* Project is made in April 2022 and published in August 2023.

**Aim of the Project:**
The aim of this study is to conduct explanatory data analysis on the data set and build a predictive model that will predict the success measure of a game. Moreover, it is intended to use additional unstructured data like text and images to develop an overall usage of whole data and exercise the application of NLP and computer vision tasks.

**Data Summary:**
Data contains information about games that were scraped from Google Play Store. It contains different types of data like numerical, categorical (nominal & ordinal), text, and image.

* Find raw data at **data/data.csv**
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
Instead of taking **Rating** or **Installs** as one target variable a combination of those two variables is created. Rating is multiplied by a log base of 10 Installs. Log base 10 is taken because there is an excessive gap between the Installs and the range of those two measures needs to be nearly the same.

---

# Walkthrough

In every Jupyter Notebook file, operations and motivations are explained in detail.

* Find the scraper at **data/scrape/0. Scraper.ipynb**
1) Data is scraped from [Google Play Official Website](https://play.google.com/) by using the BeautifulSoup module.
* Find the preprocessing and explanatory data analysis steps at **1. Preprocess EDA.ipynb**
2) Since there are many HTML elements, data is preprocessed and manipulated before feeding it to models. 
3) Also preprocessed data are visualized and some of the features' descriptive statistics are observed to gain insights.
* Find the NLP MODEL at **2.1. NLP_Model.ipynb**
(this notebook's author is my good fellow Ahmet Arif Turkmen who has excellent skills in NLP)
4) A predictive model is created based on textual features **Name** and **Description**.
* Find the Final Models at **2.1. Final Models.ipynb**
5) Different predictive models are created in that Jupyter Notebook.

