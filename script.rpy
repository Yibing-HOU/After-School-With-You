# -*- coding: utf-8 -*-
# script.rpy

# 角色定义（要放在最上方）
define s = Character("苏黎", color="#dde29d")
define y = Character("言彻", color="#6c59cb")

# 变量初始化
default affection = 0

label start :
    # 背景画面
    scene bg_classroom with fade
    # 音乐起！
    play music "audio/bgm_school_afternoon.mp3" fadein 1.0
    # 苏黎说话
    show s_normal at left
    s "又是一个阳光刺眼的下午……"
    s "教室里只剩下我一个人。"
    hide s_normal

    # 言彻登场
    show y_normal at center with dissolve
    y "你也没走？"
    hide y_normal

    # 苏黎回应
    show s_normal at left with dissolve
    s "言彻？我以为你早就回去了。"
    hide s_normal

    # 言彻再说
    show y_normal at center with dissolve
    y "忘了带笔记本。结果被阳光晃得有点晕。"
    hide y_normal

    # 苏黎总结
    show s_normal at left with dissolve
    s "……阳光确实很强。"
    hide s_normal
    return

menu:
    "调侃他":
        jump tease
    "关照他":
        jump care

label tease:
    show s_normal at left with dissolve
    s "你该不会是借口吧？其实是想偷懒。"
    hide s_normal

    show y_normal at right with dissolve
    y "哈？你想多了。"
    y "不过，和你聊天也不坏。"
    hide y_normal
    $ affection += 1
    jump afternoon

label care:
    show s_normal at left with dissolve
    s "你还好吗？要不要去医务室坐一下？"

    show y_normal at center with dissolve
    y "不用，我没事。你总是这么认真。"

    $ affection += 2
    jump afternoon

label afternoon:
    show s_normal at left with dissolve
    s "阳光越来越暖了。窗帘的影子在黑板上晃动。"
    show y_normal at center with dissolve
    y "……如果明天也是好天气，就去屋顶看看吧？"
    s "好啊。"

    if affection >= 2:
        y "那就约好了。别迟到。"
        s "嗯。"
        "【好感结局：屋顶的夏天】"
    else:
        y "随便啦，看你心情。"
        s "……真拿你没办法。"
        "【普通结局：被风吹散的下午】"

    stop music fadeout 1.0
    return
