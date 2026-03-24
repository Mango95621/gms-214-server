# Hidden Street - Ardentmill :: 910001000
# Ally :: Master of Alchemy :: 9031005

HERBALISM_SKILL = 92000000
MINING_SKILL = 92010000
SMITHING_CRAFT_SKILL = 92020000
ACCESSORY_CRAFT_SKILL = 92030000
ALCHEMY_CRAFT_SKILL = 92040000
FEE = [5000, 15000, 25000, 40000, 60000, 85000, 115000, 150000, 190000, 235000]

if not sm.hasSkill(ALCHEMY_CRAFT_SKILL):
    selection = sm.sendSay("你好。你对炼金术感兴趣吗？\r\n#L0##b听 #e炼金术#n 的说明。#l\r\n#L1#学习 #e炼金术#n。#k#l")
    if selection == 0:
        sm.sendNext("炼金术是将草药油转化为药水的科学。你可以制作恢复HP和MP的药水，让你更强壮的药水——你想象不到的那种药水。")
    elif selection == 1:
        if not sm.hasSkill(HERBALISM_SKILL):
            sm.sendSayOkay("你不能在没有学习草药学的情况下学习炼金术。")
            sm.dispose()

        if sm.hasSkill(SMITHING_CRAFT_SKILL) or sm.hasSkill(ACCESSORY_CRAFT_SKILL):
            sm.sendNext("如果你已经学习了锻造和首饰制作，你就不能学习炼金术。你必须忘记这两个专业中的一个才能学习炼金术。")
            sm.dispose()

        learn = sm.sendAskYesNo("你真的想学习 #b炼金术#k 吗？\n你必须支付 #b5,000金币#k 才能学习这个专业。 \r\n#b")
        if learn:
            if sm.getMesos() < 5000:
                sm.sendNext("嗯……我觉得你的钱不够……抱歉，请带上 #b5000金币#k。")
                sm.dispose()

            sm.giveMesos(-5000)
            sm.giveSkill(ALCHEMY_CRAFT_SKILL, 0x1000000, 13)
            sm.playSound("profession/levelup")
            sm.sendNext("恭喜！你现在是炼金术士了。酿造一些药水来提升你的基础技能。准备好后，我会教你一些新的东西。")
        else:
            sm.sendNext("选择专业之前仔细考虑。毕竟这些事情需要努力和时间。准备好后再来找我吧。")
else:
    selection = sm.sendSay("你好。你对炼金术感兴趣吗？\r\n#L2##b提升 #e炼金术#n 等级。#l\r\n#L3#忘记炼金术。#k#l")
    if selection == 2:
        if sm.isAbleToLevelUpMakingSkill(ALCHEMY_CRAFT_SKILL):
            levelup = sm.sendAskYesNo("看起来你准备好提升炼金术等级了。我会收取 #b" + str(FEE[sm.getMakingSkillLevel(ALCHEMY_CRAFT_SKILL)]) + "金币#k 作为学费。准备好学习了吗？")
            if levelup:
                if sm.getMesos() < FEE[sm.getMakingSkillLevel(ALCHEMY_CRAFT_SKILL)]:
                    sm.sendNext("你的金币不足。")
                    sm.dispose()

                sm.giveMesos(-FEE[sm.getMakingSkillLevel(ALCHEMY_CRAFT_SKILL)])
                sm.makingSkillLevelUp(ALCHEMY_CRAFT_SKILL)
                sm.sendNext("你的炼金术技能现在是 " + str(sm.getMakingSkillLevel(ALCHEMY_CRAFT_SKILL)) + " 级。")
            else:
                sm.sendNext("当然，花点时间考虑一下。我会在这里。")
                sm.dispose()
        else:
            sm.sendNext("你还没准备好学习更多炼金术。先努力提升你的基础技能吧。")
    elif selection == 3:
        unlearn = sm.sendAskYesNo("你所有的炼金术知识都将被抹去。你的炼金术等级和基础技能都将重置为0。你确定要这样做吗？")
        if unlearn:
            sm.removeSkill(ALCHEMY_CRAFT_SKILL)
            # set quest value 11497, "0"
            # start quest 3263
            # complete quest 3263
            # remove quest 3263
            sm.sendNext("你的炼金术技能已重置。如果你想再学，随时回来。")
        else:
            sm.sendSayOkay("是的。失去所有努力的工作将是一种耻辱。")
