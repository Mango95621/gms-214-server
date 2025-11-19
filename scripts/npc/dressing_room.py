# Dressing Room NPC

equip_type = 0
equip_page = 0
page_limit = 100
expire_time = 5

# flags
flag_main = 1
flag_browse = 1
flag_search = 0
# select category
# select specific page
# go back to categories

# name, buy_cost, rent_cost
categories = [
    ["帽子",                 2, 0],
    ["上衣",                 2, 0],
    ["下装",              2, 0],
    ["套装",             2, 0],
    ["鞋子",                2, 0],
    ["手套",               2, 0],
    ["披风",                2, 0],
    ["武器",              2, 0],
    ["面部配饰",     2, 0],
    ["眼部配饰",     2, 0],",      2, 0],
    ["戒指",                2, 0]
]

selected_item = 0

def prompt_main():
    text = "#e您目前拥有 #b" + str(sm.getVotePoints()) +" VP点数 #n\r\n请选择一个类别\r\n"
    count = 0
    for category in categories:
        if count == 4:
          text += "\n#b#L" + repr(count) + "#" + str(category[0]) + "#l"
          text += "\t\t\t\t\t\t\t#e#r#L999#搜索物品#l#n\r\n"
        else:
          text += "\n#b#L" + repr(count) + "#" + str(category[0]) + "#l\r\n"
        count += 1
    return text

def prompt_equips(type, page, limit):
    equip_tuple = sm.getDressingRoomEquips(type, page, limit)

    size = equip_tuple.getLeft()
    equips = equip_tuple.getRight()

    fromIndex = page
    toIndex = page + limit

    if (toIndex > size):
        toIndex = size

    text = "显示 " + repr(fromIndex) + " - " + repr(toIndex) + " of " + repr(size) + " " + categories[type][0] + " \r\n"
    for equip in equips:
        item_id = equip.getItemId()
        text += "#b#L" + repr(item_id) + "##v" + repr(item_id) + "# #z"  + repr(item_id) + "##l#k\r\n"
    text += "\r\n"

    if page != 0:
        text += "#b#L9998#上一页\r\n"

    if (toIndex) < size:
        text += "#b#L9999#下一页#l\r\n"

    text += "#b#L10000#返回分类#l"

    return text

def prompt_options(item_id):
    selected_item = item_id
    text = (
        "您已选择 #v{0}# #b#z{0}##k.\r\n\r\n"
        "请选择要执行的操作:\r\n"
        "#L1#购买 #b{1}#k VP#l\r\n"
        "#L2#租用 #b{2}#k VP#l\r\n\r\n"
        "#L0#返回列表#l"
    ).format(
        item_id,
        categories[sm.getDressingRoomEquipType(item_id)][1],
        categories[sm.getDressingRoomEquipType(item_id)][2]
    )

    return text

def prompt_search():
    text = (
    "请输入要搜索的物品的名称:"
    )

    return text

def message_done(item_id, cost, rent):
    buy_text = "购买" if not rent else "租用"
    text = (
        "你已经 {0} #v{1}# #b#z{1}##k.\r\n\r\n"
        "#b{2}#k VP点数 将从您的账户中扣除.\r\n\r\n"
    ).format(buy_text, item_id, cost)

    if rent:
        text += "该项目将于到期 #b{0} 分钟#k.".format(expire_time)

    return text


while flag_main == 1:
    selection_main = sm.sendNext(prompt_main())

    if selection_main != 999:
        flag_browse = 1
        while flag_browse == 1:
            selection_equips = sm.sendNext(prompt_equips(selection_main, equip_page, page_limit))
            if selection_equips == 9998: # previous
                equip_page -= page_limit
            elif selection_equips == 9999: # next
                equip_page += page_limit
            elif selection_equips == 10000: # exit
                flag_browse = 0
            else:
                flag_browse = 0
                selection_options = sm.sendNext(prompt_options(selection_equips))
                item = selection_equips
                if selection_options == 0: # exit - return to list
                    flag_browse = 1
                elif selection_options != 0:
                    cost = categories[selection_main][selection_options]
                    if sm.getVotePoints() < cost:
                        sm.sendNext("你没有足够的VP点数！")
                    else:
                        if selection_options == 1: # buy
                            sm.giveItem(item)
                            sm.deductVotePoints(cost)
                            sm.sendNext(message_done(item, cost, False))
                            flag_main = 0 # exit npc
                        elif selection_options == 2: # rent
                            sm.giveItemWithExpireDate(item, 1, False, 5)
                            sm.deductVotePoints(cost)
                            sm.sendNext(message_done(item, cost, True))
                            flag_main = 0 # exit npc
    elif selection_main == 999:
        flag_search = 1
        search_result = sm.sendAskText(prompt_search(), "", 0, 12)
        search_tuple = sm.getDressingRoomEquipsSearch(search_result)

        size = search_tuple.getLeft()
        equips = search_tuple.getRight()

        text_list = "显示 {0} 查询结果 '{1}'.\r\n".format(size, search_result)
        for id, string in equips.items():
            text_list += "#b#L" + repr(id) + "##v" + repr(id) + "# #z"  + repr(id) + "##l#k\r\n"

        if (size == 0):
            sm.sendNext("没有查询到结果 '{0}'.".format(search_result))
        else:
            selection_equips = sm.sendNext(text_list)

            selection_options = sm.sendNext(prompt_options(selection_equips))
            item = selection_equips
            cost = categories[sm.getDressingRoomEquipType(selection_equips)][1]
            if selection_options == 0: # exit - return to list
                flag_browse = 1
            elif selection_options != 0:
                cost = categories[sm.getDressingRoomEquipType(selection_equips)][selection_options]
                if sm.getVotePoints() < cost:
                    sm.sendNext("您没有足够的VP点!")
                else:
                    if selection_options == 1: # buy
                        sm.giveItem(item)
                        sm.deductVotePoints(cost)
                        sm.sendNext(message_done(item, cost, False))
                        flag_main = 0 # exit npc
                    elif selection_options == 2: # rent
                        sm.giveItemWithExpireDate(item, 1, False, 5)
                        sm.deductVotePoints(cost)
                        sm.sendNext(message_done(item, cost, True))
                        flag_main = 0 # exit npc
