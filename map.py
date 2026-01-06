import random


class map:
    def __init__(self, width, height, num):  # 初始化地图
        self.width = width  # 宽度
        self.height = height  # 高度
        self.num = num  # 地雷数量
        self.mp = [['.' for _ in range(width)] for _ in range(height)]  # 地图初始化为
        self.show_mp = [['■' for _ in range(width)] for _ in range(height)]  # 显示地图初始化为■
        self.where = set()  # 地雷位置集合
        self.flags = set()  # 标记集合
        for i in range(num):
            while True:
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                if (x, y) not in self.where:
                    self.where.add((x, y))
                    self.mp[y][x] = '*'  # 地雷位置标记为*
                    break

    def display(self):  # 显示地图
        print("  " + " ".join([str(i) for i in range(self.width)]))
        for y in range(self.height):
            print(str(y) + " " + " ".join(self.show_mp[y]))

    def count_mines(self, x, y):  # 计算周围地雷数量
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx, ny = x + i, y + j
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.mp[ny][nx] == '*':
                        count += 1
        return count

    def reveal(self, x, y):  # 揭示格子
        if self.show_mp[y][x] == 'F':  # 插旗状态不能揭示
            return True
        if self.show_mp[y][x] != '■':  # 已揭示过
            return True
        if self.mp[y][x] == '*':
            self.show_mp[y][x] = '*'
            return False
        else:
            count = self.count_mines(x, y)
            self.show_mp[y][x] = ' ' if str(count)=='0' else str(count)
            if count == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        nx, ny = x + i, y + j
                        if 0 <= nx < self.width and 0 <= ny < self.height:
                            if self.show_mp[ny][nx] == '■':
                                self.reveal(nx, ny)
            return True

    def flag(self, x, y):  # 插旗或取消旗子
        if 0 <= x < self.width and 0 <= y < self.height:
            if self.show_mp[y][x] == '■':
                self.show_mp[y][x] = 'F'
                self.flags.add((x, y))

            elif self.show_mp[y][x] == 'F':
                self.show_mp[y][x] = '■'
                self.flags.discard((x, y))

    def is_cleared(self):  # 检查是否清除所有非地雷格子
        for y in range(self.height):
            for x in range(self.width):
                if self.mp[y][x] != '*' and self.show_mp[y][x] == '■':
                    return False
        return True

    def reveal_all(self):  # 揭示所有格子
        for y in range(self.height):
            for x in range(self.width):
                if self.mp[y][x] == '*':
                    self.show_mp[y][x] = '*'
                else:
                    count = self.count_mines(x, y)
                    self.show_mp[y][x] = ' ' if count == 0 else str(count)
        for (fx, fy) in list(self.flags):
            if 0 <= fx < self.width and 0 <= fy < self.height:
                if self.mp[fy][fx] == '*':
                    self.show_mp[fy][fx] = 'F'
                else:
                    self.show_mp[fy][fx] = 'X'
