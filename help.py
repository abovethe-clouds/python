import time


def cin(weight, high):
    op = "请输入操作（格式：x y 或 f x y，f 表示插旗/取消）："
    while True:
        s = input(op).strip()
        do = s.split()
        if len(do) == 2 and do[0].isdigit() and do[1].isdigit():
            x = int(do[0])
            y = int(do[1])
            op = 'r'
        elif len(do) == 3 and do[0].lower() == 'f' and do[1].isdigit() and do[2].isdigit():
            op = 'f'
            x = int(do[1]);
            y = int(do[2])
        else:
            print("输入无效，请按格式输入！")
            continue
        if x < 0 or x >= weight or y < 0 or y >= high:
            print("输入坐标超出范围，请重新输入！")
            continue
        return op, x, y


def show_help():
    print("扫雷游戏规则：")
    print("1. 输入坐标揭示格子，格式：x y")
    print("2. 插旗/取消旗子，格式：f x y")
    print("3. 避开所有地雷")
    print("4. 揭示所有安全格即获胜")
    input("按回车开始游戏")


class Time:
    def __init__(self):
        self.start_time = time.time()

    def elapsed(self):
        return int(time.time() - self.start_time)
