from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from utils import Supported_Platforms_and_Pages

import logging

_logger = logging.getLogger(__name__)

class BotParser:

    def __init__(self, url, page_number=1, platform="Coursera", topic="DataScience"):
        if page_number == 1:
            raise NotImplementedError("Page Number of 1 is not supported")
        if platform not in Supported_Platforms_and_Pages:
            raise NotImplementedError(f"The platform {platform} is not supported")
        if topic not in Supported_Platforms_and_Pages[platform]:
            raise NotImplementedError(f"The topic {topic} is not supported")
        self.url = url
        self.page_number = page_number
        self.platform = platform
        self.topic = topic

        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def get_url(self):
        return self.url

    def get_response(self):
        self.driver.get(self.url)
        response = self.driver.page_source
        time.sleep(2) # TODO - Figure out appropriate value
        return response

    def shut_down(self):
        from selenium.webdriver.chrome.webdriver import WebDriver
        WebDriver().implicitly_wait()
        from selenium.webdriver.remote.webelement import WebElement
        self.driver.close()
        del self.driver
