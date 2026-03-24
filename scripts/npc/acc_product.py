# Hidden Street - Ardentmill :: 910001000
# Intaglio :: Master of Accessory Crafting :: 9031004

MINING_SKILL = 92010000
SMITHING_CRAFT_SKILL = 92020000
ACCESSORY_CRAFT_SKILL = 92030000
ALCHEMY_CRAFT_SKILL = 92040000
FEE = [5000, 15000, 25000, 40000, 60000, 85000, 115000, 150000, 190000, 235000]

if not sm.hasSkill(ACCESSORY_CRAFT_SKILL):
    selection = sm.sendSay("璀璨的光芒！水晶的纯度！棱镜的美丽！你也是珠宝商吗，朋友？让我们一起探索首饰制作的奥秘吧？\r\n#L0#听 #b#e首饰制作#n 的说明。#l\r\n#L1#学习 #e首饰制作#n。#k#l")
    if selection == 0:
        sm.sendNext("从哪里开始呢，从哪里开始呢？我可以告诉你宝石的固有之美，但是……那可能要花整晚。\n简而言之，首饰制作是一门将原始宝石或矿物塑形，直到其真正之美闪耀出来的艺术。即使是最粗糙的宝石也有可能变得优雅而强大。")
    elif selection == 1:
        if not sm.hasSkill(MINING_SKILL):
            sm.sendSayOkay("哦，不。你必须先从 #b科尔#k 那里学习采矿，我才能教你成为珠宝商。他会教你如何获得制作闪亮发光配饰所需的所有矿物和宝石。")
            sm.dispose()

        if sm.hasSkill(SMITHING_CRAFT_SKILL) or sm.hasSkill(ALCHEMY_CRAFT_SKILL):
            sm.sendNext("难道你不知道如果你已经学习了锻造和炼金，就不能学习首饰制作吗？嘘……你只需要删除你当前的一个专业，我们就可以一起学习首饰制作了！")
            sm.dispose()

        learn = sm.sendAskYesNo("哦，你准备好学习 #b首饰制作#k 了吗？\n因为你太可爱了，我会给你折扣。#b5,000金币#k 成为我的学生。\r\n")
        if learn:
            if sm.getMesos() < 5000:
                sm.sendNext("你没有 #b 5000金币#k？我希望我能帮你，但我真的不能免费教你。")
                sm.dispose()

            sm.giveMesos(-5000)
            sm.giveSkill(ACCESSORY_CRAFT_SKILL, 0x1000000, 13)
            sm.playSound("profession/levelup")
            sm.sendNext("哦！太棒了！这就是首饰制作的方式。练习，练习，练习，当你获得了足够的基础技能后，我会教你更多。")
        else:
            sm.sendNext("什么？为什么不？！我一直期待着与你分享我的知识！")
else:
    selection = sm.sendSay("璀璨的光芒！水晶的纯度！棱镜的美丽！你也是珠宝商吗，朋友？让我们一起探索首饰制作的奥秘吧？\r\n#L2##b提升 #e首饰制作#n 等级。#l\r\n#L3#忘记首饰制作。#k#l")
    if selection == 2:
        if sm.isAbleToLevelUpMakingSkill(ACCESSORY_CRAFT_SKILL):
            levelup = sm.sendAskYesNo("看起来你准备好提升首饰制作等级了。我会收取 #b" + str(FEE[sm.getMakingSkillLevel(ACCESSORY_CRAFT_SKILL)]) + "金币#k 作为学费。准备好学习了吗？")
            if levelup:
                if sm.getMesos() < FEE[sm.getMakingSkillLevel(ACCESSORY_CRAFT_SKILL)]:
                    sm.sendNext("你的金币不足。")
                    sm.dispose()
                sm.giveMesos(-FEE[sm.getMakingSkillLevel(ACCESSORY_CRAFT_SKILL)])
                sm.makingSkillLevelUp(ACCESSORY_CRAFT_SKILL)
                sm.sendNext("你的首饰制作技能现在是 " + str(sm.getMakingSkillLevel(ACCESSORY_CRAFT_SKILL)) + " 级。")
            else:
                sm.sendNext("当然，花点时间考虑一下。我会在这里。")
                sm.dispose()
        else:
            sm.sendNext("哦，你还没准备好提升你的专业等级。继续努力吧！")
    elif selection == 3:
        unlearn = sm.sendAskYesNo("你想删除你的首饰制作技能吗？你已经厌倦我了吗？你为提升等级和基础技能所付出的所有努力都将失去……所有那些……努力……消失了……你真的确定要这样做吗？")
        if unlearn:
            sm.removeSkill(ACCESSORY_CRAFT_SKILL)
            # set quest value 11496, "0"
            # start quest 3263
            # complete quest 3263
            # remove quest 3263
            sm.sendNext("已经重置了……你真是冷漠……但如果你改变主意，我会在这里。")
        else:
            sm.sendSayOkay("哦，谢谢，谢谢，谢谢！")
