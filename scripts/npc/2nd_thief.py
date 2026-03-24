# [Job Adv] Level 30 Thief

sm.setSpeakerID(1012100)

if (sm.getJob() != "MAGICIAN"):
    sm.sendSayOkay("走吧走吧")
else:
    message = "恭喜你达到30级！好了，快选择职业吧\r\n\r\n"
    message += "#b#L0#刺客之路#l\r\n"
    message += "#b#L1#侠客之路#l\r\n"

    choice = sm.sendNext(message)

    if choice == 0:
        sm.jobAdvance(410)
        sm.sendNext("好了，你是刺客")
    elif choice == 1:
        sm.jobAdvance(420)
        sm.sendNext("好了，你是侠客")
