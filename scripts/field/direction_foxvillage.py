LUMPS = 3002001
SALLY = 3002002
SNIFFS = 3002003
TWITCH = 3002004
SILVER = 3002005
COMPASS = 3002006
TIMBER = 3002007
BROOK = 3002008
PATIENCE = 3002009
TUMBLEWEED = 3002105

sm.setSpeakerID(2007)
if sm.sendAskYesNo("是否跳过教程过场动画？"):
    sm.createQuestWithQRValue(37999, "SKIP_FOXVILLAGE")

if sm.getQRValue(37999) != "SKIP_FOXVILLAGE":
    sm.lockInGameUI(True)
    sm.forcedInput(0)

    sm.spawnNpc(LUMPS, 300, 89)
    sm.showNpcSpecialActionByTemplateId(LUMPS, "summon")

    sm.spawnNpc(SALLY, -175, 0)
    sm.showNpcSpecialActionByTemplateId(SALLY, "summon")

    sm.spawnNpc(SNIFFS, 360, 103)
    sm.showNpcSpecialActionByTemplateId(SALLY, "summon")

    sm.spawnNpc(TWITCH, -238, -33)
    sm.showNpcSpecialActionByTemplateId(TWITCH, "summon")

    sm.spawnNpc(SILVER, 84, 37)
    sm.showNpcSpecialActionByTemplateId(SILVER, "summon")

    sm.spawnNpc(COMPASS, 174, 55)
    sm.showNpcSpecialActionByTemplateId(COMPASS, "summon")

    sm.spawnNpc(TIMBER, -128, 51)
    sm.showNpcSpecialActionByTemplateId(TIMBER, "summon")

    sm.spawnNpc(BROOK, -190, 77)
    sm.showNpcSpecialActionByTemplateId(BROOK, "summon")

    sm.spawnNpc(PATIENCE, 241, 72)
    sm.showNpcSpecialActionByTemplateId(PATIENCE, "summon")

    sm.spawnNpc(TUMBLEWEED, -61, 41)
    sm.showNpcSpecialActionByTemplateId(TUMBLEWEED, "summon")
    sm.sendDelay(2000)

    sm.removeEscapeButton()
    sm.setSpeakerID(TIMBER)
    sm.sendNext("我们真的已经习惯有你在这里了...")

    sm.setSpeakerID(BROOK)
    sm.sendSay("每天要吃三顿饭。特别是早餐。狐狸活着就是为了吃。")

    sm.setSpeakerID(SILVER)
    sm.sendSay("你要离开这个小镇了，但永远不要忘记你是我们尖耳狐狸的一员。不要忘记狐狸的骄傲。随时都可以回来。我们会等着你的。")

    sm.flipDialoguePlayerAsSpeaker()
    sm.sendSay("感谢你们所做的一切。我永远不会...永远不会忘记。")

    sm.setSpeakerID(TWITCH)
    sm.sendSay("影！你听起来像是要永远离开了！快点回来，下次带些好吃的来！")

    sm.setSpeakerID(SILVER)
    sm.sendSay("啊，年纪大了让我对什么都容易流泪。但别管我了，月光不肯出房间。她不想看到你离开。还有那场大雨...我觉得她一时半会儿不会停止哭泣。")

    sm.flipDialoguePlayerAsSpeaker()
    sm.sendSay("......")

    sm.setSpeakerID(TUMBLEWEED)
    sm.sendSay("我还是觉得你应该等几天和我一起去，但如果你很忙那也没办法。给，拿着这个卷轴，它会直接带你去万神殿。到了那里，找#r卡塔利昂#k谈谈。告诉他你是代表我来的，他会好好照顾你的。")

    sm.removeNpc(LUMPS)
    sm.removeNpc(SALLY)
    sm.removeNpc(SNIFFS)
    sm.removeNpc(TWITCH)
    sm.removeNpc(SILVER)
    sm.removeNpc(COMPASS)
    sm.removeNpc(TIMBER)
    sm.removeNpc(BROOK)
    sm.removeNpc(PATIENCE)
    sm.removeNpc(TUMBLEWEED)

sm.lockInGameUI(False)
sm.startQuest(38028)
sm.warp(410000000, 6)
