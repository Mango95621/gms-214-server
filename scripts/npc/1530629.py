#Snow Day Coin NPC

sm.setSpeakerID(9010040)

if sm.sendNext:
    selection = sm.sendNext("雪花活动正在进行中！\r\n#b"
                            "#L0#获取雪花硬币\r\n"
                            "#L1#消费雪花硬币\r\n"
                            "#L2#消费活动硬币\r\n")

    if selection == 0:
        selection = sm.sendNext("在这里你可以查看雪花硬币每日挑战的进度。只需点击每日任务列表即可领取全部奖励！\r\n" + chr.getAccount().getDailyStatusToNPC())
        if selection == 0:
            #chr.getAccount().completeDaily(0)
            chr.getAccount().claimDailies()
    if selection == 1:
        sm.invokeAfterDelay(1, "openShop", 9010040)
        sm.dispose()

    if selection == 2:
        sm.invokeAfterDelay(1, "openShop", 9010040)
        sm.dispose()
