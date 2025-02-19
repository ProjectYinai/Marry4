if not os.path.isfile(FP+"/point/_tea.json"):#普通的初始化
    os.chdir(FP)
    try:
        os.makedirs("point")
    except:
        pass
    file=open(FP+"/point/_tea.json","w")
    file.write("{\"stamp\":0,\"code\":{\"len\":0,\"list\":[\"_tea\"]}}")
    file.close
    to_write={"admin":[2373725901],"mgid":[555679990],"group":[],"stamp":0}
    exit()


with open(FP+"/point/_tea.json","r",encoding='utf-8') as tea_json:
    tea_datum=json.load(tea_json)
    tea_json.close()

files = os.listdir(FP+"/point/")  # 读入文件夹
num_files = len(files)  # 统计文件夹中的文件个数
#A全局变量
#G群变量
#L局部变量
if not num_files==tea_datum["code"]["len"]:
    for i in tea_datum["code"]["list"]:
        if not os.path.isfile(FP+"/point/"+i+".json"):
            file=open(FP+"/point/"+i+".json","w")
            file.write("{\"stamp\":0}")
            file.close
    tea_datum["code"]["len"]=len(tea_datum["code"]["list"])
    with open(FP+"/point/_tea.json","w",encoding='utf-8') as tea_json:
        json.dump(tea_datum,tea_json,indent=1)
        tea_json.close()