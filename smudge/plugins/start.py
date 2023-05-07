# SPDX-License-Identifier: GPL-3.0
# Copyright (c) 2023 Luiz Renato (ruizlenato@proton.me)
from typing import Union

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.helpers import ikb
from pyrogram.types import CallbackQuery, Message

from ..bot import Smudge
from ..utils.locale import locale


@Smudge.on_message(filters.command("start"))
@locale()
async def start_command(c: Smudge, m: Union[Message, CallbackQuery]):
    if isinstance(m, CallbackQuery):
        chat_type = m.message.chat.type
        reply_text = m.edit_message_text
    else:
        chat_type = m.chat.type
        reply_text = m.reply_text

    if chat_type == ChatType.PRIVATE:
        keyboard = [
            [
                (_("Language Button"), "setchatlang"),
                (_("Help Button"), "menu"),
            ],
            [
                (
                    "Smudge News 📬",
                    "https://t.me/SmudgeNews",
                    "url",
                ),
            ],
        ]
        text = _("Start Private").format(m.from_user.first_name)
    else:
        text = _("Start Group")

    await reply_text(text, reply_markup=ikb(keyboard), disable_web_page_preview=True)