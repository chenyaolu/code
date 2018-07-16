# -*- coding:utf-8 -*-
import model as md
from datetime import datetime

result_details = md.modeling()

def format_print(rank_item,rank):#输出格式的定义
    real_item = rank_item[1]
    recommend_index = int((real_item["recommend_score"]/0.5)*100)
    uncertainty_index = int((real_item["uncertainty_score"]/0.4)*100)
    goal_index = int((real_item["goal_score"]/0.4)*100)
    fame_index = int((real_item["fame_score"] / 0.8) * 100)
    print("====比赛场次推荐====")
    print("推荐排名：%d" %(rank))
    print("%s vs %s" %(real_item["team_a"],real_item["team_b"]))
    print("综合推荐指数：%d"%recommend_index)
    print("悬念指数：%d" %uncertainty_index)
    print("比分指数：%d" %goal_index)
    print("球星指数：%d" % fame_index)

'''
def ranking(result_details):
    #按照推荐分数降序排序
    #print(result_details.items())
    ranking_list = sorted(result_details.items(),key=lambda item:item[1]["recommend_score"],reverse=True)
    index = 0
    for i in ranking_list:
        index +=1
        format_print(i,index)
'''
def ranking_by_type(result_details,type="recommend",need_print=True):
    #print(result_details.items())
    key_dict = {"fame":"fame_score","goal":"goal_score",
                "uncertainty":"uncertainty_score","recommend":"recommend_score"}
    if type not in key_dict.keys():
        print("没有合适的类型！")
        return 0
    type_value = key_dict[type]
    ranking_list = sorted(result_details.items(), key=lambda item: item[1][type_value], reverse=True)
    index = 0
    for i in ranking_list:
        index += 1
        if need_print:
            format_print(i, index)
    return  ranking_list

def get_certain_ranking(result_details,ty,num):
    ranklist = ranking_by_type(result_details,ty,False)
    rank_num = num-1
    format_print(ranklist[rank_num],num)
    return ranklist[rank_num]

def get_certain_date(result_details,date_str):
    #获取当天所有的场次
    new_results = dict()
    for index,item in enumerate(result_details.values()):
        time = item["match_date"]
        time_str = time.strftime("%Y-%m-%d")
        if (date_str == time_str):
            new_results[str(index)] = item
    if (len(new_results.values()) == 0):
        print("当天没有比赛！")
        return 0

    ranking_by_type(new_results)

    #排序
    #打印输出

def main():
    ranking(result_details)


if __name__ == '__main__':
    main()