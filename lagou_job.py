import requests
import json
import pandas as pd
import time
import random

def get_cookie():
    url='https://www.lagou.com/gongsi/'
    res=requests.get(url=url,headers=headers)
    cookie=res.cookies.get_dict()
    return cookie

#获取指定页数的信息
def get_job_data(city,word,page):
    url='https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(city)
    cookie=get_cookie()
    data={
        'first':'false',
        'pn':str(page),
        'kd':word,
    }
    res=requests.post(url=url,data=data,headers=headers,cookies=cookie)
    html=res.text
    data_dict=json.loads(html)
    result_list=data_dict['content']['positionResult']['result']
    # print(result_list[0])
    for result in result_list:
        jobs_dict['positionName'].append(result.get('positionName','null'))
        jobs_dict['companyId'].append(result.get('companyId', 'null'))
        jobs_dict['companyFullName'].append(result.get('companyFullName', 'null'))
        jobs_dict['companyLogo'].append('https://www.lgstatic.com/'+result.get('companyLogo', 'null'))
        jobs_dict['industryField'].append(result.get('industryField', 'null'))
        jobs_dict['financeStage'].append(result.get('financeStage', 'null'))
        jobs_dict['firstType'].append(result.get('firstType', 'null'))
        jobs_dict['secondType'].append(result.get('secondType', 'null'))
        jobs_dict['thirdType'].append(result.get('thirdType', 'null'))
        jobs_dict['createTime'].append(result.get('createTime', 'null'))
        jobs_dict['city'].append(result.get('city', 'null'))
        jobs_dict['district'].append(result.get('district', 'null'))
        jobs_dict['businessZones'].append(result.get('businessZones', 'null'))
        jobs_dict['salary'].append(result.get('salary', 'null'))
        jobs_dict['workYear'].append(result.get('workYear', 'null'))
        jobs_dict['jobNature'].append(result.get('jobNature', 'null'))
        jobs_dict['education'].append(result.get('education', 'null'))
        jobs_dict['positionAdvantage'].append(result.get('positionAdvantage', 'null'))
        jobs_dict['latitude'].append(result.get('latitude', 'null'))
        jobs_dict['longitude'].append(result.get('longitude', 'null'))
        print(result.get('companyFullName', 'null'))





if __name__=='__main__':
    headers = {
        'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    city = input('请输入城市：')
    word=input('请输入关键词：')
    # city='重庆'
    # word='python'
    jobs_dict={
        'positionName':[],
        'companyId': [],
        'companyFullName': [],
        'companyLogo': [],
        'industryField': [],
        'financeStage': [],
        'firstType': [],
        'secondType': [],
        'thirdType': [],
        'createTime': [],
        'city': [],
        'district': [],
        'businessZones': [],
        'salary': [],
        'workYear': [],
        'jobNature': [],
        'education': [],
        'positionAdvantage': [],
        'latitude':[],
        'longitude': [],
    }
    # for page in range(1,21):
    #     try:
    #         get_job_data(city=city,word=word,page=page)
    #         print(page)
    #         time.sleep(random.randint(50,70))
    #     except Exception as e:
    #         print(e)
    #         time.sleep(120)

    page=1
    while page<=20:
        try:
            get_job_data(city=city,word=word,page=page)
            print(page)
            page+=1
            time.sleep(random.randint(60,70))
        except Exception as e:
            print(e)
            time.sleep(100)

    pd.DataFrame(jobs_dict).to_excel('拉钩网'+city+word+'.xlsx',index=False)

