
import json
import random
import re
import time
import urllib
import os
import math
#========
import sqlite3 as sql
import keyboard
import pathlib
import asyncio
import datetime
import dateutil#python-dateutil
from dateutil import rrule
from dateutil.parser import parse
import PIL#pillow
import nonebot
import nonebot.drivers.aiohttp 
from nonebot import get_driver, on_message, on_command, get_bot, on_startswith, on_fullmatch, on_notice, on_request
from nonebot.adapters import Bot, Event, Message
from nonebot.params import EventMessage, EventPlainText, Arg, CommandArg, ArgPlainText, EventType
from nonebot.matcher import Matcher
from nonebot.rule import to_me, keyword, startswith
from nonebot.adapters.onebot.v11 import PrivateMessageEvent, GroupMessageEvent


_n="\n"
FP=str(pathlib.Path().absolute())
FP=FP.replace("\\","/")
FP+="/MarrySub"
main_g=[555679990,942054420,482963384,283738174,807879174,548087783]
teach_g=str(807879174)
debug_group=[555679990,807879174,766536274,730423314,669546286,606731240]
pioneer=[2373725901,2687894198,2920568806,292069901,2920883352]
start_stamp=int(time.time())+5
from . import V,W


async def tea_notice(bot, event,matcher,stamp,id):
    print("CODE:X")
    uid=id[0]
    gid=id[1]
    mid=id[2]
    ggid="G"+str(gid)
    puid="P"+str(uid)
    iden=[0]

    notice_type=str(event.notice_type)
    if notice_type=="notify":
        try:
            sub_type=str(event.sub_type)
            target_id=int(event.target_id)
        except:
            sub_type=""
            target_id=0
        if sub_type=="poke" and target_id==2920568806:
            await poke(bot, event,matcher,stamp,id)

async def poke(bot, event,matcher,stamp,id):
    uid=id[0]
    gid=str(event.group_id)
    mid=id[2]
    ggid="G"+str(gid)
    puid="P"+str(uid)
    iden=[0]


    msg_1=["text","˚‧º·(˚ ˃̣̣̥᷄⌓˂̣̣̥᷅ )‧º·˚不要再戳茉莉啦~"]
    msg_0={"msg":[msg_1],"type":"G"}
    msg_0="˚‧º·(˚ ˃̣̣̥᷄⌓˂̣̣̥᷅ )‧º·˚不要再戳茉莉啦~"
    msg_s={"type":"text","data":{"text":msg_0}}
    await bot.send_group_msg(group_id=str(gid),message=msg_s)
    time.sleep(0.1)

