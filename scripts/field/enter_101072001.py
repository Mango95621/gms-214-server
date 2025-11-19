# id 101072001 (Ellinel Fairy Academy : Ellinel Academy Lobby), field 101072001
sm.lockInGameUI(True, True)
sm.setSpeakerType(3)
sm.setParam(5)
sm.setInnerOverrideSpeakerTemplateID(1500003) # Woonie the Fairy
sm.sendNext("Kalayan先生！")
sm.setInnerOverrideSpeakerTemplateID(1500004) # Tosh the Fairy
sm.sendSay("我们好想你！")
sm.setInnerOverrideSpeakerTemplateID(1500005) # Tracy the Fairy
sm.sendSay("我们好害怕。")
sm.setInnerOverrideSpeakerTemplateID(1500006) # Ephony the Fairy
sm.sendSay("对不起！我们再也不会在危险区域玩耍了。")
sm.setInnerOverrideSpeakerTemplateID(1500002) # Faculty Head Kalayan
sm.sendSay("不，是我的错！我应该鼓励你们那些毫无意义的小游戏！原谅我！")
sm.setInnerOverrideSpeakerTemplateID(1500000) # Cootie the Really Small
sm.sendSay("看看他们之间的情感表达！没有人类能希望与之匹敌！")
sm.setInnerOverrideSpeakerTemplateID(1500001) # Headmistress Ivana
sm.sendSay("我对你的同理心和缺乏野蛮行为印象深刻，#h0#。你帮了大忙。")
sm.sendSay("还有你，非常小的Cootie。对精灵文化如此了解是不寻常的，即使在我们自己人中间也是如此。我想邀请你在学院任职...")
sm.lockInGameUI(False, True)
sm.warp(101072002)
