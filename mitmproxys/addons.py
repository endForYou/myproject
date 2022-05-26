import json, os
import requests
import csv
import pymysql
import pymysql.cursors

db = pymysql.connect(user="root", password="rYa+wq10dFTWzYz8FeZgsWRygyKfLKULSRdKfRnEgSk=",
                     host="119.91.135.29", port=3306, database="zhiyuan_sd",
                     charset="utf8", autocommit=True)

cursor = db.cursor(pymysql.cursors.DictCursor)

sql = "insert into yzy_enroll_major_score_line_json_hn(url,json_data,params,province,collegeName) values (%s,%s,%s,%s,%s)"
college_sql = "insert into yzy_college_json_2022_new(url,json_data,params,province) values (%s,%s,%s,%s)"

# college_sql = """
# insert into yzy_college_2022(categories,college_name,belong,provinceName,cityName,code,gbCode,ranking,rankingOfEdu,
# rankingOfQS,rankingOfRK,rankingOfUSNews,rankingOfWSL,rankingOfXYH,eduLevel,features,natureType
# ) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
# """
# major_score_line_csv = path + "/湖南专业分数线.csv"
# major_score_line_out = open(major_score_line_csv, "a", newline="", encoding="utf-8")
# major_score_line_write = csv.writer(major_score_line_out, dialect='excel')
#
# college_score_line_csv = path + "/湖南院校分数线.csv"
# college_score_line_out = open(college_score_line_csv, "a", newline="", encoding="utf-8")
# college_score_line_write = csv.writer(college_score_line_out, dialect='excel')

province = "湖南"


def response(flow):
    enroll_plan_url = 'https://uwf4ce19ca8fcd150a4.youzy.cn/youzy.dms.datalib.api.enrolldata.plan.query'

    major_score_line_url = 'https://uwf4ce19ca8fcd150a4.youzy.cn/youzy.dms.datalib.api.enrolldata.enter.profession.v2.get'
    college_score_line_url = 'https://uwf4ce19ca8fcd150a4.youzy.cn/youzy.dms.datalib.api.enrolldata.enter.college.v2.get'
    college_url = 'https://uwf4ce19ca8fcd150a4.youzy.cn/youzy.dms.basiclib.api.college.query'
    college_detail_url = 'https://uwf4ce19ca8fcd150a4.youzy.cn/youzy.dms.basiclib.api.college.bycode.get'

    college_rank_url = 'https://uwf7de983aad7a717eb.youzy.cn/youzy.dms.basiclib.api.college.ranking.byyear.query'

    # 筛选出以上面url为开头的url
    # print(flow.request)

    text = ""
    params = ""
    collegeName = ""
    # print(flow.request.get_text())
    if flow.request.url.startswith(major_score_line_url):

        print(major_score_line_url)

        text = flow.response.text
        params = flow.request.get_text()
        s = json.loads(text)
        if not s['result']['professionFractions']:
            collegeName = None
        else:
            collegeName = s['result']['professionFractions'][0]['professions'][0]['collegeName']
        try:
            cursor.execute(sql, (major_score_line_url, text, params, province, collegeName))
        except BaseException:
            db1 = pymysql.connect(user="root", password="rYa+wq10dFTWzYz8FeZgsWRygyKfLKULSRdKfRnEgSk=",
                                  host="119.91.135.29", port=3306, database="zhiyuan_sd",
                                  charset="utf8", autocommit=True)
            cursor1 = db1.cursor(pymysql.cursors.DictCursor)
            cursor1.execute(sql, (major_score_line_url, text, params, province, collegeName))
    elif flow.request.url.startswith(college_detail_url):
        pass
        # print(college_detail_url)

        # text = flow.response.text
        # params = flow.request.get_text()
        # cursor.execute(college_sql, (college_detail_url, text, params, province))
    elif flow.request.url.startswith(college_rank_url):
        pass
        # text = flow.response.text
        # params = flow.request.get_text()
        # myprovince=None
        # cursor.execute(college_sql, (college_rank_url, text, params, myprovince))
    elif flow.request.url.startswith(college_url):
        pass
        # print(college_url)
        # text = flow.response.text
        # params = flow.request.get_text()
        # try:
        #     cursor.execute(college_sql, (college_url, text, params, province))
        # except BaseException:
        #     db1 = pymysql.connect(user="root", password="rYa+wq10dFTWzYz8FeZgsWRygyKfLKULSRdKfRnEgSk=",
        #                           host="119.91.135.29", port=3306, database="zhiyuan_sd",
        #                           charset="utf8", autocommit=True)
        #     cursor1 = db1.cursor(pymysql.cursors.DictCursor)
        #     cursor1.execute(college_sql, (url, text, params, province))

        # print(text)
        # 将已经编码的json字符串解码为python对象
        # enroll_plan_write.writerow([enroll_plan_url, text])
        # print(text)
    # elif flow.request.url.startswith(major_score_line_url):
    #     print(major_score_line_url)
    #     url = major_score_line_url
    #     text = flow.response.text
    #     params = flow.request.get_text()
    # elif flow.request.url.startswith(college_score_line_url):
    #     print(college_score_line_url)
    #     url = college_score_line_url
    #     text = flow.response.text
    #     params = flow.request.get_text()
    # print(text)
    # print(text)
    # 将已经编码的json字符串解码为python对象

    # print(data)
    # 在fiddler中刚刚看到每一个视频的所有信息
    # 都在aweme_list中

    # if url:
    #     try:
    #         cursor.execute(sql, (url, text, params, province, collegeName))
    #     except BaseException:
    #         db1 = pymysql.connect(user="root", password="rYa+wq10dFTWzYz8FeZgsWRygyKfLKULSRdKfRnEgSk=",
    #                               host="119.91.135.29", port=3306, database="zhiyuan_sd",
    #                               charset="utf8", autocommit=True)
    #         cursor1 = db1.cursor(pymysql.cursors.DictCursor)
    #         cursor1.execute(sql, (url, text, params, province, collegeName))

    # enroll_plan_out = open(enroll_plan_csv, "a", newline="", encoding="utf-8")
    # enroll_plan_write = csv.writer(enroll_plan_out, dialect='excel')
    # enroll_plan_write.writerow([url, params, text])
    # print(filename)
    # with open(file_name, 'a') as f:
    #     f.write(data)
    #     f.flush()
    #     print(file_name, '下载完毕')
