
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
global tea_db,tea_cur

from . import V,W



async def tea_message(bot, event,matcher,stamp,id,iden):
    print("CODE:X")
    uid=id[0]
    gid=id[1]
    mid=id[2]
    ggid="G"+str(gid)
    puid="P"+str(uid)
    msg_re="(ฅ・ー・)ฅ因以下某种原因，本群失去授权。"+_n+"1、领养人不再是群主或管理员身份。"+_n+"2、领养人退出了主群。"+_n+"3、领养人和茉莉不再是好友。"+_n+"4、群总人数超过500人但领养人不为管理员。"+_n+"5、出现了以为修复但并没有修复的bug。"+_n+"若为5请及时联系音奈。"

    
    
    g2=(await V.selecting(1000,ggid,"g2"))[0]#群授权情况：1、
    g3=(await V.selecting(1000,ggid,"g3"))[0]
    g5=(await V.selecting(1000,ggid,"g5"))[0]
    #判断授权情况

    
    if gid:#授权判断
        if not g2:
            #若无授权，根据时间戳发送提醒。
            h2=(await V.selecting(1000,ggid,"h2"))[0]
            g4=(await V.selecting(1000,ggid,"g4"))[0]
            if h2<=stamp[0] and g4>=1:
                #发送消息
                msg_1=["text","(ฅ・ー・)ฅ该群暂未授权，请联系茉莉的主人音奈，QQ号写在茉莉的个性签名哦~"+_n+"10分钟内未授权茉莉将退群哦~"]
                msg_0={"msg":[msg_1],"type":"G"}
                #await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
                #设置群授权提醒时间戳
                await V.update(1000,ggid,"h2",stamp[0]+60)
                #设置群授权提醒次数
                await V.update(1000,ggid,"g4",g4-1)
            elif h2<=stamp[0] and g4<=0:
                await V.update(1000,ggid,"g2",0)
                await V.update(1000,ggid,"g3",0)
                await V.update(1000,ggid,"g4",2)
                await V.update(1000,ggid,"h2",0)
                await bot.set_group_leave(group_id=gid,is_dismiss=True)
        else:
            #若有授权：
            #1、领养人在主群内 
            
            puid_a="P"+str(g3)
            if g3!=0 and os.path.isfile(FP+"/tea/group/555679990.json"):
                with open(FP+"/tea/group/555679990.json","r",encoding='utf-8') as group_json:
                    group_m=json.load(group_json)
                    group_json.close()
                if not puid_a in group_m["info"]:
                    #领养人不在主群，清空授权，清空领养人，刷新提醒次数，刷新时间戳。
                    await V.update(1000,ggid,"g2",0)
                    await V.update(1000,ggid,"g3",0)
                    await V.update(1000,ggid,"g4",2)
                    await V.update(1000,ggid,"h2",0)
                    msg_1=msg_re
                    #await bot.send_group_msg(group_id=str(id[1]),message=msg_1)
                    #haruki删除白名单
                    haruki_url="http://127.0.0.1:2525/haruki_client/controller/remove_whitelist"
                    payload = {"module":"pjsk","group_ids":[int(id[1])]}
                    requests.post(haruki_url, json=payload)
            #2、判断辅助机是否在该群内。若在，二次判断领养人是否为管理员。
                if os.path.isfile(FP+"/tea/group/"+str(gid)+".json"):
                    with open(FP+"/tea/group/"+str(gid)+".json","r",encoding='utf-8') as group_json:
                        group_a=json.load(group_json)
                        group_json.close()
                    if puid_a in group_a["info"]:
                        uid_a=str(g3)
                        a2_a=(await V.selecting(int(uid_a),"G5000","a2"))[0]
                        if group_a["info"][puid_a]["role"]!="member" and a2_a>=15360:
                            if g2==2:
                                await V.update(1000,ggid,"g2",1)
                            if g5>500 and group_a["info"][puid_a]["role"]!="owner":
                                await V.update(1000,ggid,"g2",0)
                                await V.update(1000,ggid,"g3",0)
                                await V.update(1000,ggid,"g4",2)
                                await V.update(1000,ggid,"h2",0)
                                msg_1=msg_re
                                #await bot.send_group_msg(group_id=str(id[1]),message=msg_1)
                                #haruki删除白名单
                                haruki_url="http://127.0.0.1:2525/haruki_client/controller/remove_whitelist"
                                payload = {"module":"pjsk","group_ids":[int(id[1])]}
                                requests.post(haruki_url, json=payload)
                        else:#领养人不为群主或管理员，清空授权，清空领养人，刷新提醒次数，刷新时间戳。
                            await V.update(1000,ggid,"g2",0)
                            await V.update(1000,ggid,"g3",0)
                            await V.update(1000,ggid,"g4",2)
                            await V.update(1000,ggid,"h2",0)
                            msg_1=msg_re
                            #await bot.send_group_msg(group_id=str(id[1]),message=msg_1)
                            #haruki删除白名单
                            haruki_url="http://127.0.0.1:2525/haruki_client/controller/remove_whitelist"
                            payload = {"module":"pjsk","group_ids":[int(id[1])]}
                            requests.post(haruki_url, json=payload)
                    elif len(group_a["info"])==0:
                        pass
                    
                    else:
                        await V.update(1000,ggid,"g2",0)
                        await V.update(1000,ggid,"g3",0)
                        await V.update(1000,ggid,"g4",2)
                        await V.update(1000,ggid,"h2",0)
                        msg_1=msg_re
                        #await bot.send_group_msg(group_id=str(id[1]),message=msg_1)
                        #haruki删除白名单
                        haruki_url="http://127.0.0.1:2525/haruki_client/controller/remove_whitelist"
                        payload = {"module":"pjsk","group_ids":[int(id[1])]}
                        requests.post(haruki_url, json=payload)
                    
                else:
                        #3、判断辅助机是否在该群内。若在，群授权g2=1，否则g2=2。
                        if g2==1:
                            await V.update(1000,ggid,"g2",2)
            elif g3==0 and g2!=0:
                await V.update(1000,ggid,"g2",0)  


                
                                    
    if gid:
        await V.update(uid,ggid,"t4",stamp[0])

        h1=(await V.selecting(1000,ggid,"h1"))[0]
        if h1<=stamp[0]:
            await V.update(1000,ggid,"h1",stamp[0]+21600)
            if os.path.isfile(FP+"/tea/group/"+str(gid)+".json"):
                with open(FP+"/tea/group/"+str(gid)+".json","r",encoding='utf-8') as group_a_json:
                    group_a=json.load(group_a_json)
                    group_a_json.close()
                #更新群总人数
                try:
                    await V.update(1000,ggid,"g5",len(group_a["info"]))
                except:
                    await V.update(1000,ggid,"g5",0)
                #更新所有群成员的数据
                for i in group_a["info"]:
                    if group_a["info"][i]["card"]=="":
                        nickname=group_a["info"][i]["nickname"]
                        nickname=nickname.replace("\'","")
                        nickname=nickname.replace("\"","")
                        try:
                            await V.update_text(group_a["info"][i]["user_id"],ggid,"s3",nickname)
                        except:
                            await V.execute("insert into "+ggid+"(user_id,group_id,s3) values ("+str(group_a["info"][i]["user_id"])+","+str(gid)+",\'"+nickname+"\')")
                    else:
                        card=group_a["info"][i]["card"]
                        card=card.replace("\'","")
                        card=card.replace("\"","")
                        try:
                            await V.update_text(group_a["info"][i]["user_id"],ggid,"s3",card)
                        except:
                            await V.execute("insert into "+ggid+"(user_id,group_id,s3) values ("+str(group_a["info"][i]["user_id"])+","+str(gid)+",\'"+card+"\')")

    #删除90天没泡过红茶且为好友的好友
    #缺漏是退群没有接收过消息的那些好友
    #b1=(await V.selecting(uid,"G5000","b1"))[0]
    #friend=iden[0]
    #if b1+90<=stamp[4] and friend:
        #pass
        #await bot.delete_friend(user_id=uid)

#获取唯一数值

