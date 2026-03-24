answer = sm.sendSay("你准备好面对 #b特雷格洛#k 了吗？#b\r\n#L0#进入特雷格洛的实验室#l")

if answer == 0:
    if sm.getParty() is None:
        sm.sendSay("请先创建一个队伍再进去。")
    elif not sm.isPartyLeader():
        sm.sendSay("请让你的队伍队长进入，如果你想挑战特雷格洛的话。")
    elif sm.checkParty():
        sm.warpInstanceIn(401052200, True)
