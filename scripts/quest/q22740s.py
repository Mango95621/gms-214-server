# Created by MechAviv
# Kinesis Introduction
# Map ID :: 101020400
# East Forest :: Magician Association
KINESIS = 1531000
NERO = 1531003
NERO_NPC = 1531010
THREE_MOON = 1531004

sm.lockForIntro()
sm.removeAdditionalEffect()
sm.blind(1, 255, 0, 500)
sm.sendDealy(500)

sm.zoomCamera(0, 2000, 0, -144, 50)

sm.teleportInField(-253, 19)
sm.forcedFlip(False)
sm.blind(1, 255, 0, 0)
sm.sendDealy(1200)

sm.blind(0, 0, 0, 1000)
sm.sendDealy(1400)

sm.setIntroBoxChat(KINESIS)
sm.sendNext("我在哪里?你是谁?")

sm.setIntroBoxChat(THREE_MOON)
sm.sendSay("我是月亮的第三个孩子，另一个世界的英雄。")


sm.setIntroBoxChat(KINESIS)
sm.sendSay("That... you... what?")


sm.setIntroBoxChat(THREE_MOON)
sm.sendSay("Steady yourself. You are yet unharmed.")


sm.setIntroBoxChat(KINESIS)
sm.sendSay("#face0##r#fs25#...A talking dog?!")


sm.setIntroBoxChat(THREE_MOON)
sm.sendSay("......")


sm.setIntroBoxChat(KINESIS)
sm.sendSay("#face2#Oh, wait, wolf. Sorry.")
sm.sendSay("这是什么地方？我以为我在地铁上。我是在做梦吗？")


sm.setIntroBoxChat(NERO)
sm.sendSay("#face4#Nope! 欢迎来到枫叶冒险岛！")

sm.spawnNpc(NERO_NPC, -45, 0)
sm.showNpcSpecialActionByTemplateId(NERO_NPC, "summon")
sm.moveNpcByTemplateId(NERO_NPC, True, 80, 100)
sm.sendDelay(500)

sm.setIntroBoxChat(NERO)
sm.sendNext("#face4#Er, it's pretty different from your world. We better get you adjusted quick.")
sm.sendSay("#face4#Here, watch this.")

sm.sendDealy(500)

sm.showEffect("Effect/BasicEff.img/pang", 0, -145, 50, 0, 0, True, 0)
sm.playSound("Kite/Crown")
sm.removeNpc(NERO_NPC)

sm.spawnNpc(NERO, -145, 0)
sm.showNpcSpecialActionByTemplateId(NERO, "summon")
sm.sendDealy(500)

sm.setIntroBoxChat(NERO)
sm.sendSay("#face0#Did you see that? That was magic.")
sm.sendSay("#face0#Pretty sure you don't have that in your world! Heh.")


sm.setIntroBoxChat(KINESIS)
sm.sendNext("So I'm not dreaming...")


sm.setIntroBoxChat(NERO)
sm.sendSay("#face0#Again, nope! Lemme officially introduce myself. I am #bNella Medionel Roonia.")
sm.sendSay("#face0#In our ancient tongue, it means half-child of the sacred moonlight. See, I'm from a real big-deal magician family...")

sm.setIntroBoxChat(KINESIS)
sm.sendSay("#face2##fs20#What on Earth are you talking about, Nero?")


sm.setIntroBoxChat(NERO)
sm.sendSay("#face2#嘿嘿嘿！我不是尼禄！")

sm.sendDealy(1000)

sm.playSound("Sound/SoundEff.img/PvP/80001740_Use")
sm.OnOffLayer_On(500, "0", 800, -120, 12, "Map/Effect2.img/kinesis/chaNero", 5, 1, -1, 0)
sm.OnOffLayer_Move(300, "0", -800, 0)
sm.sendDealy(5000)

sm.playSound("Sound/SoundEff.img/12thMS/jump_m")
sm.OnOffLayer_Off(500, "0", 0)
sm.OnOffLayer_Move(300, "0", 800, 0)
sm.sendDealy(1000)


sm.setIntroBoxChat(KINESIS)
sm.sendNext("亲爱的。听着，尼禄，我需要知道我在哪里，怎么回去。")


sm.setIntroBoxChat(NERO)
sm.sendSay("#face0#嘿，我们救了你，所以挡住你的脸，听一分钟！")

sm.sendDealy(500)

sm.setIntroBoxChat(NERO)
sm.sendNext("#face0#Do you remember what happened with the #bwhite-haired man#k?")
sm.sendSay("#face0#I should have followed you... stopped you, maybe... It was my fault. I thought being near you would allow me to tail you easily. But I wasn't able to keep up.")
sm.sendSay("#face0#Regardless, you're here now. And we need to keep you here.")


sm.setIntroBoxChat(KINESIS)
sm.sendSay("Hey, Nero? I have no idea what you're talking about.")


sm.setIntroBoxChat(NERO)
sm.sendSay("#face0#Fine, FINE! My teacher, #bGrendel the Really Old#k, is on his way. He's old and smart-looking, so maybe you'll listen to him. Just sit tight.")

sm.sendDealy(500)

sm.showFadeTransition(0, 1000, 3000)
sm.zoomCamera(0, 1000, 2147483647, 2147483647, 2147483647)

sm.moveCamera(True, 0, 0, 0)
sm.sendDealy(300)

sm.removeOverlapScreen(1000)
sm.removeNpc(NERO)
sm.unlockForIntro()
sm.startQuest(parentID)
sm.completeQuest(parentID)
sm.giveExp(3000)