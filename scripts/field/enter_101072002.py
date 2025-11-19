# id 101072002 (Ellinel Fairy Academy : Ellinel Academy Lobby), field 101072002
sm.lockInGameUI(True, True)
sm.setSpeakerType(3)
sm.setParam(5)
sm.setInnerOverrideSpeakerTemplateID(1500000) # Cootie the Really Small
sm.sendNext("什么？我可以在Ellinel工作？！")
sm.setInnerOverrideSpeakerTemplateID(1500002) # Faculty Head Kalayan
sm.sendSay("校-校长Ivana，您要把一个人类带到我们的知识殿堂里来？！")
sm.setInnerOverrideSpeakerTemplateID(1500001) # Headmistress Ivana
sm.sendSay("我们对人类的抵制已经让我们陷入困境。要不是他们的帮助，我们的孩子们就会迷失。是时候改变了...")
sm.sendSay("黑魔法师很久以前就让整个枫之谷世界陷入恐怖...现在，某些派系想要把他带回来。我们精灵不能袖手旁观。\r\n我们必须敞开心扉和思想。")
sm.setInnerOverrideSpeakerTemplateID(1500002) # Faculty Head Kalayan
sm.sendSay("呃...您说什么就是什么，校长...")
sm.setInnerOverrideSpeakerTemplateID(1500000) # Cootie the Really Small
sm.sendSay("这太酷了。我很高兴你出来看我做这一切。")
sm.setParam(17)
sm.sendSay("所以，孩子们可以再次排练他们的戏剧了？")
sm.setParam(5)
sm.setInnerOverrideSpeakerTemplateID(1500001) # Headmistress Ivana
sm.sendSay("他们已经开始创作不同的剧本了！他们一定被这次事件深深触动了。")
sm.setParam(17)
sm.sendSay("......？")
sm.moveCamera(False, 180, -400, 259)
sm.sendDelay(4737)
sm.sendDelay(100)
sm.setParam(5)
sm.setInnerOverrideSpeakerTemplateID(1500006) # Ephony the Fairy
sm.sendNext("小心了，邪恶的鼹鼠王！为了增益和金币，我就是#b#h0##k！以热三明治的名义，我要惩罚你！")
sm.setInnerOverrideSpeakerTemplateID(1500005) # Tracy the Fairy
sm.sendSay("嘿，不公平！我本来要扮演#b#h0##k的！")
sm.setInnerOverrideSpeakerTemplateID(1500007) # Phiny the Fairy
sm.sendSay("不！那是我的角色！")
sm.moveCamera(True, 0, 0, 0)
sm.sendDelay(0)
sm.sendDelay(100)
sm.setInnerOverrideSpeakerTemplateID(1500001) # Headmistress Ivana
sm.sendNext("戏剧的标题是#b爱哭鬼#h0#的鼹鼠奇妙变身#k。")
sm.setParam(17)
sm.sendSay("......")
sm.setParam(5)
sm.setInnerOverrideSpeakerTemplateID(1500000) # Cootie the Really Small
sm.sendSay("听起来像是我很想看的戏剧！")
sm.lockInGameUI(False, True)
sm.startQuest(32129)
sm.warp(101072000)
