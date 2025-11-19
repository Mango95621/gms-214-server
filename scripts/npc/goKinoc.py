# Created by MechAviv
# Map ID :: 100000000
# NPC ID :: 9110000
# Perry
maps = [["昭和镇", 100000000], ["忍者城堡", 100000000], ["六道路口", 100000000]]# TODO
sm.setSpeakerID(9110000)
selection = sm.sendNext("欢迎，要去哪儿?\r\n#L0# 前往昭和镇#l\r\n#L1# 前往忍者城堡#l\r\n#L2# 通往六道路口#l")


sm.setSpeakerID(9110000)
if sm.sendAskYesNo(maps[selection][0] + "? 安全驾驶!"):
    sm.warp(maps[selection][1])
else:
    sm.setSpeakerID(9110000)
    sm.sendNext("我觉得这次旅行不会太不舒服。不收车费，我无法升级座位。")


