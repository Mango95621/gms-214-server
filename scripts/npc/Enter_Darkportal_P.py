# Demon's Doorway (9201132) | Ribbon Pig Beach

quest = 28256   # Treasure, and Crocell the Demon  Quest
mapid = 677000006   # Crocell Strolling Path (Map before Boss Map)

if sm.hasQuest(quest):
    if sm.sendAskYesNo("你想进入吗？"):
        sm.warp(mapid, 0)
else:
    sm.sendSayOkay("#b(一扇奇怪的门)")
