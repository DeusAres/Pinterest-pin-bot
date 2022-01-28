# Pinterest-pin-bot
Automate boring pin building on pinterest through this python bot!

## Installation

```pip install selenium```

```pip install webdriver-manager```

## Usage

It's very basic to use

```
>>> import pinBot
>>> funnyBot = pinBot.bot("myEmail@no.com", "myPassword")
>>> # An instance of chromium driven by selenium will be spawned
>>> # The code will attemp login
>>> funnyBot.pin(
        image="E:\\funnyImage.jpg", 
        board="Funny", 
        section="Less funny images",
        title="Funny enough",
        description="The funniest example ever",
        link="https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_"?
        publish=False
>>> # Between every action there is a pause with time.sleep(uniform())
>>> # Increase it if you need
```

### Why publish option

Personally, I prefer to let the bot create more pins and later on manually publish them. The reason to this preference is how easy pinterest detects bot and spam and deactivates accounts (don't worry tho, you will get an email and if you click the button/link they send you they will unban you for sure)

Just to be sure you can increase `time.sleep(uniform())` between each action

Also I save data, loading times, and resources because after every uploading I didn't find a way to exit the ""Uploaded"" screen without reloading entirely the pin builder page

It might be possible to implement a publish method after an amount of time, a set of action, or called by the user in case you prefer to use ```.pin()``` method like me but I think I will do it only if someone really wishes for it

# Note

This was just a fun project and challenge, but don't get me wrong. I don't know how legal it is to use an automated software to fill up text boxes and uploading images, for your own sake and mine, you are responsible for yourself in the moment you use this code. I'm not saying pinterest police will get all your pins down and send you to pin jail but, you know, better be safe than sorry








