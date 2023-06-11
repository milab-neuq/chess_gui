
<a href="#1">一.总述</a>
<a href="#2">二.实现效果展示</a>
<a href="#3">三. 基本架构 </a>
<a href="#4">四. 典型算法 </a>
<a href="#5">五. 最后总结 </a>

# <div id="1">一. 总述</div>
**使用pyqt编写了国际棋类界面，编写如下的棋类规则，界面能按照棋类规则下棋。**

▍兵只能向前斜走一格，不能后退。
▍兵的跳吃和连吃，黑白两枚棋子紧连在一条斜线上，对方棋子的前后正好有一空棋位能跳过对方的棋子，那么就可以跳过对方的棋子把被跳过的棋子吃掉，并从棋盘上取下，若又遇上可以跳过的棋子，那么就可以连续跳过去，把被跳过的棋子吃掉，跳吃连吃可以后退
▍王的升变，对局开始前双方在棋盘上摆的棋子都是兵，兵在对局过程中，走到或跳到对方底线停下，即可升变为"王"
▍王的走法类似国际象棋的象的走法，即可以走到斜线任意位置。
▍王的跳吃和连吃，同兵，不过不管王与兵相距有几个空棋位，都可以吃。

棋局结束
1、对方所有的棋子都吃掉或对方棋子全被封锁为胜。
2、棋局进行到最后,一方无任何可以走的棋则另一方胜利。

运行main_window即可开始下棋。
# <div id="2">二. 实现效果展示</div>
<a href="#2.1">2.1 普通棋子走子</a>
<a href="#2.2">2.2 普通棋子吃子</a>
<a href="#2.3">2.3 普通棋子升王琪 </a>
<a href="#2.4">2.4 王琪走子</a>
<a href="#2.5">2.5 王琪吃子 </a>
<a href="#2.6">2.6 悔棋功能 </a>
<a href="#2.7">2.7  交换落子功能</a>
<a href="#2.8">2.8 一方计时到时结果展示</a>
<a href="#2.9">2.9 一方失败结果展示 </a>
<a href="#2.10">2.10 环路吃子展示 </a>

<div id="2.1">2.1 普通棋子走子</div>

![在这里插入图片描述](https://img-blog.csdnimg.cn/4af96f81ba20450e96bb36380d8ec94e.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/7cc99c85eb3641be8ca3c1bcb0d84645.png)

<div id="2.2">2. 2普通棋子吃子</div>

简单吃子
![在这里插入图片描述](https://img-blog.csdnimg.cn/d42daedfda5d4b82b7618085263c0d23.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/6b490c054d1f44d2adcaf22a1421fa01.png) 连续跳吃
![在这里插入图片描述](https://img-blog.csdnimg.cn/5dbb294f19b04403b210affe730ffacf.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/e15d4bdfccc748c4b29a945405ed3b29.png)


<div id="2.3">2.3 普通棋子升王琪 </div>

![在这里插入图片描述](https://img-blog.csdnimg.cn/f1acb2087af646279f245695d8c16c2b.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/a024950a7ec444eca6ec5b9c7bee9320.png)
<div id="2.4"> 2.4王琪走子 </div>

![在这里插入图片描述](https://img-blog.csdnimg.cn/0dc6e56039c947ecb1b9aa355f20077b.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/5cf8696b699d48d5ba36083634934066.png)


<div id="2.5“> 2.5 王琪吃子</div>

![在这里插入图片描述](https://img-blog.csdnimg.cn/666f32fdd24444de9990e18e0ca802ef.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/c3b8d98252574328ab79cf2c92295f60.png)
王琪连续跳吃
![在这里插入图片描述](https://img-blog.csdnimg.cn/0f27f08462ad4fcb8599a56360ee5b64.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/5f8931da228d45b5a57b23f0082bd6ae.png)
<div id="2.6">2.6 悔棋功能 </div>

![在这里插入图片描述](https://img-blog.csdnimg.cn/851be20c0ca34f0cab5422e168efb892.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/5020590267484b23b2c3e94ead8f8929.png)
  点击悔棋按钮后：
  ![在这里插入图片描述](https://img-blog.csdnimg.cn/f431871c07c64e75b9ef72cb8a3bc8aa.png)
<div id="2.7">2.7 交换落子功能 </div>

![在这里插入图片描述](https://img-blog.csdnimg.cn/e4d9b1e7ce114335a647c3cd88d31b02.png)
	点击交换双方落子后，轮到黑棋走子
	![在这里插入图片描述](https://img-blog.csdnimg.cn/75e4225d44434d58be9ec89f5854ce99.png)
<div id="2.8">2.8 一方计时到时结果展示</div>

![在这里插入图片描述](https://img-blog.csdnimg.cn/a6174146a8114d739117b1e297828993.png)

<div id="2.9"> 2.9  一方失败结果展示 </div>

![在这里插入图片描述](https://img-blog.csdnimg.cn/1330ce1e0d0d4c09a99860f442a1fb23.png)

<div id = "2.10">2.10 环路吃子展示 </div>

![在这里插入图片描述](https://img-blog.csdnimg.cn/39bc8c9fff56413ab5ac16b484717194.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/3dcccfeba50e4af79843a37039143376.png)


# <div id="3">三. 基本架构</div>
![在这里插入图片描述](https://img-blog.csdnimg.cn/ad7b38fc49174f6d87969ce1ed736214.png)
&emsp;&emsp;如上图所示，首先包装一个棋盘类(在checker_board.py)，然后是左侧的棋盘界面类(在checker_board_widget.py)，右侧的悔棋，计时按钮什么的一个界面类(在right_window.py)，其余的load_board和mode_enumerate则是工具类，用以不同方式加载棋盘。
&emsp;&emsp;**总的来说，在main_window界面封装左侧棋盘ui类，右侧悔棋计时界面类，用load_board和mode_enumerate用于以不同形式加载棋盘。**
# <div id="4">四. 典型算法</div>
**此处介绍吃子的算法及其实现**
&emsp;&emsp;对吃子规则算法写的挺low的，但也将就能用
代码实现的所有的吃子都是硬向四个方向搜索，然后递归实现
&emsp;&emsp;每当落完一字后，调用包装的棋盘类的getNextAction方法得出新的行方可落子的位置，有吃必吃最多，不能吃子则给出所有可走位置。
&emsp;&emsp;下面是其核心代码及其详细介绍：
```python
    def getNextAction(self) -> (bool, [((int, int), [((int, int), bool)])]):
        """
        返回当前局面 my_color可以行棋的位置
        及是否可以吃子
        return 格式为：(是否可吃子，[(最终位置),[((吃子位置),吃子是否为王棋)]])
        """
        can_eat, end_list = False, []
        boss_can_eat, boss_end_list = False, []
        # 这里只是为了找bug方便
        try:
            # 调用函数返回此处普通棋子吃子落子情况
            can_eat, end_list = self.there_can_eat_or_move()
            # 调用函数返回此处王琪吃子落子情况
            boss_can_eat, boss_end_list = self.there_boss_can_eat_or_move()
        except Exception as e:
            self.err_log()

        flag = can_eat or boss_can_eat
        if flag:
            # 如果存在可以吃子的
            eat_list = []
            if can_eat:
                eat_list += end_list
            if boss_can_eat:
                eat_list += boss_end_list
			# 这里是在进行王琪和普通棋子吃子最多的比较情况
            eat_len = [len(tmp[1]) for tmp in eat_list]
            max_len = max(eat_len)
            # 返回最大吃子的情况
            return True, [tmp for tmp in eat_list if len(tmp[1]) == max_len]
        else:
            # 都不能吃子则返回落子情况
            return False, end_list + boss_end_list
```
接着介绍上面代码中调用的there_boss_can_eat_or_move函数：
```python
    def there_boss_can_eat_or_move(self) -> (bool, [((int, int), [((int, int), bool)])]):
        """
                  如果当前局面有能够吃子的，必须吃子且吃最多，否则返回所有可以走的位置
        return    (是否可吃子，[(最终位置),[((吃子位置),吃子是否为王棋)]])
        """
        un_eat = []  # 保存不能吃子的最后位置情况下落子
        eat_flag = False  # 是否可吃子标识
        if_eat = []  # 保存可以吃子时的最后位置情况
        # 遍历所有王棋集合，然后搜索王棋是否可以走
        if self.my_color == self.white_color:
            for (x, y) in self.white_boss_check:
                eat_nums, end_list = self.boss_position_can_move(x, y)
                if eat_nums > 0:
                    eat_flag = True
                    if_eat += end_list
                else:
                    un_eat += end_list
        else:
            for (x, y) in self.black_boss_check:
                eat_nums, end_list = self.boss_position_can_move(x, y)
                if eat_nums > 0:
                    eat_flag = True
                    if_eat += end_list
                else:
                    un_eat += end_list
        if eat_flag:
            # 查看每个可以吃子的能力集合
            # 确保在有可以吃最多子的情况下吃最多子
            eat_len = [len(eat[1]) for eat in if_eat]
            max_len = max(eat_len)
            if_eat = [eat for eat in if_eat if len(eat[1]) == max_len]
            return True, if_eat
        return False, un_eat
```
然后是涉及到的self.boss_position_can_move函数：该函数返回从一个位置出发，将会返回王棋从此位置开始的搜索吃子情况结果。
```python
    def boss_position_can_move(self, x, y) -> (bool, [((int, int), [((int, int), bool)])]):
        """
        return           (是否可吃子，[(最终位置),[((吃子位置),吃子是否为王棋)]])
        """

        # 1. 检查四个方向，查看是否能够无视距离吃子
        flag = False
        un_eat = []
        end_eat = []
        directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        for direct in directions:
            tmp_x, tmp_y = x + direct[0], y + direct[1]
            while self.check_bound(tmp_x, tmp_y) and self.check_bound(tmp_x + direct[0], tmp_y + direct[1]):
                # 1.1如果有己方棋子  显然该方向不能走
                if self.board[self.my_color][tmp_x][tmp_y] != 0:
                    break
                # 1.2 如果新位置有敌方棋子，则需查看是否可以吃子
                elif self.board[1 - self.my_color][tmp_x][tmp_y] != 0:
                	# self.if_can_eat函数仅仅简单判断是否可从第一个位置吃子然后落到第二个位置
                    if self.if_can_eat(tmp_x - direct[0], tmp_y - direct[1], tmp_x + direct[0], tmp_y + direct[1]):
                        # 已经明确可以吃子了,返回从当前位置可以吃最大子
                        flag = True
                        # 首先清空用于环路检测的list
                        self.my_list_to_detect_circle_for_boss.clear()
                        can_eat_nums, can_eat = self.check_boss_max_eat(tmp_x - direct[0], tmp_y - direct[1],
                                                                        tmp_x + direct[0], tmp_y + direct[1])
                        # 直接将吃子情况加入集合即可  因为在there_boss_can_move中才进行排序选最大
                        end_eat += can_eat
                    break
                # 1.3如果新位置没有任何棋子  则需要接着检查
                else:
                    un_eat.append(((tmp_x, tmp_y), []))
                    tmp_x, tmp_y = tmp_x + direct[0], tmp_y + direct[1]
            # 发现了边界小bug，为了吃子判断导致无法下到边界
            if self.check_bound(tmp_x, tmp_y) and not self.check_bound(tmp_x + direct[0], tmp_y + direct[1]):
                # 如果边界没有子则可以吃
                if self.board[self.white_color][tmp_x][tmp_y] == 0 and self.board[self.black_color][tmp_x][tmp_y] == 0:
                    un_eat.append(((tmp_x, tmp_y), []))


        if flag:
            return True, end_eat
        # 否则将可以走的地方返回
        return False, un_eat
```
```python
 	# 列表
    my_list_to_detect_circle_for_boss = []

    def check_boss_max_eat(self, x, y, new_x, new_y) -> (bool, [((int, int), [((int, int), bool)])]):
        """
            需要非常注意，boss跳吃了一个子后，之后的接着跳吃同样无视距离
        """
        if not self.if_can_eat(x, y, new_x, new_y):
            return 0, [((x, y), [])]

        # 否则递归此函数检查 四个方向（不能包含原来方向） 查看能否再次跳吃
        max_eat = 1
        middle_x, middle_y = int((new_x + x) / 2), int((new_y + y) / 2)
        end_list = [((new_x, new_y), [((middle_x, middle_y), self.board[1 - self.my_color][middle_x][middle_y] == 2)])]
        # 如果成环，需要直接返回不能吃子
        if (middle_x, middle_y) in self.my_list_to_detect_circle_for_boss:
            return 0, [((x, y), [])]
        self.my_list_to_detect_circle_for_boss.append((middle_x, middle_y))

        for direct in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
            # 不可重复
            if (new_x + direct[0] * 2, new_y + direct[1] * 2) == (x, y):
                continue
            else:
                """
                否则沿着一个方向检查，检查如果能够吃一个子，那么就接着递归check就可以
                """
                tmp_x, tmp_y = new_x + direct[0], new_y + direct[1]
                can_eat_flag = False
                """沿着此方向直到遇到第一个敌方棋子"""
                while self.check_bound(tmp_x, tmp_y) and self.check_bound(tmp_x + direct[0], tmp_y + direct[1]) and \
                        self.board[1 - self.my_color][tmp_x][tmp_y] == 0:
                    tmp_x, tmp_y = tmp_x + direct[0], tmp_y + direct[1]
                    # 如果率先遇到了我方棋子，直接没了
                    if self.board[self.my_color][tmp_x][tmp_y] == 1:
                        break

                if self.check_bound(tmp_x, tmp_y) and self.board[self.my_color][tmp_x][tmp_y] != 1:
                    if self.check_bound(tmp_x, tmp_y) and self.check_bound(tmp_x + direct[0],
                                                                           tmp_y + direct[1]) and self.if_can_eat(
                            tmp_x - direct[0], tmp_y - direct[1], tmp_x + direct[0], tmp_y + direct[1]):
                        # 已经明确可以吃子了
                        can_eat_flag = True
                       


                if can_eat_flag:
                	# 递归调用
                    tem_eat, tem_eaten = self.check_boss_max_eat(tmp_x - direct[0], tmp_y - direct[1],
                                                                 tmp_x + direct[0], tmp_y + direct[1])

                    if tem_eat > 0:
                        if max_eat < tem_eat + 1:
                            max_eat = tem_eat + 1
                            for eat in tem_eaten:
                                eat[1].append(
                                    ((middle_x, middle_y), self.board[1 - self.my_color][middle_x][middle_y] == 2))
                            end_list = tem_eaten
                        elif max_eat == tem_eat + 1:
                            for eat in tem_eaten:
                                eat[1].append(
                                    ((middle_x, middle_y), self.board[1 - self.my_color][middle_x][middle_y] == 2))
                            end_list += tem_eaten

        return max_eat, end_list
```
总的来讲，最最核心的是一个典型的递归程序，递归的一步步，如果可以吃子，则给出此位置的最大吃子数，如果不能，则将给出此位置的所有可能落子的位置。

# <div id="5">五. 最后总结</div>

&emsp;&emsp;从熟悉pyqt5，到最后编写程序结束。总的来说对如何简单使用qt有了更多了解及体验，对python的认识也更加深入，比如上面的吃子返回的类型，没有进行封装就这样使用其实不太好，但是写简单递归算法的时候就是会感觉很好用。
&emsp;&emsp;还有对于吃子规则的实现中可否吃子的判断，确切的说应该是有特定的数学式子可以进行加工处理，偷懒就应搜索了。对于架构或者说数据的表达来说也不好，其实最开始经过了一个小小的挫折后拿到了王师兄的未实现规则的完整代码，那个架构其实挺好，但是可能基于对二维棋盘的些许强求，偷懒？最后就自己写了。
&emsp;&emsp;些许期待，总是想要有一个很好的架构，然后完完整整的先设计好每一个函数，然后再填写补充功能，并且最后能对整个项目有充分的了解，对自己的代码有完全的掌控了，在此小项目上仍旧没有达成，希望以后可以达到那样的能力吧。

-------------------------------------------------------------------------------------------------------------

github地址：[基