# RAG Chatbot Integration for Blogs or Websites

This repository contains reference code for integrating a Retrieval-Augmented Generation (RAG) chatbot feature into any website. 
The provided scripts and resources demonstrate how to set up and run the chatbot, allowing you to add sophisticated conversational 
capabilities to your web application.

NOTE: This involves scraping text data for the given website so make sure you have the required permissions to do this

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Retrieval-Augmented Generation (RAG) based chatbot
- Easy integration with any website
- Comprehensive example scripts
- Detailed instructions and requirements provided

## Requirements
The required packages and dependencies are listed in the `requirements.txt` file. Ensure you have Python installed on your 
system before proceeding with the installation.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/rag-chatbot.git
    cd rag-chatbot
    ```

2. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
## OPENAI API KEY
You need to create your own OPENAI_API_KEY in a .env file wihtin the same repo to access the OPENAI LLMs and Embedding models. 
Note that you can you use other services like Google cloud platform key or AWS as well with minimal chnages

## Customization
In the given script I use this for on my ![blog](https://mlrad.io/) but the code is written in such a way as to make it easy to try it for your won websites/blogs and with different scrapers, llms, DBs etc!

## Usage
To run the chatbot script as provided, execute the following command:
```bash
python main.py
```
This will start the chatbot, and you can interact with it as per the instructions or integration details provided in the script.
## Sample Output
![Example Output](https://github.com/SaiGullapally/GPTify_your_blog_or_website/blob/main/sample_output/example_output.png)
## Contributing
Contributions are welcome! If you have suggestions for improvements or find any issues, please open an issue or submit a pull request. 
For major changes, please discuss them in an issue first to ensure alignment with the project's goals.

