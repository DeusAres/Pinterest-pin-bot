import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from random import uniform


# This should work until pinterest doesn't change his layout
# or html code. If any of find_element* methods doesn't work
# prepare for trouble and make it double 
# You'll need to change one of this strings
# or `board` inside pin method

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
new_pin = "//*[starts-with(@style, 'background-color: rgb(255, 255, 255); border: 0px; border-radius: 8px; box-sizing: border-box; cursor: pointer; height: 60px; outline: none; padding: 0px; width: 40px;')]"
return_pin_builder = "//*[starts-with(@class, 'JJV MIw Rym QLY p6V ojN Cii kOw Smz')]"

class bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.login()

    def login(self):
        chrome_options = Options()
        chrome_options.add_argument(__file__ + "\\selenium")
        chrome_options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options
        )
        self.driver.get(pinterest_home)

        # In case login is needed
        try:
            # Click log in link
            self.driver.find_element_by_xpath(pre_login_button).click()

            # Log in
            try:
                # In case username is logged without password
                user = self.driver.find_element_by_name("id")
                user.send_keys(self.username)
                time.sleep(uniform(2, 6))
            except:
                pass
            
            pas = self.driver.find_element_by_name("password")
            pas.send_keys(self.password)
            time.sleep(uniform(2, 6))
            self.driver.find_element_by_xpath(login_button).click()
            time.sleep(uniform(2, 6))

        except:
            print("Already logged")

        # Go pin builder page
        self.driver.get(pin_builder)

    def pin(self, image, board, 
            section=None,
            title=None,
            description=None,
            link=None, 
            publish=False):
        """
        image: str, path to image
        board: str, case sensitive
        section: str (None if doesn't apply), case sensitive
        title: str
        description: str
        link: str
        publish: bool, if True pin will be published
            the reason for this is that you can create
            multiple pins in one pin builder page and
            publish them later on
               
        """

        time.sleep(uniform(2, 6))

        # Upload image
        self.driver.find_element_by_xpath(image_input).send_keys(image)
        time.sleep(uniform(2, 6))

        # Enter pin name
        if title:
            self.driver.find_element_by_xpath(pin_name).send_keys(title)
            time.sleep(uniform(2, 6))

        # Enter description
        if description:
            self.driver.find_element_by_xpath(pin_description).send_keys(description)
            time.sleep(uniform(2, 6))

        # Enter link
        if link:
            self.driver.find_element_by_xpath(pin_link).send_keys(link)
            time.sleep(uniform(2, 6))

        # Open board drop-down menu
        self.driver.find_element_by_xpath(drop_down_menu).click()
        time.sleep(uniform(2, 6))

        # Select board
        board = "//div[@data-test-id='board-row-" + board + "']"
        self.driver.find_element_by_xpath(board).click()
        time.sleep(uniform(2, 6))

        if section:
            section = "//div[@data-test-id='section-row-" + section + "']"
            self.driver.find_element_by_xpath(board).click()
            time.sleep(uniform(2, 6))

        if publish:
            # Click publish button
            self.driver.find_element_by_xpath(publish_button).click()
            time.sleep(uniform(7, 15))
            # Go pin builder page
            self.driver.get(pin_builder)
                    
        else:
            # Create new pin to publish
            self.driver.find_element_by_xpath(new_pin).click()

