# College-Chat-Bot
Combining LLMs with RAG systems to develop a chatbot that answers questions based on a college course.

Welcome to the repository for the Chatbot project. This project involves building a chatbot using Retrieval-Augmented Generation (RAG) with LangChain, Pinecone, a pre-trained Language Model (LLM), and Streamlit to assist with questions related to the Professional Seminar 2 subject in a college curriculum. This README provides a comprehensive overview of the project, including explanations of core concepts, implementation details, and usage instructions.


## Introduction

The Chatbot is designed to provide answers to queries related to the Professional Seminar 2 subject. Using advanced AI techniques, this chatbot combines the power of a pre-trained Language Model (LLM), Pinecone, LangChain, and Streamlit to deliver accurate and contextually relevant responses.

## Key Concepts

### Language Models (LLM)

Language Models (LLMs) are pre-trained models designed to understand and generate human language. They can perform tasks such as translation, summarization, and question answering without needing additional training. Popular examples include OpenAI's GPT-3 and Google's BERT.

### Pinecone

Pinecone is a vector database that allows for efficient and scalable similarity searches. It is used in this project to store embeddings of documents and retrieve relevant documents based on the user's query.

### LangChain

LangChain is a framework that facilitates the building of applications with language models. It provides tools for integrating different components required for language model applications, such as data retrieval, model inference, and response generation.

### Streamlit

Streamlit is an open-source app framework used to create and share custom web apps for machine learning and data science. It turns data scripts into interactive, shareable web apps in just a few minutes.

### Demostration

![Desktop 2024 08 13 - 21 17 26 03](https://github.com/user-attachments/assets/dac2b58f-2d1f-41a5-bbb0-4d69faff4fc4)



.....

## Implementation Details

### Data Preparation

Data preparation involves collecting documents and information related to Professional Seminar 2 and converting them into a format that can be used by the retrieval system.

1. **Collecting Data**: Gather all relevant documents, articles, and lecture notes.
2. **Cleaning Data**: Remove any irrelevant information and standardize the format.
3. **Embedding Data**: Use the pre-trained LLM to convert documents into embeddings and store them in Pinecone for efficient retrieval.

### Model Integration

The core of the chatbot involves integrating the pre-trained LLM, Pinecone, LangChain, and Streamlit.

1. **Setting up Pinecone**: Initialize Pinecone and upload the document embeddings.
2. **Using LangChain**: Utilize LangChain to handle the interaction between the user's query, document retrieval, and response generation.
4. **Implementing Streamlit**: Create an interactive web interface using Streamlit to allow users to interact with the chatbot.

### Chatbot Interface

The chatbot interface is the user-facing component that allows users to interact with the system.

1. **Web Interface**: Created a web-based interface using Streamlit where users can enter their queries and receive responses.
2. **Backend Integration**: Connected the web interface to the backend system that handles the query processing using LangChain and Pinecone.


### Conclusion

The Chatbot project showcases the integration of advanced AI technologies to create an intelligent academic assistant. By utilizing Retrieval-Augmented Generation (RAG), the chatbot provides accurate and contextually relevant responses. This project successfully combines the power of pre-trained Language Models (LLM), Pinecone for efficient document retrieval, LangChain for seamless interaction management, and Streamlit for an accessible user interface. The chatbot is specifically designed to assist with Professional Seminar 2, enhancing students' understanding of course material. Future improvements could include expanding the knowledge base, fine-tuning models, adding user feedback mechanisms, and integrating advanced features like multilingual support and voice interaction. This project demonstrates the practical application of AI in creating a reliable and efficient educational tool, highlighting the potential for further development and customization in various domains.
