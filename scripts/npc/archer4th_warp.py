# Bowman 4th Job NPC Warp Script

MANON_PREV_MAP = 240020400
GRIFFEY_PREV_MAP = 240020100
MANONS_DARK_FOREST = 924000200
DARK_GRIFFEY_FOREST = 924000201


sm.setSpeakerID(parentID)
sm.sendNext("你有成为英雄的潜质吗？唯一能找到答案的方法就是采取行动...")
if not sm.hasQuest(1455):
    sm.dispose()

selection = sm.sendNext("如果你同意参加这个测试，我会送你去莫恩和格里菲。当然，如果你有能力自己访问莫恩森林或格里菲森林，请随意。你想怎么做？\r\n\r\n#L0##b请送我去莫恩森林。\r\n#L1#请送我去格里菲森林。#l\r\n#L2#没什么。我会自己去的。#l#n")
if selection == 0:
    sm.sendNext("你想去莫恩森林吗？我会送你去那里。如果你找不到另一个怪物，自己回来找我。")
    sm.warpInstanceIn(MANONS_DARK_FOREST, False)
elif selection == 1:
    sm.sendNext("你想去格里菲森林吗？我会送你去那里。如果你找不到另一个怪物，自己回来找我。")
    sm.warpInstanceIn(DARK_GRIFFEY_FOREST, False)
