# Mastema (2450017) | Demon 4th job advancement
sm.setSpeakerID(parentID)
if sm.getChr().getLevel() >= 100 \
        and sm.getChr().getJob() == 3111 \
        and sm.sendAskYesNo("你准备好了吗，#h #？如果你准备好了，我会通过时间裂缝把你送到过去。 "
                            "你在过去很强大，#h #，所以要小心。"):
        
        sm.sendNext("祝你好运，#h #")
        sm.warpInstanceIn(927000100, False)
