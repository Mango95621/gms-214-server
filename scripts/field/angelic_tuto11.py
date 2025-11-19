# Created by MechAviv
# Map ID :: 940011110
# Eastern Region of Pantheon : East Sanctum

# [SET_DRESS_CHANGED] [01 00 ]
sm.curNodeEventEnd(True)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(True, True, False, False)
sm.forcedInput(0)
sm.forcedInput(2)
sm.sendDelay(60)


sm.forcedInput(0)
sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg1/2", 1200, 0, -120, -2, -2, False, 0)
sm.sendDelay(1200)


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("天啊，你看起来太棒了！看看那双腿！还有那头发！还有你的——你为什么那样看着我？")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("我-我穿的是什么？！我的裤子在哪里？！")
# Unhandled User Effect [PlaySoundWithMuteBGM] Packet: 23 15 00 56 6F 69 63 65 2E 69 6D 67 2F 41 6E 67 65 6C 69 63 5F 46 2F 31


OBJECT_1 = sm.sendNpcController(3000119, 150, 220)
sm.showNpcSpecialActionByObjectId(OBJECT_1, "summon", 0)
sm.sendDelay(90)


OBJECT_2 = sm.sendNpcController(3000115, 250, 220)
sm.showNpcSpecialActionByObjectId(OBJECT_2, "summon", 0)
sm.sendDelay(90)


OBJECT_3 = sm.sendNpcController(3000111, 350, 220)
sm.showNpcSpecialActionByObjectId(OBJECT_3, "summon", 0)
sm.sendDelay(90)


sm.setSpeakerID(3000119)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("在那里！那个女孩手臂上有圣物！")


sm.setSpeakerID(3000115)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("我们真的需要伤害像她这样漂亮的小东西吗？圣物已经离开了圣殿，不会给我们带来任何麻烦。")


sm.setSpeakerID(3000119)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("别傻了！我们不能让某个小傻瓜抢走我们的功劳！")


sm.setSpeakerID(3000111)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("我-我很抱歉，嗯，女士，你能把那个圣物给我吗？")


sm.setSpeakerID(3000111)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("你就是我之前看到的那些变态之一！")


sm.setSpeakerID(3000111)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("嗯，与其说是'变态'，更像是解放者。听着，也许你可以把你那个漂亮的手镯给我一会儿，我可以带你出去吃晚餐...")


sm.setSpeakerID(3000111)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("不可能，你这个老怪人！我甚至没法把这个东西从我手臂上弄下来。")


sm.setSpeakerID(3000119)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("你能不能停止调情？！抓住那个傻瓜，我们离开这里！")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendSay("#h0#！现在是狠狠教训他们的时候了。")


sm.setSpeakerID(3000132)
sm.removeEscapeButton()
sm.flipDialoguePlayerAsSpeaker()
sm.setSpeakerType(3)
sm.sendSay("我-我该怎么做？！")


sm.showEffect("Effect/Direction10.img/effect/tuto/BalloonMsg1/3", 900, 30, -70, -2, -2, False, 0)
sm.sendDelay(900)


sm.setSpeakerID(3000119)
sm.removeEscapeButton()
sm.setSpeakerType(3)
sm.sendNext("你这可爱的小脑袋里究竟在酝酿什么疯狂的鬼点子？走吧！咱们出发！")


sm.sendDelay(300)

sm.sendNpcController(OBJECT_1, False)
sm.sendNpcController(OBJECT_2, False)
sm.sendNpcController(OBJECT_3, False)
sm.spawnMob(9300560, 150, 239, False)
sm.spawnMob(9300561, 250, 239, False)
sm.spawnMob(9300562, 350, 239, False)
sm.chatScript("按CTRL键攻击.")
sm.systemMessage("按CTRL键攻击.")
sm.showFieldEffect("lightning/screenMsg/0", 0)
sm.setTemporarySkillSet(0)
sm.setInGameDirectionMode(False, True, False, False)

while sm.hasMobsInField():
    sm.waitForMobDeath()
sm.warp(940001050, 0)