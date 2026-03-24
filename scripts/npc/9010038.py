from net.swordie.ms.scripts import ScriptUtil as su;


mapleLeafID 	= 4001126
mesosBagID 		= 4031138

mapleItemEquips 	= [
    1003863, # - Onyx Maple Hat
    1012376, # - Onyx Maple Gum
    1052612, # - Onyx Maple Suit
    1102562, # - Onyx Maple Cape
    1113034, # - Onyx Maple Ring
    1122252, # - Onyx Maple Pendant
    1132228  # - Onyx Maple Buckle

];
mapleItemWeapons 	= [
    1212066, # - Onyx Maple Rod
    1222061, # - Onyx Maple Soul Shooter
    1232060, # - Onyx Maple Devil Sword
    1242065, # - Onyx Maple Chain Sword
    1252064, # - Onyx Maple Scepter
    1302277, # - Onyx Maple Sword
    1312155, # - Onyx Maple Axe
    1322205, # - Onyx Maple Mace
    1332227, # - Onyx Maple Cutter
    1352825, # - Onyx Maple Claw
    1362092, # - Onyx Maple Cane
    1372179, # - Onyx Maple Wand
    1382211, # - Onyx Maple Staff
    1402199, # - Onyx Maple Two-handed Sword
    1412137, # - Onyx Maple Two-handed Axe
    1422142, # - Onyx Maple Maul
    1432169, # - Onyx Maple Spear
    1442225, # - Onyx Maple Polearm
    1452207, # - Onyx Maple Longbow
    1462195, # - Onyx Maple Crossbow
    1472216, # - Onyx Maple Steer
    1482170, # - Onyx Maple Grip
    1492181, # - Onyx Maple Shooter
    1522096, # - Pearl Maple Twin Angels
    1532100, # - Onyx Maple Cannon
    1542070, # - Scarlet Katana
    1552070  # - Onyx Maple Fan

];


strBuyOptions = "你想买什么？#b\r\n#L0#吸血鬼之血\r\n#L1#红曜石枫叶装备\r\n#L2#红曜石枫叶武器\r\n#L3#用枫叶兑换经验值";

buyOptionsSelection = sm.sendSayOkay(strBuyOptions);
buyEquipSelection = -1;
buyEquipYesNo = -1;

#==========================
# Vampire Blood
#==========================

if buyOptionsSelection == 0:
    answer = sm.sendAskNumber("你想购买多少个 #v2433559##b吸血鬼之血？\r\n#r 500 #b枫叶 #k每个", 0, 1, 1000)

    totalCost = answer * 500

    if sm.getQuantityOfItem(4001126) < totalCost:
        sm.sendSayOkay("你的 #v4001126##b枫叶 不足。")
        sm.dispose()

    if not sm.canHold(2433559, answer):
        sm.sendSayOkay("请确保你的背包有空间。")

    else:
        sm.consumeItemFromDiffStacks(4001126, totalCost)
        sm.giveItem(2433559, answer)
        sm.sendSayOkay("享受你的 #v2433559##b吸血鬼之血 吧！")

#==========================
# EQUIPMENT
#==========================

if buyOptionsSelection == 1:
    strItemEquipsList = "你想买什么？\r\n\r\n每个物品需要： \r\n"+su.getItemImg(mapleLeafID)+" #b5000\r\n"+su.getItemImg(mesosBagID)+" #b1000万金币\r\n\r\n#b";
    i = 0;
    for itemEquip in mapleItemEquips:
        strItemEquipsList += su.addSelectItem(i)+su.getItemImg(itemEquip)+"   "+su.getItemName(itemEquip)+"\r\n";
        i+=1;

    buyEquipSelection = sm.sendSayOkay(strItemEquipsList);


if buyEquipSelection >= 0:
    buyEquipStr = "你确定要购买：" + su.getItemImg(mapleItemEquips[buyEquipSelection]) + "\r\n " +su.getItemImg(mapleLeafID)+" #b5000 \r\n "+su.getItemImg(mesosBagID)+" #b 1000万金币？";
    buyEquipYesNo = sm.sendAskYesNo(buyEquipStr);

if buyEquipYesNo == True:
    mapleLeafQuantity = sm.getQuantityOfItem(mapleLeafID);
    if mapleLeafQuantity >= 5000 and sm.getMesos() >= 10000000:
        if chr.getEquipInventory().getEmptySlots() <= 0:
            sm.sendSayOkay("请清出背包空间");
            sm.dispose();
        else:
            sm.deductMesos(10000000);
            chr.consumeItemFromDiffStacks(mapleLeafID,5000);
            sm.giveItem(mapleItemEquips[buyEquipSelection]);
            sm.dispose();
    else:
        sm.sendSayOkay("你的枫叶或金币不足");
        sm.dispose();


#==========================
# WEAPONS
#==========================

if buyOptionsSelection == 2:
    strItemEquipsList = "你想买什么？\r\n\r\n每个物品需要： \r\n"+su.getItemImg(mapleLeafID)+" #b5000\r\n"+su.getItemImg(mesosBagID)+" #b1000万金币\r\n\r\n#b";
    i = 0;
    for itemEquip in mapleItemWeapons:
        strItemEquipsList += su.addSelectItem(i)+su.getItemImg(itemEquip)+"   "+su.getItemName(itemEquip)+"\r\n";
        i+=1;

    buyEquipSelection = sm.sendSayOkay(strItemEquipsList);


if buyEquipSelection >= 0:
    buyEquipStr = "你确定要购买：" + su.getItemImg(mapleItemWeapons[buyEquipSelection]) + "  \r\n" +su.getItemImg(mapleLeafID)+" #b5000  \r\n"+su.getItemImg(mesosBagID)+" #b 1000万金币？";
    buyEquipYesNo = sm.sendAskYesNo(buyEquipStr);

if buyEquipYesNo == True:
    mapleLeafQuantity = sm.getQuantityOfItem(mapleLeafID);
    if mapleLeafQuantity >= 5000 and sm.getMesos() >= 10000000:
        if chr.getEquipInventory().getEmptySlots() <= 0:
            sm.sendSayOkay("请清出背包空间");
            sm.dispose();
        else:
            sm.deductMesos(10000000);
            chr.consumeItemFromDiffStacks(mapleLeafID,5000);
            sm.giveItem(mapleItemWeapons[buyEquipSelection]);
            sm.dispose();
    else:
        sm.sendSayOkay("你的枫叶或金币不足");
        sm.dispose();

#==========================
# Trade Maple Leaves For Experience
#==========================

if buyOptionsSelection == 3:
    answer = sm.sendAskNumber("你想兑换多少个 #v4001126##b枫叶？", 0, 1, 1000)

    totalExp = answer * 35 # EXP Per Maple leaf.
    totalQty = answer * 1  # Leaves Per EXP Tick.

    if sm.getQuantityOfItem(4001126) < totalQty:
        sm.sendSayOkay("你的#v4001126##b枫叶 不足。\r\n#k你只有#r#c4001126#\r\n。")
        sm.dispose()

    else:
        sm.consumeItemFromDiffStacks(4001126, totalQty)
        sm.giveExp(totalExp)
        sm.sendSayOkay("谢谢你的 #v4001126##b枫叶。\r\n#k享受经验值吧！")
