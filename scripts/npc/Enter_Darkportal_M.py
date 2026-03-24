# Demon's Doorway (9201129) | Close to the Sky

quest = 28198   # Treasure, and Marbas the Demon  Quest
mapid = 677000000   # Marbas Strolling Path (Map before Boss Map)

if sm.hasQuest(quest):
    if sm.sendAskYesNo("你想进入吗？"):
        sm.warp(mapid, 0)
else:
    sm.sendSayOkay("#b(一扇奇怪的门)")
