pink = "\033[38;5;211m"
reset = "\033[0m"
red = "\033[31m"
magenta = "\033[35m"
green = "\033[32m"
blue = "\033[34m"
cyan = "\033[36m"
yellow = "\033[33m"

art = [
    "⣇⣿⠘⣿⣿⣿⡿⡿⣟⣟⢟⢟⢝⠵⡝⣿⡿⢂⣼⣿⣷⣌⠩⡫⡻⣝⠹⢿⣿⣷",
    "⡆⣿⣆⠱⣝⡵⣝⢅⠙⣿⢕⢕⢕⢕⢝⣥⢒⠅⣿⣿⣿⡿⣳⣌⠪⡪⣡⢑⢝⣇",
    "⡆⣿⣿⣦⠹⣳⣳⣕⢅⠈⢗⢕⢕⢕⢕⢕⢈⢆⠟⠋⠉⠁⠉⠉⠁⠈⠼⢐⢕⢽",
    "⡗⢰⣶⣶⣦⣝⢝⢕⢕⠅⡆⢕⢕⢕⢕⢕⣴⠏⣠⡶⠛⡉⡉⡛⢶⣦⡀⠐⣕⢕",
    "⡝⡄⢻⢟⣿⣿⣷⣕⣕⣅⣿⣔⣕⣵⣵⣿⣿⢠⣿⢠⣮⡈⣌⠨⠅⠹⣷⡀⢱⢕",
    "⡝⡵⠟⠈⢀⣀⣀⡀⠉⢿⣿⣿⣿⣿⣿⣿⣿⣼⣿⢈⡋⠴⢿⡟⣡⡇⣿⡇⡀⢕",
    "⡝⠁⣠⣾⠟⡉⡉⡉⠻⣦⣻⣿⣿⣿⣿⣿⣿⣿⣿⣧⠸⣿⣦⣥⣿⡇⡿⣰⢗⢄",
    "⠁⢰⣿⡏⣴⣌⠈⣌⠡⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⣉⣉⣁⣄⢖⢕⢕⢕",
    "⡀⢻⣿⡇⢙⠁⠴⢿⡟⣡⡆⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣵⣿",
    "⡻⣄⣻⣿⣌⠘⢿⣷⣥⣿⠇⣿⣿⣿⣿⣿⣿⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿",
    "⣷⢄⠻⣿⣟⠿⠦⠍⠉⣡⣾⣿⣿⣿⣿⣿⣿⢸⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⠟",
    "⡕⡑⣑⣈⣻⢗⢟⢞⢝⣻⣿⣿⣿⣿⣿⣿⣿⠸⣿⠿⠃⣿⣿⣿⣿⣿⣿⡿⠁⣠",
    "⡝⡵⡈⢟⢕⢕⢕⢕⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⠿⠋⣀⣈⠙",
    "⡝⡵⡕⡀⠑⠳⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⢉⡠⡲⡫⡪⡪⡣"
]

stats = [
    f"{magenta}👤 User       {red}❯ {reset}Viraj Prashad",
    f"{green}💻 Role(dream){red}❯ {reset}Security Engineer",
    f"{blue}🎯 Focus      {red}❯ {reset}Offensive Security",
    f"{cyan}🛠️ Hobby      {red}❯ {reset}Opensource Contribution",
    f"{yellow}🐧 Platform   {red}❯ {reset}Arch Linux(btw)",
    "",
    f"{magenta}🔥 Leetcode   {red}❯ {reset}300+ Problems",
    f"{green}💻 GFG        {red}❯ {reset}250+ Problems",
    f"{blue}📊 CodeChef   {red}❯ {reset}500+ Problems",
    f"{cyan}📊 CodeForces {red}❯ {reset}50+  Problems",
    f"{yellow}🚩 PicoCTF    {red}❯ {reset}100+ CTFs",
    f"{magenta}🛡️ TryHackme  {red}❯ {reset}50+  Rooms",
    f"{green}📦 HackTheBox {red}❯ {reset}Skilled (Rank)"
]

content = "<h3><code>[Vivichan@Arch]:~$ neofetch</code></h3>\n\n```ansi\n"
for i in range(14):
    left_side = f"{pink}{art[i]}{reset}"
    right_side = stats[i] if i < len(stats) else ""
    content += f"{left_side}    {right_side}\n"
content += "```\n"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)
