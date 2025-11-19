# Custom NPC script used for @sell player command
# Author: Clueless Cow

from net.swordie.ms.loaders import ItemData
from net.swordie.ms.constants import ItemConstants
from net.swordie.ms.enums import InvType

def disposeAll():
    sm.dispose()
    chr.dispose()

def sellItemsFromTab(invType = InvType.EQUIP):
    # query inv info
    inventory = chr.getInventoryByType(invType)
    invItems = inventory.getItems()
    tabName = ""
    if invType == InvType.CONSUME:
        tabName = "消耗品"
    elif invType == InvType.ETC:
        tabName = "材料"
    else:
        tabName = "装备"

    # empty inv
    if len(invItems) == 0:
        sm.sendSayOkay("您没有要出售的商品")
        disposeAll()
        return

    # has at least 1 item in inv
    if len(invItems) == 1:
        # only has 1 item, proceed to ask for confirmation
        sellingItems = list(invItems)
        _itemId = invItems.get(0).getItemId()
        confirmed = sm.sendAskYesNo("你确定要卖吗 #i{}# #z{}#".format(_itemId, _itemId))
    else:
        # has more than 1 item, prompt mode selection
        optionList = "请选择您想要出售的 {} tab:\r\n#L1##r全部#k#l\r\n#L2##g在选定物品中销售#k#l\r\n#L3#暂时不卖了#l\r\n".format(tabName)
        option = sm.sendNext(optionList)
        if option:
            if option == 1:
                # sell everything
                sellingItems = list(invItems)
                confirmed = sm.sendAskYesNo("你确定要卖吗 #r全部#k 在您的背包装备中?")
            if option == 2:
                # sell from/to
                sortedItems = list(invItems)
                sortedItems.sort(key=lambda x: x.getBagIndex())
                itemListTemplate = "此选项将出售选中的所有可出售的物品.\r\n请选择 #r<order>#k item:\r\n"
                for item in sortedItems:
                    itemListTemplate += "#L{}##i{}# #z{}##l\r\n".format(item.getBagIndex(), item.getItemId(), item.getItemId())
                startIndex = sm.sendNext(itemListTemplate.replace("<order>", "STARTING"))
                endIndex = sm.sendNext(itemListTemplate.replace("<order>", "ENDING"))
                if startIndex > endIndex:
                    startIndex, endIndex = endIndex, startIndex
                sellingItems = filter(lambda x: (startIndex <= x.getBagIndex() <= endIndex), sortedItems)
                soldItemsTemplate = "您将出售以下物品:\r\n"
                for item in sellingItems:
                    soldItemsTemplate += "#i{}# #z{}#\r\n".format(item.getItemId(), item.getItemId(), item.getBagIndex())
                confirmed = sm.sendAskYesNo(soldItemsTemplate)
        else:
            # 'maybe later' option / no response
            disposeAll()
            return
    # finish asking for selling items, proceed to actually sell it
    if not confirmed:
        sm.sendSayOkay("感谢您使用我的服务")
        disposeAll()
        return

    # player confirmed
    totalMesos = 0
    for item in sellingItems:
        cost = 0
        id = item.getItemId()
        quantity = item.getQuantity()
        if ItemConstants.isEquip(id):
            cost = item.getPrice() * quantity
        else:
            info = ItemData.getItemInfoByID(id)
            if info:
                cost = info.getPrice() * quantity
            else:
                continue
        totalMesos += cost

    if chr.canAddMoney(totalMesos):
        # remove item from inv
        for soldItem in sellingItems:
            _id = soldItem.getItemId()
            _quantity = soldItem.getQuantity()
            if ItemConstants.isEquip(_id):
                chr.consumeItem(soldItem)
            else:
                chr.consumeItem(_id, _quantity)
        # add money
        chr.addMoney(totalMesos)
        sm.sendSayOkay("您已收到｛｝金币。感谢您使用我的服务!".format(totalMesos))
        disposeAll()
        return
    else:
        sm.sendSayOkay("#r您已达到最大金币上限。#k请至少存入｛｝金币，然后再次运行该命令！".format(totalMesos))
        disposeAll()
        return

inventoryList = "请选择要出售的物品:\r\n#L1#装备#l\r\n#L2#消耗品#l\r\n#L3#材料#l\r\n"
selectedInv = sm.sendNext(inventoryList)

if selectedInv == 1:
    sellItemsFromTab(InvType.EQUIP)
elif selectedInv == 2:
    sellItemsFromTab(InvType.CONSUME)
elif selectedInv == 3:
    sellItemsFromTab(InvType.ETC)
else:
    sm.sendSayOkay("物品无效。请再次运行该命令!")
    disposeAll()