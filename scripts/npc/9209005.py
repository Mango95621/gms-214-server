# Fishing Npc (9209005 Tae Gong)

from net.swordie.ms.constants import GameConstants

FISH_NET = 2270008
NET_COST = 3000000

FISHING_MAP = GameConstants.FISHING_MAP

opts = ["前往钓鱼地图", "购买渔网", "兑换", "兑换", "兑换"]
menu = sm.sendNext("你想做什么？\r\n#b" + sm.menu(opts) + "#k")

def exchangeFish(opt):
    sm.sendNext("待完成：")

if menu == 0:
    sm.warp(FISHING_MAP)
elif menu == 1:
    if sm.sendAskYesNo("需要 " + str(NET_COST) + 金币来购买120个渔网。你想要购买吗？"):
        if sm.getMesos() >= NET_COST and sm.canHold(FISH_NET):
            sm.deductMesos(NET_COST)
            sm.giveItem(FISH_NET, 120)
            sm.sendSayOkay("钓鱼愉快！")
        else:
            sm.sendNext("看起来你的金币不足或背包空间不足。")
elif menu >= 2 and menu <= 4:
    exchangeFish(menu)
