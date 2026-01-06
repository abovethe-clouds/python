import map
import help
help.show_help()
weight = input("请输入地图宽度（默认10）：")
height = input("请输入地图高度（默认10）：")
num = input("请输入地雷数量（默认10）：")
if weight == '':
    weight = 10
else:
    weight = int(weight)
if height == '':
    height = 10
else:
    height = int(height)
if num == '':
    num = 10
else:
    num = int(num)
game_map = map.map(weight, height, num)
timer = help.Time()
while True:
    print("剩余标记数：{}".format(game_map.num - len(game_map.flags)))
    game_map.display()
    op, x, y = help.cin(weight, height)
    if op == 'f':
        game_map.flag(x, y)
        continue
    if not game_map.reveal(x, y):
        print("游戏结束！你踩到地雷了！")
        game_map.reveal_all()
        game_map.display()
        break
    if game_map.is_cleared():
        print("恭喜你！你赢了！")
        game_map.reveal_all()
        game_map.display()
        print("用时：{}秒".format(timer.elapsed()))
        break