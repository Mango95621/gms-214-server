answer = sm.sendSay("你准备好面对 #b维克托#k 了吗？#b\r\n#L0#进入维克托的工作坊#l")

if answer == 0:
    if sm.getParty() is None:
        sm.sendSay("请先创建一个队伍再进去。")
    elif not sm.isPartyLeader():
        sm.sendSay("请让你的队伍队长进入，如果你想挑战维克托的话。")
    elif sm.checkParty():
        sm.warpInstanceIn(401051200, True)
