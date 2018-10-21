from turtle import *
speed(10)
pensize(7)
penup()
begin_fill()
goto(0,-200)
pendown()
circle(200)
end_fill()

penup()
goto(0,-125)
pendown()
begin_fill()
color('white')
circle(120)
end_fill()


penup()
goto(0,-5)
pendown()

# 画右下 四分一圆，填充颜色为天蓝
begin_fill()    # 开始填充颜色
fillcolor('#00BFFF') # 填充颜色
pencolor('black')    # 画笔颜色
pensize(3)           # 画笔大小
forward(120)         # 往前走120
right(270)           # 向右旋转270度
circle(120,-90)      # 顺时针画四分一圆，半径为120
left(90)             # 向左转90度
forward(120)         # 向前走120
end_fill()           # 填充颜色完毕

# 画左上四分之一圆，填充蓝色为天蓝
begin_fill()       # 开始填充颜色
color('#00BFFF')   # 填充颜色参数
pencolor('black')  # 画笔颜色
pensize(3)         # 画笔大小
forward(120)       # 往前走120
left(90)           # 左转90度
circle(120,90)     # 逆时针画四分之一圆，半径为120
left(90)           # 左转90度
forward(120)       # 往前走120
end_fill()         # 填充颜色完毕

# 四个圆外画一个黑色的圈
right(90)     # 右转90度
forward(120)  # 往前走120度
left(90)      # 左转90度
circle(120)   # 画一个圈

# write B
penup()        # 抬起笔尖
pensize(9)     # 画笔大小
goto(-105,80)  # 把笔尖移到相应到坐标位置
color('white') # 画笔颜色为白色
pendown()      # 笔尖放到画布上
left(150)      # 向左转150度
forward(55)    # 往前走55

# 画出 B 中左边的 一条竖线
pensize(7)     # 更改画笔大小
right(90)      # 右旋转90度
forward(20)    # 往前走20

# 画出B中上半部分的弧度
for i in range(10):  # 顺时针画15度角圆后旋转15度，重复10次
    circle(-15,15)

right(35)    #右旋转35度
forward(23)  # 往前走23

# 画出B中下半部分度弧度
backward(18) # 后退走18
left(180)    # 左转180度

for i in range(10): # 顺时针画15度角圆后旋转15度，重复10次
    circle(-15,15)

right(30)   # 右旋转30度
forward(23) # 往前走23


# write W
penup()      # 笔尖抬起
right(210)   # 右旋转210
pensize(9)   # 画笔大小
goto(95,95)  # 移动到相应度坐标
pendown()    # 笔尖放到画布下
left(45)     # 左旋转45度
forward(50)  # 往前走50，画出 W最左边度一条线
backward(50) # 往后退50，回到原点
right(30)    # 右旋转30度
forward(50)  # 往前走50，画出 w第二条线
left(30)     # 左旋转30度
backward(50) # 往后退50，画出 w第三条线
right(35)    # 右旋转35度
forward(50)  # 往前走50，画出w 最右边度线



# write M
penup()
goto(-25,130)
pendown()
left(55)

pencolor('white')   # 画笔颜色为白色
forward(50)

left(30)
backward(50)

right(60)
forward(50)

left(30)
backward(50)


hideturtle() # 隐藏笔尖
done()       # 完成操作