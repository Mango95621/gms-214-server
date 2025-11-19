# Hidden Street : Road to the Mine 1 ; Xenon 3rd Job

# spawnPoint = 533 28
# lackey sp = 1184 28

BLACK_WINGS_LACKEY = 2159397
BLACK_WINGS_GOON = 9300643

sm.lockInGameUI(True)
sm.sendDelay(30)

sm.spawnNpc(BLACK_WINGS_LACKEY, 1184, 28)
sm.moveCamera(False, 250, 700, 28)
sm.sendDelay(2500)

# TODO: just moves back left and right
# sm.moveNpcByTemplateId(BLACK_WINGS_LACKEY, True, 100, 100)
# sm.moveCamera(True, 250, 0, 0)

sm.setSpeakerID(BLACK_WINGS_LACKEY)
sm.sendNext("嘿，你在这里做什么？另外那个人去哪儿了？你看起来不太眼熟...")
sm.setPlayerAsSpeaker()
sm.sendSay("我是黑翼成员。")
sm.setSpeakerID(BLACK_WINGS_LACKEY)
sm.sendSay("是吗？让我看看...我觉得我以前见过你的脸。我想我在从Gelimer那里收到的一些命令中见过你。")
sm.setPlayerAsSpeaker()
sm.sendSay("你搞错了。")
sm.setSpeakerID(BLACK_WINGS_LACKEY)
sm.sendSay("是吗？也许我最好和Gelimer确认一下。我可不想惹上麻烦。跟我来！")
sm.setPlayerAsSpeaker()
sm.sendSay("也许我应该直接解决掉这家伙...")

sm.moveCamera(True, 1000, 0, 0)
sm.lockInGameUI(False)
sm.removeNpc(BLACK_WINGS_LACKEY)
sm.spawnMob(BLACK_WINGS_GOON, 610, 28, False)
