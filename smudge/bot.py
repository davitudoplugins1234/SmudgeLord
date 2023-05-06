# SPDX-License-Identifier: GPL-3.0
# Copyright (c) 2023 Luiz Renato (ruizlenato@proton.me)
import os
import shutil
import sys

from pyrogram import Client
from pyrogram.enums import ParseMode

from config import API_HASH, API_ID, BOT_TOKEN, WORKERS

from .database import database


class Smudge(Client):
    def __init__(self):
        name = self.__class__.__name__.lower()

        super().__init__(
            name,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=WORKERS,
            parse_mode=ParseMode.HTML,
            plugins={"root": "smudge.plugins"},
            sleep_threshold=180,
        )

    async def start(self):
        await database.connect()
        await super().start()

    async def stop(self) -> None:
        if database.is_connected:
            await database.close()
        await super().stop()
