# Spam-Email-Classifier
description :
The Spam Message Classifier is a machine learning-based web application designed to classify text messages as either spam or not spam (ham). Built using Python, this project leverages Natural Language Processing (NLP) and a Logistic Regression model to analyze message content and make accurate predictions. A simple and clean interface is provided using Streamlit, making it easy for users to interact with the model directly in their web browser.

The primary goal of this project is to demonstrate how spam detection can be achieved using a small, real-world dataset and basic machine learning tools. This project is beginner-friendly and serves as a great introduction to NLP, machine learning pipelines, text classification, and deploying models as interactive web applications.

The model has been trained on the well-known SMS Spam Collection Dataset, which contains over 5,000 SMS messages labeled as either "spam" or "ham" (not spam). The dataset is publicly available and widely used in academic and learning contexts. Before training, messages are cleaned and transformed using the TF-IDF (Term Frequency–Inverse Document Frequency) technique to convert raw text into numerical feature vectors. These vectors are then used to train a Logistic Regression classifier, which was found to perform exceptionally well on the dataset, achieving over 99% accuracy on the test data.

The project is divided into two main components: the machine learning model and the Streamlit application. The ML part involves reading the dataset, preprocessing the text, vectorizing it, splitting the data into training and testing sets, and finally training the model. The trained model and vectorizer are saved using Python’s pickle module so they can be reused without retraining.

The second part is the Streamlit web application (app.py), which loads the trained model and vectorizer, then takes user input through a text box. When a message is entered, the app predicts whether it is spam or not and displays the result on the screen. The interface is clean, responsive, and provides immediate feedback, making it easy to test various kinds of messages.

This project is not only practical but also very easy to run locally. With a few simple steps like installing required packages, training the model once, and launching the Streamlit app, any user can get the application running on their own machine in minutes. It is an excellent project for students, beginners in AI/ML, or even developers looking to create their first data science web app.

The application can be enhanced further by adding features such as visual analytics of spam keywords, custom dataset uploading, support for multiple languages, and deploying it online using Streamlit Cloud, Heroku, or Render. These improvements would make the tool more robust and useful in real-world scenarios.

In summary, the Spam Message Classifier Streamlit App is a great learning project that combines machine learning, NLP, and web development using Python. It offers hands-on experience with real data, teaches you how to build a machine learning pipeline, and introduces you to deploying interactive ML applications in a user-friendly manner. Whether you're just starting your ML journey or want to explore how data science meets web apps, this project is a perfect fit.

output :
