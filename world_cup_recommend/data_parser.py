# -*- coding:utf-8 -*-
import csv
#以下整理数据
def data_clean(path):
    list = []
    file = open(path, "r+", encoding='UTF-8')  # 读入数据
    lines = csv.DictReader(file)
    for line in lines:
        list.append(dict(line))  # 整理成字典，加入列表
    return list
'''
def parser_history_match(): #读取数据，整理数据以待使用
    list = []
    match_file_path = "source_data/history_matches.csv"#获取数据路径
    file = open(match_file_path,"r+",encoding='UTF-8')#读入数据
    lines = csv.DictReader(file)
    for line in lines:
        list.append(dict(line))#整理成字典，加入列表
    return list

def parser_squads():
    list = []
    match_file_path = "source_data/squads.csv"  # 获取数据路径
    file = open(match_file_path, "r+", encoding='UTF-8')  # 读入数据
    lines = csv.DictReader(file)
    for line in lines:
        list.append(dict(line))  # 整理成字典，加入列表
    return list

def parser_team_info():
    list = []
    match_file_path = "source_data/team_info.csv"  # 获取数据路径
    file = open(match_file_path, "r+", encoding='UTF-8')  # 读入数据
    lines = csv.DictReader(file)
    for line in lines:
        list.append(dict(line))  # 整理成字典，加入列表
    return list

def parser_wc_group_matches():
    list = []
    match_file_path = "source_data/wc_group_matches.csv"  # 获取数据路径
    file = open(match_file_path, "r+", encoding='UTF-8')  # 读入数据
    lines = csv.DictReader(file)
    for line in lines:
        list.append(dict(line))  # 整理成字典，加入列表
    return list
'''
def main():
    parser_history_match = data_clean("source_data/history_matches.csv")
    parser_squads = data_clean("source_data/squads.csv")
    parser_team_info = data_clean("source_data/team_info.csv")
    parser_wc_group_matches = data_clean("source_data/wc_group_matches.csv")

if __name__ == '__main__':
    main()
