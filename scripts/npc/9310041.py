# Zhikeseng (9310041)  |  Mount Song-Shaolin Area : Temple Plaza

INTERCEPTED_MESSAGE = 4034635
ELDER_JUNG = 9310049
WISE_CHIEF_PRIEST = 9310053
NOT_A_DEMON = 62002

sm.removeEscapeButton()
sm.setSpeakerID(parentID)
sm.setBoxChat()
if sm.hasQuest(62001):
    if sm.hasQuest(NOT_A_DEMON):
        sm.sendSayOkay("我在等待...")

    elif sm.hasQuestCompleted(NOT_A_DEMON):
        sm.sendSayOkay("原来你终究是人类啊...")

    else:
        sm.sendNext("你好！再见！少林寺关闭了！尽快再来拜访我们！")

        sm.flipBoxChat()
        sm.flipBoxChatPlayerNoEscape()
        if not sm.hasItem(INTERCEPTED_MESSAGE):
            sm.sendNext("#b(我觉得我不能仅凭 elder Jung 的一句话就进去，我应该在再来之前找到那封信。)")
            sm.diposse()
        sm.sendNext("等等，我需要把这封信送给 #b#p"+ str(WISE_CHIEF_PRIEST) +"##k！嵩山 Hamlet 的 #b#p"+ str(ELDER_JUNG) +"##k 派我来的！")

        sm.setSpeakerID(parentID)
        sm.setBoxChat()
        sm.sendNext("#b#p"+ str(WISE_CHIEF_PRIEST) +"##k？你是说 #b#p"+ str(WISE_CHIEF_PRIEST) +"##k？"
                    "你怎么不早说！就是 #b#p"+ str(WISE_CHIEF_PRIEST) +"##k 下令不让我放任何人进去的！")

        sm.sendNext("随便看看。连香炉都被恶灵附身了，你看起来比它们还可怕。")

        sm.sendNext("你体内大概有一群恶魔在跳舞，所以我不能让你进去。再见！")

        sm.flipBoxChat()
        sm.flipBoxChatPlayerNoEscape()
        sm.sendNext("好吧。。听好了混蛋。\r\n"
                    "我的外表是'独特'不是'可怕'，我没有被附身。")

        sm.setSpeakerID(parentID)
        sm.setBoxChat()
        response = sm.sendAskYesNo("上次那个人也是这么说的，然后他全身起火并试图吃掉我的法衣。 "
                    "如果你真的想进寺庙和 #b#p"+ str(WISE_CHIEF_PRIEST) +"##k 谈话，你得证明你是人类。")

        if response:
            sm.sendNext("那么打败100个香炉，把它们偷走的念珠带给我。 "
                        "因为人类拿着它们会发光，我就能判断你是不是人类。")
            sm.startQuestNoCheck(NOT_A_DEMON) # [Shaolin Temple] Not a demon

else:
    sm.sendSayOkay("你好！再见！少林寺关闭了！尽快再来拜访我们！")
