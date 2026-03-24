from net.swordie.ms.enums import InvType

potList = ["力量 %", "敏捷 %", "智力 %", "运气 %", "全属性 %", "力量", "敏捷", "智力", "运气", "攻击", "魔法攻击", "全属性", "最大MP", "最大HP", "HP %", "MP %", "BOSS伤害", "IED", "攻击 %", "魔法攻击 %", "伤害 %", "每10级力量", "每10级敏捷", "每10级智力", "每10级运气", "最小暴击", "最大暴击", "#r使用当前列表继续"]
cubeList = [[2710000, "神秘方块", 700], [2711005, "大师工艺方块", 2000], [5062009, "红色方块", 11000], [5062000, "奇迹方块", 15000], [5062005, "强化奇迹方块", 20000], [5062006, "白金奇迹方块", 30000], [5062500, "附加潜力方块", 30000]]
playerPotList = []
eeScroll=0
tempList = []
listitem = []
itemID = []
newlist = []
bagIndex = 0
bPotCube = 5062500
requirementsArr = [{}, {}, {}, {}, {}]
circulatorsList = [[2702000, "能力循环器", 250], [5062800, "奇迹循环器", 4000]]

action = sm.sendNext("你好，我可以帮你给装备打方块或者重置内在潜能。\r\n#b#L0#我想给我的装备打方块。#l\r\n#L1#我想重置我的内在能力。#l")
if action == 0:
    def checkWhatIsIt(str):
        if str.count("%") > 0:
            return "%"
        else:
            return "+"
    def FilterPots(givenPots, toFilterIn):
        toFilterIn = toFilterIn.split("\r\n")
        for x in range(len(givenPots)):
            print "\n".join(s for s in givenPots if toFilterIn[x] in s)
    for x in range(len(cubeList)):
        newlist.append('#L'+str(x)+'##v'+str(cubeList[x][0])+'#'+'#t'+str(cubeList[x][0])+'##l\r\n')
    selection = sm.sendNext("嘿 #h #. 我负责自动打方块。请选择下面的方块：\r\n\r\n\r\n"+''.join(newlist))
    selectedCube = selection
    newlist = []
    if cubeList[selectedCube][0] == bPotCube:
        listitem = eval(sm.getItemsEligibleForBonusPot())
    else:
        listitem = eval(sm.getItemsEligibleForBasePot(cubeList[selectedCube][0]))
    listitem.sort()
    for x in range(len(listitem)):
        itemID.append(sm.getItemIDByBagIndex(listitem[x], InvType.EQUIP))
        newlist.append('\n#L'+str(listitem[x])+'##v'+str(itemID[x])+'#'+"#t"+str(itemID[x])+"#\r\n")
    if not newlist:
        sm.sendSayOkay("没有可打方块的装备。")
        sm.dispose()
    selection = sm.sendNext(''.join(newlist))
    bagIndex = selection
    itemToCube = str(sm.getItemIDByBagIndex(selection, InvType.EQUIP))
    selection = sm.sendNext("你选择了 #v"+itemToCube+"# #e #t"+itemToCube+"##n。\r\n\r\n你想怎么打方块？\r\n#L0#手动给装备打方块。#l\r\n#L1#使用预设的潜力行自动打方块。#l")
    if cubeList[selectedCube][0] == 5062500:
        bonus = True
    else:
        bonus = False
    if selection == 0:
        while sm.sendNext("#fs12#"+ sm.getPotentialLines(bagIndex, False, bonus) + "\r\n按任意行重新打方块。") > -1:
            if sm.hasItem(cubeList[selectedCube][0]):
                if sm.getQuantityOfItem(cubeList[selectedCube][0]) <= 1:
                    sm.setBoxChat()
                    sm.sendNext("你的方块快用完了。")
                    sm.setSpeakerID(9270064)
                sm.consumeCube(bagIndex, cubeList[selectedCube][0])
                sm.consumeItem(cubeList[selectedCube][0])

            else:
                if chr.getUser().getMaplePoints() >= cubeList[selectedCube][2]:
                    sm.consumeCube(bagIndex, cubeList[selectedCube][0])
                    chr.addNx(-cubeList[selectedCube][2])
                else:
                    sm.sendSayOkay("你的NX不足，无法打方块。")
                    break
    elif selection == 1:
        choice = 0
        while choice < len(potList) - 1:
            text = ""
            for x in range(len(potList)):
                text += "#L" + str(x) + "##b" + potList[x] + "#l\r\n"
            choice = sm.sendNext(text)
            if choice < len(potList) - 1:
                amount = sm.sendAskNumber("你想要打多少 " + potList[choice] + "？", 1, 1, 100)
                #
                outPut = ""
                for k in range (len(requirementsArr)):
                    outPut += "#bCombo " + str(k + 1) + ":\r\n"
                    for key, value in requirementsArr[k].items():
                        outPut += "#r" + ("{}: {}".format(key, value)) + ", "
                    outPut += "\r\n"
                combo = sm.sendAskNumber(outPut + "你想把这个属性添加到哪个Combo？", 0, 1, 5)
                requirementsArr[combo - 1][potList[choice]] = amount
        if choice == len(potList) - 1:
            chosenStatsSay = "一旦达成这些组合中的任意一个，NPC将自动停止打方块。\r\n"
            outPut = ""
            for k in range (len(requirementsArr)):
                outPut += "#bCombo " + str(k) + ":\r\n"
                for key, value in requirementsArr[k].items():
                    outPut += "#r" + ("{}: {}".format(key, value)) + ", "
                outPut += "\r\n"
            chosenStatsSay += outPut
            sm.sendNext(chosenStatsSay)
            while sm.sendNext("#fs12#"+ sm.getPotentialLines(bagIndex, False, bonus) + "\r\n按任意行重新打方块。") > -1:
                if sm.itemHasWantedStatsList(requirementsArr, bagIndex, bonus):
                    sm.setNpcOverrideBoxChat(9270064)
                    sm.sendNext("装备已达到要求的属性。")
                    sm.dispose()
                if sm.hasItem(cubeList[selectedCube][0]):
                    sm.consumeCube(bagIndex, cubeList[selectedCube][0])
                    sm.consumeItem(cubeList[selectedCube][0])

                else:
                    if chr.getUser().getMaplePoints() >= cubeList[selectedCube][2]:
                        sm.consumeCube(bagIndex, cubeList[selectedCube][0])
                        chr.addNx(-cubeList[selectedCube][2])
                    else:
                        sm.sendSayOkay("你的NX不足，无法打方块。")
                        sm.dispose()
elif action == 1:
    newlist = ""
    for x in range(len(circulatorsList)):
        newlist += ('#L'+str(x)+'##v'+str(circulatorsList[x][0])+'#'+'#t'+str(circulatorsList[x][0])+'##l\r\n')
    circulatorChoice = sm.sendNext(newlist)
    while sm.sendNext("#fs12#" + sm.getInnerAbilityLines() + "\r\n按任意行重置你的内在能力。") > -1:
        if sm.hasItem(circulatorsList[circulatorChoice][0]):
            if sm.getQuantityOfItem(circulatorsList[circulatorChoice][0]) <= 1:
                sm.setNpcOverrideBoxChat(9270064)
                sm.sendNext("你的循环器快用完了。")
                sm.setSpeakerID(9270064)
            if sm.resetInnerAbility(circulatorsList[circulatorChoice][0]):
                sm.consumeItem(circulatorsList[circulatorChoice][0])
            else:
                sm.sendNext("你不能用这个循环器重置内在能力。")
                sm.dispose()

        else:
            if sm.getHonorExp() >= circulatorsList[circulatorChoice][2]:
                if sm.resetInnerAbility(circulatorsList[circulatorChoice][0]):
                    sm.consumeItem(circulatorsList[circulatorChoice][0])
                    sm.deductHonorExp(circulatorsList[circulatorChoice][2])
                else:
                    sm.sendNext("你不能用这个循环器重置内在能力。")
                    sm.dispose()
            else:
                sm.sendSayOkay("你的荣誉经验值不足，无法重置内在能力。")
                sm.dispose()
