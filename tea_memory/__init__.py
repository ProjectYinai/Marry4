
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
import PIL# type: ignore #pillow
import nonebot # type: ignore
import nonebot.drivers.aiohttp  # type: ignore # type: ignore
from nonebot import get_driver, on_message, on_command, get_bot, on_startswith, on_fullmatch, on_notice, on_request # type: ignore
from nonebot.adapters import Bot, Event, Message # type: ignore
from nonebot.params import EventMessage, EventPlainText, Arg, CommandArg, ArgPlainText, EventType # type: ignore
from nonebot.matcher import Matcher # type: ignore
from nonebot.rule import to_me, keyword, startswith # type: ignore
from nonebot.adapters.onebot.v11 import PrivateMessageEvent, GroupMessageEvent # type: ignore


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
version=240731
temp_stamp=int(time.time())
code_lista=["a1","a2","a3","a4","a5","a6","a7","a8","a9","a10",
            "b1","b2","b3","b4","b5","b6","b7","b8","b9","b10","b11","b12",
            "p1",
            "q1","q2","q3"]
code_listg=["g1","g2","g3","g4",
            "h1","h2",
            "s1","s2","s3",
            "t1","t2","t3","t4"]

from . import A,B,C,D,E,V,W,X,Z
X_tea_message=on_message(priority=99,block=False)
@X_tea_message.handle()
async def X_tea_message(bot: Bot, event: Event, matcher: Matcher):
    #定时刷新信息
    #储存数据
    #监测领养人管理员身份
    #未授权提示
    print("HANDLE:X")
    stamp,id,iden=await birthday(bot, event, matcher)
    await X.tea_message(bot, event,matcher,stamp,id,iden)
    await matcher.finish()

Z_tea_request=on_request(priority=99,block=False)
@Z_tea_request.handle()
async def Z_tea_request(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:Z")
    stamp,id,iden=await birthday(bot, event, matcher)
    await Z.tea_request(bot, event,matcher,stamp,id,iden)
    await matcher.finish()

#================================================
command_A1={"泡茉莉","泡红茶","泡咖啡","泡牛奶","泡奶茶",
           "午夜好","凌晨好","清晨好","早上好","中午好","下午好","黄昏好","晚上好","晚安",
           "我的好感度","红茶浓度"}
command_A2={"茉莉以后叫我","茉莉请叫我","茉莉叫我"}
A_tea_time_1=on_fullmatch(command_A1,priority=3,block=True)
A_tea_time_2=on_startswith(command_A2,priority=3,block=True)
@A_tea_time_1.handle()
@A_tea_time_2.handle()
async def A_tea_time(bot: Bot, event: Event, matcher: Matcher):#泡茉莉
    print("HANDLE:A")
    stamp,id,iden=await birthday(bot, event, matcher)
    if iden[1] and iden[2] and iden[3]:
        await A.tea_time(bot, event,matcher,stamp,id,iden)
    await matcher.finish()

command_B1={"茉莉帮助",
            "茉莉今天吃什么","茉莉今天恰什么","茉莉今天炫什么",
            "茉莉今天喝什么",
            "茉莉帮我抽个签"}
B_help_1=on_fullmatch(command_B1,priority=2,block=True) 
@B_help_1.handle()
async def B_help(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:B")
    stamp,id,iden=await birthday(bot, event, matcher)
    if iden[1] and iden[2] and iden[3]:
        await B.help(bot, event,matcher,stamp,id,iden)
    await matcher.finish()



#command_C1={}
command_C2={"/同意昵称","/拒绝昵称","强制刷新群",
            "强制修改","强制更改"}
#C_admin_1=on_fullmatch(command_C1,priority=2,block=True)
C_admin_2=on_startswith(command_C2,priority=2,block=True)
#@C_admin_1.handle()
@C_admin_2.handle()
async def C_admin(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:C")
    stamp,id,iden=await birthday(bot, event, matcher)
    #管理员指令
    #1、强制更改
    #2、生成授权码
    #3、同意昵称

    if iden[1] and iden[2] and id[0] in pioneer and iden[3]:
        await C.admin(bot, event,matcher,stamp,id,iden)
    await matcher.finish()

#command_D1={}
command_D2={"授权申请","申请授权","查授权"}
#D_applicant_1=on_fullmatch(command_D1,priority=2,block=True)
D_applicant_2=on_startswith(command_D2,priority=2,block=True)
#@D_applicant_1.handle()
@D_applicant_2.handle()
async def D_applicant(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:D")
    stamp,id,iden=await birthday(bot, event, matcher)
    #领养人指令
    #1、申请授权

    if iden[1] and iden[2]!=-1:
        await D.applicant(bot, event,matcher,stamp,id,iden)
    await matcher.finish()


command_E1={"抽群老婆","抽群老婆十连","群老婆十连","群老婆排行榜","群老婆up"}
command_E2={"娶群老婆"}
E_group_wife_1=on_fullmatch(command_E1,priority=5,block=True)
E_group_wife_2=on_startswith(command_E2,priority=5,block=True)
@E_group_wife_1.handle()
@E_group_wife_2.handle()
async def E_group_wife(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:E")
    stamp,id,iden=await birthday(bot, event, matcher)
    if iden[1] and iden[2] and iden[3]:
        await E.group_wife(bot, event,matcher,stamp,id,iden)
    await matcher.finish()


#================================================
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
    #检测是否为三号机
    bot_id=nonebot.get_bots()
    if "2920883352" in bot_id and not id[1] in debug_group:
        await matcher.finish()
    #========
    #代码版本查询（是否有新增/减少代码）
    await renew_def(bot, event, matcher,stamp,id)
    #========
    #刷新好友列表
    await refriend_def(bot, event, matcher,stamp,id)
    #========
    #黑白名单查询
    iden=await iden_def(bot, event, matcher,stamp,id)
    return([stamp,id,iden])
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

async def renew_def(bot, event, matcher,stamp,id):
    global tea_db,tea_cur
    puid="P"+str(id[0])
    ggid="G"+str(id[1])
    #查找个人代码是否齐全，主要为G5000
    #tea_cur.execute("select a0 from G5000 where user_id==1000")
    #for tea_row in tea_cur:
        #A0=tea_row[0]
    #if A0!=version:
        #for i in code_lista:
            #tea_cur.execute("alter table G5000 add column "+str(i)+" int if not exists (select "+str(i)+" from G5000)")
    
    #检查是否存在该群表


    #检查群代码是否齐全
    if id[1]:
        #tea_cur.execute("select g0 from "+ggid+" where user_id==1000")
        go=await V.selecting(1000,ggid,"g0")
        if go[0]!=version:
            try:#尝试创建新表，若存在报错跳过
                await V.execute("create table "+str(ggid)+"""(user_id integer primary key autoincrement not null,
                                group_id int not null,
                                g0 int)""")
            except:
                pass
            try:#尝试创建uid1000，若存在报错跳过
                await V.execute("insert into "+str(ggid)+"""(user_id,group_id,g0,g1,g4) values(1000,5000,171223,1,3)""")
            except:
                pass
            for i in code_listg:
                try:
                    if i in ["s3"]:#该列需用text格式储存数据
                        await V.execute("alter table "+ggid+" add column "+i+" text")
                    else:#该列需用int格式储存数据
                        await V.execute("alter table "+ggid+" add column "+i+" int")
                except:
                    pass
            await V.update(1000,ggid,"g0",version)


               
    #判断表G5000是否存在此uid
    temp_1=await V.selecting(id[0],"G5000","user_id")
    if temp_1[0]==0 and id[0]:
        await V.execute("insert into G5000 (user_id,group_id) values ("+str(id[0])+",5000)")

    #判断该uid在G5000是否为最新版
    ao=await V.selecting(id[0],"G5000","a0")
    if ao[0]!=version:
        print("判断该uid在G5000是否为最新版")
        a1=await V.selecting(id[0],"G5000","a1")
        a6=await V.selecting(id[0],"G5000","a6")
        for i in code_lista:
            if i=="a1" and a1[0]==0:#好友黑白名单
                await V.update(id[0],"G5000","a1",1)
            elif i=="a6" and a6[0]==0:#相遇日子（原优先）
                await V.update(id[0],"G5000","a6",stamp[4])
        await V.update(id[0],"G5000","a0",version)

        
    #判断表G****是否存在此uid
    temp_2=await V.selecting(id[0],ggid,"user_id")
    if temp_2[0]==0:
        await V.execute("insert into "+ggid+" (user_id,group_id) values ("+str(id[0])+","+str(id[1])+")")

    #判断该uid在G****是否为最新版
    go=await V.selecting(id[0],ggid,"g0")
    if go[0]!=version:
        print("判断该uid在G****是否为最新版")
        for i in code_listg:
            if i=="a1" :#and a1[0]==0:#好友黑白名单
                await V.update(id[0],"G5000","a1",1)
        await V.update(id[0],ggid,"g0",version)



async def refriend_def(bot, event, matcher,stamp,id):
    q3=await V.selecting(1000,"G5000","q3")
    print(str(q3))
    if q3[0]<=stamp[0]:
        if not os.path.isfile(FP+"/tea/friend_list.json"):
            os.chdir(FP)
            try:
                os.makedirs("tea")
            except:
                pass
            file=open(FP+"/tea/friend_list.json","w")
            file.write("")
            file.close
        friend=await bot.get_friend_list()
        friend_list={}
        for i in friend:
            puid_a="P"+str(i["user_id"])
            temp_1={puid_a:i}
            friend_list.update(temp_1)
        with open(FP+"/tea/friend_list.json","w",encoding='utf-8') as tea_json:
            json.dump(friend_list,tea_json,indent=1)
            tea_json.close()
        await V.update(1000,"G5000","q3",stamp[0]+3600)


async def iden_def(bot, event, matcher,stamp,id):
    global tea_db,tea_cur
    uid=id[0]
    gid=id[1]
    mid=id[2]
    puid="P"+str(uid)
    ggid="G"+str(gid)

    with open(FP+"/tea/friend_list.json","r",encoding='utf-8') as tea_json:
            friend_list=json.load(tea_json)
            tea_json.close()
    #是否为好友
    if puid in friend_list:
        friend=1
    else:
        friend=0
    #是否为个人白名单
    a1=await V.selecting(uid,"G5000","a1")
    idenP=a1[0]
    #是否为群白名单
    if not gid:
        idenG=1
    else:
        g1=await V.selecting(1000,ggid,"g1")
        g2=await V.selecting(1000,ggid,"g2")
        if g2[0]==1:
            idenG=1
        elif g2[0]==2:
            idenG=2
        else:
            idenG=0
        if g1[0]==0:
            idenG=-1
    #群内是否存在辅助机
    if os.path.exists(FP+"/tea/group/"+str(gid)+".json"):
        idenSub=1
    else:
        idenSub=0

    return([friend,idenP,idenG,idenSub])
#==============================================================================


#普通的初始化
if not os.path.exists(FP+"/tea"):
    os.chdir(FP)
    os.makedirs("tea")
tea_db=sql.connect(FP+"/tea/tea_data.db")
tea_cur=tea_db.cursor()
try:
    tea_cur.execute("""select * from G5000""")
    GV=tea_cur.fetchall()#global variable
except sql.OperationalError:
    tea_cur.execute("""create table G5000
                    (user_id integer primary key autoincrement not null,
                    group_id int not null,
                    a0 int)""")

    tea_cur.execute("""insert into G5000(user_id,group_id,a0)
                    values(1000,5000,171223)""")
tea_cur.execute("select a0 from G5000 where user_id==1000")
for tea_row in tea_cur:
        A0=tea_row[0]
if A0!=version:
    for i in code_lista:
        try:
            if i in ["a3","a4","a5"]:
                tea_cur.execute("alter table G5000 add column "+i+" text")
            else:
                tea_cur.execute("alter table G5000 add column "+i+" int")
        except:
            pass
    tea_cur.execute("update G5000 set a0="+str(version)+" where user_id==1000")
tea_db.commit()
tea_db.close()
#==============================================================================
#获取唯一数值









#结束后删除