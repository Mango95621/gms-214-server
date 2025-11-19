# Root Abyss | Abyssal Cave  (Vellum's Boss Map)

from net.swordie.ms.enums import WeatherEffNoticeType

sm.showWeatherNotice("贝伦不见了. 看看祭坛周围.", WeatherEffNoticeType.SnowySnowAndSprinkledFlowerAndSoapBubbles, 10000)
if sm.hasQuest(30012):
    sm.waitForMobDeath(9400942)
    sm.completeQuest(30012) #[Root Abyss] Defeat the Final Guardian
    sm.dispose()

