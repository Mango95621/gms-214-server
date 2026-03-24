# [Job Adv] Level 30 Magician

sm.setSpeakerID(1012100)

if (sm.getJob() != "MAGICIAN"):
    sm.sendSayOkay("走吧走吧")
else:
    message = "恭喜你达到30级！好了，快选择职业吧\r\n\r\n"
    message += "#b#L0#火与毒之路#l\r\n"
    message += "#b#L1#冰与雷之路#l\r\n"
    message += "#b#L2#牧师之路#l\r\n"

    choice = sm.sendNext(message)

    if choice == 0:
        sm.jobAdvance(210)
        sm.sendNext("好了，你放火和毒")
    elif choice == 1:
        sm.jobAdvance(220)
        sm.sendNext("哇，冰霜")
    elif choice == 2:
        sm.jobAdvance(230)
        sm.sendNext("好了，现在会治疗了")
