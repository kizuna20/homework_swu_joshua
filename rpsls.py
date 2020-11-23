#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：土木三班何菊山
日期：2020/11/22
"""
import random  #导入random模块
computer_choice=random.randint(0,4)
def name_to_number(name):
    if name=="石头":
        name=0
    elif name=="史波克":
        name=1
    elif name=="纸":
        name=2
    elif name=="蜥蜴":
        name=3
    elif name=="剪刀":
        name=4
    return name
def number_to_name(number):
    if number==0:
        number='石头'
    elif number==1:
        number='史波克'
    elif number==2:
        number='纸'
    elif number==3:
        number='蜥蜴'
    elif number==4:
        number='剪刀'
    return number
def rpsls(player_choice):
    i=name_to_number(player_choice)
    if i==0:
        if computer_choice==1 or 2:
            print('计算机赢了')
        elif computer_choice==3 or 4:
            print('您赢了')
        elif computer_choice==0:
            print('您和计算机出的一样呢')
    elif i==1:
        if computer_choice==3 or 2:
            print('计算机赢了')
        elif computer_choice==0 or 4:
            print('您赢了')
        elif computer_choice==1:
            print('您和计算机出的一样呢')
    elif i==2:
        if computer_choice==3 or 4:
            print('计算机赢了')
        elif computer_choice==1 or 0:
            print('您赢了')
        elif computer_choice==2:
            print('您和计算机出的一样呢')
    elif i==3:
        if computer_choice==0 or 4:
            print('计算机赢了')
        elif computer_choice==1 or 2:
            print('您赢了')
        elif computer_choice==3:
            print('您和计算机出的一样呢')
    elif i==4:
        if computer_choice==1 or 0:
            print('计算机赢了')
        elif computer_choice==2 or 3:
            print('您赢了')
        elif computer_choice==4:
            print('您和计算机出的一样呢')
    return
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
if choice_name in ['剪刀','石头','史波克','纸','蜥蜴']:
    print('您的选择为：',choice_name)
    print('计算机的选择为：',number_to_name(computer_choice))
    rpsls(choice_name)
else :
    print('Error: No Correct Name')