sm.lockUI()
FANZY = 1500010

sm.removeEscapeButton()

sm.flipDialoguePlayerAsSpeaker()
sm.sendNext("#b呸！我差点淹死了！#k")

sm.setSpeakerID(FANZY)
sm.sendSay("一定有什么魔法阻止人们游过去。")

sm.flipDialoguePlayerAsSpeaker()
sm.sendSay("#b你本可以提前告诉我！#k")

sm.setSpeakerID(FANZY)
sm.sendSay("我不是全知全能的，而且你是个很好的测试对象。我们得找其他方法。")

sm.unlockUI()
sm.startQuest(32102)
sm.completeQuest(32102)

sm.warp(101070000, 0)