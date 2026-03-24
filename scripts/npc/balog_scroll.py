# Suspicious Man (1061016) | Stairway to the Underground Temple

items = [
2040728,
2040729,
2040730,
2040731,
2040732,
2040733,
2040734,
2040735,
2040736,
2040737,
2040738,
2040739
]
balrogLeather = 4001261

if sm.hasItem(balrogLeather):
    sm.sendNext("你好 #h0#。我看到你有 #c"+ str(balrogLeather) +"# 块"+ ("s" if sm.getQuantityOfItem(balrogLeather) > 1 else "") +"巴洛古皮革，有兴趣交换成物品吗？")
else:
    sm.sendNext("你好 #h0#。我可以交换 #z"+str(balrogLeather)+"# 成物品")


selString = "好的，这是我可以提供给你的\r\n#b"
i = 0
while i < len(items):
    selString += "#L"+ str(i) +"##z"+ str(items[i]) +"##l\r\n"
    i += 1
selection = sm.sendNext(selString)

quantity = sm.sendAskNumber("你愿意用多少 #b#z"+ str(balrogLeather) +"##k 来交换我的 #b#z"+ str(items[selection]) +"##k？"
                 "\r\n你有 #c"+ str(balrogLeather) +"# 块"+ ("s" if sm.getQuantityOfItem(balrogLeather) > 1 else "") +"巴洛古皮革", 1, 1, 100)

if not sm.canHold(items[selection]):
    sm.sendSayOkay("你的背包空间不足。")
elif sm.getQuantityOfItem(balrogLeather) < quantity:
    sm.sendSayOkay("你骗不了我\r\n你没有足够的皮革块。")
else:
    sm.giveItem(items[selection], quantity)
    sm.consumeItem(balrogLeather, quantity)
    sm.sendSayOkay("感谢你的兑换")
