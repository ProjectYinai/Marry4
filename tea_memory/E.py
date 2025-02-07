
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
from PIL import Image
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
#img="http://q1.qlogo.cn/g?b=qq&nk="+str()+"&s=100"

async def group_wife(bot, event,matcher,stamp,id,iden):
    print("CODE:E")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)
    
    if not gid:
        await matcher.finish()

    #重置群老婆up表
    if msg_raw=="抽群老婆":
        await random_wife(bot, event,matcher,stamp,id,iden)
    elif msg_raw=="抽群老婆十连" or msg_raw=="群老婆十连":
        await random_wife_ten(bot, event,matcher,stamp,id,iden)
    elif msg_raw=="群老婆排行榜":
        await wife_rank(bot, event,matcher,stamp,id,iden)
    elif "娶群老婆" in msg_raw:
        await marry_wife(bot, event,matcher,stamp,id,iden)

async def wife_rank(bot, event,matcher,stamp,id,iden):
    print("DEF:wife_rank")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.raw_message)

    s1_info=await V.execute("select user_id,s1 from "+ggid+" where s1>=1 order by s1 desc")
    s1_list=[]
    for row in s1_info:
        s1_list.append(row)

    if len(s1_list)<=5:
        msg_1=["text","( 〞 0 ˄ 0 )错误代码：E-1。\n排行榜数据过少，当前群老婆数为"+str(len(s1_list))+"名，到达6名后即可使用排行榜功能！"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
        await matcher.finish()

    index_u=-1
    for i in range(len(s1_list)):
        if s1_list[i][0]==uid:
            index_u=i
            break

    msg_1=["text","==群老婆排行榜=="]

    #第一名
    rank_1_card=(await V.selecting(s1_list[0][0],ggid,"s3"))[0]
    rank_1_card=rank_1_card
    if rank_1_card == 0:
        rank_1_card="锟斤拷"
    a="1.【"+str(rank_1_card)+"】"+str(s1_list[0][1])+"次"
    #第二名
    rank_2_card=(await V.selecting(s1_list[1][0],ggid,"s3"))[0]
    rank_2_card=rank_2_card
    if rank_2_card == 0:
        rank_2_card="锟斤拷"
    b="2.【"+str(rank_2_card)+"】"+str(s1_list[1][1])+"次"
    #第三名
    rank_3_card=(await V.selecting(s1_list[2][0],ggid,"s3"))[0]
    rank_3_card=rank_3_card
    if rank_3_card == 0:
        rank_3_card="锟斤拷"
    c="3.【"+str(rank_3_card)+"】"+str(s1_list[2][1])+"次"
    #如果排名为前1,2,3,4名，则展示前五
    if index_u in [0,1,2,3,4]:
        #第四名
        rank_4_card=(await V.selecting(s1_list[3][0],ggid,"s3"))[0]
        rank_4_card=rank_4_card
        if rank_4_card == 0:
            rank_4_card="锟斤拷"
        d="4.【"+str(rank_4_card)+"】"+str(s1_list[3][1])+"次"
        #第五名
        rank_5_card=(await V.selecting(s1_list[4][0],ggid,"s3"))[0]
        rank_5_card=rank_5_card
        if rank_5_card == 0:
            rank_5_card="锟斤拷"
        e="5.【"+str(rank_5_card)+"】"+str(s1_list[4][1])+"次"
        #如果排名为1,2,3,4名
        if index_u in [0,1,2,3]:
            msg_2=["text",_n+a+_n+b+_n+c+_n+d+_n+e]
        elif index_u in [4]:
            rank_6_card=(await V.selecting(s1_list[5][0],ggid,"s3"))[0]
            rank_6_card=rank_6_card
            if rank_6_card == 0:
                rank_6_card="锟斤拷"
            f="6.【"+str(rank_6_card)+"】"+str(s1_list[5][1])+"次"
            msg_2=["text",_n+a+_n+b+_n+c+_n+d+_n+e+_n+f]
        msg_0={"msg":[["reply",str(mid)],msg_1,msg_2],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    elif index_u!=-1:
        #第n-1名且不同分
        for i in range(index_u+1):
            if s1_list[i][1]==s1_list[index_u][1]:
                index_ud=i-1
                break
            elif i==index_u:
                index_ud=index_u-1
                break
        rank_4_card=(await V.selecting(s1_list[index_ud][0],ggid,"s3"))[0]
        rank_4_card=rank_4_card
        if rank_4_card == 0:
            rank_4_card="锟斤拷"
        d=str(index_ud+1)+".【"+str(rank_4_card)+"】"+str(s1_list[index_ud][1])+"次"
        #第n名
        rank_5_card=(await V.selecting(s1_list[index_u][0],ggid,"s3"))[0]
        rank_5_card=rank_5_card
        if rank_5_card == 0:
            rank_5_card="锟斤拷"
        e=str(index_u+1)+".【"+str(rank_5_card)+"】"+str(s1_list[index_u][1])+"次"
        #第n+1名
        if index_u+1!=len(s1_list):
            rank_6_card=(await V.selecting(s1_list[index_u+1][0],ggid,"s3"))[0]
            rank_6_card=rank_6_card
            if rank_6_card == 0:
                rank_6_card="锟斤拷"
            f=str(index_u+2)+".【"+str(rank_6_card)+"】"+str(s1_list[index_u+1][1])+"次"
            msg_2=["text",_n+a+_n+b+_n+c+_n+"······"+_n+d+_n+e+_n+f]
        else:
            msg_2=["text",_n+a+_n+b+_n+c+_n+"······"+_n+d+_n+e]
        msg_0={"msg":[["reply",str(mid)],msg_1,msg_2],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    else:
        msg_1=["text","( 〞 0 ˄ 0 )错误代码：E-2。\n店长被抽中次数为0！"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)  

async def marry_wife(bot, event,matcher,stamp,id,iden):
    print("DEF:marry_wife")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.raw_message)


    if msg_raw!="娶群老婆":
        no=re.findall("[0-9]{1,11}",msg_raw)
    else:
        msg_1=["text","( 〞 0 ˄ 0 )错误代码：E5-1_n_请加上艾特对象！"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
        await matcher.finish()

    uid_a=int(no[0])
    puid_a="P"+str(uid_a)

    #获取娶群老婆时间戳
    t3=(await V.selecting(uid,ggid,"t3"))[0]
    if t3<=stamp[2]:
        if (await V.selecting(uid_a,ggid,"user_id"))[0]:
            #获取数字1昵称（本人）
            s3=(await V.selecting(uid,ggid,"s3"))[0]
            if s3!=0:
                card=s3
            else:
                card="锟斤拷"
            #获取数字2昵称（对象）
            s3_a=(await V.selecting(uid_a,ggid,"s3"))[0]
            if s3_a!=0:
                card_a=s3_a
            else:
                card_a="锟斤拷"
            #======== 
            #回复的消息
            urllib.request.urlretrieve("http://q1.qlogo.cn/g?b=qq&nk="+str(uid)+"&s=100","img.png")
            urllib.request.urlretrieve("http://q1.qlogo.cn/g?b=qq&nk="+str(uid_a)+"&s=100","img_a.png")
            img=Image.open("img.png")
            imgcopy=img.copy()
            img_a=Image.open("img_a.png")
            img_acopy=img_a.copy()
            img_white=Image.open(FP+"/tea/img_white.png")
            img_white.paste(imgcopy,(0,0))
            img_white.paste(img_acopy,(100,0))
            img_white.save(FP+"/tea/img_white.png")
            img_save="file:///"+FP+"/tea/img_white.png"
            if int(uid)==int(uid_a):
                msg_1=["text","~婚礼现场~"]
                msg_2=["image",img_save]
                if stamp[0]%2==0 or 1:
                    msg_3=["text","(*ﾟーﾟ)自己娶自己是什么操作啦，虽然确实可以这要做就是了。"]
                else:
                    msg_3=["text","(*ﾟ∇ﾟ)祝【店长】的头像角色会成为你真正的老婆~"]
                msg_0={"msg":[["reply",str(mid)],msg_1,msg_2,msg_3],"type":"G"}    
            else:
                msg_1=["text","~婚礼现场~"]
                msg_2=["image",img_save]
                msg_3=["text","(*ﾟ∇ﾟ)祝【"+str(card)+"】和【"+str(card_a)+"】百年好合~"]
                msg_0={"msg":[["reply",str(mid)],msg_1,msg_2,msg_3],"type":"G"}
            await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
            #========
            #写入抽中次数
            s1_a=(await V.selecting(uid_a,ggid,"s1"))[0]
            await V.update(uid_a,ggid,"s1",s1_a+1)
            #写入时间戳
            await V.update(uid,ggid,"t3",stamp[2]+30)

        else:
            msg_1=["text","( 〞 0 ˄ 0 )错误代码：E5-2_n_对象不在此群中！"]
    else:
        last_time=t3-stamp[2]
        msg_1=["text","( ｣ﾟДﾟ)｣＜还在转cd，"+_n+"冷却时间"+str(last_time)+"分！"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        tea_data=await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
        




async def random_wife_ten(bot, event,matcher,stamp,id,iden):
    print("DEF:random_wife")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)

    if not gid:
        await matcher.finish()

    t2=(await V.selecting(uid,ggid,"t2"))[0]

    if t2<=stamp[2]:#判断时间戳

        #确定群总人数
        with open(FP+"/tea/group/"+str(gid)+".json","r",encoding='utf-8') as group_a_json:
            group_a=json.load(group_a_json)
            group_a_json.close()
        member_count=len(group_a["info"])

        #确定加群后的活跃人数
        t4_u=await V.execute("select user_id,t4 from "+ggid+" where t4>0 order by t4 desc")
        t4=[]
        for row in t4_u:
            t4.append(row)
        activity_count=len(t4)
        #T4的结构：[(uid1,stamp1),(uid2,stamp2)``````]
        #确认当前群总人数，若小于50人取总人数，若50~500取50人，大于500人取十分之一。
        if member_count<=50:
            count=member_count
        elif member_count<=500:
            count=50
        elif member_count>500:
            count=member_count//10 
        #确认已录入时间戳总人数，若时间戳总人数小于当前群过滤人数，取时间戳，否则取过滤人数。
        if count<=activity_count:
            count=count
        elif count>activity_count:
            count=activity_count

        #将up池和随机池总和。
        #这段是随机池
        x=[]
        if count>=1:
            for i in range(count):
                x.append(t4[i][0])
        else:
            await matcher.finish()
        #这段是up池
        y=[]
        if count>=1:
            for i in t4:
                if i[1]+10800>=stamp[0]:
                    for j in range(3):
                        y.append(i[0])
                elif i[1]+21600>=stamp[0]:
                    for j in range(2):
                        y.append(i[0])
                elif i[1]+43200>=stamp[0]:
                    for j in range(1):
                        y.append(i[0])
                else:
                    break
        else:
            print("await matcher.finish()")
            await matcher.finish()
        z=len(x)+len(y)
        #确认初始种子
        seed=stamp[1]+uid
        msg_4=_n
        for i in range(10):
            #确认该循环种子
            random.seed(seed)
            #随便抽一个。重复十遍。
            ranpond=random.randint(1,z)
            #修改种子
            seed+=23
            if ranpond<=len(y):
                ranwife=random.choice(y)
            else:
                ranwife=random.choice(x)
            #增加数字1次数
            s1_a=(await V.selecting(ranwife,ggid,"s1"))[0]
            await V.update(ranwife,ggid,"s1",s1_a+1)
            #修改时间戳
            await V.update(uid,ggid,"t2",stamp[2]+45)#为测试改为1秒注意！
            #发送消息
            s3_a=(await V.selecting(ranwife,ggid,"s3"))[0]
            if s3_a==0:
                s3_a="锟斤拷"
            if ranpond<=len(y):
                msg_4+="[UP!]【"+str(s3_a)+"】"+_n
            else:
                msg_4+="【"+str(s3_a)+"】"+_n
            


        #发送消息
        msg_1=["text","今天你亲爱的群老婆是："]
        msg_2=["text",msg_4]
        msg_3=["text","这十个哒！"]     
        msg_0={"msg":[["reply",str(mid)],msg_1,msg_2,msg_3],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    else:
        last_time=(await V.selecting(uid,ggid,"t2"))[0]-stamp[2]
        msg_1=["text","( ｣ﾟДﾟ)｣＜还在转cd，"+_n+"冷却时间"+str(last_time)+"分！"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)


async def random_wife(bot, event,matcher,stamp,id,iden):
    print("DEF:random_wife")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)

    if not gid:
        await matcher.finish()

    t1=(await V.selecting(uid,ggid,"t1"))[0]

    if t1<=stamp[0]:#判断时间戳

        #确定群总人数
        with open(FP+"/tea/group/"+str(gid)+".json","r",encoding='utf-8') as group_a_json:
            group_a=json.load(group_a_json)
            group_a_json.close()
        member_count=len(group_a["info"])

        #确定加群后的活跃人数
        t4_u=await V.execute("select user_id,t4 from "+ggid+" where t4>0 order by t4 desc")
        t4=[]
        for row in t4_u:
            t4.append(row)
        activity_count=len(t4)
        #T4的结构：[(uid1,stamp1),(uid2,stamp2)``````]
        #确认当前群总人数，若小于50人取总人数，若50~500取50人，大于500人取十分之一。
        if member_count<=50:
            count=member_count
        elif member_count<=500:
            count=50
        elif member_count>500:
            count=member_count//10 
        #确认已录入时间戳总人数，若时间戳总人数小于当前群过滤人数，取时间戳，否则取过滤人数。
        if count<=activity_count:
            count=count
        elif count>activity_count:
            count=activity_count

        #将up池和随机池总和。
        #这段是随机池
        x=[]
        if count>=1:
            for i in range(count):
                x.append(t4[i][0])
        else:
            await matcher.finish()
        #这段是up池
        y=[]
        if count>=1:
            for i in t4:
                if i[1]+10800>=stamp[0]:
                    for j in range(3):
                        y.append(i[0])
                elif i[1]+21600>=stamp[0]:
                    for j in range(2):
                        y.append(i[0])
                elif i[1]+43200>=stamp[0]:
                    for j in range(1):
                        y.append(i[0])
                else:
                    break
        else:
            print("await matcher.finish()")
            await matcher.finish()
        #随便抽一个。
        z=len(x)+len(y)
        ranpond=random.randint(1,z)
        if ranpond<=len(y):
            ranwife=random.choice(y)
        else:
            ranwife=random.choice(x)
        #增加数字1次数
        s1_a=(await V.selecting(ranwife,ggid,"s1"))[0]
        await V.update(ranwife,ggid,"s1",s1_a+1)
        #修改时间戳
        await V.update(uid,ggid,"t1",stamp[0]+300)#为测试改为1秒注意！
        #发送消息
        img="http://q1.qlogo.cn/g?b=qq&nk="+str(ranwife)+"&s=100"
        puid_a="P"+str(ranwife)
        ranwife_nickname=""
        s3_a=(await V.selecting(ranwife,ggid,"s3"))[0]
        if s3_a==0:
            s3_a="锟斤拷"
        

        #发送消息
        msg_1=["text","今天你亲爱的群老婆是："]
        msg_2=["image",img]
        if ranpond<=len(y):
            msg_3=["text","[UP!]【"+str(s3_a)+"】("+str(ranwife)+")哒！"]
        else:
            msg_3=["text","【"+str(s3_a)+"】("+str(ranwife)+")哒！"]       
        msg_0={"msg":[["reply",str(mid)],msg_1,msg_2,msg_3],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    else:
        last_time=(await V.selecting(uid,ggid,"t1"))[0]-stamp[0]
        msg_1=["text","( ｣ﾟДﾟ)｣＜还在转cd，"+_n+"冷却时间"+str(last_time)+"秒！"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)


