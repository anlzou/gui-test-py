from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map

# 用于测试的例子，部分取自 Faker ，也就是 from pyecharts.faker import Faker
provinces = ["广东", "北京", "上海", "辽宁", "湖南", "四川", "西藏"]
guangdong_city = ["汕头市", "汕尾市", "揭阳市", "阳江市", "肇庆市", "广州市", "惠州市"]
country = ["China", "Canada", "Brazil", "Russia", "United States", "Africa", "Germany"]
value = [300, 100, 2000, 800, 10000, 400, 5000]

##1. 基本图形
# 显示其中的某些省市和数据
def map_base() -> Map:
    c = (
        Map()
        .add("", [list(z) for z in zip(provinces, value)], "china")
        .set_global_opts(title_opts=opts.TitleOpts(title="map-基本图形"))
    )
    return c
# if __name__ == '__main__':
    # city_map = map_base()
    # city_map.render(path="test_map_1.html")

##2. 用颜色图例表示数据特征，连续性表示，max_ 表示图例展示的最大数值，如果比该数值大，那么颜色都是一样的
# 连续性数据显示，不同颜色不同省份
def map_visualmap() -> Map:
    c = (
        Map()
        .add("", [list(z) for z in zip(provinces, value)], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="连续型数据"),
            visualmap_opts=opts.VisualMapOpts(max_= 2000),
        )
    )
    return c
# if __name__ == '__main__':
#     city_ = map_visualmap()
#     city_.render(path="test_map_1.html")

##3. 显示世界地图
# 显示世界地图
def map_world() -> Map:
    c = (
        Map()
        .add("", [list(z) for z in zip(country, value)], "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="世界地图"),
            visualmap_opts=opts.VisualMapOpts(max_=2000),
        )
    )
    return c
# if __name__ == '__main__':
#     country_ = map_world()
#     country_.render(path="test_map_1.html")

##4. 显示某个省的下级地图
# 显示广东省地图
def map_guangdong() -> Map:
    c = (
        Map()
        .add("", [list(z) for z in zip(guangdong_city, value)], "广东")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="广东地图"),
            visualmap_opts=opts.VisualMapOpts(max_=2000),
        )
    )
    return c
# if __name__ == '__main__':
#     gd = map_guangdong()
#     gd.render(path="test_map_1.html")

##5. 分段图例显示，split_number 表示图例所分的段数
# 分段图例
def map_visualmap_piece() -> Map:
    c = (
        Map()
        .add("", [list(z) for z in zip(provinces, value)], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="分段型数据"),
            visualmap_opts=opts.VisualMapOpts(max_=2000, split_number=8, is_piecewise=True),
        )
    )
    return c
if __name__ == '__main__':
    map_piece = map_visualmap_piece()
    map_piece.render(path="test_map_1.html")