from net.swordie.ms.enums import InvType

eeScroll=0
listitem = []
itemID = []
newlist = []
selection = sm.sendNext("#e<装备强化NPC>#n \r\n \r\n 嘿 #h #. 我负责装备强化。请选择下面的选项： \r\n \r\n \r\n#b#L1#使用装备强化。#l \r\n#L0##b使用因果剪刀#l \r\n#L2#还原装备溯源.#l")
if selection == 0:
    selection = sm.sendNext("请选择你想做什么：\r\n\r\n#L0##b为指定物品使用因果剪刀。#l\r\n#L1#为所有可用装备使用因果剪刀（每个装备4000 NX）。#l");
    if selection == 0:
        newlist = []
        listitem = eval(sm.getScissorEquips())
        listitem.sort()
        for x in range(len(listitem)):
            itemID.append(sm.getItemIDByBagIndex(listitem[x], InvType.EQUIP))
            newlist.append('#L'+str(listitem[x])+'##v'+str(itemID[x])+'#'+"#t"+str(itemID[x])+"#\r\n")
        if not newlist:
            sm.sendSayOkay("没有装备可以使用剪刀")
            sm.dispose()
        selection = sm.sendNext(''.join(newlist))
        itemToScissor = str(sm.getItemIDByBagIndex(selection, InvType.EQUIP))
        if sm.sendAskAccept("你选择了 #v"+itemToScissor+"# #e #t"+itemToScissor+"##n。这将花费4000 NX。#"):
            sm.applyScissor(selection)
    elif selection == 1:
        sm.applyScissorToAll()
elif selection == 1:
    newlist = []
    listitem = eval(sm.getAllEEScrolls())
    listitem.sort()
    for x in range(len(listitem)):
        itemID.append(sm.getItemIDByBagIndex(listitem[x], InvType.CONSUME))
        newlist.append('\n#L'+str(listitem[x])+'##v'+str(itemID[x])+'#'+"#t"+str(itemID[x])+"#\r\n")
    if not newlist:
        sm.sendSayOkay("你没有任何装备强化卷轴。")
        sm.dispose()
    eeScroll = sm.sendNext(''.join(newlist))
    newlist = []
    itemID = []
    listitem = eval(sm.getEquipsForEE())
    listitem.sort()
    for x in range(len(listitem)):
        itemID.append(sm.getItemIDByBagIndex(listitem[x], InvType.EQUIP))
        newlist.append('\n#L'+str(listitem[x])+'##v'+str(itemID[x])+'#'+"#t"+str(itemID[x])+"#\r\n")
    if not newlist:
        sm.sendSayOkay("没有可强化的装备")
        sm.dispose()
    selection = sm.sendNext(''.join(newlist))
    if sm.isEqpEligibleForAddedChance(selection) > 0:
        selectionNX = sm.sendNext("额外机会。\r\n这将使你成功的机会乘以#1.5倍。\r\n#L0#不增加额外机会#l\r\n#L1#增加机会（费用：#"+str(sm.isEqpEligibleForAddedChance(selection))+"#n NX）#l")
        if selectionNX == 0:
            sm.EnchantItem(selection, eeScroll, selection, 0)
        elif selectionNX == 1:
            sm.EnchantItem(selection, eeScroll, selection, 1)
    else:
        sm.EnchantItem(selection, eeScroll, selection, 0)

elif selection == 2:
    newlist = []
    listitem = eval(sm.getEquipmentTracesByIndex())
    for x in range(len(listitem)):  
        item = sm.getItemIDByBagIndex(listitem[x], InvType.EQUIP)
        itemID.append(sm.getItemIDByBagIndex(listitem[x], InvType.EQUIP))
        newlist.append('#L'+str(listitem[x])+'##v'+str(itemID[x])+'#'+"#t"+str(itemID[x])+"#\r\n")
    if not newlist:
        sm.sendSayOkay("没有可还原的装备")
        sm.dispose()
    selection = sm.sendNext(''.join(newlist))
    itemToRestore = str(sm.getItemIDByBagIndex(selection, InvType.EQUIP))
    if sm.sendAskAccept("你选择了 #v"+itemToRestore+"# #e #t"+itemToRestore+"##n。这将花费TBD NX。#"):
        sm.restoreEquipTrace(selection)
