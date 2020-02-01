import datetime
from pyecharts import options as opts
from pyecharts.charts import Map

# 用于测试的例子，部分取自 Faker ，也就是 from pyecharts.faker import Faker
provinces = ["湖北", "浙江", "广东", "河南", "重庆", "湖南", "安徽", "北京", "四川", "上海", "山东", "广西", "江苏", "海南", "辽宁", "江西", "福建", "陕西",
             "黑龙江", "河北", "云南", "天津", "山西", "内蒙古", "甘肃", "香港", "贵州", "吉林", "宁夏", "台湾", "新疆", "青海", "澳门"]
guangdong_city = ["汕头市", "汕尾市", "揭阳市", "阳江市", "肇庆市", "广州市", "惠州市"]
value = [4586, 428, 254, 278, 182, 277, 200, 114, 142, 112, 158, 78, 129, 46, 41, 162, 101, 63, 43, 65, 70, 29, 35, 18,
         26, 10, 12, 14, 17, 8, 14, 6, 7]


# 连续性数据显示，不同颜色不同省份
# 今日数据全国确诊病例数据图
def map_visualmap() -> Map:
    c = (
        Map()
            .add("", [list(z) for z in zip(provinces, value)], "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title=datetime.date.today()),
            visualmap_opts=opts.VisualMapOpts(max_=100),
        )
    )
    return c


if __name__ == '__main__':
    city_ = map_visualmap()
    city_.render(path="test_map_1.html")
