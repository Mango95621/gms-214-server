sm.lockInGameUI(True)
sm.curNodeEventEnd(True)
sm.removeEscapeButton()
sm.setPlayerAsSpeaker()

sm.sendNext("嗯...")
sm.sendSay("(我在哪里？我不认识这个地方...这不是我之前在的洞穴...呃，全身都疼。)")

sm.forcedInput(1)
sm.sendDelay(600)

sm.forcedInput(0)
sm.sendNext("(这看起来像是个治疗室...我在哪里？我发生了什么事？)")
sm.sendSay("(我必须想起发生了什么...)")
sm.sendSay("(黑魔法师违背了承诺，摧毁了奥西利亚的南部地区，那里是我母亲和戴米安所在的地方。他摧毁了我的家...)")
sm.sendSay("(我的挂坠盒！我的挂坠盒在哪里？)")
sm.sendSay("(我是在战斗中丢失了吗？那是我从家人那里唯一剩下的东西...不...)")

sm.forcedInput(2)
sm.sendDelay(600)

sm.forcedInput(0)
sm.sendNext("(我去了时间神殿向黑魔法师复仇...在路上，我让#p2151009#离开，以摆脱指挥官们。#p2159309#试图阻止我，但我决心已定...说起来，我想知道英雄们怎么样了？)")
sm.sendSay("(黑魔法师对我来说太强大了。我知道他会很强，但我以为我至少能造成一点伤害。我唯一做到的就是打破了他的屏障和撕破了他的长袍...多么可悲。)")
sm.sendSay("(但是...我是怎么活下来的？黑魔法师绝不会放过我。是有其他人介入吗？英雄们...？)")
sm.sendSay("(呃，现在我头疼。我甚至不知道我现在在哪里。这个地方太奇怪了。然而...这是否意味着枫叶世界没有被摧毁？)")

sm.forcedInput(1)
sm.sendDelay(600)

sm.forcedInput(0)
sm.sendNext("(我应该检查一下自己。无论如何我都需要我的恶魔之怒...但还剩下多少？)")

sm.showBalloonMsg("Effect/Direction6.img/effect/tuto/balloonMsg0/13", 2000)
sm.sendDelay(1500)

sm.sendNext("(不！我的恶魔护盾太弱了...我从未见过它这么糟糕。几乎所有的力量和能力都消失了。这怎么可能发生？)")
sm.sendSay("(我几乎不能这样战斗。那个戴帽子的男人...他看起来不危险，但我不能相信任何人。)")
sm.sendSay("(重建我的力量需要时间，坐在这里什么也做不了。我需要离开。)")

sm.forcedInput(1)