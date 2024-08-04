
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
global tea_db,tea_cur
tea_db=sql.connect(FP+"/tea/tea_data.db")
tea_cur=tea_db.cursor()


async def selecting(uid,table,column):

    feedback=[]
    try:
        selection=tea_cur.execute("select "+column+" from "+table+" where user_id=="+str(uid))
        for row in selection:
            feedback.append(row[0])
            break
    except:
        pass
    if len(feedback)==0 or str(feedback[0])=="None":
        feedback=[0]
    tea_db.commit() 

    return(feedback)

    msg_1=["text","(*ﾟーﾟ)"]
    msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
    tea_data=await W.msg_sent(bot, event,matcher,tea_data,stamp,id,favour,iden,msg_0)


async def select_nowhere(table,column):
    feedback=[]
    try:
        if len(column)==1:
            selection=tea_cur.execute("select "+column[0]+" from "+table)
        elif len(column)>=2:
            column_a=str(column[0])
            for i in range (len(column)):
                if i != 0:
                    column_a+=","+str(column[i])
            selection=tea_cur.execute("select "+column+" from "+table)
        for row in selection:
            feedback.append(row)
    except:
        pass
    if len(feedback)==0 or str(feedback[0])=="None":
        feedback=[0]
    return(feedback)

async def update(uid,ggid,code,value):
    tea_cur.execute("update "+str(ggid)+" set "+str(code)+"="+str(value)+" where user_id=="+str(uid))
    tea_db.commit() 
 
async def update_text(uid,ggid,code,value):
    tea_cur.execute("update "+str(ggid)+" set "+str(code)+"=\'"+str(value)+"\' where user_id=="+str(uid))
    tea_db.commit() 
    

async def execute(code):
    feedback=tea_cur.execute(code)
    tea_db.commit()
    return(feedback)