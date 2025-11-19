# Root Abyss - Temporal Crevasse (Von Bon's Map)
from net.swordie.ms.enums import WeatherEffNoticeType

sm.showWeatherNotice("在时间裂缝中召唤半半.", WeatherEffNoticeType.SnowySnowAndSprinkledFlowerAndSoapBubbles, 10000)
if sm.hasQuest(3009):
    sm.waitForMobDeath(9303154)
    sm.completeQuest(30009) #[Root Abyss] Defeat the First Guardian