import json

import discord


class DScrapeClient(discord.Client):
    def __init__(self, token, channel_id, limit, save_format, ignore_bots, skip_no_text_context, include_discriminator,
                 **options):
        super().__init__(**options)
        self.channel_id = channel_id
        if limit == 'none':
            self.limit = None
        else:
            self.limit = int(limit)
        self.save_format = save_format
        self.ignore_bots = ignore_bots
        self.skip_no_text_context = skip_no_text_context
        self.include_discriminator = include_discriminator
        print("Initializing bot")
        self.run(token)

    async def on_ready(self):
        print('Logged in as {0}'.format(self.user))
        print('Attempting to access channel {0}'.format(self.channel_id))
        channel = self.get_channel(int(self.channel_id))
        if channel is None:
            raise ChannelNotFoundException()
        print('Reading messages (this could take a while)')
        messages = await channel.history(limit=self.limit).flatten()

        print('Read messages! logging out...')
        await DScrapeClient.close(self)

        filtered = self.message_filter(messages)
        self.save_messages(filtered)

    def message_filter(self, messages):
        filtered = []
        for message in messages:
            if self.ignore_bots == 'yes' and message.author.bot is True:
                continue
            if self.skip_no_text_context == 'yes' and message.content == '':
                continue
            filtered.append(message)
        return filtered

    def save_messages(self, messages):
        # convert message objects to something we can write to a json file
        converted = []
        for message in messages:
            converted.append([self.get_author_name(message), message.content])

        if self.save_format == 'json':
            with open('{0}-{1}_messages.json'.format(self.channel_id, len(converted)), 'w', encoding='utf-8') as f:
                json.dump(converted, f, ensure_ascii=False, indent=4)
        elif self.save_format == 'conversation':
            with open('{0}-{1}_messages.txt'.format(self.channel_id, len(converted)), 'w', encoding='utf-8') as f:
                for message in converted:
                    f.write('{0}: {1}\n'.format(message[0], message[1]))
        else:
            raise InvalidSaveTypeException()

    def get_author_name(self, message):
        if self.include_discriminator == 'no':
            return message.author.name
        return message.author.name + '#' + message.author.discriminator


class ChannelNotFoundException(Exception):
    def __init__(self, message='Channel not found, make sure the ID is correct and you have access'):
        super().__init__(message)


class InvalidSaveTypeException(Exception):
    def __init__(self, message='Invalid save format. Check README.md for more info'):
        super().__init__(message)
