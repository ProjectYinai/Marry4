
import json
import random
import re
import time
import urllib
import os

#========
import requests
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
async def applicant(bot, event,matcher,stamp,id,iden):
    print("CODE:D")
    uid=id[0]
    gid=id[1]
    mid=id[2]
    raw_msg=str(event.raw_message)
    no=re.findall("[0-9]{1,11}",str(event.raw_message))
    print("CODE:D")

    if re.search("授权申请",raw_msg) or re.search("申请授权",raw_msg) :
        await authorization(bot, event,matcher,stamp,id,iden,no)
    elif re.search("查授权",raw_msg) and gid:
        await check(bot, event,matcher,stamp,id,iden)


async def check(bot, event,matcher,stamp,id,iden):
    print("DEF:check")
    uid=id[0]
    gid=id[1]
    mid=id[2]
    ggid="G"+str(gid)
    raw_msg=str(event.raw_message)
    no=re.findall("[0-9]{1,11}",str(event.raw_message))


    

    if raw_msg=="查授权":
        g2=(await V.selecting(1000,ggid,"g2"))[0]
        g3=(await V.selecting(1000,ggid,"g3"))[0]
        msg_1="查询群号："+str(gid)+_n
        if g2:
            msg_2="授权查询：已授权"+_n+"领养人："+str(g3)+_n
        else:
            msg_2="授权查询：未授权"+_n
        if os.path.isfile(FP+"/tea/group/"+str(gid)+".json"):
            msg_3="辅助机已刷新此群缓存"
        else:
            msg_3="辅助机未在此群，或本群缓存未刷新"
        msg_4=["text",msg_1+msg_2+msg_3]
        msg_0={"msg":[["reply",str(mid)],msg_4],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    else:
        g2=(await V.selecting(1000,"G"+str(no[0]),"g2"))[0]
        g3=(await V.selecting(1000,"G"+str(no[0]),"g3"))[0]
        msg_1="查询群号："+str(no[0])+_n
        if g2:
            msg_2="授权查询：已授权"+_n+"领养人："+str(g3)+_n
        else:
            msg_2="授权查询：未授权"+_n
        if os.path.isfile(FP+"/tea/group/"+str(no[0])+".json"):
            msg_3="辅助机已刷新此群缓存"
        else:
            msg_3="辅助机未在此群，或本群缓存未刷新"
        msg_4=["text",msg_1+msg_2+msg_3]
        msg_0={"msg":[["reply",str(mid)],msg_4],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)

async def authorization(bot, event,matcher,stamp,id,iden,no):
    print("DEF:authorization")
    uid=id[0]
    gid=id[1]
    mid=id[2]
    ggid="G"+str(gid)

    gid_a=int(no[0])
    ggid_a="G"+str(gid_a)
    print("D:authorization")


    if str(event.message)=="授权申请" or  str(event.message)=="申请授权":
        await matcher.finish()
    #确实是否为主群
    if not gid in [555679990]:
        await matcher.finish()

    group_info=await bot.get_group_member_list(group_id=str(555679990),no_cache=True)
    info={}
    for i in group_info:
        puid="P"+str(i["user_id"])
        info.update({puid:i})
    if len(info)!=0:
        with open(FP+"/tea/group/"+str(555679990)+".json","w",encoding='utf-8') as group_json:
            json.dump({"stamp":stamp[0],"info":info},group_json,indent=1)
            group_json.close()

            
    #检查茉莉是否在领养群内
    try:
        in_group=await bot.get_group_info(group_id=str(gid_a),no_cache=True)
        if in_group["max_member_count"]==0:
            point=1
        else:
            temp_1=list(await V.execute("PRAGMA table_info("+str(ggid_a)+")"))
            g3=await V.selecting(1000,ggid_a,"g3")
            a2=(await V.selecting(uid,"G5000","a2"))[0]
            if temp_1[0]==0:
                point=2
            elif g3[0]!=0:
                point=3
            elif a2<1024:
                point=5
            else:
                
                point=0
    except:
        point=4
    

    print("point:"+str(point))
    if point==1:
        msg_1=["text","( 〞 0 ˄ 0 )错误代码：D-1。\n茉莉主号机不在该群内。"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    elif point==2:
        msg_1=["text","( 〞 0 ˄ 0 )错误代码：D-2。\n不存在该群缓存，请在领养群内触发未授权提示后再试。"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    elif point==3:
        msg_1=["text","( 〞 0 ˄ 0 )错误代码：D-3。\n本群已授权且已存在领养人。若想更改领养人，请联系茉莉的主人音奈更改。_n_不过更新了一下pjsk的授权~"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
        #haruki
        haruki_url="http://127.0.0.1:2525/haruki_client/controller/add_whitelist"
        payload = {"module":"pjsk","group_ids":[int(gid_a)]}
        requests.post(haruki_url, json=payload)
    elif point==4:
        msg_1=["text","( 〞 0 ˄ 0 )错误代码：D-4。\n该群不存在！请确认群号是否输入正确，并保证茉莉在该群中。"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    elif point==5:
        msg_1=["text","( 〞 0 ˄ 0 )错误代码：D-5。\n领养人好感度等级未到20级！"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    
    elif point==0:
        tea_db=sql.connect(FP+"/tea/tea_data.db")
        tea_cur=tea_db.cursor()
        #更改群授权
        await V.update(1000,ggid_a,"g2",2)
        #更改领养人
        await V.update(1000,ggid_a,"g3",uid)
        #刷新群授权提醒次数
        await V.update(1000,ggid_a,"g4",3)
        msg_1=["text","｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡领养成功~"+_n+"领养群："+str(in_group["group_name"])+_n+"领养有效期：-1天，大概。"+_n+"请领养人不要删除茉莉好友！不要退出主群！可永久屏蔽主群！"]
        msg_0={"msg":[["at",str(uid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
        #写入haruki
        haruki_url="http://127.0.0.1:2525/haruki_client/controller/add_whitelist"
        payload = {"module":"pjsk","group_ids":[int(gid_a)]}
        requests.post(haruki_url, json=payload)

        


       