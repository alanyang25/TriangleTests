import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="class")
def chrome_driver_init(request):
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=900,600")
    options.add_argument("--headless")
    web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()

# @pytest.fixture(scope="class")
# def firefox_driver_init(request):
#     options = webdriver.FirefoxOptions()
#     options.add_argument("--headless")
#     web_driver = webdriver.Firefox(executable_path=r'C:\webdrivers\geckodriver.exe', options=options)
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()
