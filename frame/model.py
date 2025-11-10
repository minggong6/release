"""
参赛选手模型文件

参赛选手需要实现model()函数，该函数应该返回一个字典，包含桥梁的构建方案。

返回格式:
{
    "sticks": [
        {
            "p0": [int, int],  # 起始点网格坐标 [grid_x, grid_y]
            "p1": [int, int],  # 结束点网格坐标 [grid_x, grid_y]
            "material": str  # 材料名称 ("wood", "steel", "road", "counterweight")
        },
        ...
    ]
}

注意:
- 所有坐标都是网格格数的整数坐标
- 点可以重复（表示多个点在同一位置）
- 如果地图原本位置存在点就不生成新的点
- 单个点的连接桥数目不超过上限（默认8）
- 梁长度不能超过材料的最大建造长度
- 总成本不能超过关卡预算
- 不能在同一对节点间放置多个梁，即使是不同材料也不可以
"""

def model() -> dict:
    """
    桥梁构建算法的主要函数

    Returns:
        包含桥梁构建方案的字典
    """
    
    sticks = [
        {"p0": [-33, 3], "p1": [-25, 3], "material": "road"},
        {"p0": [-25, 3], "p1": [-17, 3], "material": "road"},
        {"p0": [-17, 3], "p1": [-9, 3], "material": "road"},
        {"p0": [-9, 3], "p1": [-1, 3], "material": "road"},
        {"p0": [-1, 3], "p1": [7, 3], "material": "road"},
        {"p0": [7, 3], "p1": [15, 3], "material": "road"},
        {"p0": [15, 3], "p1": [23, 3], "material": "road"},
        {"p0": [23, 3], "p1": [31, 3], "material": "road"},
        {"p0": [31, 3], "p1": [37, 3], "material": "road"},
    ]

    return {
        "sticks": sticks
    }