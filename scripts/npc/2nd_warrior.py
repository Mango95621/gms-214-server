# [Job Adv] Level 30 Warrior

sm.setSpeakerID(1012100)

if (sm.getJob() != "WARRIOR"):
    sm.sendSayOkay("走吧走吧")
else:
    message = "恭喜你达到30级！好了，快选择职业吧\r\n\r\n"
    message += "#b#L0#战士之路#l\r\n"
    message += "#b#L1#准骑士之路#l\r\n"
    message += "#b#L2#枪手之路#l\r\n"

    choice = sm.sendNext(message)

    if choice == 0:
        sm.jobAdvance(110)
        sm.sendNext("好了，你用剑")
    elif choice == 1:
        sm.jobAdvance(120)
        sm.sendNext("好了，你用枪")
    elif choice == 2:
        sm.jobAdvance(130)
        sm.sendNext("好了，你用大锤子")
