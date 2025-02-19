
import json
import random
import re
import time
import urllib
import os

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

async def tea_request(bot, event,matcher,stamp,id,iden):
    print("CODE:Z")
    uid=id[0]
    gid=id[1]
    mid=id[2]
    ggid="G"+str(gid)

    request_type=str(event.request_type)

    if request_type=="friend":
        print("加好友申请٩( 'ω' )و get！")
        flag_a=str(event.flag)
        await bot.set_friend_add_request(flag=flag_a,approve=True)
        time.sleep(3)
        msg_1="(ฅ・▽・)ฅ店长早呢~"
        await bot.send_private_msg(user_id=uid,message=msg_1)
    elif request_type=="group":
        #print("邀请加入群٩( 'ω' )و get！")
        a2=(await V.selecting(uid,"G5000","a2"))[0]
        sub_type=str(event.sub_type)
        if sub_type=="invite" and not uid in pioneer and a2<1024:
            flag_a=str(event.flag)
            await bot.set_group_add_request(flag=flag_a,approve=False)
        elif sub_type=="invite" and not uid in pioneer and a2>=1024:
            flag_a=str(event.flag)
            await bot.set_group_add_request(flag=flag_a,approve=True)
        elif sub_type=="invite" and uid in pioneer:
            flag_a=str(event.flag)
            await bot.set_group_add_request(flag=flag_a,approve=True)
