# Vote Item NPC \ Cygnus \ 9010034 \ Free Market

VoteShop = { #[itemid, price, expiration time]
    0 : [5211067, 5, 24],
    1 : [5211068, 2, 1],
    2 : [5360042, 1, 2],
    3 : [5211068, 5, 4],
    4 : [5360042, 2, 4],
    5 : [5211068, 7, 12],
    6 : [5360042, 3, 6],
    7 : [5211060, 20, 24],
    8 : [5211046, 10, 3],
    9 : [5050100, 10, 0],
    10 : [5051001, 5, 0],
    11 : [2023604, 4, 0],
    12 : [2023380, 5, 0],
    13 : [1122171, 6, 12],
    14 : [1122219, 5, 72],
    15 : [1122219, 10, 168],
    16 : [2022035, 4, 24],

}

votePrice = 1
votecoinId = 4310195
secondaryPendantPrice = 20

if sm.sendNext:
    selection = sm.sendNext("你好，我叫赛克斯，这是你可以消费#b投票点数#k的地方。\r\n"
                            "\r\n#e你有 #r " + str(sm.getVotePoints()) + " #b投票点数。\r\n#n#b"
                            "#L0#我想用投票点数兑换投票硬币\r\n"
                            "#L1#我想用投票硬币兑换投票点数\r\n"
                            "#L2#我想从投票商店购买物品\r\n"
                            "#L3#我想购买7天副项链槽位（角色）\r\n")

    items = []
    if selection == 0:
        amount = sm.sendAskNumber("#b#e一个投票硬币需要 #r(1)#b 投票点数。\r\n"
                                  "你目前有 #e#r" + str(sm.getVotePoints()) + " #b投票点数\r\n"
                                                                                            "#k#e你想兑换多少个？", 1, 1, 100)
        price = amount * votePrice
        if sm.getVotePoints() >= price and chr.canHold(votecoinId, amount):
            sm.deductVotePoints(price)
            sm.giveItem(votecoinId, amount)
            sm.dispose()
        else:
            sm.sendNext("你的#b投票点数#k不足，或者你的背包没有足够空间放置这个物品。")
            sm.dispose()

    elif selection == 1:
        amount = sm.sendAskNumber("#b#e一个投票点数需要 #r(1)#b 投票硬币。\r\n"
                                  "你目前有 #r" + str(sm.getQuantityOfItem(votecoinId)) + " #b投票硬币。\r\n"
                                                                                                 "#k你想兑换多少个？", 1, 1, 100)
        if sm.getQuantityOfItem(votecoinId) >= amount:
            sm.deductVotePoints(votePrice * amount)
            chr.consumeItem(votecoinId, amount);
            sm.dispose()
        else:
            sm.sendNext("你的投票硬币不足以进行这次兑换。")
            sm.dispose()

    elif selection == 2:
        items = VoteShop
    elif selection == 3:
        answer = sm.sendAskYesNo("你确定要用 #r" + str(secondaryPendantPrice) + "#b 投票点数#k 购买一个永久副项链槽位吗？")
        if answer and sm.getVotePoints() >= secondaryPendantPrice:
            if sm.setSecondaryPendantDateInXDays(7):
                sm.deductVotePoints(secondaryPendantPrice)
                sm.sendSayOkay("请重新登录以使副项链槽位生效。")
                sm.dispose()
            else:
                sm.sendSayOkay("你已经拥有一个副项链槽位了")
                sm.dispose()
        else:
            sm.sendNext("你的#b投票点数#k不足。")
            sm.dispose()
