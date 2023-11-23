# News Classification System

Live demo : https://newscategoricalclassifier.streamlit.app/

This repository comprises a comprehensive solution for scraping news articles from the Indian Express webpage, categorizing them into distinct topics, and deploying a highly accurate model for real-time article classification. The system utilizes web scraping techniques, advanced classification algorithms, and a user-friendly deployment interface.

## 1. Web Scraping:

In the initial phase, news articles are extracted from the Indian Express website. The web scraping code, implemented using Beautiful Soup, can be found in the notebook `news_webscraping_NonStopIO.ipynb`. This code navigates the webpage, extracts relevant information, and prepares the data for subsequent processing.

## 2. Classification:

Articles are intelligently categorized into six distinct classes: 'business,' 'sports,' 'political-pulse,' 'entertainment,' 'lifestyle,' and 'education.' The classification algorithm is implemented in the notebook `news_classification_NonStopIO.ipynb`. Leveraging TF-IDF vectorization, the model achieves an impressive accuracy rate of approximately 98.44%. This high accuracy ensures reliable and precise categorization of news articles.

## 3. Deployment:

The deployment phase involves making the model accessible in a user-friendly manner. The deployment code is available in the notebook `news_deployment_NonStopIO.ipynb`. Streamlit, a powerful Python library for creating web applications, is employed to develop an interactive web interface. Users can easily interact with the system and receive real-time classifications for news articles.

## How to Use:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/news-categorization.git
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Code:**
   Execute the web scraping, classification, or deployment code as needed, following the instructions provided in each notebook.

4. **Explore the Deployed Model:**
   Access the deployed model through the following link: [News Categorical Classifier](https://newscategoricalclassifier.streamlit.app/). Experience real-time news article categorization through an intuitive and user-friendly interface.

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
