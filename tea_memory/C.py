
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
global tea_db,tea_cur
from . import V,W



async def admin(bot, event,matcher,stamp,id,iden):
    print("CODE:C")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)

    if re.search("/同意昵称",msg_raw):
        await agree_custom_nickname(bot, event,matcher,stamp,id,iden)
    elif re.search("/拒绝昵称",msg_raw):
        await disagree_custom_nickname(bot, event,matcher,stamp,id,iden)
    elif re.search("强制修改",msg_raw) or re.search("强制更改",msg_raw):
         await force_modify(bot, event,matcher,stamp,id,iden)

async def force_modify(bot, event,matcher,stamp,id,iden):
    print("DEF:force_modify")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)
    msg_raw=msg_raw.replace("强制修改","")
    msg_raw=msg_raw.replace("强制更改","")

    modify=msg_raw.split()
    obj=str(modify[0])
    table="G"+str(modify[1])
    column=str(modify[2])
    point=str(modify[3])
    await V.update(obj,table,column,point)
    msg_1=["text","对象："+obj+_n]
    msg_2=["text","表："+table+_n]
    msg_3=["text","列："+column+_n]
    msg_4=["text","数值："+point]
    msg_0={"msg":[msg_1,msg_2,msg_3,msg_4],"type":"G"}
    await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)


async def agree_custom_nickname(bot, event,matcher,stamp,id,iden):
    print("DEF:agree_custom_nickname")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)

    uid_a=int(no[0])
    puid_a="P"+str(uid_a)

    a5=(await V.selecting(uid_a,"G5000","a5"))[0]


    if a5!="0" and a5!=0:
            await V.update_text(uid_a,"G5000","a4",a5)
            await V.update_text(uid_a,"G5000","a5",0)
            #发送成功反馈
            msg_1=["text","已将("+str(uid_a)+")的昵称改为【"+a5+"】！"]
            msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
            await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
            #私聊对方已审核完毕
            with open(FP+"/tea/friend_list.json","r",encoding='utf-8') as tea_json:
                friend_list=json.load(tea_json)
                tea_json.close()
            if puid_a in friend_list:
                msg_0="(◍ ´꒳` ◍)店长的昵称审核成功啦，茉莉以后就叫你【"+a5+"】了哦~"
                await bot.send_private_msg(user_id=str(uid_a),message=msg_0)
    else:
            msg_1=["text","错误代码：C-1_n_对象临时自定义昵称为空！"]
            msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
            await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)



async def disagree_custom_nickname(bot, event,matcher,stamp,id,iden):
    print("DEF:disagree_custom_nickname")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)

    uid_a=int(no[0])
    puid_a="P"+str(uid_a)


    msg_1=["text", "已拒绝("+str(uid_a)+")的昵称！"]
    msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
    await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)

    await V.update_text(uid_a,"G5000","a5",0)
    with open(FP+"/tea/friend_list.json","r",encoding='utf-8') as tea_json:
        friend_list=json.load(tea_json)
        tea_json.close()
    if puid_a in friend_list:
        msg_0="( 〞 0 ˄ 0 )店长的昵称审核失败！若多次设置违规昵称，茉莉可能会不理店长了哦！"
        await bot.send_private_msg(user_id=str(uid_a),message=msg_0)

