# 140090000
LILIN = 1202000

if not "helper=clear" in sm.getQRValue(21019):
    sm.setSpeakerID(LILIN)
    sm.flipSpeaker()
    sm.sendNext("你终于醒来了...！")

    sm.setPlayerAsSpeaker()
    sm.sendSay("你是...？")

    sm.setSpeakerID(LILIN)
    sm.flipSpeaker()
    sm.sendSay("与黑魔法师战斗的英雄...我一直等待着你醒来！")

    sm.setPlayerAsSpeaker()
    sm.sendSay("谁... 你是谁？你在说什么？")
    sm.sendSay("我是谁...？我什么都记不起来... 哎呀，我的头好痛！")

    sm.reservedEffect("Effect/Direction1.img/aranTutorial/face")
    sm.addQRValue(21019, "helper=clear")
else:
    sm.setSpeakerID(LILIN)
    sm.flipSpeaker()
    sm.sendNext("你还好吗？")

    sm.setPlayerAsSpeaker()
    sm.sendSay("我什么都记不起来了。我在哪里？你又是谁...？")

    sm.setSpeakerID(LILIN)
    sm.flipSpeaker()
    sm.sendSay(
        "保持冷静。没有必要惊慌。你什么都记不起来是因为黑魔法师的诅咒抹去了你的记忆。我会告诉你需要知道的一切...一步一步来。")
    sm.sendSay(
        "你是一个英雄，在数百年前与黑魔法师战斗并拯救了枫叶世界。但在最后一刻， "
        "黑魔法师的诅咒让你睡了很长很长的时间。那就是你失去所有记忆的原因。")
    sm.sendSay(
        "这个岛叫做瑞恩，是黑魔法师困住你的地方。尽管它的名字，这个岛因为黑魔法师的诅咒而常年被冰雪覆盖。你是在冰窟深处被发现的。")
    sm.sendSay(
        "我叫莉莉安，属于瑞恩部族。瑞恩部族一直等待着一个英雄的归来，现在我们终于找到了你。你终于回来了！")
    sm.sendSay(
        "我说得太多了。如果你不能完全理解我刚才告诉你的那些也没关系。你最终会明白的。现在，#b你应该前往城镇#k。我会留在你身边帮助你直到你到达那里。")
    sm.hireTutor(True)
    sm.warp(140090100, 1)
