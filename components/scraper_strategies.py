from abc import ABC, abstractmethod
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import os

class AbstractWebsiteTextScraper(ABC):
    """Abstract strategy Base Class to define the signatures/contracts of the critical methods
    for the concrete strategy implementations
    """
    def __init__(self, output_store_dir: str, root_domain: str) -> None:
        """initializes the parameters of the scraper
        Args:
            output_store_dir (str): the local dir to store the scraped text documents at
        """
        self.output_store_dir =  output_store_dir
        self.root_domain = root_domain
        if not os.path.exists(self.output_store_dir):
            os.makedirs(self.output_store_dir)
    

    @abstractmethod
    def start_scraping(self) -> int:
        """Starts scraping the root domain and its subpages

        Returns:
            int: 0 or 1 depending on whether the sraping was successful or ran into error
        """
        pass


class SimpleWebsiteTextScraper(AbstractWebsiteTextScraper):
    """scrapes the website and all the subpages of the website using
    requests and beautiful soup packages
    """
    def __init__(self, output_store_dir: str, root_domain: str):
        """nitializes the parameters of the scraper

        Args:
            output_store_dir (str): output directory to store the scrpaed data
            root_domain (str): the root domain for scraping, only links beginnign 
            with the root domain will be scraped
        """
        super().__init__(output_store_dir, root_domain)
        # keep track of pages that have been parsed
        self.parsed_pages = []
        # keep track of when a page was scraped
        self.date_time = None

    def post_process_page_text(self, website_domain: str, page_text: str) -> str:
        """Post processing the page text by adding the website domain andother info within the text

        Args:
            website_domain (str): the url of the website whose page text is being post processed
            page_text (str): the page text to be post processed

        Returns:
            str: page text after post processing
        """
        
        text_to_be_added = f"\
            Website URL: {website_domain} \n\n \
            Date on which the data was downloaded from the website: {datetime.now().date()} \n\n \
            Time at which the data was downloaded from the website: {datetime.now().time()} \n\n \
            ----------------------------Document Text Begins:---------------------------- \n\n"

        return text_to_be_added + page_text

    def save_page_text(self, website_domain: str, page_text: str):
        """saves the page text locally as a txt document

        Args:
            website_domain (str): url of the website page from which the page text was scraped
            page_text (str): page text to be saved
        """
        document_name = re.sub('[/,:,.]', '__', website_domain)+'.txt'
        file_path = os.path.join(self.output_store_dir, document_name)
        with open(file_path, "w") as f:
            f.write(page_text)
        

    def scrape(self, website_domain:str) -> None:
        """scrapes the given website and all the subpages

        Args:
            website_domain (str): the url of the website whose pages we need to scrape the text from
        """
        # check to ensure we do not have infinite loop when there are circular links
        if website_domain not in self.parsed_pages:
            print(f"beginning scraping web page: {website_domain}")
            self.parsed_pages.append(website_domain)
            self.date_time = datetime.now()
            response = requests.get(website_domain)
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")
            page_text = soup.get_text()
            page_text = self.post_process_page_text(website_domain, page_text)
            self.save_page_text(website_domain, page_text)
            print(f"completed scraping web page: {website_domain}")
            # Extract sub pages

            sub_pages=[i.attrs['href'] for i in soup.find_all('a') if i.attrs['href'].startswith(self.root_domain)]
            for sub_page in sub_pages:
                # filter out already parsed
                if sub_page not in self.parsed_pages:
                    self.scrape(sub_page)

    def start_scraping(self) -> int:
        """scrapes the root domain and subpages

        Returns:
            int: error status 0 if successful else 1
        """
        try:
            self.scrape(website_domain=self.root_domain)
            print(f"Completed scraping:{self.root_domain}. The saved text documents can be found at:{self.output_store_dir}")
            return 0
        except Exception as e:
            print('An exception occurred: {}'.format(e))
            return 1


