sel = sm.sendSayOkay("你好朋友，今天我能为你做什么？\r\n\r\n#L0#保卫梦境#l\r\n#L1#挑战路西德#l")
if sel == 0:
    sm.sendSayOkay("Alan 请添加梦境守护者")
else:
    if sm.getParty() is None:
        sm.sendSay("请先创建一个队伍再进去。")
    elif not sm.isPartyLeader():
        sm.sendSay("请让你的队伍队长进入，如果你想挑战路西德的话。")
    elif sm.checkParty():
        sm.warpInstanceIn(450004150, True)
