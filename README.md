# Predicting mobile games' success using deep learning

This repository contains a comprehensive project that develops a predictive model capable of forecasting mobile games' success based on the data scraped from Google Play Store.

Additionally, this project utilizes deep learning through the use of TensorFlow.

**Aim of the Project:**
The aim of this study is to conduct explanatory data analysis on the data set and build a predictive model that will predict the success measure of a game. Moreover, it is intended to use additional unstructured data like text and images to develop an overall usage of whole data and exercise the application of NLP and computer vision tasks.

**Data Summary:**
Data contains information about games that were scraped from Google Play Store. It contains different types of data like numerical, categorical (nominal & ordinal), text, and image. The folder that contains the image is in data/icon_png.

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
| Installs             | Total installs up to current day (not continuous) |
| Current Version      | Current version of the game |
| Requires Android     | Required min Android version |
| Content Rating	     | Targeted audience |
| Offered By	         | Developer of the game |
| Interactive Elements | Additional feature of the game|
| In-app Products      | Premium services within the app |

**Success measure (Target Variable):**
Instead of taking **Rating** or **Installs** as one target variable a combination of those two variables is created. Rating is multiplied by a log base of 10 Installs. Log base 10 is taken because there is an excessive gap between the Installs and the range of those two measures needs to be nearly the same.
