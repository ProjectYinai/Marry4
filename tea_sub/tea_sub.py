
import json
import random
import re
import time
import urllib
import os
#========
import sqlite3 as sql
import pathlib
import asyncio
import datetime
import dateutil#python-dateutil
from dateutil import rrule
from dateutil.parser import parse
import PIL#pillow
#========
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
main_g=[555679990,942054420,482963384,283738174,807879174,548087783]
teach_g=str(807879174)
debug_group=[555679990,807879174,766536274,730423314,669546286,606731240]
pioneer=[2373725901,2687894198,2920568806,292069901,2920883352]
start_stamp=int(time.time())+5



X_tea_message=on_message(priority=99,block=False)
@X_tea_message.handle()
async def X_tea_message(bot: Bot, event: Event, matcher: Matcher):
    #定时刷新信息
    #储存数据
    #监测领养人管理员身份
    #未授权提示
    stamp,id=await birthday(bot, event, matcher)
    #await tea_message(bot, event,matcher,stamp,id)
    await matcher.finish()

Z_tea_request=on_request(priority=99,block=False)
@Z_tea_request.handle()
async def Z_tea_request(bot: Bot, event: Event, matcher: Matcher):
    stamp,id=await birthday(bot, event, matcher)
    await tea_request(bot, event,matcher,stamp,id)
    await matcher.finish()

async def tea_request(bot, event,matcher,stamp,id):
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
        print("邀请加入群٩( 'ω' )و get！")
        sub_type=str(event.sub_type)
        if sub_type=="invite":
            flag_a=str(event.flag)
            await bot.set_group_add_request(flag=flag_a,approve=True)


async def birthday(bot, event, matcher):#Happy Birthday!
    #========
    #时间戳获取
    stamp=await stamp_def(bot, event, matcher)
    if start_stamp>=stamp[0]:#初始启动刻1分钟不执行任务
        await matcher.finish()
    #========
    #id获取
    id=await id_def(bot, event, matcher)
    #========
    #刷新群缓存
    if id[1]:
        await renew(bot, event, matcher,stamp,id)
    return([stamp,id])

#==============================================================================
#时间戳获取
async def stamp_def(bot, event, matcher):
    birthday=1513971000
    time_stamp=int(time.time())
    time_interval=time_stamp-birthday
    time_stamp_sec=int(time_interval)
    time_stamp_min=int(time_interval/60)
    time_stamp_hour=int(time_interval/3600)
    time_stamp_day=int(time_interval/86400)
    
    birthday="2017-12-23"
    time_stamp_mon=rrule.rrule(rrule.MONTHLY,dtstart=parse("2017-12-23"),until=datetime.date.today()).count()
    time_stamp_year=rrule.rrule(rrule.YEARLY,dtstart=parse("2017-12-23"),until=datetime.date.today()).count()


    time_local_yday=int(time.localtime().tm_yday)
    time_local_wday=int(time.localtime().tm_wday)
    time_local_sec=int(time.localtime().tm_sec)
    time_local_min=int(time.localtime().tm_min)
    time_local_hour=int(time.localtime().tm_hour)
    time_local_mday=int(time.localtime().tm_mday)
    time_local_mon=int(time.localtime().tm_mon)
    time_local_year=int(time.localtime().tm_year)

    stamp=[time_stamp,
    time_stamp_sec,
    time_stamp_min,
    time_stamp_hour,
    time_stamp_day,
    time_stamp_mon,
    time_stamp_year,
    time_local_yday,
    time_local_wday,
    time_local_sec,
    time_local_min,
    time_local_hour,
    time_local_mday,
    time_local_mon,
    time_local_year]

    return(stamp)

#id获取
async def id_def(bot, event, matcher):
    if str(event.post_type)=="message":
        if str(event.message_type)=="private":
            uid=int(event.user_id)
            gid=0
            mid=int(event.message_id)
        elif str(event.message_type)=="group" and str(event.sub_type)=="normal":
            uid=int(event.user_id)
            gid=int(event.group_id)
            mid=int(event.message_id)
        elif str(event.message_type)=="group" and str(event.sub_type)=="notice":
            uid=0
            gid=int(event.group_id)
            mid=0
        else:
            uid=0
            gid=0
            mid=0
    elif str(event.post_type)=="notice":
        if "group" in str(event.notice_type):
            uid=0
            gid=int(event.group_id)
            mid=0
        else:
            uid=0
            gid=0
            mid=0
    elif str(event.post_type)=="request":
        if str(event.request_type)=="friend":
            uid=int(event.user_id)
            gid=0
            mid=0
        elif str(event.request_type)=="group":
            uid=int(event.user_id)
            gid=int(event.group_id)
            mid=0
        else:
            uid=0
            gid=0
            mid=0
    else:
        uid=0
        gid=0
        mid=0
    id=[uid,gid,mid]
    return(id)

#刷新群数据
async def renew(bot, event, matcher,stamp,id):
    gid=id[1]
    ggid="G"+str(gid)
    with open(FP+"/tea/group/_group.json","r",encoding='utf-8') as group_json:
        group=json.load(group_json)
        group_json.close()

    if not os.path.isfile(FP+"/tea/group/"+str(gid)+".json"):
        file=open(FP+"/tea/group/"+str(gid)+".json","w")
        file.write("")
        file.close
            #获取该群群成员列表
        info={}
        try:
            group_info=await bot.get_group_member_list(group_id=str(gid),no_cache=True)
            for i in group_info:
                puid="P"+str(i["user_id"])
                info.update({puid:i})
        except:
            pass
        if len(info)!=0:
            with open(FP+"/tea/group/"+str(gid)+".json","w",encoding='utf-8') as group_json:
                json.dump({"stamp":stamp[0],"info":info},group_json,indent=1)
                group_json.close()



    if group["stamp"]<=stamp[0] and len(group["list"])>=1:
        #查询最新应刷新群号
        gid_a=group["list"][0]
        #查询辅助机是否在此群中
        try:
            in_group=await bot.get_group_info(group_id=str(gid_a),no_cache=True)
        except:
            del group["list"][0]
            with open(FP+"/tea/group/_group.json","w",encoding='utf-8') as group_json:
                json.dump(group,group_json,indent=1)
                group_json.close()
            await matcher.finish()

        if not in_group["max_member_count"]==0:
            #查询该群是否存在缓存
            if not os.path.isfile(FP+"/tea/group/"+str(gid_a)+".json"):
                file=open(FP+"/tea/group/"+str(gid_a)+".json","w")
                file.write("")
                file.close
            #获取该群群成员列表
            group_info=await bot.get_group_member_list(group_id=str(gid_a),no_cache=True)
            info={}
            for i in group_info:
                puid="P"+str(i["user_id"])
                info.update({puid:i})
            if len(info)!=0:
                with open(FP+"/tea/group/"+str(gid_a)+".json","w",encoding='utf-8') as group_json:
                    json.dump({"stamp":stamp[0],"info":info},group_json,indent=1)
                    group_json.close()
            #增加刷新时间戳
            group["stamp"]=stamp[0]+(len(group_info)//10)
        else:
            #辅助机不存在此群中，删除缓存
            try:
                os.remove(FP+"/tea/group/"+str(gid_a)+".json")
            except:
                pass
            group["stamp"]=stamp[0]+30
        #删除最新应刷新群号
        del group["list"][0]
    if not gid in group["list"] and not os.path.isfile(FP+"/tea/group/"+str(gid)+".json"):
        group["list"].insert(0,gid)
    elif not gid in group["list"] and len(group["list"])<=63:
        group["list"].append(gid)
    #写入group.json
    with open(FP+"/tea/group/_group.json","w",encoding='utf-8') as group_json:
            json.dump(group,group_json,indent=1)
            group_json.close()


    
    

if not os.path.isfile(FP+"/tea/group/_group.json"):
    os.chdir(FP)
    try:
        os.makedirs("tea")
    except:
        pass
    os.chdir(FP+"/tea")
    try:
        os.makedirs("group")
    except:
        pass
    file=open(FP+"/tea/group/_group.json","w")
    file.write(str({}))
    file.close
    group_list={"stamp":0,"list":[]}
    with open(FP+"/tea/group/_group.json","w",encoding='utf-8') as group_json:
            json.dump(group_list,group_json,indent=1)
            group_json.close()