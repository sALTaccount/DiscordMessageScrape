
# DiscordMessageScrape

DiscordMessageScrape is a simple program to scrape discord messages from a channel

# WARNING!!!!!
This program implements [discord selfbots](https://medium.com/@scarlettokun/selfbots-explanation-and-perspectives-51d437ce0849) to scrape messages. This is against Discord TOS, and you run the risk of your account being banned by using this program. Use at your own discression!
# Features

- Variety of saving formats
- Option to ignore bot messages
- Option to include user discriminator
- Adjustable message download limits

# Table of Contents

1. [Installation](#Installation)
2. [Usage](#Usage)
3. [Wiki](#Wiki)

# Installation

DiscordMessageScrape is written in Python 3 and thus requires [Python3](https://www.python.org/downloads/)

First, clone the repository

``$ git clone https://github.com/sALTaccount/DiscordMessageScrape``

``$ cd DiscordMessageScrape``

Then, install the requirements

``$ pip install -r requirements.txt``

# Usage

Inside of config.cfg, there are a couple of settings you need to change before using DiscordMessageScrape

Firstly, put in the discord token of the account you want to use (Instructions for getting your token are in the wiki)
```Token = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX```

Next, input the channel ID of the channel you want to download the messages from (instructions also in the wiki)
```Channel_ID = 1234567890```

Finally, enter the limit to how many messages you want to download.
Set limit to the amount of messages you want to download
```Limit = 20000```
Or alternatively, set it to `none` to download the entire channel
```Limit = none```

Those are the only settings you need to change for the program to work, the rest are for customizing the output

# Wiki

## Token
Your discord token. Learn how to get it [here](https://discordhelp.net/discord-token)
## Channel_ID 
The ID of the channel you want to download messages from. You can get the ID by enabling [developer mode](https://www.howtogeek.com/714348/how-to-enable-or-disable-developer-mode-on-discord/). Right click on the channel and press "Copy ID"
## Limit 
The amount of messages you want to download
```Limit = 20000```
Set it to `none` to download the entire channel
```Limit = none```
## Save_format
There are currently 2 save formats: `json` and `conversation`
### JSON
The JSON is structured as a list of lists. Each list in the main list has two strings structured as follows:

`[author, message]`
### Conversation
Conversation format outputs as a txt in the following format:
```
user1: hello
user2: yo whats up
user1: I heard that somebody is downloading chat withe DiscordMessageScrape
user3: isn't that the program that salt wrote? he is so awesome!
```
## Ignore_bots
Ignore messages written by bots

## Skip_no_text_context
Skips any messages that do not contain any text

## Include_discriminator
Include the user's [discriminator](https://discord.fandom.com/wiki/Discriminator) in the author's name when saving
