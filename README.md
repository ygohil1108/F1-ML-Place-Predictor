# F1 Racing Machine Learning Place Predictor

 An End-to-End Machine Learning Project Formula 1 Racing

# Overview
- This project is an end-to-end machine learning web application that predicts the final places of drivers at future races based on historical racing and telemetry data.
- This project adds value to the field of Formula 1 data science by showing the metrics that best predict good outcomes for drivers and constructors.
- This project aims to predict the finish domains of the drivers based on race data. It will predict either Podium (1st -3rd), Points (4th - 10th), or No Points (11th - 20th). 
- Since Formula 1 Racing is a sport decided in mere seconds, it is very important to follow the best Machine Learning practices to get the best results.

# Skills Demonstrated
The skills I learned through this project include advanced knowledge of Python libraries used for Data Science, Machine Learning, Data Storage, and Databases. I also learned Amazon Web Services like s3, Sagemaker, EC2, and many more AWS services in order to train the model on large amounts of data. To create the F1 ML Web App, I had to learn HTML, CSS, Javascript, and Python backend programming using Flask. 

# Before vs. After
Keep in mind, I had no practical Machine Learning knowledge before this project. 

Through the struggles of this project I have become very comfortable with Machine Learning practices like data preprocessing, One-Hot-Encoding, Imputing Missing Values, Training and Testing splits, preventing Data Leakage, Machine Learning Algorithms, SMOTE, Hyperparameter Tuning, Class Imbalance, and scoring metrics to understand how well a machine learning model will perform. 

# How It Works
   +-------------------+
   |    Frontend       |
   | (HTML/CSS/JS)     |
   +-------------------+
          |

          
   +-------------------+
   | Flask Backend     |
   +-------------------+
          |


          
   +-------------------+
   |   MongoDB         |
   +-------------------
          
         AWS
          |
   +-------------------+
   |   AWS Machine     |
   |   Learning        |
   +-------------------+
          |
   +-------------------+
   |   MongoDB         |
   |   (Models)        |
   +-------------------+
          |
   +-------------------+
   |   DataHandler     |
   |    MongoDB        |
   +-------------------+
          |
   +-------------------+
   | Kaggle Dataset    |
   +-------------------+

# Website Preview
Website Link: Almost Done

Once you get on the website, navigate to the grand prix dropdown. Select a grand prix, then navigate to the driver dropdown and select a driver.
Once you have chosen both a grand prix and a driver, press the Pirelli tire button below to get the predicted outcome of the driver at that race. If you would like to do another prediction press the predict result button below. 

# Limitations
Right now, the model I have employed has an f1 score of about 0.75 and an accuracy of about 0.78. The general areas of improvement are edge cases. For example, from the confusion matrix, we can see it is sometimes difficult for the model to decide whether a case is actually just Points but it predicts Podium and also if a case is actually No Points but the model predicts Points. I will provide the visuals for this in the repo. Because this sport is very nuanced and there are many rule changes pertaining to the car each year, I think I have a data limitation problem from the dataset I am sourcing from. I think the model would have more context if it were given information like overtakes, car performance, and other more telling data.

# Future Improvements
I plan to come back to this project and try to improve the predictive power of the model. I will try to use deep learning and neural networks, currently, I have only experimented and tuned the best models provided by sklearn ensemble and imbalance learn's models. I will also see if there is a way to scrape data from other sources and map them correctly to the training data. 

# Getting Started
Since the project is cross-platform there is no easy way to get started. However, I can tell you where and how to start up the necessary project files. In any code editor, you can take the Folder F1 Place Predictor, which is made up of two Python files. DataHandler.py and main.py. You can adjust DataHandler to train from the years you specify in the constructor. Then you can run main.py to export the data to a Database. Make sure to install all the necessary imports in the code and to install Pymongo on your machine if you plan on using that as your database.

Then take the training data from the database and load it into any environment where you have enough computing power to perform machine learning tasks. I decided to use AWS for my machine learning training. This requires you to set up an AWS account and store the training data file in your Amazon S3 bucket. Then spin up a notebook instance in Amazon Sagemaker and use the Jupyter Notebook I provided to train the model and get the scoring metrics. Run this program and it should save a model to your S3 bucket.

Now transfer the model joblib files to the models folder in the ModelTransform Project File under the Data Handling folder in this repo. This will save your model in chunks to the MongoDB Database.

All the work under the hood is now done. 

I have the Frontend and the Backend Files in this repo where you can see how it works with the Web Application. Basically, the Backend framework receives and fulfills API requests made by the user in the front end. There is a Python script called app.py that handles these requests and uses the data and models from the MongoDB database to fulfill these requests. 

# Conclusion
Please reach out to me if you have any questions or confusion. This is my first big personal project so please let me know Github best practices and ways I can clarify my code and my deployment. I never thought the day would come when I would write my own README file, so I am very excited to share my project with you. 

