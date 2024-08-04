
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

async def help(bot, event,matcher,stamp,id,iden):
    print("CODE:B")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)

    if msg_raw=="茉莉帮助":
        await tea_help(bot, event,matcher,stamp,id,iden)
    elif msg_raw=="茉莉今天吃什么" or msg_raw=="茉莉今天恰什么" or msg_raw=="茉莉今天炫什么":
        await what_to_eat(bot, event,matcher,stamp,id,iden)
    elif msg_raw=="茉莉今天喝什么":
        await what_to_drink(bot, event,matcher,stamp,id,iden)
    elif msg_raw=="茉莉帮我抽个签":
        await tea_fortune(bot, event,matcher,stamp,id,iden)


async def tea_fortune(bot, event,matcher,stamp,id,iden):
    print("DEF:tea_fortune")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)
    
    fortune_list=["元吉（最为吉祥）","大吉（非常吉祥）","吉（吉祥）","无咎（没有灾难）","悔（懊悔）","吝（困难）","厉（危险）","咎（小灾）","凶（凶祸）"]
    fortune_code=random.choice(fortune_list)

    if fortune_code=="元吉（最为吉祥）" or fortune_code=="大吉（非常吉祥）" or fortune_code=="吉（吉祥）":
        msg_1=["text","(◍ > ω < ◍)店长抽到了："+fortune_code+"！"]


    elif fortune_code=="无咎（没有灾难）" or fortune_code=="悔（懊悔）" or fortune_code=="吝（困难）":
        msg_1=["text","(*ﾟーﾟ)店长抽到了："+fortune_code+"！"]

    elif fortune_code=="厉（危险）" or fortune_code=="咎（小灾）" or fortune_code=="凶（凶祸）":
        msg_1=["text","( 〞 0 ˄ 0 )店长抽到了："+fortune_code+"！"]

    msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
    await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)


async def tea_help(bot, event,matcher,stamp,id,iden):
    print("DEF:tea_help")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)
    

    img="file:///"+FP+"/tea/marry_help.png"
    msg_1=["image",img]
    msg_0={"msg":[msg_1],"type":"G"}
    await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)


async def what_to_eat(bot, event,matcher,stamp,id,iden):
    print("DEF:what_to_eat")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)
    
    with open(FP+"/tea/B1.json",'r',encoding='utf-8') as B1_json:
        B1_read=json.load(B1_json)
        B1_json.close

    to_eat=random.choice(B1_read)

    msg_1=["text","(ฅ・▽・)ฅ茉莉今天推荐店长吃【"+to_eat+"】呢！"]
    msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
    tea_data=await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    return(tea_data)

async def what_to_drink(bot, event,matcher,stamp,id,iden):
    print("DEF:what_to_drink")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)
    
    with open(FP+"/tea/B2.json",'r',encoding='utf-8') as B2_json:
        B2_read=json.load(B2_json)
        B2_json.close

    to_drink=random.choice(B2_read)

    msg_1=["text","(ฅ・▽・)ฅ茉莉今天推荐店长吃【"+to_drink+"】呢！"]
    msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
    tea_data=await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    return(tea_data)

