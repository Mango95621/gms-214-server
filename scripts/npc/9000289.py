# Sylph Ring NPC

from net.swordie.ms.loaders import ItemData

sylphRings = [1114200,1114219,1114201,1114205,1114206,1114202,1114212,1114211,1114210,1114230]
stageOne = 1114200
stageTwo = 1114219
stageThree = 1114201
stageFour = 1114205
stageFive = 1114206
stageSix = 1114202
stageSeven = 1114212
stageEight = 1114211
stageNine = 1114210
stageTen = 1114230
freudsJournal = 4460005

if sm.hasItem(stageTen) or chr.getEquippedInventory().containsItem(stageTen):
    sm.sendSayOkay("你终于完成了你的#b精灵之环#k... 我的研究也完成了。祝你未来好运。")

else:
    response = sm.sendNext("欢迎凡人。你来寻求力量，而我寻求知识。我将用#b精灵之环#k换取#b弗洛伊德日记#k。\r\n"
                           "#L0#什么是精灵之环。#l\r\n"
                           "#L1#是的，我想要一个精灵之环。#l\r\n#r"
                           "#L2#我想升级我的精灵之环。#l\r\n")

    if response == 0:

        sm.sendSayOkay("精灵之环是一枚非常强大的戒指，只有我能为其注入力量。要让这枚戒指发挥全部潜力，"
                       "我需要#r10本#b弗洛伊德日记#k，因为那些日记中蕴含着完全唤醒精灵的力量。")
        sm.dispose()

    elif response == 1:

        for x in range (len(sylphRings)):
            if sm.hasItem(sylphRings[x]):
                sm.sendSayOkay("凡人，我不能给你已经拥有的东西。如果你想要升级你的戒指，"
                               "可以再和我对话并选择#r升级#k选项。")
                sm.dispose()

        if not sm.hasItem(freudsJournal):
            sm.sendSayOkay("凡人，不要挑战我的耐心，我能感觉到你没有#b弗洛伊德日记#k。")
            sm.dispose()

        if not sm.canHold(stageOne):
            sm.sendSayOkay("凡人，你以为背包满了还能拿#b精灵之环#k吗？")
            sm.dispose()

        for x in range (len(sylphRings)):
            if chr.getEquippedInventory().containsItem(sylphRings[x]):
                sm.sendSayOkay("凡人，我不能给你已经拥有的东西。如果你想升级戒指，"
                               "请卸下装备后再来和我对话，选择#r升级#k选项。")
                sm.dispose()

        if sm.hasItem(freudsJournal):
            answer = sm.sendAskYesNo("啊，是的凡人，我能感受到你#b弗洛伊德日记#k散发出的能量。你想要"
                                     "领取你的#b精灵之环#k吗？")

            if answer:
                sm.sendSayOkay("那么凡人，做完了... 戒指现在属于你了。当你获得更多"
                               "#b弗洛伊德日记#k时再来找我，我们可以一起解开精灵的奥秘。")
                sm.consumeItem(freudsJournal)
                sm.giveItem(stageOne)
                sm.dispose()

            else:
                sm.sendSayOkay("不要浪费我的时间凡人。")

    elif response == 2:

        if not sm.canHold(stageOne):
            sm.sendSayOkay("凡人，你以为背包满了还能升级#b精灵之环#k吗？")
            sm.dispose()

        if not sm.hasItem(freudsJournal):
            sm.sendSayOkay("凡人，不要挑战我的耐心，我能感觉到你没有#b弗洛伊德日记#k。")
            sm.dispose()

        for x in range (len(sylphRings)):
            if chr.getEquippedInventory().containsItem(sylphRings[x]):
                sm.sendSayOkay("凡人，我不能在戒指装备着的时候为你升级，请"
                               "卸下装备后再来和我对话。")
                sm.dispose()

        if sm.hasItem(freudsJournal):

            if sm.hasItem(stageOne):

                stage1 = sm.sendAskYesNo("你想解锁#b精灵之环#k中隐藏的力量吗？")

                if stage1:
                    sm.consumeItem(freudsJournal)
                    sm.consumeItem(stageOne)
                    sm.giveItem(stageTwo)
                    sm.sendSayOkay("那么凡人，做完了... 戒指已被注入魔法能量。当你获得更多"
                                   "#b弗洛伊德日记#k时再来找我，我们可以一起进一步探索精灵的奥秘。")
                    sm.dispose()

                else:
                    sm.sendSayOkay("不要浪费我的时间凡人。")

            elif sm.hasItem(stageTwo):

                stage1 = sm.sendAskYesNo("你想解锁#b精灵之环#k中隐藏的力量吗？")

                if stage1:
                    sm.consumeItem(freudsJournal)
                    sm.consumeItem(stageTwo)
                    sm.giveItem(stageThree)
                    sm.sendSayOkay("那么凡人，做完了... 戒指已被注入魔法能量。当你获得更多"
                                   "#b弗洛伊德日记#k时再来找我，我们可以一起进一步探索精灵的奥秘。")
                    sm.dispose()

                else:
                    sm.sendSayOkay("不要浪费我的时间凡人。")

            elif sm.hasItem(stageThree):

                stage1 = sm.sendAskYesNo("你想解锁#b精灵之环#k中隐藏的力量吗？")

                if stage1:
                    sm.consumeItem(freudsJournal)
                    sm.consumeItem(stageThree)
                    sm.giveItem(stageFour)
                    sm.sendSayOkay("那么凡人，做完了... 戒指已被注入魔法能量。当你获得更多"
                                   "#b弗洛伊德日记#k时再来找我，我们可以一起进一步探索精灵的奥秘。")
                    sm.dispose()

                else:
                    sm.sendSayOkay("不要浪费我的时间凡人。")

            elif sm.hasItem(stageFour):

                stage1 = sm.sendAskYesNo("你想解锁#b精灵之环#k中隐藏的力量吗？")

                if stage1:
                    sm.consumeItem(freudsJournal)
                    sm.consumeItem(stageFour)
                    sm.giveItem(stageFive)
                    sm.sendSayOkay("那么凡人，做完了... 戒指已被注入魔法能量。当你获得更多"
                                   "#b弗洛伊德日记#k时再来找我，我们可以一起进一步探索精灵的奥秘。")
                    sm.dispose()

                else:
                    sm.sendSayOkay("不要浪费我的时间凡人。")

            elif sm.hasItem(stageFive):

                stage1 = sm.sendAskYesNo("你想解锁#b精灵之环#k中隐藏的力量吗？")

                if stage1:
                    sm.consumeItem(freudsJournal)
                    sm.consumeItem(stageFive)

                    def giveRing():
                        Ring = ItemData.getEquipDeepCopyFromID(stageSix, False)
                        Ring.setSocket(0, 4311)
                        chr.addItemToInventory(Ring)

                    giveRing()
                    sm.sendSayOkay("那么凡人，做完了... 戒指已被注入魔法能量。当你获得更多"
                                   "#b弗洛伊德日记#k时再来找我，我们可以一起进一步探索精灵的奥秘。")
                    sm.dispose()

                else:
                    sm.sendSayOkay("不要浪费我的时间凡人。")

            elif sm.hasItem(stageSix):

                stage1 = sm.sendAskYesNo("你想解锁#b精灵之环#k中隐藏的力量吗？")

                if stage1:
                    sm.consumeItem(freudsJournal)
                    sm.consumeItem(stageSix)

                    def giveRing():
                        Ring = ItemData.getEquipDeepCopyFromID(stageSeven, False)
                        Ring.setSocket(0, 4311)
                        Ring.setOptionBase(1, 40601)
                        chr.addItemToInventory(Ring)

                    giveRing()
                    sm.sendSayOkay("那么凡人，做完了... 戒指已被注入魔法能量。当你获得更多"
                                   "#b弗洛伊德日记#k时再来找我，我们可以一起进一步探索精灵的奥秘。")
                    sm.dispose()

                else:
                    sm.sendSayOkay("不要浪费我的时间凡人。")

            elif sm.hasItem(stageSeven):

                stage1 = sm.sendAskYesNo("你想解锁#b精灵之环#k中隐藏的力量吗？")

                if stage1:
                    sm.consumeItem(freudsJournal)
                    sm.consumeItem(stageSeven)

                    def giveRing():
                        Ring = ItemData.getEquipDeepCopyFromID(stageEight, False)
                        Ring.setSocket(0, 4311)
                        Ring.setOptionBase(0, 40601)
                        Ring.setOptionBase(1, 30291)
                        chr.addItemToInventory(Ring)

                    giveRing()
                    sm.sendSayOkay("那么凡人，做完了... 戒指已被注入魔法能量。当你获得更多"
                                   "#b弗洛伊德日记#k时再来找我，我们可以一起进一步探索精灵的奥秘。")
                    sm.dispose()

                else:
                    sm.sendSayOkay("不要浪费我的时间凡人。")

            elif sm.hasItem(stageEight):

                stage1 = sm.sendAskYesNo("你想解锁#b精灵之环#k中隐藏的力量吗？")

                if stage1:
                    sm.consumeItem(freudsJournal)
                    sm.consumeItem(stageEight)

                    def giveRing():
                        Ring = ItemData.getEquipDeepCopyFromID(stageNine, False)
                        Ring.setSocket(0, 4311)
                        Ring.setOptionBase(0, 40601)
                        Ring.setOptionBase(1, 30291)
                        Ring.setOptionBase(2, 42051)
                        chr.addItemToInventory(Ring)

                    giveRing()
                    sm.sendSayOkay("那么凡人，做完了... 戒指已被注入魔法能量。当你获得更多"
                                   "#b弗洛伊德日记#k时再来找我，我们可以一起进一步探索精灵的奥秘。")
                    sm.dispose()

                else:
                    sm.sendSayOkay("不要浪费我的时间凡人。")

            elif sm.hasItem(stageNine):

                stage1 = sm.sendAskYesNo("你想解锁#b精灵之环#k中隐藏的力量吗？")

                if stage1:
                    sm.consumeItem(freudsJournal)
                    sm.consumeItem(stageNine)

                    def giveRing():
                        Ring = ItemData.getEquipDeepCopyFromID(stageTen, False)
                        Ring.setSocket(0, 4311)
                        Ring.setSocket(1, 4311)
                        Ring.setSocket(2, 4311)
                        Ring.setOptionBase(0, 40601)
                        Ring.setOptionBase(1, 30291)
                        Ring.setOptionBase(2, 42051)
                        chr.addItemToInventory(Ring)

                    giveRing()

                    sm.sendSayOkay("那么凡人，做完了... 戒指已被注入魔法能量。当你获得更多"
                                   "#b弗洛伊德日记#k时再来找我，我们可以一起进一步探索精灵的奥秘。")
                    sm.dispose()

                else:
                    sm.sendSayOkay("不要浪费我的时间凡人。")

            else:
                sm.sendSayOkay("不要浪费我的时间凡人。我知道你没有#b精灵之环#k。")
