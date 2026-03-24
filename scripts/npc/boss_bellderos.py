answer = sm.sendSay("你想去哪里？#b \r\n#L0#维德罗斯的客厅#l\r\n#L1#继续前往马格努斯#l\r\n#L2#锻造龙王遗物\r\n#L3#算了#l")

# sm.chat("Response was " + str(response) + "\r\rAnswer was " + str(answer))
if answer == 0:
    if sm.getParty() is None:
        sm.sendSay("请先创建一个队伍再进去。")
    elif not sm.isPartyLeader():
        sm.sendSay("请让你的队伍队长进入，如果你想挑战维德罗斯的话。")
    elif sm.checkParty():
        sm.warpInstanceIn(401053100, True)
elif answer == 1:
    sm.warp(401060000)
elif answer == 2:
    if not sm.hasItem(4033403):
        sm.sendSayOkay("你没有 #v4033403# #b#z4033403##k。")
        sm.dispose()
    elif not sm.hasItem(4033404):
        sm.sendSayOkay("你没有 #v4033404# #b#z4033404##k。")
        sm.dispose()
    elif not sm.hasItem(4033405):
        sm.sendSayOkay("你没有 #v4033405# #b#z4033405##k。")
        sm.dispose()
    elif not sm.canHold(4033406):
        sm.sendSayOkay("请先在背包里腾出空间。")
        sm.dispose()
    else:
        sm.consumeItem(4033403)
        sm.consumeItem(4033404)
        sm.consumeItem(4033405)
        sm.giveItem(4033406)
        sm.chat("你获得了一个龙王遗物")
        sm.dispose()
