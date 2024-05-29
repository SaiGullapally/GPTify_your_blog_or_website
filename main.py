from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain_text_splitters import RecursiveCharacterTextSplitter

from components import (
    OpenAIEmbeddingsFactory,
    OpenAIGPT3p5Factory,
    SimpleWebsiteTextScraper,
    WrappedChromaVectorDB,
)
from components.data_loaders import TxtDataLoader

load_dotenv()

import os

# USER CONFIGS
API_KEY = os.getenv("OPENAI_API_KEY")
BLOG = "https://mlrad.io"
SCRAPING_OUTPUT_DIR = "/Users/sai/Desktop/ML/GPTify_your_blog_or_website/output"
TEMPERATURE = 0.1
QUESTION = "What is the difference between convolution and attention?"
SCRAPER_CLASS = SimpleWebsiteTextScraper
DATA_LOADER_CLASS = TxtDataLoader
LLM_FACTORY_CLASS = OpenAIGPT3p5Factory
EMBEDDINGS_FACTORY_CLASS = OpenAIEmbeddingsFactory
VECTOR_DB_CLASS = WrappedChromaVectorDB


def instantiate_and_run_qa_chain() -> None:
    # instantiate components
    scraper = SCRAPER_CLASS(output_store_dir=SCRAPING_OUTPUT_DIR, root_domain=BLOG)
    data_loader = DATA_LOADER_CLASS()
    embeddings_factory = EMBEDDINGS_FACTORY_CLASS(api_key=API_KEY)
    embeddings_model = embeddings_factory.get_embeddings_model()
    llm_factory = LLM_FACTORY_CLASS(api_key=API_KEY)
    llm = llm_factory.get_llm()
    vector_db_wrapper = VECTOR_DB_CLASS(k=5)
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=10000,
        chunk_overlap=4000,
        length_function=len,
        is_separator_regex=False,
    )

    # run the system
    scraper.scrape_root_domain()
    text_data = data_loader.load_data(data_dir=scraper.output_store_dir)
    print("splitting text into chunks")
    text_chunks = text_splitter.split_text(text_data)
    vector_db = vector_db_wrapper.create_vector_db_from_texts(
        texts=text_chunks, embeddings_model=embeddings_model
    )
    print("setting up QA chain")
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vector_db.as_retriever(search_kwargs={"k": vector_db_wrapper.k}),
        chain_type="stuff",
        return_source_documents=True,
    )
    print("calling QA chain")

    response = qa_chain(QUESTION)

    print(f"\n\nQUESTION\n{QUESTION}")
    print(f"RESPONSE \n", response["result"])
    return


if __name__ == "__main__":
    instantiate_and_run_qa_chain()
