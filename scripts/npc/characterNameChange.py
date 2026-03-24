# Mr.Newname (ID: 902016)

if chr.getLevel() < 33:
    sm.sendSayOkay("你可以从33级开始使用 #i4034803##b#t4034803##k。请至少达到33级后再试。")
elif sm.hasItem(4034803):
    sm.openUI(1110)
else:
    sm.sendSayOkay("你需要一个 #i4034803##b#t4034803##k 来更改你的名字。")
