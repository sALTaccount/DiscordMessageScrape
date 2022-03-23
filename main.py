import configparser as cg
import logging

import bot

if __name__ == '__main__':
    cfg = cg.ConfigParser()
    print('Reading config...')
    cfg.read('config.cfg')
    client = bot.DScrapeClient(cfg['DEFAULT']['Token'],
                               cfg['DEFAULT']['Channel_id'],
                               cfg['DEFAULT']['Limit'],
                               cfg['DEFAULT']['Save_format'],
                               cfg['DEFAULT']['Ignore_bots'],
                               cfg['DEFAULT']['Skip_no_text_context'],
                               cfg['DEFAULT']['Include_discriminator'])
