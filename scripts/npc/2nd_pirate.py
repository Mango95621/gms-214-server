# [Job Adv] Level 30 Pirate

sm.setSpeakerID(1012100)

if (sm.getJob() != "PIRATE"):
    sm.sendSayOkay("走吧走吧")
else:
    message = "恭喜你达到30级！好了，快选择职业吧\r\n\r\n"
    message += "#b#L0#海上拳手#l\r\n"
    message += "#b#L1#七海枪手#l\r\n"

    choice = sm.sendNext(message)

    if choice == 0:
        sm.jobAdvance(510)
        sm.sendNext("好了，你用拳")
    elif choice == 1:
        sm.jobAdvance(520)
        sm.sendNext("好了，你用枪")
