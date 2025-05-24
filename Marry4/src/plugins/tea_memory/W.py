
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

#========
_n="\n"
FP=str(pathlib.Path().absolute())
FP=FP.replace("\\","/")
FP+="/MarrySub"
main_g=str(555679990)
teach_g=str(807879174)
debug_group=[555679990,807879174,766536274,730423314]
pioneer=[2373725901,2687894198,2920568806,292069901,2920883352]

time_1=0

from . import V
async def msg_sent(bot, event,matcher,stamp,id,iden,msg_s):
    global time_1
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    if str(event.post_type)=="message":
        msg_raw=str(event.message)
        no=re.findall("[0-9]{1,11}",msg_raw)
    print("CODE:W")
    a4=(await V.selecting(uid,"G5000","a4"))[0]
    if a4=="" or a4=="0" or a4==0:#判断是否有自定义昵称
        PA5="店长"
    else:
        PA5=a4
    
    friend=iden[0]
    with open(FP+"/tea/friend_list.json","r",encoding='utf-8') as tea_json:
        friend_list=json.load(tea_json)
        tea_json.close()
    if puid in friend_list:
        friend=1
    else:
        friend=0
    
    #是否为群聊？
    #输出替换？
    #发送格式？（艾特，回复，图片，文本）
    #格式为[[type,msg],[type,msg]......]
    #[消息格式，消息/ID]
    msg_t=[]
    for i in msg_s["msg"]:
        if i[0]=="text":
            msg_text=await msg_replace_def(i[1],PA5)
            msg_out={"type":"text","data":{"text":msg_text}}
            msg_t.append(msg_out)
        elif i[0]=="at":
            msg_out={"type":"at","data":{"qq":i[1]}}
            msg_t.append(msg_out)
        elif i[0]=="reply":
            if gid:
                msg_out={"type":"reply","data":{"id":i[1]}}
                msg_t.append(msg_out)
            else:
                pass
        elif i[0]=="image":
            msg_out={"type":"image","data":{"file":i[1]}}
            msg_t.append(msg_out)
    if gid and msg_s["type"]=="G":
        try:
            await asyncio.wait_for(bot.send_group_msg(group_id=str(gid),message=msg_t),timeout=5)
            time.sleep(0.1)
        except:
            if time_1<=stamp[0]:
                pass
                #msg_t="群消息发送失败！请检查是否风控！"
                #await bot.send_private_msg(user_id=str(2373725901),message=msg_t)
                #time_1=stamp[0]+3600
    elif friend:
        await bot.send_private_msg(user_id=str(uid),message=msg_t)
        time.sleep(0.1)



async def msg_replace_def(msg_out,PA5):
    msg_out=msg_out.replace("【店长】",PA5)
    msg_out=msg_out.replace("_n_","\n")

    return(msg_out)

#获取唯一数值
