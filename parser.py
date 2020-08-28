from bs4 import BeautifulSoup
import json
from utils import Tags, SupportedPages
from selenium_bot import BotParser

class HtmlParser:

    def __init__(self, response, page_number=1, section='Data Science'):
        """
        Instantiates the class by creating a `bs4.soup` object

        Parameters
        ------------
        response : str
            string containing the response from the URL
        page_number: int
            Page Number of the result
        section : str
            Section to apply the parsing to
        """
        self.soup = BeautifulSoup(response, 'html.parser')
        self.page_number = page_number
        if section not in SupportedPages:
            raise NotImplementedError(f"The section {section} is not supported")

    def _get_body(self):
        self.soup = self.soup.body

    def _fetch_tag_and_id(self, tag, _id=None, _class=None):
        if _id is not None and _class is not None:
            raise NotImplementedError("The functionality has not been implemented yet")

        if _class is not None:
            _class = [_class] if isinstance(_class, str) else _class
            self.soup = [value for value in self.soup.children if value.name == tag and value['class'] == _class]
        elif _id is not None:
            self.soup = [value for value in self.soup.children if value.name == tag and value['id'] == _id]
        else:
            self.soup = [value for value in self.soup.children if value.name == tag]

        assert len(self.soup) == 1
        self.soup = self.soup[0]

    def get_total_pages(self):
        if self.page_number != 1:
            raise ValueError("Total Pages can be retrieved while in page number 1 only")
        raise NotImplementedError("The functionality has not been implemented")

    def crawl_page(self):
        # TODO - The result is not exactly same as what I expected. Check
        if self.page_number == 1:
            raise NotImplementedError("WHAT THE FUNCK")
        self._get_body()
        self._fetch_tag_and_id(tag=Tags.div, _id='rendered-content')
        self._fetch_tag_and_id(tag=Tags.div, _class='rc-MetatagsWrapper')
        self._fetch_tag_and_id(tag=Tags.div, _class='rc-BrowseApp')
        self._fetch_tag_and_id(tag=Tags.div, _class='browse-children-wrapper')
        self._fetch_tag_and_id(tag=Tags.section, _class='rc-DomainPage')
        self._fetch_tag_and_id(tag=Tags.div, _class='product-offerings-wrapper')
        self._fetch_tag_and_id(tag=Tags.section, _class='rc-ProductOfferings')
#        self._fetch_tag_and_id(tag=Tags.div, _class=['offerings-wrapper', 'bt3-container', 'body-container'])
#        self._fetch_tag_and_id(tag=Tags.div, _class='rc-ListGoogleSchemaMarkup')
#        self.soup = self.soup.script.contents[0].split('\n')[1].strip()
#        return json.loads(self.soup)


# if __name__ == "__main__":
#     from urllib.request import urlopen
#     web_url = urlopen('https://www.coursera.org/browse/data-science?page=2')
#     read = web_url.read()
