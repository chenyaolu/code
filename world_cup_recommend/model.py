# -*- coding:utf-8 -*-
import data_parser as dp
import math
from datetime import datetime

def get_team_info(team_info,team_name):#得到排名和简称
    for team in team_info:
        if team["Name"] == team_name:
            return int(team["Rank"]),team["Code"]

def get_match_umcertainty(match,rank_a,rank_b):#计算uncertainty，得到悬念大小的计算
    rank_diff = abs(rank_a-rank_b)
    odds_win,odds_draw,odds_lose = float(match["Odds Win"]),float(match["Odds Draw"]),float(match["Odds Lose"])
    avg_odds = (odds_win+odds_draw+odds_lose)/3
    std_odds = math.sqrt( ((odds_win-avg_odds)**2 +(odds_draw-avg_odds)**2 + (odds_lose-avg_odds)**2 )/3)
    uncertainty = 0.5*1/rank_diff + 0.5*1/(1+std_odds)
    return uncertainty

def get_match_goals(history_matches,team_a,team_b):#计算进球期望，进球越多越好
    matches_a,matches_b =0,0
    scores_a,scores_b = 0,0
    for match in history_matches:
        if match["Home Team"] == team_a or match["Away Team"] == team_a:
            matches_a += 1
            scores_a += int(match["Score Home"]) + int(match["Score Away"])
        if match["Home Team"] == team_b or match["Away Team"] == team_b:
            matches_b += 1
            scores_b += int(match["Score Home"]) + int(match["Score Away"])
    goals_exp = 0.5*scores_a/(matches_a*90) + 0.5*scores_b/(matches_b*90)
    return goals_exp*10

def get_match_fame(squads,code_a,code_b):
    fame_a,fame_b=0,0
    for player in squads:
        player_post_count = player["Instagram Posts"]
        player_fans_count = player["Instagram Fans"]
        if player["Nation"] == code_a:
            fame_a += get_player_fame_bonus(player_post_count) * get_player_fame_lvl(player_fans_count)
        if player["Nation"] == code_b:
            fame_b += get_player_fame_bonus(player_post_count) * get_player_fame_lvl(player_fans_count)
    match_fame = 0.5*fame_a + 0.5*fame_b
    return match_fame/100

def get_player_fame_bonus(post_count):
    post_count = int(post_count)
    if post_count<100:
        return 1
    elif post_count<500:
        return 1.1
    elif post_count<1000:
        return 1.2
    else:
        return 1.3

def get_player_fame_lvl(fans_count):
    fans_count = int(fans_count)
    if fans_count < 10000:
        return 1
    elif fans_count < 1e5:
        return 2
    elif fans_count < 1e6:
        return 5
    elif fans_count < 1e7:
        return 10
    elif fans_count < 50000000:
        return 20
    else:
        return 50

def format_date(date,time): #输出标准化的日期
    month = int(date.split(".")[0])
    day = int(date.split(".")[1])
    hour = int(time.split(":")[0])
    minute = int(time.split(":")[1])
    return datetime(year=2018,month=month,day=day,hour=hour,minute=minute)

def modeling():
    #导入数据
    parser_history_match = dp.data_clean("source_data/history_matches.csv")
    parser_squads = dp.data_clean("source_data/squads.csv")
    parser_team_info = dp.data_clean("source_data/team_info.csv")
    parser_wc_group_matches = dp.data_clean("source_data/wc_group_matches.csv")

    match_details = dict()

    for match in parser_wc_group_matches:
        result_map = dict()
        #获取比赛的基本信息
        match_id = match["No."]
        match_date = format_date(match["Date"],match["Time"])#比赛时间
        team_a,team_b = match["TeamA"],match["TeamB"]
        rank_a,code_a = get_team_info(parser_team_info,team_a)
        rank_b,code_b = get_team_info(parser_team_info, team_b)

        uncertainty_score = get_match_umcertainty(match,rank_a,rank_b)#悬念
        goal_score = get_match_goals(parser_history_match,team_a,team_a)#进球期望
        fame_score = get_match_fame(parser_squads,code_a,code_b)#球员知名度

        #print(match_id + " " + team_a + "  vs  " + team_b + ":")
        #print("uncertainty score:%.2f" % uncertainty_score)
        #print("goal_score:%.2f" % goal_score)
        #print("fame_score:%.2f" % fame_score)

        #生成比赛推荐结果,首先是整理数据
        recommend_score = (uncertainty_score+goal_score+fame_score)/3
        #保存数据
        result_map["match_id"] = match_id
        result_map["team_a"] = team_a
        result_map["team_b"] = team_b
        result_map["uncertainty_score"] = uncertainty_score
        result_map["goal_score"] = goal_score
        result_map["fame_score"] = fame_score
        result_map["recommend_score"] = recommend_score
        result_map["match_date"] = match_date #加入时间

        match_details[match_id] = result_map

    return match_details

if __name__ == '__main__':
    modeling()