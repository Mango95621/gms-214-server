# Vote Points & Donation Points NPC

# Format to follow for items
# ItemID, Quantity/Duration, Cost, Time-sensitive (0 : false | 1 : enabled)

# ===========================================
# VP Items
# ===========================================

vp_exp = [
    [5360042, 240, 4, 1],
    [5360000, 1440, 8, 1],
    [2022463, 30, 2, 1],
    [2022461, 30, 2, 1],
    [5211048, 240, 4, 1],
    [5211046, 1440, 8, 1],
    [2023380, 30, 4, 1]
]

vp_cosmetics = [
    [5062400, 1, 1, 0],
	[2430182, 50, 2, 0],
	[2210010, 8, 3, 0],
	[5072000, 20, 1, 0],
	[5072000, 20, 1, 0],
	[5073000, 20, 1, 0],
	[5076000, 20, 3, 0],
	[5077000, 20, 3, 0]
]

vp_game_changers = [
	[2435383, 9999999, 24, 0],
	[1202236, 240, 2, 1],
	[5680729, 1, 8, 0],
	[1202089, 10080, 8, 1],
    [1202090, 10080, 8, 1],
    [1202091, 1080, 8, 1]
]

vp_pet_shop = [
    [5190000, 1, 1, 0],
    [5190001, 1, 1, 0],
    [5190006, 1, 1, 0],
    [5190009, 1, 1, 0],
    [5190010, 1, 1, 0],
    [5190011, 1, 1, 0],
    [5190002, 1, 1, 0],
    [5190003, 1, 1, 0],
    [5190004, 1, 1, 0],
    [5190005, 1, 1, 0]
]

# ===========================================
# DP Items
# ===========================================

# Format to follow for items
# ItemID, Quantity/Duration, Cost, Time-sensitive (0 : false | 1 : enabled)

dp_exp = [
    [2450015, 30, 250, 0],  # 3x Exp 30 Min
    [2450016, 60, 400, 0], # 3x Exp 60 Min
    [2023722, 30, 250, 0],  # 2x Meso Buff 30 min
]

dp_cosmetics = [
    [5552000, 1, 200, 0],  # Hair Slot
    [5553000, 1, 200, 0],  # Face Slot
	[5155000, 1, 1000, 0], # Carta's Indigo Pearl
	[5155004, 1, 1000, 0], # Carta's Teal Pearl
	[5155005, 1, 1000, 0], # Carta's Scarlet Pearl
]

# TODO: wz edit pet-vacs string to change names
# and have 2 different pvacs one for 1 day and a 2nd for 7 days.

dp_game_changers = [
    [5680047, 1, 100, 1],  # Pvac // 1 Day (time-sensitive)
    [5680047, 1, 600, 1],  # Pvac // 7 Day (time-sensitive)
    [1202236, 1, 8000, 0],  # Frenzy Totem
    [4034803, 1, 1000, 0],  # Name Change Coupon
    [2435383, 1, 4000, 0], # Pendant Slot Permanent Coupon
	[1122303, 1, 1000, 0], # Hellia Necklace
	[1132183, 1, 1000, 0], # Avenger Quiver Belt
	[1152101, 1, 1000, 0], # Doom Shoulder
	[1113171, 1, 1000, 0]  # Grin Ring
]


dp_surprise_box = [
    [5068300, 1, 250, 0], # Pet Box
	[2435163, 1, 300, 0], # Random Damage Skin
	[5190013, 1, 1000, 0] # Open Pet Shop Skill
]

# ===============================================

main_menu = sm.options("点券交易", "捐赠点数交易")

# Options for vote point menu
vp_menu = sm.options("经验 / 掉落率卷", "消耗品", "游戏商店", "宠物商店")
# Options for donation point menu
dp_menu = sm.options("经验 / 掉落率卷", "消耗品", "游戏商店", "抽奖商店")

# for sub-menu item options
option = ""
def showOptions(text, items, duration):
    option = text + "\r\n#b"
    for x in range (len(items)):
        name = items[x][0]
        qty  = items[x][1]
        cost = items[x][2]
        if duration:
            option += "#L" + str(x) + "##i" + str(name) + "# #z" + str(name) + "# (" + str(qty) + " Min)" + " (" + str(cost) + " Points)" + "#l \r\n"
        else:
            option += "#L" + str(x) + "##i" + str(name) + "# #z" + str(name) + "# (" + str(qty) + ")" + " (" + str(cost) + " Points)" + "#l \r\n"

    return sm.sendNext(option)

def exchange(opt, items, duration, donation):
    name = items[opt][0]
    qty  = items[opt][1]
    cost = items[opt][2]
    timed = items[opt][3]

    currency = sm.getVotePoints()
    currencyName = "点券"
    if donation:
        currency = sm.getDonationPoints()
        currencyName = "捐赠点数"

    durOrQty = ""
    if duration:
        durOrQty = "(#b" + str(qty) + " min#k)"
    else:
        durOrQty = "(#b" + str(qty) + "#kx)"

    timeMsg = ""
    if timed == 1:
        timeMsg = "\r\n\r\n#r(这是一个时间期限的物品，一旦物品进入您的背包，持续时间将立即开始扣减!!#k)"

    if sm.sendAskYesNo("您目前拥有 #b" + str(currency) + " " + currencyName + "#k.\r\n您确定要以下物品吗?:\r\n " +
    durOrQty + " 的 #b#z " + str(name) + "##k #i" + str(name) + "# 为了 #r" + str(cost) + "#k " + currencyName + "?" + timeMsg):
            if currency >= cost:
                if sm.canHold(name):
                    if duration:
                        if timed == 1: # is time sensitive
                            sm.giveItemWithExpireDate(name, 1, False, qty)
                        else:
                            sm.giveItem(name, 1)
                    else:
                        if timed == 1:
                            sm.giveItemWithExpireDate(name, 1, False, qty)
                        else:
                            sm.giveItem(name, qty)

                    if donation: # is donation points
                        sm.deductDonationPoints(cost)
                    else:
                        sm.deductVotePoints(cost)
                    sm.sendSayOkay("您已获得 " + durOrQty + " #b#z" + str(name) + "##k for #r" + str(cost) + "#k " + currencyName + ".")
                else:
                    sm.sendNext("请确保您的背包中有足够的空间")
            else:
                sm.sendNext("你没有足够的 " + currencyName + ". 你需要 #r" + str(cost) + "#k " + currencyName + ".")


def showAndExchange(msg, items, has_duration, donation):
     selection = showOptions(msg, items, has_duration)
     exchange(selection, items, has_duration, donation)

# =========================== Vote Points =========================================================

def votePointOptions():
    type = False
    prompt = "您目前拥有 #b" + str(sm.getVotePoints()) + " 点券#k.\r\n你要用点券买什么?\r\n\r\n(#d你可以通过网站或联系管理员来获取点券#k!)\r\n"
    selection = sm.sendNext(prompt + "#b" + vp_menu + "#k")

    if selection == 0:
        showAndExchange("您想从经验/掉落率券商店购买什么？", vp_exp, True, type) # items have have a duration
    elif selection == 1:
        showAndExchange("你想从化妆品店买什么?", vp_cosmetics, False, type) # items don't have a duration
    elif selection == 2:
        showAndExchange("你想从游戏商店买什么?", vp_game_changers, True, type)
    elif selection == 3:
        showAndExchange("你想从宠物商店买什么？", vp_pet_shop, False, type)


# =========================== Donation Points ======================================================

def donationPointOptions():
    type = True # is DP
    prompt = "您目前拥有 #b" + str(sm.getDonationPoints()) + " 捐赠点数#k.\r\n你要用捐赠点数买什么?\r\n\r\n(#d你可以通过捐赠来获取捐赠点数#k.)\r\n"
    selection = sm.sendNext(prompt + "#b" + dp_menu + "#k")

    if selection == 0:
        showAndExchange("您想从经验/掉落券商店买什么?", dp_exp, True, type) # items have have a duration
    elif selection == 1:
        showAndExchange("您想从消耗品商店买什么?", dp_cosmetics, False, type) # items don't have a duration
    elif selection == 2:
        showAndExchange("您想从游戏商店买什么?", dp_game_changers, True, type)
    elif selection == 3:
        showAndExchange("你想从抽奖商店买什么?", dp_surprise_box, False, type)

# ===================================================================================================

selection = sm.sendNext("嘿！你想让我做什么?\r\n#b" + main_menu + "#k")
if selection:
    donationPointOptions()
else:
	votePointOptions()