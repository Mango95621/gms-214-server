response = sm.sendAskYesNo("你想去万神殿吗？")

if response:
    sm.warp(400000001, 1)
