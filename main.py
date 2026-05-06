import random

# --------------------------
# 角色資料
# --------------------------
avatar = {
    "hat": "   ",    # 帽子
    "head": "(^_^)",   # 臉
    "body": " | |"    # 身體
}

# --------------------------
# 抽卡池（用符號表示）
# --------------------------
gacha_pool = {
    "棒球帽": "hat",
    "禮帽": "hat",
    "草帽":"hat",
    "皇冠": "hat",
    "微笑臉": "head",
    "生氣臉": "head",
    "墨鏡臉": "head",
    "T恤": "body",
    "西裝": "body",
    "和服": "body"
}

# 對應符號
item_icons = {
    "棒球帽": "🧢",
    "禮帽": "🎩",
    "草帽":"👒",
    "皇冠": "👑",
    "微笑臉": "😀",
    "生氣臉": "😠",
    "墨鏡臉": "😎",
    "T恤": "|👕|",
    "西裝": "|👔|",
    "和服": "|👘|"
}

inventory = []   # 背包
records = []     # 記帳紀錄
points = 0       # 點數

# --------------------------
# 歡迎訊息
# --------------------------
print("===================================")
print("      歡迎使用大學生記帳App！")
print("透過記帳累積點數，抽卡收集道具，裝扮你的角色！")
print("點數可以讓你抽卡，抽到的帽子、臉、衣服都可以裝備～")
print("希望你以後會乖乖記帳，不要再忘記啦！")
print("===================================")

# --------------------------
# 顯示角色
# --------------------------
def show_character():
    print("\n你的角色：")
    print(" ", avatar["hat"])
    print(" ", avatar["head"])
    print(" ", avatar["body"])
    print()

# --------------------------
# 記帳功能（+5 點數）
# --------------------------
def add_record():
    global points
    print("\n格式：支出 食物 100")
    data = input("請輸入記帳： ")

    try:
        kind, category, amount = data.split()
        amount = int(amount)
    except:
        print("格式錯誤，請重新輸入。")
        return

    records.append((kind, category, amount))
    points += 5
    print("記帳成功！獲得 5 點，目前點數：", points)

# --------------------------
# 查看記帳紀錄
# --------------------------
def show_records():
    if not records:
        print("\n目前沒有任何記帳紀錄。")
        return

    print("\n你的記帳紀錄：")
    for i, (kind, category, amount) in enumerate(records, start=1):
        print(f"{i}. {kind} {category} {amount}")

# --------------------------
# 抽卡（10 點）
# --------------------------
def draw_gacha():
    global points
    if points < 10:
        print("點數不足，需要 10 點。")
        return

    points -= 10
    item = random.choice(list(gacha_pool.keys()))
    inventory.append(item)
    print("抽到：", item)
    print("剩餘點數：", points)

# --------------------------
# 顯示背包
# --------------------------
def show_inventory():
    print("\n你的背包：", inventory if inventory else "（空）")

# --------------------------
# 裝備道具
# --------------------------
def equip_item():
    if not inventory:
        print("背包是空的！")
        return

    print("\n你的道具：", inventory)
    item = input("想裝備哪一個？：")

    if item not in inventory:
        print("沒有這件道具。")
        return

    part = gacha_pool[item]      # hat / head / body
    avatar[part] = item_icons[item]

    print("已裝備：", item)

# --------------------------
# 主迴圈
# --------------------------
while True:
    print("1. 記帳（+5 點）")
    print("2. 抽卡（10 點）")
    print("3. 顯示角色")
    print("4. 顯示背包")
    print("5. 裝備道具")
    print("6. 查看記帳紀錄")
    print("7. 離開")
    
    choice = input("請選擇：")

    if choice == "1":
        add_record()
    elif choice == "2":
        draw_gacha()
    elif choice == "3":
        show_character()
    elif choice == "4":
        show_inventory()
    elif choice == "5":
        equip_item()
    elif choice == "6":
        show_records()
    elif choice == "7":
        print("再見！")
        break
    else:
        print("選項錯誤，請重新輸入。")
