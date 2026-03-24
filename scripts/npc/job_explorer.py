# TODO: {serverName} Custom Beginnings - Explorer

speaker = 2007 # maple administrator

# JobOptions: { string jobName, string jobDesc, int jobId }
options = [
    ["战士", "能力强且具有防御力", 100],
    ["弓箭手", "远程且善于控制", 300],
    ["法师", "智慧且具有魔法", 200],
    ["飞侠", "迅速且隐秘", 400],
    ["海盗", "独特且魅力十足", 500],
    ["Jett", "与其他英雄不同", 508],
]

optionText = "是时候选择你的职业了\r\n作为#b冒险家#k, 你可以选择下面 " + str(len(options)) + " 种职业"

for idx, job in enumerate(options):
    optionText += "\r\n#b#L" + str(job[2]) + "#" + job[0] + "#k, " + job[1] + "#l"
choice = sm.sendNext(optionText)


for job in options:
    if (choice == job[2]):
        response = sm.sendAskYesNo("那么，你想要成为 #b" + job[0] + "#k 吗？")
        if response:
            sm.jobAdvance(job[2])
            sm.doJobEnd()
            sm.sendSayOkay("你现在是一名 #b" + job[0] + "#k 了！")
        else:
            # executes the current script again
            sm.dispose()
            sm.startScript("job_explorer", "npc")
