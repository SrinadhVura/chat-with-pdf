# chat-with-pdf

## Repository Description:

Welcome to the repository for our cutting-edge project leveraging OpenAI's GPT-3.5 Turbo to develop an interactive AI chatbot capable of extracting valuable insights from PDF documents. Our objective is to revolutionize user interaction with digital content through advancements in artificial intelligence and natural language processing.

## Project Highlights:

- **GPT-3.5 Turbo Integration**: Discover the seamless integration of GPT-3.5 Turbo, a state-of-the-art language model, enabling human-like text generation and precise contextual understanding for an interactive user experience.

- **Web Application with Streamlit Cloud**: Dive into the development of a web application hosted on Streamlit Cloud, designed to provide efficient and intuitive responses to users' inquiries based on the content of uploaded PDF files.

- **Embedding Generation and Similarity Search**: Understand the methodologies and techniques employed to generate embeddings using GPT-3.5 Turbo and perform similarity searches, enhancing the responsiveness and relevance of the AI chatbot's responses.

- **FAISS Vector Database**: Explore the implementation of a robust vector database utilizing FAISS (Facebook AI Similarity Search), ensuring efficient storage, representation, and retrieval of embeddings for optimal performance.

- **Dynamic and Adaptive AI Bot**: Learn about the culmination of our components resulting in a dynamic, adaptive AI bot, custom-built in real-time to respond specifically to a user's query based on the content of the uploaded PDF.



Join us in exploring this repository to uncover the innovations, strategies, and technologies that drive our vision of enhancing information extraction from PDF documents using state-of-the-art AI capabilities and the powerful FAISS vector database by Meta.

---
# Running the App Locally:

To run the AI chatbot application locally, follow these steps:

1. **Download the Repository:**
   Visit the GitHub repository at [https://github.com/Digiotai2025/chat-with-pdf](https://github.com/Digiotai2025/chat-with-pdf) and download it as a zip file. Extract the contents of the zip file to a directory of your choice.

2. **Clone the Repository (Alternative):**
   Alternatively, you can use the GitHub CLI to clone the repository. Run the following command in your command line interface (CLI):
   ```sh
   gh repo clone Digiotai2025/chat-with-pdf
   ```

3. **Navigate to Repository Directory:**
   Navigate to the downloaded or cloned repository's directory using the CLI:
   ```sh
   cd chat-with-pdf
   ```

4. **Install Python Dependencies:**
   Run the following command to install the necessary Python dependencies from the `requirements.txt` file:
   ```sh
   python -m pip install -r requirements.txt
   ```

5. **Create `secrets.toml` File:**
   Create a file named `secrets.toml` in the `.streamlit` directory within the repository. The contents of the file should be similar to the required configuration.

6. **Run the App:**
   Run the following command to start the application:
   ```sh
   streamlit run chat-with-pdf.py
   ```

7. **Access the App:**
   The app will be up and running on port number 8501 at [https://localhost:8501/](https://localhost:8501/).

Enjoy interacting with the AI chatbot locally!
