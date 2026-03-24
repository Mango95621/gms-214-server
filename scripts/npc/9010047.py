#Secondary transfer NPC - 9010047 - Script name = 9010047.py
# On selection 1 and 2 - NX deduction is handled on the SecondaryFunction.
from net.swordie.ms.client.character.items import BodyPart

STONE_SHIELD = 1092068
PRICE = 100000

selection = sm.sendNext("你好，我叫盖尔，负责在你的副武器之间转移潜能。\r\n"
                        "\r\n#e你有#r " + str(sm.getNX()) + " #bNX#n。\r\n\r\n"
                        "#L0#购买一个副武器#l \r\n"                                                                
                        "#L1#购买一个石盾 #e#r(100,000) NX#b#n#l \r\n"
                        "#L2#将装备的副武器潜能转移到背包第一个石盾上 #e#r(100,000) NX#b#n#l \r\n"
                        "#L3#将背包第一个石盾的潜能转移到当前装备的副武器上 #e#r(100,000) NX#b#n #r\r\n#e(这将覆盖你装备的副武器的潜能)#n.#l"
                        "#L4##d#e卸下你当前的副武器.#l")

if selection == 0:
    sm.invokeAfterDelay(1, "openShop", 9072100)
    sm.dispose()
elif selection == 1:
    if not sm.canHold(1092068):
        sm.sendSayOkay("你的装备栏没有空间。")
        sm.dispose()
    if sm.getNX() >= PRICE:
        sm.deductNX(PRICE)
        sm.giveItem(1092068)
        sm.sendSayOkay("感谢你的购买！")
    else:
        sm.sendSayOkay("你的 #rNX#k 不足。")

elif selection == 2:
    result = sm.SecondaryFunction(1)
    if result == -1:
        sm.sendSayOkay("要么你的背包里没有石盾，要么石盾没有潜能。")
    elif result == -2:
        sm.sendSayOkay("你当前没有装备副武器。")
    elif result == -3:
        sm.sendSayOkay("你的 #rNX#k 不足，无法执行此操作。")
    elif result == -4:
        sm.sendSayOkay("你背包里的第一个石盾已经有潜能了。请把没有潜能的石盾放在背包的第一个格子。")

    else:
        sm.sendSayOkay("我已经将你的副武器潜能转移到你背包里的第一个石盾上了。")

elif selection == 3:
    result = sm.SecondaryFunction(0)
    if result == -1:
        sm.sendSayOkay("要么你的背包里没有石盾，要么石盾没有潜能。")
    elif result == -2:
        sm.sendSayOkay("你当前没有装备副武器。")
    elif result == -3:
        sm.sendSayOkay("你的 #rNX#k 不足，无法执行此操作。")
    else:
        sm.sendSayOkay("我已经将你石盾的潜能转移到你的装备副武器上了。")

elif selection == 4:
    currentSecondary = chr.getEquippedItemByBodyPart(BodyPart.Shield)
    if currentSecondary is not None and chr.canHold(currentSecondary.getItemId()):
        sm.unequip(currentSecondary)
    else:
        sm.sendNext("你没有装备副武器，或者无法将其放入装备栏。")
