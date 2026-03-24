# [Job Adv] Level 30 Bowman

sm.setSpeakerID(1012100)

if (sm.getJob() != "BOWMAN"):
    sm.sendSayOkay("走吧走吧")
else:
    message = "恭喜你达到30级！好了，快选择职业吧\r\n\r\n"
    message += "#b#L0#猎人之路#l\r\n"
    message += "#b#L1#弩弓手之路#l\r\n"

    choice = sm.sendNext(message)

    if choice == 0:
        sm.jobAdvance(310)
        sm.sendNext("好了，你现在弓箭手了")
    elif choice == 1:
        sm.jobAdvance(320)
        sm.sendNext("好了，你现在用弩了")
