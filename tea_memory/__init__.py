
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
from nonebot_plugin_apscheduler import scheduler


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

from . import A,B,C,D,E,V,W,X,Y,Z
X_tea_message=on_message(priority=99,block=False)
@X_tea_message.handle()
async def X_tea_message(bot: Bot, event: Event, matcher: Matcher):
    #定时刷新信息
    #储存数据
    #监测领养人管理员身份#
    #未授权提示
    print("HANDLE:X")
    print(int(round(time.time()*1000)))
    stamp,id,iden=await birthday(bot, event, matcher)
    await X.tea_message(bot, event,matcher,stamp,id,iden)
    print(int(round(time.time()*1000)))
    await matcher.finish()

Y_tea_notice=on_notice(priority=99,block=False)
@Y_tea_notice.handle()
async def Y_tea_notice(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:Y")
    stamp=await stamp_def(bot, event, matcher)
    id=await id_def(bot, event, matcher)
    await Y.tea_notice(bot, event,matcher,stamp,id)
    await matcher.finish()

Z_tea_request=on_request(priority=99,block=False)
@Z_tea_request.handle()
async def Z_tea_request(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:Z")
    #print(int(round(time.time()*1000)))
    stamp,id,iden=await birthday(bot, event, matcher)
    
    await Z.tea_request(bot, event,matcher,stamp,id,iden)
    #print(int(round(time.time()*1000)))
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
    #print(int(round(time.time()*1000)))
    stamp,id,iden=await birthday(bot, event, matcher)
    if iden[1] and iden[2] and iden[3]:
        await A.tea_time(bot, event,matcher,stamp,id,iden)
    #print(int(round(time.time()*1000)))
    await matcher.finish()

command_B1={"茉莉帮助",
            "茉莉今天吃什么","茉莉今天恰什么","茉莉今天炫什么",
            "茉莉今天喝什么",
            "茉莉帮我抽个签"}
B_help_1=on_fullmatch(command_B1,priority=2,block=True) 
@B_help_1.handle()
async def B_help(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:B")
    #print(int(round(time.time()*1000)))
    stamp,id,iden=await birthday(bot, event, matcher)
    if iden[1] and iden[2] and iden[3]:
        await B.help(bot, event,matcher,stamp,id,iden)
    #print(int(round(time.time()*1000)))
    await matcher.finish()



command_C1={"一键删除好友"}
command_C2={"/同意昵称","/拒绝昵称","强制刷新群",
            "强制修改","强制更改",
            "添加群白名单"}
C_admin_1=on_fullmatch(command_C1,priority=2,block=True)
C_admin_2=on_startswith(command_C2,priority=2,block=True)
@C_admin_1.handle()
@C_admin_2.handle()
async def C_admin(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:C")
    #print(int(round(time.time()*1000)))
    stamp,id,iden=await birthday(bot, event, matcher)
    #管理员指令
    #1、强制更改
    #2、生成授权码
    #3、同意昵称

    if iden[1] and iden[2] and id[0] in pioneer and iden[3]:
        await C.admin(bot, event,matcher,stamp,id,iden)
    #print(int(round(time.time()*1000)))
    await matcher.finish()

#command_D1={}
command_D2={"授权申请","申请授权","查授权"}
#D_applicant_1=on_fullmatch(command_D1,priority=2,block=True)
D_applicant_2=on_startswith(command_D2,priority=2,block=True)
#@D_applicant_1.handle()
@D_applicant_2.handle()
async def D_applicant(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:D")
    #print(int(round(time.time()*1000)))
    stamp,id,iden=await birthday(bot, event, matcher)
    #领养人指令
    #1、申请授权

    if iden[1] and iden[2]!=-1:
        await D.applicant(bot, event,matcher,stamp,id,iden)
    #print(int(round(time.time()*1000)))
    await matcher.finish()


command_E1={"抽群老婆","抽群老婆十连","群老婆十连","群老婆排行榜","群老婆up"}
command_E2={"娶群老婆"}
E_group_wife_1=on_fullmatch(command_E1,priority=5,block=True)
E_group_wife_2=on_startswith(command_E2,priority=5,block=True)
@E_group_wife_1.handle()
@E_group_wife_2.handle()
async def E_group_wife(bot: Bot, event: Event, matcher: Matcher):
    print("HANDLE:E")
    #print(int(round(time.time()*1000)))
    stamp,id,iden=await birthday(bot, event, matcher)
    if iden[1] and iden[2] and iden[3]:
        await E.group_wife(bot, event,matcher,stamp,id,iden)
    #print(int(round(time.time()*1000)))
    await matcher.finish()

#================================================
global friend_list
@scheduler.scheduled_job("interval", minutes=60, id="job_0")
async def run_every_1_hour():
    print("SCHEDULER:job_0")
    bot = get_bot()
    stamp=await stamp_def(bot, 1, 2)
    global friend_list
    with open(FP+"/tea/friend_list.json","r",encoding='utf-8') as tea_json:
            friend_list=json.load(tea_json)
            tea_json.close()


@scheduler.scheduled_job("cron", hour="3", id="job_1")
async def run_every_1_day():
    print("SCHEDULER:job_1")
    bot = get_bot()
    stamp=await stamp_def(bot, 1, 2)
    bot=get_bot()
    friend=await bot.get_friends_with_category()

    t1=0
    t2=0
    for i in friend[1]["buddyList"]:
        #print("DEF:force_modify"+str(t1))
        t1+=1
        uid_a=i["user_id"]
        b1=(await V.selecting(uid_a,"G5000","b1"))[0]
        if b1+90<=stamp[4]:
            await bot.delete_friend(user_id=uid_a)
            time.sleep(1)
            t2+=1

@scheduler.scheduled_job("interval", minutes=61, id="job_2")
async def refriend_def():
    print("SCHEDULER:job_2")
    bot = get_bot()
    stamp=await stamp_def(bot, 1, 2)
    q3=await V.selecting(1000,"G5000","q3")
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
        friends_with_category=await bot.get_friends_with_category()
        friend=friends_with_category[1]["buddyList"]
        friend_list={}
        for i in friend:
            puid_a="P"+str(i["user_id"])
            temp_1={puid_a:i}
            friend_list.update(temp_1)
        with open(FP+"/tea/friend_list.json","w",encoding='utf-8') as tea_json:
            json.dump(friend_list,tea_json,indent=1)
            tea_json.close()
        await V.update(1000,"G5000","q3",stamp[0]+3600)


#================================================
async def birthday(bot, event, matcher):#Happy Birthday!
    #========
    #print(int(round(time.time()*1000)))
    #========
    #时间戳获取
    stamp=await stamp_def(bot, event, matcher)
    if start_stamp>=stamp[0]:#初始启动刻1分钟不执行任务
        await matcher.finish()
    #========
    #print(int(round(time.time()*1000)))
    #id获取
    id=await id_def(bot, event, matcher)
    #========
    #print(int(round(time.time()*1000)))
    #检测是否为三号机
    bot_id=nonebot.get_bots()
    if "2920883352" in bot_id and not id[1] in debug_group:
        await matcher.finish()
    #========
    #print(int(round(time.time()*1000)))
    #代码版本查询（是否有新增/减少代码）
    await renew_def(bot, event, matcher,stamp,id)
    #========
    #print(int(round(time.time()*1000)))
    #刷新好友列表
    #await refriend_def(bot, event, matcher,stamp,id)
    #========
    #print(int(round(time.time()*1000)))
    #黑白名单查询
    iden=await iden_def(bot, event, matcher,stamp,id)
    #print(int(round(time.time()*1000)))
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





async def iden_def(bot, event, matcher,stamp,id):
    global tea_db,tea_cur
    uid=id[0]
    gid=id[1]
    mid=id[2]
    puid="P"+str(uid)
    ggid="G"+str(gid)
    global friend_list
    
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
        getsize=os.path.getsize(FP+"/tea/group/"+str(gid)+".json")
        if getsize>=256:
            idenSub=1
        else:
            os.remove(FP+"/tea/group/"+str(gid)+".json")
            idenSub=0
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
with open(FP+"/tea/friend_list.json","r",encoding='utf-8') as tea_json:
            friend_list=json.load(tea_json)
            tea_json.close()
#==============================================================================
#获取唯一数值









#结束后删除
'''
要使用Python调用API端点，你可以使用requests库。这是一个非常流行且易于使用的HTTP库。以下是一个简单的示例，展示了如何使用requests库来调用一个API端点：

首先，你需要安装requests库（如果你还没有安装的话）。你可以使用以下命令通过pip进行安装：
        
bash
复制代码
pip install requests

    
然后，你可以编写Python代码来调用API端点。例如，假设你有一个GET请求的API端点，URL为https://api.example.com/data，你可以这样做：
        
python
复制代码
import requests

# API端点的URL
url = 'https://api.example.com/data'

# 发送GET请求
response = requests.get(url)

# 检查响应状态码
if response.status_code == 200:
    # 解析JSON响应
    data = response.json()
    print(data)
else:
    print(f"请求失败，状态码: {response.status_code}")

    
如果API需要身份验证，你可以在请求中添加认证信息。例如，如果API使用Bearer Token进行认证，你可以这样做：
        
python
复制代码
import requests

# API端点的URL
url = 'https://api.example.com/data'

# Bearer Token
token = 'your_bearer_token_here'

# 设置请求头
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

# 发送GET请求
response = requests.get(url, headers=headers)

# 检查响应状态码
if response.status_code == 200:
    # 解析JSON响应
    data = response.json()
    print(data)
else:
    print(f"请求失败，状态码: {response.status_code}")

    
如果你需要发送POST请求并附带一些数据，可以这样做：
        
python
复制代码
import requests

# API端点的URL
url = 'https://api.example.com/data'

# 要发送的数据
payload = {
    'key1': 'value1',
    'key2': 'value2'
}

# 发送POST请求
response = requests.post(url, json=payload)

# 检查响应状态码
if response.status_code == 200:
    # 解析JSON响应
    data = response.json()
    print(data)
else:
    print(f"请求失败，状态码: {response.status_code}")
'''