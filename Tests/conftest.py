from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
import pytest
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
@pytest.fixture(params=["chrome"],scope='class')
def setup(request):
    if request.param=="chrome":
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # if request.param=="firefox":
    #     driver=webdriver.firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver=driver
    driver.get("https://www.facebook.com/")

    yield
    time.sleep(5)
    driver.close()