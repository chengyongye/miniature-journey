# 公众号配置
# 公众号appId
app_id = "wx9c665798cb319218"
# 公众号appSecret
app_secret = "665b63858ecc2eed085f8b8afa1780b6"
# 模板消息id
# 每日消息
template_id1 = "VLR4J6r6jl0Da5QdaAOEQNxwdZGt27u6VTDS_X3Ff-8"
# 课程消息,上课提醒
template_id2 = "nPC1zbbrOnRSY4YBHIMAahIZxcUIpxTE5Vx19YdhFMo"
# 晚安心语
template_id3 = "8VJhm4CBa03dYwXOezL_sLkMxejKfDsf4hutMAenhHc"
# 接收公众号消息的微信号
# 这是openid
user = ["ouKMI6bZGcaLxIOeLZx0X5YGnuyM"]
user = ["ouKMI6RAhxFrwMuTB3hSP2nWfnQI"]
# 信息配置
# 所在省份
province = "甘肃"
# 所在城市
city = "兰州"
# 生日，如果月份或者日期小于10，直接用对应的数字即可，例如1997-1-1，---------倒计时
birthday = "2002-02-12"
# 在一起的日子，格式同上------------计时器
love_date = "2023-11-11"
# 天行数据晚安心语 key
good_Night_Key = "cfd81789d07aed8cd85ee83f5567c4f9"
# -------------------------------------------------------------------------
# 设置学期第一周开始日期
year = 2024
month = 3
day = 4
# 每日推送时间
post_Time = "07:40:00"
# 每节课提醒时间（有课才会提醒）, 时:分:秒  的形式, 字符串, 根据个人需要设置几次
time_table = ["07:55:00", "10:10:00", "14:10:00", "16:55:00"]
# 课程时间
course_Time = ["8:05--9:55", "10:20--12:10", "14:30--16:20", "16:45--18:35", ]
# 晚安心语及第二天课程推送时间
good_Night_Time = "23:00:00"
# 课程表 "1"代表第一周，依次类推，根据个人实际课表添加，有几周就添加几周,
# 每一行代表一天, 例如  ['', '编译原理', '', '数据库原理及应用', '数据分析原理', '']  代表周一
classes = \
    {
        "1": [
            ['未知', '未知', '未知', '未知'],
            ['未知', '未知', '未知', '未知'],
            ['未知', '未知', '未知', '未知'],
            ['未知', '未知', '未知', '未知'],
            ['未知', '未知', '未知', '未知'],
        ],
      
        
    }

# 模板 1：每日提醒模板
# 本周是开学的第: {{weeks.DATA}} 周
# 今天是: {{date.DATA}}
# 城市： {{city.DATA}}
# 天气： {{weather.DATA}}
# 最低气温: {{min_temperature.DATA}}
# 最高气温: {{max_temperature.DATA}}
# 今天是破壳日的第: {{love_day.DATA}} 天
# 距离开学还有: {{birthday.DATA}} 天
# ----------------今日课程----------------
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}

# 模板 2 课程单推
# 课程信息: {{classInfo.DATA}}

# 模板 3 晚安心语推送和第二天课程推送
# {{goodNight.DATA}}
# ----------------明日课程----------------
# 明天是: {{week.DATA}}
# 第一讲: {{firstClass.DATA}}
# 第二讲: {{secondClass.DATA}}
# 第三讲: {{thirdClass.DATA}}
# 第四讲: {{fourthClass.DATA}}
# 第五讲: {{fifthClass.DATA}}
# 第六讲: {{sixthClass.DATA}}
