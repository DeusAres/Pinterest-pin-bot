import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from random import uniform

# Your Pinterest account details
user_name = "yourEmail@gmail.com"
user_password = "yourPassword"


# driver = webdriver.Chrome('./chromedriver')
pinterest_home = "https://www.pinterest.com/"
pre_login_button = (
    '//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/button'
)
login_button = "//button[@type='submit']"
pin_builder = "https://www.pinterest.com/pin-builder/"
pin_name = "//*[starts-with(@id, 'pin-draft-title-')]"
pin_description = (
    "//*[starts-with(@id, 'pin-draft-description-')]/div/div/div/div/div/div/div"
)
image_input = "//*[starts-with(@id, 'media-upload-input-')]"
pin_link = "//*[starts-with(@id, 'pin-draft-link-')]"
drop_down_menu = "//button[@data-test-id='board-dropdown-select-button']"
publish_button = "//button[@data-test-id='board-dropdown-save-button']"
return_pin_builder = "//*[starts-with(@class, 'JJV MIw Rym QLY p6V ojN Cii kOw Smz')]"


# Definitions for Selenium, don't change them
def create():
    chrome_options = Options()
    chrome_options.add_argument(__file__ + "\\selenium")
    chrome_options.add_argument("--log-level=3")
    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=chrome_options
    )
    driver.get(pinterest_home)

    return driver


# Pinterest Log in
def login(driver):
    try:
        # Click log in link

        driver.find_element_by_xpath(pre_login_button).click()

        # Log in
        try:
            user = driver.find_element_by_name("id")
            user.send_keys(user_name)
            time.sleep(uniform(2, 6))
        except:
            pass
        pas = driver.find_element_by_name("password")
        pas.send_keys(user_password)
        time.sleep(uniform(2, 6))
        driver.find_element_by_xpath(login_button).click()
        time.sleep(uniform(2, 6))
    except:
        print("Already logged")
    # Go pin builder page
    driver.get(pin_builder)


def pin(image, board, title=None, description=None, link=None, driver=None):

    board = "//div[@data-test-id='board-row-" + board + "']"
    time.sleep(uniform(2, 6))

    # Click the upload button
    driver.find_element_by_xpath(image_input).send_keys(image)
    time.sleep(uniform(2, 6))

    # Enter pin name
    driver.find_element_by_xpath(pin_name).send_keys(title)
    time.sleep(uniform(2, 6))

    # Enter description
    driver.find_element_by_xpath(pin_description).send_keys(description)
    time.sleep(uniform(2, 6))

    # Enter link
    if link != None:
        driver.find_element_by_xpath(pin_link).send_keys(link)
        time.sleep(uniform(2, 6))

    # Open board drop-down menu
    driver.find_element_by_xpath(drop_down_menu).click()
    time.sleep(uniform(2, 6))

    # Select board
    driver.find_element_by_xpath(board).click()
    time.sleep(uniform(2, 6))

    """
    # Click publish button
    driver.find_element_by_xpath(publish_button).click()
    time.sleep(uniform(7, 15))
    """

    # Create new pin to publish
    driver.find_element_by_xpath(
        "//*[starts-with(@style, 'background-color: rgb(255, 255, 255); border: 0px; border-radius: 8px; box-sizing: border-box; cursor: pointer; height: 60px; outline: none; padding: 0px; width: 40px;')]"
    ).click()
