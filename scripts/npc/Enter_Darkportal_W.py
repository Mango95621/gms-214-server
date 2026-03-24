# Demon's Doorway (9201128) | Big Rocky Road

quest = 28179   # Treasure, and Andras the Demon  Quest
mapid = 677000004   # Andras Strolling Path (Map before Boss Map)

if sm.hasQuest(quest):
    if sm.sendAskYesNo("你想进入吗？"):
        sm.warp(mapid, 0)
else:
    sm.sendSayOkay("#b(一扇奇怪的门)")
