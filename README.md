# Pinterest-pin-bot
Create and fill multiple pins has never been easier

# Requirements
Python 3+, pip

# Installation

```pip install selenium```

```pip install webdriver-manager```

# Settings

This is a module to support your main script.

In order to use you need to fill `user_name` and `user_password` with your datas

![image](https://user-images.githubusercontent.com/60852205/151545604-f613a8e1-610c-49a2-b382-f81cda74254c.png)

Now, here's the decisional part

You can use `# Click publish button` or `# Create new pin to publish` part

![image](https://user-images.githubusercontent.com/60852205/151545996-9e36d928-81b7-4f3e-bb5a-e637915b4caf.png)

Personally, I prefer to let the bot create more pins and later on manually publish. The reason to this preference is how easy pinterest detects bot and spams and deactivates accounts (don't worry tho, you will get an email and if you click the button/link they send you they will unban you for sure)

Just to be sure you can increase `time.sleep(uniform())` between each action

# Usage

This module is based on creating and instance of driver and passing it to the functions (and in the next version I'm gonna change that into an object with methods, seems more reasonable)

``` EXAMPLE
import toPinterest as tP

# Create a new driver instance
driver = tP.create()
# A selenium instance will be spawned

# Login into your pinterest account
tP.login(driver)

# Now you can pass 
tP.pin(image, board, title, description, link, driver)




