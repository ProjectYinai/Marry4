
import json
import random
import re
import time
import urllib
import os
import math
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

#==========
#好感度等级查询

async def tea_time(bot, event,matcher,stamp,id,iden):
    print("CODE:A")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)

    #获取泡茉莉对话
    a_cup_of_marry=message_read_def("A1")
    favour=await favour_def(bot, event, matcher,stamp,id)

    if msg_raw=="泡茉莉":#泡茉莉随机选择
        dict_kind=a_cup_of_marry["kinds_of_tea"]
        list_kind=list(dict_kind)
        kind_key=random.choice(list_kind)
        kind=dict_kind[kind_key]
        await a_cup_of_tea(bot, event,matcher,stamp,id,iden,favour,kind)
    elif msg_raw in a_cup_of_marry["kinds_of_tea"]:#泡茶指定选择
        kind=a_cup_of_marry["kinds_of_tea"][msg_raw]
        await a_cup_of_tea(bot, event,matcher,stamp,id,iden,favour,kind)
    #打招呼
    greeting=["午夜好","凌晨好","清晨好","早上好","中午好","下午好","黄昏好","晚上好","晚安"]
    if msg_raw in greeting:
        await marry_greet(bot, event,matcher,stamp,id,iden,favour)
    #更改自定义昵称
    if re.search("茉莉以后叫我",msg_raw) or re.search("茉莉请叫我",msg_raw) or re.search("茉莉叫我",msg_raw):
        await custom_nickname(bot, event,matcher,stamp,id,iden,favour)
    #我的好感度
    if msg_raw in ["我的好感度","红茶浓度"]:
        await tea_concentration(bot, event,matcher,stamp,id,iden,favour)


async def template(bot, event,matcher,tea_data,stamp,id,favour,iden):
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)

    msg_1=["text","(*ﾟーﾟ)"]
    msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
    await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)

async def tea_concentration(bot, event,matcher,stamp,id,iden,favour):
    print("DEF:tea_concentration")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)


    favor=(await V.selecting(uid,"G5000","a2"))[0]
    msg_1=["text","["+favour[2]+"]_n_"]
    msg_2=["text","茉莉对店长大人的好感度超级大呢！"+_n+"大概"+str(favor)+"点吧ww~~"+_n+"[更详细的内容跟茉莉加好友后会偷偷发给店长呢ww~]"]
    msg_0={"msg":[["reply",str(mid)],msg_1,msg_2],"type":"G"}
    await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)

    if iden[0]:
       
        favor=(await V.selecting(uid,"G5000","a2"))[0]
        cups=(await V.selecting(uid,"G5000","a7"))[0]
        plays=(await V.selecting(uid,"G5000","a8"))[0]
        days=(await V.selecting(uid,"G5000","a6"))[0]
        days=stamp[4]-days


        msg_1=["text","一杯红茶，溶入"+str(favor)+"点互相的爱慕；一吮香甜，回想"+str(cups)+"杯红茶的时光。点燃引路之灯，见证"+str(plays)+"次欢乐的笑容；牵引系心之线，忆起"+str(days)+"天前相遇的过往。至此，感谢【店长】的陪伴！"]
        msg_0={"msg":[msg_1],"type":"P"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)



async def custom_nickname(bot, event,matcher,stamp,id,iden,favour):
    print("DEF:custom_nickname")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)

    msg_raw=msg_raw.replace("茉莉以后叫我","")
    msg_raw=msg_raw.replace("茉莉请叫我","")
    msg_raw=msg_raw.replace("茉莉叫我","")

    if not iden[0]:
        msg_1=["text","(*ﾟーﾟ)抱歉，【店长】需要先和茉莉加好友才能使用自定义昵称呢~"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
        return()
    
    if msg_raw!="":
        stamp_cn=(await V.selecting(uid,"G5000","b12"))[0]
        if msg_raw=="茉莉" or msg_raw=="三色仮茉莉":#如果叫茉莉
            msg_1=["text","(*ﾟーﾟ)如果【店长】是茉莉，那茉莉是谁呢······"]
            msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
            await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)

        elif len(msg_raw)>=16:#如果字符超出
            msg_1=["text","(*ﾟーﾟ)店长的名字太长啦，稍微改短一点吧~"]
            msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
            await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)

        elif stamp_cn<=stamp[2] and len(msg_raw)<15:
            #发送群消息
            msg_1=["text","(*ﾟ∇ﾟ)明白啦，审核成功后茉莉就叫店长【"+msg_raw+"】了哦~"]
            msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
            await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
            #更改临时自定义昵称
            await V.update_text(uid,"G5000","a5",msg_raw)
            #修改时间戳
            await V.update(uid,"G5000","b12",stamp[2]+480)
            #发送教学群通知
            msg_SP=""
            msg_SP+="申请人QQ："+str(uid)+_n
            msg_SP+="申请所在群："+str(gid)+_n
            msg_SP+="申请昵称："+msg_raw
            await bot.send_group_msg(group_id=teach_g,message=msg_SP)
            time.sleep(1)
            msg_SP=""
            msg_SP+="/同意昵称"+str(uid)+" "+str(random.randint(1000,9999))
            await bot.send_group_msg(group_id=teach_g,message=msg_SP)
            
        else:
            msg_1=["text","(*ﾟーﾟ)店长更改昵称的冷却时间还没好呢，还剩"+str(stamp_cn-stamp[2])+"分钟！"]
            msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
            await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    else:
        msg_1=["text","(*ﾟ∇ﾟ)茉莉已经将店长的自定义昵称重置啦~如果想再次更改茉莉对店长的称呼，请告诉茉莉哦ww~"]
        msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
        await V.update(uid,"G5000","a4",0)

async def marry_greet(bot, event,matcher,stamp,id,iden,favour):
    print("DEF:marry_greet")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.raw_message)
    no=re.findall("[0-9]{1,11}",msg_raw)
    span=["凌晨好","清晨好","早上好","中午好","下午好","黄昏好","晚上好","午夜好","晚安"]


    #确认当前时间段
    quantum=[]
    if int(stamp[-4])==1 or int(stamp[-4])==2 or int(stamp[-4])==3 or int(stamp[-4])==4:
        quantum.append(2)#凌晨
    if int(stamp[-4])==4 or int(stamp[-4])==5 or int(stamp[-4])==6 or int(stamp[-4])==7:
        quantum.append(3)#清晨
    if int(stamp[-4])==7 or int(stamp[-4])==8 or int(stamp[-4])==9 or int(stamp[-4])==10:
        quantum.append(4)#早上
    if int(stamp[-4])==10 or int(stamp[-4])==11 or int(stamp[-4])==12 or int(stamp[-4])==13:
        quantum.append(5)#中午
    if int(stamp[-4])==13 or int(stamp[-4])==14 or int(stamp[-4])==15 or int(stamp[-4])==16:
        quantum.append(6)#下午
    if int(stamp[-4])==16 or int(stamp[-4])==17 or int(stamp[-4])==18 or int(stamp[-4])==19:
        quantum.append(7)#黄昏
    if int(stamp[-4])==19 or int(stamp[-4])==20 or int(stamp[-4])==21 or int(stamp[-4])==22:
        quantum.append(8)#晚上
    if int(stamp[-4])==22 or int(stamp[-4])==23 or int(stamp[-4])==0 or int(stamp[-4])==1:
        quantum.append(9)#午夜
    if int(stamp[-4])>=19 or int(stamp[-4])<=4:
        quantum.append(10)#晚安


    #刷新今日早上好次数
    stamp_gr=(await V.selecting(uid,"G5000","b11"))[0]
    if stamp_gr!=stamp[4]:
        for i in range(11):
            if i >=2:
                await V.update(uid,"G5000","b"+str(i),0)
        await V.update(uid,"G5000","b11",stamp[4])
        await V.update(uid,"G5000","a10",0)

    code=span.index(msg_raw)+2
    times_gr=(await V.selecting(uid,"G5000","b"+str(code)))[0]
    times=(await V.selecting(uid,"G5000","a10"))[0]
    if code in quantum:#如果当前时段匹配
        A2=message_read_def("A2")
        type=A2["greeting_"+str(code)]["type"]
        msg_g=A2["greeting_"+str(code)]["group"]
        message=A2["greeting_"+str(code)]["message"]
        if times_gr==0:
            #确定增加好感度量
            if times<=1:
                pointA=random.randint(12,20)
                msg_3="[好感度+"+str(pointA)+"]"
            else:
                pointA=0
                msg_3="今天聊得真开心呢ww~"
            #发送群消息
            msg_1="["+favour[2]+"]_n_"
            msg_2="(*ﾟ∇ﾟ)【店长】"+type+"呢ww~_n_"
            msg_0=["text",msg_1+msg_2+msg_3]
            msg_0={"msg":[["reply",str(mid)],msg_0],"type":"G"}
            await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
            #发送私聊消息
            msg_1=[]
            NSW=["normalN"]
            for i in NSW:
                if len(message[i])!=0:
                    for j in message[i]:
                        msg_1.append(["text",j[0]])
            msg_0=random.choice(msg_1)
            msg_0={"msg":[msg_0],"type":"P"}
            await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
            #增加个人打招呼次数
            a8=(await V.selecting(uid,"G5000","a8"))[0]
            await V.update(uid,"G5000","a8",a8+1)
            #修改时间戳
            a10=(await V.selecting(uid,"G5000","a10"))[0]
            await V.update(uid,"G5000","b"+str(code),1)
            await V.update(uid,"G5000","a10",a10+1)
            #增加好感度
            if times<=1:
                a2=(await V.selecting(uid,"G5000","a2"))[0]
                await V.update(uid,"G5000","a2",a2+pointA)
        else:            
            msg_1=["text","(*ﾟーﾟ)【店长】今天已经说过["+type+"]啦~"]
            msg_0={"msg":[["reply",str(mid)],msg_1],"type":"G"}
            await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)

    else:#如果当前时段不匹配
        #确定当前时段真正的打招呼
        msg_1="(*ﾟーﾟ)【店长】，现在是"
        quantum_a=[]
        for i in quantum:
            if i==2:
                quantum_a.append("[凌晨好]")
            elif i==3:
                quantum_a.append("[清晨好]")
            elif i==4:
                quantum_a.append("[早上好]")
            elif i==5:
                quantum_a.append("[中午好]")
            elif i==6:
                quantum_a.append("[下午好]")
            elif i==7:
                quantum_a.append("[黄昏好]")
            elif i==8:
                quantum_a.append("[晚上好]")
            elif i==9:
                quantum_a.append("[午夜好]")
            elif i==10:
                quantum_a.append("[晚安]")
        if len(quantum_a)==1:
            msg_1+=quantum_a[0]+"的时间呢~"
        elif len(quantum_a)==2:
            msg_1+=quantum_a[0]+"和"+quantum_a[1]+"的时间呢~"
        elif len(quantum_a)==3:
            msg_1+=quantum_a[0]+"、"+quantum_a[1]+"和"+quantum_a[2]+"的时间呢~"
        msg_0=["text",msg_1]
        msg_0={"msg":[["reply",str(mid)],msg_0],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
    

async def a_cup_of_tea(bot, event,matcher,stamp,id,iden,favour,kind):
    print("DEF:a_cup_of_tea")
    uid,gid,mid=id
    puid="P"+str(uid)
    ggid="G"+str(gid)
    msg_raw=str(event.message)
    no=re.findall("[0-9]{1,11}",msg_raw)

    #查询时间戳+返回已泡茉莉
    b1=(await V.selecting(uid,"G5000","b1"))[0]#个人泡茉莉时间戳/时间戳天
    p1=(await V.selecting(1000,"G5000","p1"))[0]#当天泡茉莉总次数
    q1=(await V.selecting(1000,"G5000","q1"))[0]#当天泡茉莉总次数时间戳/时间戳天

    #若为第二天，清空当天泡茉莉次数
    if q1!=stamp[4]:
        
        await V.update(1000,"G5000","p1",0)
        await V.update(1000,"G5000","q1",stamp[4])
    #若今天没泡茶，开始泡茶
    if b1!=stamp[4]:
        #随机好感度
        pointA=random.randint(24,40)
        #查询当天泡茉莉次数
        p1=(await V.selecting(1000,"G5000","p1"))[0]
        
        #获取群聊和私聊消息
        a_cup_of_marry=message_read_def("A1")
        #组织群语言
        msg_1="["+str(favour[2])+"]_n_"
        msg_2=random.choice(a_cup_of_marry[kind]["group"])
        msg_3="_n_[好感度+"+str(pointA)+"|今天的第"+str(p1)+"杯茉莉~]"
        msg_1=msg_1+msg_2+msg_3
        
        if not iden[0]:
            if random.randint(1,12)==1:
                msg_1+=_n+"[tip:和茉莉加好友后会有更多互动哦！]"
        #发送群消息
        msg_0={"msg":[["reply",str(mid)],["text",msg_1]],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
        #========
        #组织私聊消息
        msg_0=[]
        #查天气
        weather_code=int(stamp[3]*stamp[3]*279/562432%10)
        if weather_code<7:
            weather="S"
        else:
            weather="R"
        #查季节
        if stamp[-2]==3 or stamp[-2]==4 or stamp[-2]==5 :
            season="spring"
        elif stamp[-2]==6 or stamp[-2]==7 or stamp[-2]==8 :
            season="summer"
        elif stamp[-2]==9 or stamp[-2]==10 or stamp[-2]==11 :
            season="autumn"
        elif stamp[-2]==12 or stamp[-2]==1 or stamp[-2]==2 :
            season="winter"
        NN="normalN"
        NW="normal"+weather
        SN=season+"N"
        SW=season+weather
        NSW=[NN,NW,SN,SW]
        #查私聊消息
        msg_1=a_cup_of_marry[kind]["message"]
        msg_2=[]
        
        for i in NSW:
            if len(a_cup_of_marry[kind]["message"][i])!=0:
                for j in a_cup_of_marry[kind]["message"][i]:
                    msg_2.append(["text",j[0]])
        #发私聊消息
        msg_0=random.choice(msg_2)
        print(str(msg_0))
        msg_0={"msg":[msg_0],"type":"P"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)

        #========
        #修改时间戳
        b1=(await V.selecting(uid,"G5000","b1"))[0]
        await V.update(uid,"G5000","b1",stamp[4])
        #增加好感度
        a2=(await V.selecting(uid,"G5000","a2"))[0]
        await V.update(uid,"G5000","a2",a2+pointA)
        #增加泡茉莉次数
        a7=(await V.selecting(uid,"G5000","a7"))[0]
        await V.update(uid,"G5000","a7",a7+1)
        #增加当天泡茉莉次数
        await V.update(1000,"G5000","p1",p1+1)
    else:#今天已经喝茶啦~
        '''msg_1="|ω・`)今天【店长】已经喝了茉莉的饮料啦ww~"
        msg_0={"msg":[
            ["reply",str(mid)],
            ["text",msg_1]
        ],
        "type":"G"}'''

        #随机好感度
        #查询当天泡茉莉次数
        p1=(await V.selecting(1000,"G5000","p1"))[0]
        
        #获取群聊和私聊消息
        a_cup_of_marry=message_read_def("A1")
        #组织群语言
        msg_1="["+str(favour[2])+"]_n_"
        msg_2=random.choice(a_cup_of_marry[kind]["group"])
        msg_3="_n_[今天的第"+str(p1)+"杯茉莉~]"
        msg_1=msg_1+msg_2+msg_3
        
        if not iden[0]:
            if random.randint(1,12)==1:
                msg_1+=_n+"[tip:和茉莉加好友后会有更多互动哦！]"
        #发送群消息
        msg_0={"msg":[["reply",str(mid)],["text",msg_1]],"type":"G"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)
        #========
        #组织私聊消息
        msg_0=[]
        #查天气
        weather_code=int(stamp[3]*stamp[3]*279/562432%10)
        if weather_code<7:
            weather="S"
        else:
            weather="R"
        #查季节
        if stamp[-2]==3 or stamp[-2]==4 or stamp[-2]==5 :
            season="spring"
        elif stamp[-2]==6 or stamp[-2]==7 or stamp[-2]==8 :
            season="summer"
        elif stamp[-2]==9 or stamp[-2]==10 or stamp[-2]==11 :
            season="autumn"
        elif stamp[-2]==12 or stamp[-2]==1 or stamp[-2]==2 :
            season="winter"
        NN="normalN"
        NW="normal"+weather
        SN=season+"N"
        SW=season+weather
        NSW=[NN,NW,SN,SW]
        #查私聊消息
        msg_1=a_cup_of_marry[kind]["message"]
        msg_2=[]
        
        for i in NSW:
            if len(a_cup_of_marry[kind]["message"][i])!=0:
                for j in a_cup_of_marry[kind]["message"][i]:
                    msg_2.append(["text",j[0]])
        #发私聊消息
        msg_0=random.choice(msg_2)
        print(str(msg_0))
        msg_0={"msg":[msg_0],"type":"P"}
        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)

        #========
        #增加泡茉莉次数
        a7=(await V.selecting(uid,"G5000","a7"))[0]
        await V.update(uid,"G5000","a7",a7+1)
        #增加当天泡茉莉次数
        await V.update(1000,"G5000","p1",p1+1)

        await W.msg_sent(bot, event,matcher,stamp,id,iden,msg_0)

    




#================================================================

def message_read_def(code):
    with open(FP+"/tea/"+code+".json",'r',encoding='utf-8') as message_json:
        message_read=json.load(message_json)
        message_json.close
    return(message_read)






async def favour_def(bot, event, matcher,stamp,id):
    global tea_data
    uid=id[0]
    gid=id[1]
    mid=id[2]
    ggid="G"+str(gid)
    puid="P"+str(uid)


    a2=await V.selecting(uid,"G5000","a2")
    favor=a2[0]
    if favor <= 0:
        favor=0
        favor_level=0
        favor_text=str(favor_level)
    elif favor>=15360:
        favor_level=(favor-15360)*10//2688+100
        favor_text=str(favor_level)
    elif favor>=12672:
        favor_level=(favor-12672)*10//2432+90
        favor_text=str(favor_level)
    elif favor>=10240:
        favor_level=(favor-10240)*10//2176+80
        favor_text=str(favor_level)
    elif favor>=8064:
        favor_level=(favor-8064)*10//1920+70
        favor_text=str(favor_level)
    elif favor>=6144:
        favor_level=(favor-6144)*10//1664+60
        favor_text=str(favor_level)
    elif favor>=4480:
        favor_level=(favor-4480)*10//1408+50
        favor_text=str(favor_level)
    elif favor>=3072:
        favor_level=(favor-3072)*10//1152+40
        favor_text=str(favor_level)
    elif favor>=1920:
        favor_level=(favor-1920)*10//1152+30
        favor_text=str(favor_level)
    elif favor>=1024:
        favor_level=(favor-1024)*10//896+20
        favor_text=str(favor_level)
    elif favor>=384:
        favor_level=(favor-384)*10//640+10
        favor_text=str(favor_level)
    else:
        favor_level=favor*10//384
        favor_text=str(favor_level)

    
    a4=(await V.selecting(uid,"G5000","a4"))[0]
    if a4=="" or a4=="0" or a4==0:#判断是否有自定义昵称
        s3=(await V.selecting(uid,ggid,"s3"))[0]
        if s3==0:
            card="锟斤拷"
    else:
        s3=a4
    

    if favor_level>=100:
        favor_name="蘑菇酱"
        favor_level_name="Lv."+favor_text+"-"+s3+"牌蘑菇酱"
    elif favor_level>=90:
        favor_name="比自己更加珍贵的存在"
        favor_level_name="Lv."+favor_text+"-比自己更加珍贵的存在"
    elif favor_level>=80:
        favor_name="无法取代的存在"
        favor_level_name="Lv."+favor_text+"-无法取代的存在"
    elif favor_level>=70:
        favor_name="灵魂相连的伴侣"
        favor_level_name="Lv."+favor_text+"-灵魂相连的伴侣"
    elif favor_level>=60:
        favor_name="值得信赖的伙伴"
        favor_level_name="Lv."+favor_text+"-值得信赖的伙伴"
    elif favor_level>=50:
        favor_name="亲密无间的朋友"
        favor_level_name="Lv."+favor_text+"-亲密无间的朋友"
    elif favor_level>=40:
        favor_name="非常要好的朋友"
        favor_level_name="Lv."+favor_text+"-非常要好的朋友"
    elif favor_level>=30:
        favor_name="较为熟悉的朋友"
        favor_level_name="Lv."+favor_text+"-较为熟悉的朋友"  
    elif favor_level>=20:
        favor_name="相互认识的关系"
        favor_level_name="Lv."+favor_text+"-相互认识的关系" 
    elif favor_level>=10:
        favor_name="打过招呼的关系"
        favor_level_name="Lv."+favor_text+"-打过招呼的关系"
    else :
        favor_name="初次见面的关系"
        favor_level_name="Lv."+favor_text+"-初次见面的关系"

    return([favor_level,favor_name,favor_level_name])


