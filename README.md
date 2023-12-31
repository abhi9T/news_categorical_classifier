# News Classification System

Live demo : https://newscategoricalclassifier.streamlit.app/

This repository comprises a comprehensive solution for scraping news articles from the Indian Express webpage, categorizing them into distinct topics, and deploying a highly accurate model for real-time article classification. The system utilizes web scraping techniques, advanced classification algorithms, and a user-friendly deployment interface.

## 1. Web Scraping:

In the initial phase, news articles are extracted from the Indian Express website. The web scraping code, implemented using Beautiful Soup, can be found in the notebook `news_webscraping_NonStopIO.ipynb`. This code navigates the webpage, extracts relevant information, and prepares the data for subsequent processing.

## 2. Classification:

Articles are intelligently categorized into six distinct classes: 'business,' 'sports,' 'political-pulse,' 'entertainment,' 'lifestyle,' and 'education.' The classification algorithm is implemented in the notebook `news_classification_NonStopIO.ipynb`. Leveraging TF-IDF vectorization for building vectorical data from textual data and implementing Support Vector Classifier for classification, the model achieves an impressive accuracy rate of approximately 98.44%. This high accuracy ensures reliable and precise categorization of news articles.

## 3. Deployment:

The deployment phase involves making the model accessible in a user-friendly manner. The deployment code is available in the notebook `news_deployment_NonStopIO.ipynb`. Streamlit, a powerful Python library for creating web applications, is employed to develop an interactive web interface. Users can easily interact with the system and receive real-time classifications for news articles.

# How to Use:

Follow these steps to utilize the News Classification System:

1. **Web Scraping:**
   - Open the `news_webscraping_NonStopIO.ipynb` notebook in Google Colab.
   - Run the web scraping code to generate a CSV file for classification.

   **Note: If you encounter any errors during execution, try running the code again, as real-time updates on the news website may cause intermittent issues.**

2. **Classification:**
   - Download the CSV file generated from the web scraping notebook.
   - Open the `news_classification_NonStopIO.ipynb` notebook in Google Colab.
   - Upload the CSV file and run the code to generate the classification model.

3. **Deployment:**
   - Download the classification model.
   - Open the `news_deployment_NonStopIO.ipynb` notebook in Google Colab.
   - Upload the model and run the code to generate the `app.py` file.

4. **GitHub Repository Setup:**
   - Create a GitHub repository and upload all the generated files, including the notebooks, CSV file, model file, and `app.py`.
   - Include a `requirements.txt` file specifying the necessary dependencies.

5. **Streamlit App Deployment:**
   - Visit Streamlit and create a new app deployment.
   - Connect the app to the GitHub repository containing all the files.
   - Deploy the app on the Streamlit cloud.
   - After deployment, you'll receive a permanent URL for the running application.

By following these steps, you'll have the News Classification System deployed on the Streamlit cloud, providing a user-friendly interface for real-time news article categorization. Users can access the application through the provided URL.

## Notebooks:

- **news_webscraping_NonStopIO.ipynb:**
  Web scraping code for extracting news articles from the Indian Express webpage.

- **news_classification_NonStopIO.ipynb:**
  Classification code for categorizing news articles into predefined categories using TF-IDF vectorization.

- **news_deployment_NonStopIO.ipynb:**
  Deployment code using Streamlit to create an interactive web application for real-time news classification.

## Deployment Link:

Explore the deployed model [here](https://newscategoricalclassifier.streamlit.app/). Interact with the system, input news articles, and witness accurate categorization results.

Feel free to delve into the code, customize it for your needs, and contribute to the enhancement of this news categorization system. If you encounter any issues or have suggestions, please create an issue in the repository.

![Screenshot 2023-11-23 044717](https://github.com/abhi9T/news_categorical_classifier/assets/122251068/b278bfa4-45f8-4f8a-9c72-2b8a7e1ee2d7)

![Screenshot 2023-11-23 044644](https://github.com/abhi9T/news_categorical_classifier/assets/122251068/6034addc-0ae2-44a5-935f-d3351496cf39)

![Screenshot 2023-11-23 044508](https://github.com/abhi9T/news_categorical_classifier/assets/122251068/ccb20290-a776-4e37-aa64-f43948b1e600)
