# F1 Racing Machine Learning Place Predictor

 An End-to-End Machine Learning Project Formula 1 Racing

# Overview
- This project is an end-to-end machine learning web application that predicts the final places of drivers at future races based on historical racing and telemetry data.
- This project adds value to the field of Formula 1 data science by showing the metrics that best predict good outcomes for drivers and constructors.
- This project aims to predict the finish domains of the drivers based on race data. It will predict either Podium (1st -3rd), Points (4th - 10th), or No Points (11th - 20th). 
- Since Formula 1 Racing is a sport decided in mere seconds, it is very important to follow the best Machine Learning practices to get the best results.

# Resources 
Kaggle Dataset: https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020

# Skills Demonstrated
- Advanced knowledge of Python libraries used for Data Science, Machine Learning, Data Storage, and Databases.
- Proficiency in Amazon Web Services (AWS) tools like s3, Sagemaker, EC2, and various other AWS services for efficient large-scale model training.
- Mastery of HTML, CSS, JavaScript, and Python backend programming with Flask to create the F1 ML Web App.

# Before vs. After
- Keep in mind, I had no practical Machine Learning knowledge before this project.

- Through the struggles of this project, I have gained proficiency in various Machine Learning practices including:

   - Data preprocessing techniques
   - One-Hot-Encoding for categorical data
   - Imputing missing values in datasets
   - Conducting Training and Testing splits for model evaluation
   - Creating Machine Learning Pipelines using Scaling and Estimators
   - Preventing Data Leakage in machine learning pipelines
   - Familiarity with a variety of Machine Learning Algorithms
   - Application of SMOTE (Synthetic Minority Over-sampling Technique)
   - Hyperparameter Tuning for optimizing model performance
   - Managing Class Imbalance in classification tasks
   - Understanding and utilizing scoring metrics to assess machine learning model performance

# How It Works
- Please view the video demonstration that shows how the app works. I am currently still deploying the web application online. 

# Website Preview
Website Link: Almost Done

- Once on the website, follow these steps:

   1. Navigate to the grand prix dropdown.
   2. Select a grand prix from the options available.
   3. Next, navigate to the driver dropdown.
   4. Select a driver from the list provided.
   5. After choosing both a grand prix and a driver, proceed with the following steps:

- Locate and press the Pirelli tire button located below.
   - By doing so, you'll receive the predicted outcome of the selected driver for that particular race.
- If you wish to make another prediction, simply follow these steps:

1. Press the predict result button situated below.

# Limitations
- The current model I've implemented demonstrates an f1 score of approximately 0.75 and an accuracy of around 0.78.
- The key areas for enhancement mainly involve addressing edge cases.
- For instance, the confusion matrix analysis reveals situations where the model struggles to distinguish between certain scenarios:
- It occasionally faces challenges in distinguishing between cases that could be accurately categorized as Points, but the model predicts them as Podium.
- Additionally, it sometimes encounters difficulty in discerning No Points scenarios, leading to Points predictions.
- Visual representations illustrating these instances will be provided within the repository.
- Given the intricate nature of Formula 1, characterized by nuanced rules and annual car performance modifications, it's apparent that there's a data limitation inherent to the dataset I'm utilizing.
- Addressing this limitation, the model could potentially benefit from incorporating more comprehensive information such as:
1. Overtaking data
2. Car performance metrics
3. Other pertinent factors that offer deeper insights.

By integrating these additional facets, the model could gain a broader context, potentially leading to improved predictions and a more accurate representation of the intricate dynamics of Formula 1 racing.

# Future Improvements
- In the future, I have plans to revisit this project with the goal of enhancing the model's predictive capabilities.
- To achieve this, I intend to explore the implementation of deep learning techniques and neural networks.
- It's important to note that, up to this point, I've primarily focused on experimenting with and fine-tuning the best models offered by sklearn's ensemble and imbalance learn's models.
- As part of the improvement process, I'll investigate the possibility of sourcing data from alternative and diverse sources.
- A key objective will be to appropriately integrate this new data into the existing training dataset.
- Furthermore, I'll keep a close eye on updates from the dataset's creator, particularly any updates related to the 2023 data.
- Upon the release of the 2023 data, my plan is to undertake the following steps:
- Retrain the model using data up to 2022.
- Utilize the newly available 2023 data to enhance the predictive accuracy of the model.

Ultimately, these efforts are aimed at refining the model's performance and ensuring its alignment with the most up-to-date information, thus contributing to the accuracy and relevance of the predictions provided on the website.

# Getting Started
- As this project spans multiple platforms, the initial setup process may seem complex. However, I'm here to guide you through the steps needed to kick-start the project files.

- Begin by using any code editor to work with the "F1 Place Predictor" folder, which consists of two Python files: "DataHandler.py" and "main.py".

- In the "DataHandler.py" file, you have the flexibility to customize data training based on the years you specify in the constructor.

- Running the "main.py" file will enable data export to a database. Ensure that you've installed all the required dependencies and libraries in your code, including "Pymongo" if you intend to use it as your database solution.

- With the training data now available in the database, proceed to load it into an environment with sufficient computational capacity to handle machine learning tasks.

- For my machine learning training, I opted for AWS, which entails setting up an AWS account and storing the training data file within your Amazon S3 bucket.

- Utilize Amazon Sagemaker to launch a notebook instance, where you can employ the provided Jupyter Notebook for model training and obtaining scoring metrics.

- Running this notebook will save a trained model to your designated S3 bucket.

- The next step involves transferring the generated "joblib" model files to the "models" folder within the "ModelTransform Project File" found under the "Data Handling" section of this repository.

- By completing this step, your model will be systematically stored in sections within the MongoDB Database.

- With the groundwork laid, the intricate backend processing is now complete.

- Within this repository, you'll find both frontend and backend files that illuminate how the Web Application operates.

- The backend framework is responsible for processing API requests generated by users within the frontend interface.

- The "app.py" Python script is pivotal in managing these requests, tapping into the data and models housed in the MongoDB database to seamlessly fulfill user queries.

- By following these steps, you'll be well on your way to understanding and implementing the end-to-end functionality of the F1 Place Predictor web application.

# Conclusion
Please reach out to me if you have any questions or confusion. This is my first big personal project so please let me know Github best practices and ways I can clarify my code and my deployment. I never thought the day would come when I would write my own README file, so I am very excited to share my project with you. 

