# 点格棋

本分支做的工作是使用QT5的框架，编写点格棋可视化。

功能目前达到的是将棋盘做出来，同时使用信号与槽较好的接受信号，对鼠标的点击事件做出相关反应。

目前仅支持双玩家对抗，机器对抗暂时因为学艺不精没弄出来，但是由于上一个棋类使用的是启发式——蒙特卡洛，这次也打算做，目前项目的机器分为随机bot以及一个简易的蒙特卡洛bot,大致雏形已经做出来，详情可见相关文件。

1. rollout 对应蒙特卡洛bot
2. random对应随机bot
![image](https://github.com/milab-neuq/chess_gui/blob/main/dotbox_gui/QQ%E5%9B%BE%E7%89%8720230619001050.png?raw=true)
