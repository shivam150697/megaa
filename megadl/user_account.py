# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae
# This plugin is working only if you Login with Mega Account

import json
import os
import time

from pyrogram import Client, filters
from pyrogram.types import Message
from hurry.filesize import size

from megadl.account import m
from megadl.mega_dl import GITHUB_REPO
from config import Config
from megadl.mega_help import progress_for_pyrogram, humanbytes

# Get Mega user Account info
@Client.on_message(filters.command("info") & filters.private)
async def accinfo(_, message: Message):
  if message.from_user.id not in Config.AUTH_USERS:
    await message.reply_text("**Sorry this bot isn't a Public Bot 🥺! But You can make your own bot ☺️, Click on Below Button!**", reply_markup=GITHUB_REPO)
    return
  if Config.USER_ACCOUNT == "False":
    await message.reply_text("You didn't setup a Mega.nz Account to Get details!")
    return
  get_user = m.get_user()
  imported_user = json.dumps(get_user)
  uacc_info = json.loads(imported_user)
  acc_email = uacc_info['email']
  acc_name = uacc_info['name']
  acc_quota = m.get_quota()
  js_acc_space = m.get_storage_space()
  acc_space_f = json.dumps(js_acc_space)
  acc_space = json.loads(acc_space_f)
  btotal_space = acc_space['total']
  bused_space = acc_space['used']
  bfree_space = btotal_space - bused_space
  total_space = size(btotal_space)
  used_space = size(bused_space)
  free_space = size(bfree_space)
  await message.reply_text(f"**~ Your User Account Info ~** \n\n▪ **Account Name:** `{acc_name}` \n▪ **Email:** `{acc_email}` \n▪ **Storage,** \n - **Total:** `{total_space}` \n - **Used:** `{used_space}` \n - **Free:** `{free_space}` \n▪ **Quota:** `{acc_quota} MB`")


# uplaod files
@Client.on_message(filters.command("upload") & filters.private)
async def uptomega(client: Client, message: Message):
  if message.from_user.id not in Config.AUTH_USERS:
    await message.reply_text("**Sorry this bot isn't a Public Bot 🥺! But You can make your own bot ☺️, Click on Below Button!**", reply_markup=GITHUB_REPO)
    return
  if Config.USER_ACCOUNT == "False":
    await message.reply_text("You didn't setup a Mega.nz Account to Get details!")
    return
  todownfile = message.reply_to_message
  if not todownfile:
    await message.reply_text("**Please reply to a Media File to Upload!**")
    return
  if todownfile.media is None:
    await message.reply_text("Sorry, I can't Upload Text to Mega! Please reply to a Media File!")
    return
  try:
    start_time = time.time()
    megaupmsg = await message.reply_text("**Starting to Download The Content to My Server! This may take while 😴**")
    toupload = await client.download_media(message=todownfile, progress=progress_for_pyrogram, progress_args=("**Trying to Download!** \n", megaupmsg, start_time))
    await megaupmsg.edit("**Successfully Downloaded the File!**")
    await megaupmsg.edit("**Trying to Upload to Mega.nz**")
    uploadfile = m.upload(f"{toupload}")
    link = m.get_upload_link(uploadfile)
    await megaupmsg.edit(f"**Successfully Uploaded To Mega.nz** \n\n**Link:** `{link}` \n\n**Powered by @NexaBotsUpdates**")
    if toupload is not None:
      os.remove(toupload)
  except Exception as e:
    await megaupmsg.edit(f"**Error:** `{e}`")
    if toupload is not None:
      os.remove(toupload)
    else:
      print("Why this file is gae?")
