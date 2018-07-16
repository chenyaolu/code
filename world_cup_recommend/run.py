# -*- coding:utf-8 -*-
import model as md
import data_exporter as de
from datetime import datetime

HELP_MSG = '''
    请输入：
    1.help - 获取帮助信息
    2.ranking - 获取所有排名
    3.select{type}{num} - 获取第num位的type类型排名，其中type=uncertainty/goal/fame
    4.ranking type {type} - 获取分类排名
    5.date {date} - 获取某天的推荐信息，默认为当天
'''
def help():
    print(HELP_MSG)

def  key_word_handler(str):
    str = str.strip()
    if str == "help":
        help()
    elif str == "ranking":
        de.ranking_by_type(md.modeling())
    elif str.startswith("ranking type"):
        ty = str.split(" ")[2]
        de.ranking_by_type(md.modeling(),ty)
    elif str.startswith("select "):
        ty = str.split(" ")[1]
        num = int(str.split(" ")[2])
        de.get_certain_ranking(md.modeling(),ty,num)
    elif str.startswith("date"):
        if(str == "date" or str.strip() == "date" ):
            print("获取当天日期:"+datetime.now().strftime("%Y-%m-%d"))
            de.get_certain_date(md.modeling(), datetime.now().strftime("%Y-%m-%d"))
        else:
            date_str = str.split(" ")[1]
            print("您输入的时间是:%s" %date_str)
            de.get_certain_date(md.modeling(),date_str)

    else:
        print("输入错误，请重新输入！")

def main():
    print(HELP_MSG)
    while True:
        str = input("请输入命令：")
        key_word_handler(str)

if __name__ == '__main__':
    main()
