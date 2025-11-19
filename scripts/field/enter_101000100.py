from net.swordie.ms.connection.packet import Effect
from net.swordie.ms.connection.packet import User
from net.swordie.ms.enums import TextEffectType
from net.swordie.ms.util import Position

sm.lockInGameUI(True)

effect = Effect.createFieldTextEffect("#fs20#- 几个月后，森林和房子都恢复了 -", 50, 2000, 4,
                                      Position(0, 0), 1, 4 , TextEffectType.BlackFadedBrush, 0, 0)
sm.getChr().getField().broadcastPacket(User.effect(effect))
sm.sendDelay(4000)

sm.lockInGameUI(False)