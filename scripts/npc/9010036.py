from net.swordie.ms.scripts import ScriptUtil as su

# NX Item NPC \ Lilin \ 9010036 \ Free Market

cubes = { #[itemid, price, expiration time]
    0 : [2711000, 750, 0],
    1 : [2711003, 2000, 0],
    2 : [5062001, 4000, 0],
    3 : [5062009, 11000, 0],
    4 : [2711004, 15000, 0],
    5 : [5062005, 20000, 0],
    6 : [5062006, 30000, 0],
    7 : [5062500, 30000, 0],
    8 : [2702000, 250, 0],
    9 : [5062800, 4000, 0],
}

scrolls = { #[itemid, price]
    0 : [2049300, 250000, 0],
    1 : [2049301, 10000, 0],
    2 : [2049419, 15000, 0],
    3 : [2048305, 180000, 0],
    4 : [2048306, 300000, 0],
    5 : [2049100, 2500, 0],
    6 : [2048079, 7000, 0],
    7 : [2048080, 7000, 0],
}

scrollingTools = { #[itemid, price]
    0 : [5610000, 5000, 0],
    1 : [5610001, 6000, 0],
    2 : [2532000, 25000, 0],
    3 : [2531000, 50000, 0],
    4 : [2530000, 17500, 0],
    5 : [5068000, 17500, 0],
    6 : [2470003, 8000, 0],
}

GameEnhancing = {
    0 : [5133000, 1000, 0],
    1 : [5610001, 6000, 0],
    2 : [2532000, 25000, 0],
    3 : [2531000, 50000, 0],
    4 : [2530000, 17500, 0],
    5 : [5068000, 17500, 0],
    6 : [2470003, 8000, 0],
}
hiredMerchants = {
    0 : [5030000, 7000, 24],
    1 : [5030000, 28000, 168],
    2 : [5030000, 42000, 336],
}

messagingItems = {
    0 : [5072000, 2000, 0],
    1 : [5077000, 10000, 0],
    2 : [5076000, 10000, 0],
}

etcItems = {
    0 : [2434327, 10000, 0],
    1 : [2434326, 15000, 0],
    2 : [2434325, 20000, 0],
    3 : [2502000, 1000, 0],
}

gach = {
    0 : [5220000, 1500, 0],
    1 : [5220100, 30000, 0]
}

coupons = {
    0 : [2434257, 4000, 0],
    1 : [2430768, 4000, 0],
    2 : [2430769, 4000, 0],
    3 : [2430771, 4000, 0],
    4 : [2430770, 4000, 0],
    5 : [2350000, 4000, 0]
}

if sm.sendNext:
    selection = sm.sendNext("你好，我叫莉莉安，这是你可以消费#bNX#k的地方。\r\n"
                            "\r\n#e你有#r " + str(sm.getNX()) + " #bNX。\r\n#n#b"
                            "#L0#方块\r\n"
                            "#L1#卷轴\r\n"
                            "#L2#强化工具\r\n"
                            "#L3#游戏增强\r\n"
                            "#L4#雇佣商人\r\n"
                            "#L5#其他\r\n"
                            "#L6#消息\r\n"
                            "#L7#冒险岛\r\n"
                            "#L8#扩展槽位\r\n")

    items = []
    if selection == 0:
        items = cubes
    elif selection == 1:
        items = scrolls
    elif selection == 2:
        items = scrollingTools
    elif selection == 3:
        items = GameEnhancing
    elif selection == 4:
        items = hiredMerchants
    elif selection == 5:
        items = etcItems
    elif selection == 6:
        items = messagingItems
    elif selection == 7:
        items = gach
    elif selection == 8:
        items = coupons

    output = "选择你想购买的物品 \r\n"
    for x in range (len(items)):
        output += "#b" + su.addSelectItem(x) + su.getItemImg(items[x][0]) + "   " + su.getItemName(items[x][0]) + " #r#e(" + str(items[x][1]) + ") NX#n"
        if items[x][2] > 0:
            output += " 持续 " + str(items[x][2] / 24) + " 天"
        output += "\r\n"
    selection = sm.sendNext(output)
    itemId = items[selection][0]
    text = "你想购买多少个 #r" + su.getItemName(itemId) + " #b？"
    amount = sm.sendAskNumber(text, 1, 1, 1000)
    totalPrice = items[selection][1] * amount
    answer = sm.sendAskYesNo("你确定要购买 " + str(amount) + " 个 #b" + su.getItemName(itemId) + " #k 吗？需要 #r(" + str(totalPrice) + ") NX")
    if answer and sm.canHold(itemId, amount) and chr.getUser().getMaplePoints() >= totalPrice:
        sm.giveItem(itemId, amount, items[selection][2])
        chr.addNx(-totalPrice)
    else:
        sm.sendNext("你的NX不足或背包空间不够")
