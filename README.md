# IBM-Capstone-Project

Summary
This capstone project aims to predict the success of the SpaceX Falcon 9 first-stage landing using various machine learning classification algorithms. The core steps of the project include:

Data collection, cleaning, and formatting
Exploratory data analysis (EDA)
Interactive data visualization
Machine learning-based prediction
Our analysis indicates that certain rocket launch features correlate with the success or failure of the launches. The decision tree algorithm was identified as the most effective machine learning model for predicting Falcon 9 first-stage landing success.

Introduction
The goal of this capstone project is to predict whether the Falcon 9 first-stage rocket will successfully land. SpaceX advertises Falcon 9 launches at a price of $62 million, significantly lower than the $165 million charged by other providers. A large part of this cost savings comes from the reusability of the Falcon 9 first stage. By predicting the success of a first-stage landing, we can estimate the cost of a launch. This information could also be valuable to potential competitors bidding against SpaceX for rocket launches.

Unsuccessful landings are typically planned, and sometimes SpaceX performs controlled ocean landings. The central question we aim to answer is: Given a set of features about a Falcon 9 rocket launch (e.g., payload mass, orbit type, launch site), can we predict whether the first stage of the rocket will land successfully?

Methodology
The methodology for this project consists of:

Data Collection, Wrangling, and Formatting
Using SpaceX API and web scraping techniques

Exploratory Data Analysis (EDA)
Using Pandas, NumPy, and SQL for data exploration

Data Visualization
Using Matplotlib, Seaborn, Folium, and Dash for interactive data visualization

Machine Learning Prediction
Implementing Logistic Regression, Support Vector Machine (SVM), Decision Trees, and K-Nearest Neighbors (KNN)

Data Collection Using SpaceX API
Data Collection API.ipynb

Libraries used: requests, pandas, numpy, datetime

Data is retrieved from the SpaceX API, specifically filtered for Falcon 9 launches. The API is accessed using requests.get(), and the response is processed into a DataFrame using json_normalize(). Missing values are filled with the mean value of their respective columns. This process results in 90 rows and 17 columns.

Data Collection Using Web Scraping
Data Collection with Web Scraping.ipynb

Libraries used: sys, requests, BeautifulSoup, re, unicodedata, pandas

Data is scraped from the Falcon 9 and Falcon Heavy launches page. After requesting the webpage, the table data is parsed using BeautifulSoup, and a DataFrame is created with the extracted data. This process results in 121 rows and 11 columns.

Exploratory Data Analysis (EDA)
EDA with Pandas and Numpy.ipynb

Libraries used: pandas, numpy

Basic insights are derived using Pandas and NumPy functions such as value_counts(), including:

Number of launches per site
Orbit type distributions
Mission outcome counts
EDA with SQL.ipynb

Framework used: IBM DB2
Libraries used: ibm_db

SQL queries are used to extract valuable insights from the data, such as:

Unique launch sites
Total payload mass for NASA launches
Average payload mass for a specific booster version
Data Visualization
Data Visualization with Matplotlib and Seaborn

Libraries used: pandas, numpy, matplotlib.pyplot, seaborn

Various visualizations (scatterplots, bar charts, line charts) are used to explore relationships between features, such as:

Flight number vs. launch site
Payload mass vs. launch site
Mission outcome vs. orbit type
Interactive Data Visualization with Folium

Libraries used: folium, wget, pandas, math

Folium is used to create interactive maps to visualize launch sites, successful and failed landings, and distances to nearby landmarks such as cities and highways.

Data Visualization with Dash

Libraries used: pandas, dash, plotly.express

Dash is employed to create an interactive web application for visualizing launch site success rates and payload mass correlations. Users can interact with pie charts and scatterplots.

Machine Learning Prediction
Machine Learning Prediction.ipynb

Libraries used: pandas, numpy, matplotlib.pyplot, seaborn, sklearn

The machine learning phase includes:

Standardization: Data is standardized using StandardScaler.
Model Training: Models are trained using LogisticRegression, SVC, DecisionTreeClassifier, and KNeighborsClassifier.
Hyperparameter Tuning: GridSearchCV is used to find the best hyperparameters for each model.
Evaluation: Models are evaluated based on accuracy scores and confusion matrices.
The models are ranked based on their best GridSearchCV scores as follows:

Decision Tree (best score: 0.889)
K-Nearest Neighbors (best score: 0.848)
Support Vector Machine (best score: 0.848)
Logistic Regression (best score: 0.846)
Discussion
The data visualizations suggest that certain features, such as payload mass and orbit type, may influence the success or failure of a mission. For example, heavier payloads show higher success rates for certain orbit types like Polar, LEO, and ISS. However, GTO orbit shows a mix of successful and unsuccessful missions.

Each feature's impact on the final mission outcome is complex, but machine learning algorithms can learn these patterns from historical data to predict future mission success.

Conclusion
This project aimed to predict the success of Falcon 9 first-stage landings based on various launch features. Machine learning algorithms were employed to learn from past data, and the decision tree algorithm emerged as the most effective model for predicting the launch outcome.

Completed: 17/11/2024
