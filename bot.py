#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)


if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "AnyDLBot",
        bot_token=Config.TG_BOT_TOKEN,7082761448:AAEgOi8rUCWhlMscXoCJwMzE3SXugvUXIk4
        api_id=Config.APP_ID,20032302
        api_hash=Config.API_HASH,728e53578ce2536a4a39595652a27f4a
        plugins=plugins
    )
    Config.AUTH_USERS.add(683538773)
    app.run()
