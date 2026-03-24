# Created by MechAviv
# ID :: [4000021]
# Maple Road : Entrance to Adventurer Training Center

sm.setSpeakerID(12100)
selection = sm.sendNext("这是训练你基本技能的完美地方。你想在哪里训练？\r\n#b#L0#冒险者训练中心 1#l\r\n#b#L1#冒险者训练中心 2#l\r\n#b#L2#冒险者训练中心 3#l\r\n#b#L3#冒险者训练中心 4#l")
if selection == 0:
    sm.warp(4000022, 4)
elif selection == 1:
    sm.warp(4000023, 4)
elif selection == 2:
    sm.warp(4000024, 4)
elif selection == 3:
    sm.warp(4000025, 4)
