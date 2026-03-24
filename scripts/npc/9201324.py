sm.setSpeakerID(9201324)
sm.sendNext("我好像弄丢了我的宠物，你能帮我找她吗？我需要先确认你是值得信任的！")
if sm.sendAskYesNo("准备好回答我的问题了吗？"):
    question = sm.sendAskText("雅典娜·皮尔斯的弓是什么颜色的？", "", 1, 20)
    if question == "Blue" or question == "blue":
        sm.sendNext("我太高兴了，我能信任你！快点吧，我真的好想她。")
        sm.sendNext("拿着这个物品，这样她就知道你是值得信任的了。")
        sm.sendNext("我从一个冒险家那里听说，他们可能在海浪深处的洞穴里见过她。")
        sm.sendNext("请把她安全地还给我。")
        if sm.canHold(4161080):
            sm.giveItem(4161080)
        else:
            sm.sendNext("你的背包没有空间放我的物品了！")

else:
    sm.sendNext("请回来再回答我的问题！")
