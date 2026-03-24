from net.swordie.ms.constants import ItemConstants

# Lao (2091012) | Mu Lung Dojo Hall

# Dojo Array Start

itemsDojo = [
    [5062500,5062006,2070018,2046897],
    [2431174,2433808,4001832,4310015,4021031,2502000,2430692,2022740,2022741,2022742,2022743,2022744,2022745,2022794,2022795,2022796,2022797,2022798,2022799,3700080,3700096,3010425,3700049,5220000,5220100,3010412,3010521],
    [1002790,1002791,1002792,1002793,1002794,1052160,1052161,1052162,1052163,1052164,1072361,1072362,1072363,1072364,1072365,1082239,1082240,1082241,1082242,1082243],
    [1212012,1222012,1232012,1242012,1252012,1312038,1322061,1332075,1332076,1342012,1362017,1372045,1382059,1402047,1412034,1422038,1432049,1442067,1452059,1462051,1472071,1482024,1492025,1522016,1532016,1542012,1552057],
    [1002776,1002777,1002778,1002779,1002780,1032031,1052155,1052156,1052157,1052158,1052159,1072356,1072357,1072358,1072359,1072360,1082234,1082235,1082236,1082237,1082238,1092057,1092058,1092059,1122012],
    [1212011,1222011,1232011,1242011,1252011,1312037,1322060,1332074,1332075,1342011,1362016,1372044,1382057,1402046,1412033,1422037,1432047,1442063,1452057,1462050,1472068,1482023,1492023,1522015,1532015,1542013,1552013],
    [1003280,1003281,1003282,1003283,1003284,1052374,1052375,1052376,1052377,1052378,1072544,1072545,1072546,1072547,1072548,1082328,1082329,1082330,1082331,1082332],
    [1212017,1222017,1232017,1242017,1252018,1302173,1312072,1322107,1332148,1332149,1342040,1362022,1372100,1382124,1402111,1412071,1422073,1432099,1442136,1452129,1462118,1472141,1482102,1492101,1522020,1532037,1542033,1552033],
    [1003285,1003286,1003287,1003288,1003289,1032108,1052379,1052380,1052381,1052382,1052383,1072549,1072550,1072551,1072552,1072553,1082333,1082334,1082335,1082336,1082337,1092092,1092093,1092094,1122148],
    [1212018,1222018,1232018,1242018,1252022,1302174,1312073,1322108,1332150,1332151,1342041,1362023,1372101,1382125,1402112,1412072,1422074,1432100,1442137,1452130,1462119,1472142,1482103,1492102,1522021,1532038,1542034,1552034],
]

costDojoPoints = [
    [400000,400000,100000,2000000],
    [20000,400000,5000,100000,50000,8000,15000,7000,7000,7000,7000,7000,7000,7000,35000,35000,35000,35000,35000,35000,5000000,12000000,50000000,100000000,20000,400000,100000000,500000000],
    [100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000],
    [250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000,250000],
    [125000,125000,125000,125000,125000,200000,125000,125000,125000,125000,125000,125000,125000,125000,125000,125000,125000,125000,125000,125000,125000,100000,100000,100000,250000],
    [500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000,500000],
    [175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000,175000],
    [750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000,750000],
    [200000,200000,200000,200000,200000,240000,200000,200000,200000,200000,200000,200000,200000,200000,200000,200000,200000,200000,200000,200000,200000,150000,150000,150000,400000],
    [1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000,1000000],
]

# Dojo Array Finish

dojoHall = 925020001

if sm.getFieldID() == dojoHall:
    selection = sm.sendNext("我的师父是慕灵最强的人。他的挑战可以获得武斗点数，你可以在这里消费。\r\n你目前有 #r"+ str(sm.getDojoPoints()) +" #b武斗点数\r\n#b"
                            "#L0#用竹子福袋换取1,000,000武斗点数。#l\r\n"
                            "#L1#用1,000,000武斗点数换取竹子福袋。#l\r\n"
                            "#L2#消费武斗点数.#l\r\n")

    if selection == 0:
        answer = sm.sendAskNumber("你想要购买多少个 #b#v 3993002 # #t 3993002 #(s)#k？", 0, 1, 1000)

        Total = answer * 1
        totalQty = answer * 1000000

        if  sm.getDojoPoints() <= totalQty:
            sm.sendSayOkay("你的#b武斗点数#k不足。")
            sm.dispose()

        else:
            sm.deductDojoPoints(totalQty)
            sm.giveItem(3993002, Total)
            sm.sendSayOkay("感谢你的购买！\r\n你还剩 #r"+ str(sm.getDojoPoints()) +"#b 武斗点数#k。")
            sm.dispose()

    if selection == 1:
        answer = sm.sendAskNumber("你想要卖出多少个 #b#v 3993002 # #t 3993002 #(s)#k？", 0, 1, 1000)

        Total = answer * 1
        totalQty = answer * 1000000


        if not sm.hasItem(3993002, Total):
            sm.sendSayOkay("你的 #b#v 3993002 # #t 3993002 #(s)#k 不足。")
            sm.dispose()

        else:
            sm.consumeItem(3993002, Total)
            sm.giveDojoPoints(totalQty)
            sm.sendSayOkay("感谢你的购买！\r\n你现在有 #r"+ str(sm.getDojoPoints()) +"#b 武斗点数#k。")
            sm.dispose()

    if selection == 2:

        selection1 = sm.sendNext("你想从哪个类别购买物品？\r\n你目前有 #r"+ str(sm.getDojoPoints()) +" #b武斗点数\r\n"
                                "#L0#消耗品.#l\r\n"
                                "#L1#其他.#l\r\n"
                                "#L2#逆时针防具.#l\r\n"
                                "#L3#逆时针武器.#l\r\n"
                                "#L4#永恒防具.#l\r\n"
                                "#L5#永恒武器.#l\r\n"
                                "#L6#深渊防具.#l\r\n"
                                "#L7#深渊武器.#l\r\n"
                                "#L8#无畏防具.#l\r\n"
                                "#L9#无畏武器.#l\r\n")

        listStr = "你想要购买什么物品？ #b"

        i = 0

        while i < len(itemsDojo[selection1]):
            listStr += "\r\n#L" + str(i) + "##v" + str(itemsDojo[selection1][i]) + "#"   "#z" + str(itemsDojo[selection1][i]) + "# #r(" + str(costDojoPoints[selection1][i]) + " 武斗点数)#b"

            i += 1

        selection2 = sm.sendNext(listStr)

        if selection1 == 0 or selection1 == 1:
            materialStr = "你想要 #b#v" + str(itemsDojo[selection1][selection2]) + "##z" + str(itemsDojo[selection1][selection2]) + "#s？ \r\n #k这需要付费。\r\n"

        else:
            materialStr = "你想要 #b#v" + str(itemsDojo[selection1][selection2]) + "##z" + str(itemsDojo[selection1][selection2]) + "#？ \r\n#k这需要付费。\r\n"

        i = 0

        if costDojoPoints[selection1][selection2] > 0:
            materialStr += "\r\n#i4001620#   #r" + str(costDojoPoints[selection1][selection2]) + " #b武斗点数"

        if (selection1 == 0 or selection1 == 1) and not ItemConstants.isThrowingItem(itemsDojo[selection1][selection2]):
            sm.chat("a")
            materialStr += "\r\n\r\n你想购买多少个？"
            amount = sm.sendAskNumber(materialStr, 1, 1, 50000)

            TotalCost = (amount * costDojoPoints[selection1][selection2])
            TotalQty = amount

            if sm.getDojoPoints() <= TotalCost:
                sm.sendSayOkay("恐怕你买不起这个。")
                sm.dispose()

            else:
                if not sm.canHold(itemsDojo[selection1][selection2]):
                    sm.sendSayOkay("请确保你的背包有空间，再来和我对话。")
                    sm.dispose()

                else:
                    i = 0
                    if costDojoPoints[selection1][selection2] > 0:
                        sm.deductDojoPoints(TotalCost)
                        sm.giveItem(itemsDojo[selection1][selection2], TotalQty)
                        sm.sendSayOkay("需要其他帮助再来找我。")

        else:
            response = sm.sendAskYesNo(materialStr)



            if sm.getDojoPoints() <= costDojoPoints[selection1][selection2]:
                sm.sendSayOkay("恐怕你买不起这个。")
                sm.dispose()

            else:
                if not sm.canHold(itemsDojo[selection1][selection2]):
                    sm.sendSayOkay("请确保你的背包有空间，再来和我对话。")
                    sm.dispose()

                else:
                    i = 0
                    if costDojoPoints[selection1][selection2] > 0:
                        sm.deductDojoPoints(costDojoPoints[selection1][selection2])
                        sm.giveItem(itemsDojo[selection1][selection2])
                        sm.sendSayOkay("需要其他帮助再来找我。")

elif sm.sendNext:
    selection = sm.sendNext("嘿，你想来慕灵武斗场碰碰运气吗？\r\n#b"
                            "#L0#是的，现在就传送到武斗场。#l\r\n"
                            "#L1#不，我想购买一些东西。#l\r\n")
    if selection == 0: #
        sm.warp(925020001)
    if selection == 1:

        selection1 = sm.sendNext("你想从哪个类别购买物品？\r\n你目前有 #r"+ str(sm.getDojoPoints()) +" #b武斗点数\r\n"
                                                                                                                                               "#L0#消耗品.#l\r\n"
                                                                                                                                               "#L1#其他.#l\r\n"
                                                                                                                                               "#L2#逆时针防具.#l\r\n"
                                                                                                                                               "#L3#逆时针武器.#l\r\n"
                                                                                                                                               "#L4#永恒防具.#l\r\n"
                                                                                                                                               "#L5#永恒武器.#l\r\n"
                                                                                                                                               "#L6#深渊防具.#l\r\n"
                                                                                                                                               "#L7#深渊武器.#l\r\n"
                                                                                                                                               "#L8#无畏防具.#l\r\n"
                                                                                                                                               "#L9#无畏武器.#l\r\n")

        listStr = "你想要购买什么物品？ #b"

        i = 0

        while i < len(itemsDojo[selection1]):
            listStr += "\r\n#L" + str(i) + "##v" + str(itemsDojo[selection1][i]) + "#"   "#z" + str(itemsDojo[selection1][i]) + "# #r(" + str(costDojoPoints[selection1][i]) + " 武斗点数)#b"

            i += 1

        selection2 = sm.sendNext(listStr)

        if selection1 == 0 or selection1 == 1:
            materialStr = "你想要 #b#v" + str(itemsDojo[selection1][selection2]) + "##z" + str(itemsDojo[selection1][selection2]) + "#s？ \r\n #k这需要付费。\r\n"

        else:
            materialStr = "你想要 #b#v" + str(itemsDojo[selection1][selection2]) + "##z" + str(itemsDojo[selection1][selection2]) + "#？ \r\n#k这需要付费。\r\n"

        i = 0

        if costDojoPoints[selection1][selection2] > 0:
            materialStr += "\r\n#i4001620#   #r" + str(costDojoPoints[selection1][selection2]) + " #b武斗点数"

        if selection1 == 0 or selection1 == 1:
            materialStr += "\r\n\r\n你想购买多少个？"
            amount = sm.sendAskNumber(materialStr, 1, 1, 50000)

            TotalCost = (amount * costDojoPoints[selection1][selection2])
            TotalQty = amount

            if sm.getDojoPoints() <= TotalCost:
                sm.sendSayOkay("恐怕你买不起这个。")
                sm.dispose()

            else:
                if not sm.canHold(itemsDojo[selection1][selection2]):
                    sm.sendSayOkay("请确保你的背包有空间，再来和我对话。")
                    sm.dispose()

                else:
                    i = 0
                    if costDojoPoints[selection1][selection2] > 0:
                        sm.deductDojoPoints(TotalCost)
                        sm.giveItem(itemsDojo[selection1][selection2], TotalQty)
                        sm.sendSayOkay("需要其他帮助再来找我。")

        else:
            response = sm.sendAskYesNo(materialStr)



            if sm.getDojoPoints() <= costDojoPoints[selection1][selection2]:
                sm.sendSayOkay("恐怕你买不起这个。")
                sm.dispose()

            else:
                if not sm.canHold(itemsDojo[selection1][selection2]):
                    sm.sendSayOkay("请确保你的背包有空间，再来和我对话。")
                    sm.dispose()

                else:
                    i = 0
                    if costDojoPoints[selection1][selection2] > 0:
                        sm.deductDojoPoints(costDojoPoints[selection1][selection2])
                        sm.giveItem(itemsDojo[selection1][selection2])
                        sm.sendSayOkay("需要其他帮助再来找我。")
