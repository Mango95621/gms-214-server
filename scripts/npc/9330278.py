if sm.sendNext:
    selection = sm.sendNext("你好。我有附近最好的图腾。想看看吗？\r\n你目前有 #r"+ str(sm.getFriendPoints()) +" #b友谊点数\r\n"
                            "#L0#用 #r1000#b 友谊点数兑换 #v 04310126 # #t 04310126 #(s)\r\n"
                            "#L1#用 #v 04310126 # #t 04310126 #(s) 兑换 #r1000#b 友谊点数\r\n\r\n"
                            "#L2##v 1202086 # #z 1202086 ##r (1000 友谊点数)#b\r\n"
                            "#L3##v 1202085 # #z 1202085 ##r (1000 友谊点数)#b\r\n"
                            "#L4##v 1202084 # #z 1202084 ##r (1000 友谊点数)#b\r\n"
                            "#L5##v 1202083 # #z 1202083 ##r (1000 友谊点数)#b\r\n"
                            "#L6##v 1202124 # #z 1202124 ##r (5000 友谊点数)#b\r\n"
                            "#L7##v 1202089 # #z 1202089 ##r (6000 友谊点数)#b\r\n"
                            "#L8##v 1202090 # #z 1202090 ##r (6000 友谊点数)#b\r\n"
                            "#L9##v 1202091 # #z 1202091 ##r (6000 友谊点数)#b\r\n"
                            "#L10##v 1182162 # #z 1182162 ##r (6000 友谊点数)#b\r\n"
                            "#L11##v 1202094 # #z 1202094 ##r (10000 友谊点数)#b\r\n"
                            "#L12##v 1202095 # #z 1202095 ##r (10000 友谊点数)#b\r\n"
                            "#L13##v 1202096 # #z 1202096 ##r (10000 友谊点数)#b\r\n"
                            "#L14##v 1202097 # #z 1202097 ##r (10000 友谊点数)#b\r\n"
                            "#L15##v 1202050 # #z 1202050 ##r (15000 友谊点数)#b\r\n"
                            "#L16##v 1202054 # #z 1202054 ##r (15000 友谊点数)#b\r\n"
                            "#L17##v 1202058 # #z 1202058 ##r (15000 友谊点数)#b\r\n"
                            "#L18##v 1202062 # #z 1202062 ##r (15000 友谊点数)#b\r\n"
                            "#L19##v 1202236 # #z 1202236 ##r (500000 友谊点数)#b\r\n")


    if selection == 0:
        answer = sm.sendAskNumber("你想购买多少个 #b#v 04310126 # #t 04310126 #(s)#k ？", 0, 1, 1000)

        Total = answer * 1
        totalQty = answer * 1000  # Cost Per Coin

        if  sm.getFriendPoints() < totalQty:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()

        else:
            sm.deductFriendPoints(totalQty)
            sm.giveItem(4310126, Total)
            sm.sendSayOkay("感谢你的购买！\r\n你还剩 #r"+ str(sm.getFriendPoints()) +"#b 友谊点数#k。")
            sm.dispose()

    if selection == 1:
        answer = sm.sendAskNumber("你想卖出多少个 #b#v 04310126 # #t 04310126 #(s)#k ？", 0, 1, 1000)

        Total = answer * 1
        totalQty = answer * 1000  # Cost Per Coin


        if not sm.hasItem(4310126, Total):
            sm.sendSayOkay("你的 #b#v 04310126 # #t 04310126 #(s)#k 不足。")
            sm.dispose()

        else:
            sm.consumeItem(4310126, Total)
            sm.giveFriendPoints(totalQty)
            sm.sendSayOkay("感谢你的购买！\r\n你现在有 #r"+ str(sm.getFriendPoints()) +"#b 友谊点数#k。")
            sm.dispose()

    if selection == 2:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202086 # #z 1202086 ##k 吗？\r\n\r\n#b#v 4031138 # #r50,000,000 #b金币\r\n\r\n#b#v 3800453 ##r 1000 #b 友谊点数")
        if  sm.getFriendPoints() <= 1000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()

        elif  sm.getMesos() < 50000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()

        elif not sm.canHold(1202086):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()

        else:
            sm.deductFriendPoints(1000)
            sm.deductMesos(50000000)
            sm.giveItem(1202086)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 3:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202085 # #z 1202085 ##k 吗？\r\n\r\n#b#v 1202086 # #t 1202086 #\r\n\r\n#b#v 4031138 # #r50,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  1000 #b 友谊点数")
        if  sm.getFriendPoints() < 1000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()

        elif  sm.getMesos() < 50000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()

        elif not sm.hasItem(1202086):
            sm.sendSayOkay("你没有 #b#v 1202086 # #t 1202086 #。")
            sm.dispose()

        elif not sm.canHold(1202085):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()

        else:
            sm.deductFriendPoints(1000)
            sm.consumeItem(1202086)
            sm.deductMesos(50000000)
            sm.giveItem(1202085)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 4:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202084 # #z 1202084 ##k 吗？\r\n\r\n#b#v 1202085 # #t 1202085 #\r\n\r\n#b#v 4031138 # #r50,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  1000 #b 友谊点数")
        if  sm.getFriendPoints() < 1000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()

        elif not sm.hasItem(1202085):
            sm.sendSayOkay("你没有 #b#v 1202085 # #t 1202085 #。")
            sm.dispose()

        elif  sm.getMesos() < 50000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()

        elif not sm.canHold(1202084):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()

        else:
            sm.deductFriendPoints(1000)
            sm.consumeItem(1202085)
            sm.deductMesos(50000000)
            sm.giveItem(1202084)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 5:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202083 # #z 1202083 ##k 吗？\r\n\r\n#b#v 1202084 # #t 1202084 #\r\n\r\n#b#v 4031138 # #r50,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  1000 #b 友谊点数")
        if  sm.getFriendPoints() < 1000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()

        elif  sm.getMesos() < 50000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()

        elif not sm.hasItem(1202084):
            sm.sendSayOkay("你没有 #b#v 1202084 # #t 1202084 #。")
            sm.dispose()

        elif not sm.canHold(1202083):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()

        else:
            sm.deductFriendPoints(1000)
            sm.deductMesos(50000000)
            sm.consumeItem(1202084)
            sm.giveItem(1202083)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 6:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202124 # #z 1202124 ##k 吗？\r\n\r\n#b#v 1202083 # #t 1202083 #\r\n\r\n#b#v 4031138 # #r100,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  5000 #b 友谊点数")
        if  sm.getFriendPoints() < 5000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 100000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202083):
            sm.sendSayOkay("你没有 #b#v 1202083 # #t 1202083 #。")
            sm.dispose()
        elif not sm.canHold(1202124):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(5000)
            sm.deductMesos(100000000)
            sm.consumeItem(1202083)
            sm.giveItem(1202124)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 7:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202089 # #z 1202089 ##k 吗？\r\n\r\n#b#v 1202124 # #t 1202124 #\r\n\r\n#b#v 4031138 # #r100,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  6000 #b 友谊点数")
        if  sm.getFriendPoints() < 6000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 100000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202124):
            sm.sendSayOkay("你没有 #b#v 1202124 # #t 1202124 #。")
            sm.dispose()
        elif not sm.canHold(1202094):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(6000)
            sm.deductMesos(100000000)
            sm.consumeItem(1202124)
            sm.giveItem(1202089)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 8:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202090 # #z 1202090 ##k 吗？\r\n\r\n#b#v 1202124 # #t 1202124 #\r\n\r\n#b#v 4031138 # #r100,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  6000 #b 友谊点数")
        if  sm.getFriendPoints() < 6000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202124):
            sm.sendSayOkay("你没有 #b#v 1202124 # #t 1202124 #。")
            sm.dispose()
        elif not sm.canHold(1202090):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(6000)
            sm.deductMesos(100000000)
            sm.consumeItem(1202124)
            sm.giveItem(1202090)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 9:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202091 # #z 1202091 ##k 吗？\r\n\r\n#b#v 1202124 # #t 1202124 #\r\n\r\n#b#v 4031138 # #r100,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  6000 #b 友谊点数")
        if  sm.getFriendPoints() < 6000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 100000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202124):
            sm.sendSayOkay("你没有 #b#v 1202124 # #t 1202124 #。")
            sm.dispose()
        elif not sm.canHold(1202091):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(6000)
            sm.deductMesos(100000000)
            sm.consumeItem(1202124)
            sm.giveItem(1202091)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 10:
        selection = sm.sendAskYesNo("你想购买 #b#v 1182162 # #z 1182162 ##k 吗？\r\n\r\n#b#v 1202124 # #t 1202124 #\r\n\r\n#b#v 4031138 # #r100,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  6000 #b 友谊点数")
        if  sm.getFriendPoints() < 6000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 100000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202124):
            sm.sendSayOkay("你没有 #b#v 1202124 # #t 1202124 #。")
            sm.dispose()
        elif not sm.canHold(1182162):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(6000)
            sm.consumeItem(1202124)
            sm.deductMesos(100000000)
            sm.giveItem(1182162)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 11:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202094 # #z 1202094 ##k 吗？\r\n\r\n#b#v 1202089 # #t 1202089 #\r\n\r\n#b#v 4031138 # #r250,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  30000 #b 友谊点数")
        if  sm.getFriendPoints() < 10000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 250000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202089):
            sm.sendSayOkay("你没有 #b#v 1202089 # #t 1202089 #。")
            sm.dispose()
        elif not sm.canHold(1202094):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(10000)
            sm.consumeItem(1202089)
            sm.deductMesos(250000000)
            sm.giveItem(1202094)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 12:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202095 # #z 1202095 ##k 吗？\r\n\r\n#b#v 1202089 # #t 1202089 #\r\n\r\n#b#v 4031138 # #r250,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  30000 #b 友谊点数")
        if  sm.getFriendPoints() < 10000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 250000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202089):
            sm.sendSayOkay("你没有 #b#v 1202089 # #t 1202089 #。")
            sm.dispose()
        elif not sm.canHold(1202095):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(10000)
            sm.consumeItem(1202089)
            sm.deductMesos(250000000)
            sm.giveItem(1202095)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 13:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202096 # #z 1202096 ##k 吗？\r\n\r\n#b#v 1202089 # #t 1202089 #\r\n\r\n#b#v 4031138 # #r250,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  30000 #b 友谊点数")
        if  sm.getFriendPoints() < 10000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 250000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202089):
            sm.sendSayOkay("你没有 #b#v 1202089 # #t 1202089 #。")
            sm.dispose()
        elif not sm.canHold(1202096):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(10000)
            sm.consumeItem(1202089)
            sm.deductMesos(250000000)
            sm.giveItem(1202096)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 14:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202097 # #z 1202097 ##k 吗？\r\n\r\n#b#v 1202089 # #t 1202089 #\r\n\r\n#b#v 4031138 # #r250,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  30000 #b 友谊点数")
        if  sm.getFriendPoints() < 10000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 250000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202089):
            sm.sendSayOkay("你没有 #b#v 1202089 # #t 1202089 #。")
            sm.dispose()
        elif not sm.canHold(1202097):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(10000)
            sm.consumeItem(1202089)
            sm.deductMesos(250000000)
            sm.giveItem(1202097)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 15:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202050 # #z 1202050 ##k 吗？\r\n\r\n#b#v 1202094 # #t 1202094 #\r\n\r\n#b#v 4031138 # #r250,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  15000 #b 友谊点数")
        if  sm.getFriendPoints() < 15000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 250000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202094):
            sm.sendSayOkay("你没有 #b#v 1202124 # #t 1202124 #。")
            sm.dispose()
        elif not sm.canHold(1202050):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(15000)
            sm.consumeItem(1202094)
            sm.giveItem(1202050)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 16:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202054 # #z 1202054 ##k 吗？\r\n\r\n#b#v 1202095 # #t 1202095 #\r\n\r\n#b#v 4031138 # #r250,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  15000 #b 友谊点数")
        if  sm.getFriendPoints() < 15000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 250000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202095):
            sm.sendSayOkay("你没有 #b#v 1202095 # #t 1202095 #。")
            sm.dispose()
        elif not sm.canHold(1202054):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(15000)
            sm.consumeItem(1202095)
            sm.deductMesos(250000000)
            sm.giveItem(1202054)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 17:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202058 # #z 1202058 ##k 吗？\r\n\r\n#b#v 1202097 # #t 1202097 #\r\n\r\n#b#v 4031138 # #r250,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  15000 #b 友谊点数")
        if  sm.getFriendPoints() < 15000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 250000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202097):
            sm.sendSayOkay("你没有 #b#v 1202097 # #t 1202097 #。")
            sm.dispose()
        elif not sm.canHold(1202058):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(15000)
            sm.consumeItem(1202097)
            sm.deductMesos(250000000)
            sm.giveItem(1202058)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 18:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202062 # #z 1202062 ##k 吗？\r\n\r\n#b#v 1202096 # #t 1202096 #\r\n\r\n#b#v 4031138 # #r250,000,000 #b金币\r\n\r\n#b#v 3800453 ##r  15000 #b 友谊点数")
        if  sm.getFriendPoints() < 15000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 250000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif not sm.hasItem(1202096):
            sm.sendSayOkay("你没有 #b#v 1202096 # #t 1202096 #。")
            sm.dispose()
        elif not sm.canHold(1202062):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(15000)
            sm.consumeItem(1202096)
            sm.deductMesos(250000000)
            sm.giveItem(1202062)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()

    if selection == 19:
        selection = sm.sendAskYesNo("你想购买 #b#v 1202236 # #z 1202236 ##k 吗？\r\n我的价格不便宜，这是我需要的。\r\n\r\n#b#v 4460005 # #t 4460005 #\r\n\r\n#b#v 1202062 # #t 1202062 #\r\n\r\n#b#v 1202058 # #t 1202058 #\r\n\r\n#b#v 1202054 # #t 1202054 #\r\n\r\n#b#v 1202050 # #t 1202050 #\r\n\r\n#b#v 4031138 # #r1,000,000,000 #b金币\r\n\r\n#v 4031866 # #r10,000,000 #bNX\r\n\r\n#v 3800453 ##r  500000 #b 友谊点数")
        if  sm.getFriendPoints() < 500000:
            sm.sendSayOkay("你的#b友谊点数#k不足。")
            sm.dispose()
        elif  sm.getMesos() < 1000000000:
            sm.sendSayOkay("你的#b金币#k不足。")
            sm.dispose()
        elif  sm.getNX() < 10000000:
            sm.sendSayOkay("你的#bNX#k不足。")
            sm.dispose()
        elif not sm.hasItem(4460005):
            sm.sendSayOkay("你没有 #b#v 1202062 # #t 1202062 #。")
            sm.dispose()
        elif not sm.hasItem(1202058):
            sm.sendSayOkay("你没有 #b#v 1202058 # #t 1202058 #。")
            sm.dispose()
        elif not sm.hasItem(1202054):
            sm.sendSayOkay("你没有 #b#v 1202054 # #t 1202054 #。")
            sm.dispose()
        elif not sm.hasItem(1202050):
            sm.sendSayOkay("你没有 #b#v 1202050 # #t 1202050 #。")
            sm.dispose()
        elif not sm.hasItem(1202062):
            sm.sendSayOkay("你没有 #b#v 1202050 # #t 1202050 #。")
            sm.dispose()
        elif not sm.canHold(1202236):
            sm.sendSayOkay("请确保你的背包有空间。")
            sm.dispose()
        else:
            sm.deductFriendPoints(500000)
            sm.deductMesos(1000000000)
            sm.deductNX(10000000)
            sm.consumeItem(1202050)
            sm.consumeItem(1202054)
            sm.consumeItem(1202058)
            sm.consumeItem(1202062)
            sm.consumeItem(4460005)
            sm.giveItem(1202236)
            sm.sendSayOkay("感谢你的购买！")
            sm.dispose()
