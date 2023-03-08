# Summary

## 贪心算法总结篇 <a href="#tan-xin-suan-fa-zong-jie-pian" id="tan-xin-suan-fa-zong-jie-pian"></a>

我刚刚开始讲解贪心系列的时候就说了，贪心系列并不打算严格的从简单到困难这么个顺序来讲解。

因为贪心的简单题可能往往过于简单甚至感觉不到贪心，如果我连续几天讲解简单的贪心，估计录友们一定会不耐烦了，会感觉贪心有啥好学的。

但贪心的难题又真的有点难，所以我是简单困难交错着讲的，这样大家就感觉难度适中，而且贪心也没有什么框架和套路，所以对刷题顺序要求没有那么高。

但在贪心系列，我发的题目难度会整体呈现一个阶梯状上升，细心的录友们应该有所体会。

在刚刚讲过的回溯系列中，大家可以发现我是严格按照框架难度顺序循序渐进讲解的，**和贪心又不一样，因为回溯法如果题目顺序没选好，刷题效果会非常差！**

同样回溯系列也不允许简单困难交替着来，因为前后题目都是有因果关系的，**相信跟着刷过回溯系列的录友们都会明白我的良苦用心，哈哈**。

**每个系列都有每个系列的特点，我都会根据特点有所调整，大家看我每天的推送的题目，都不是随便找一个到就推送的，都是先有整体规划，然后反复斟酌具体题目的结果**。

那么在贪心总结篇里，我按难易程度以及题目类型大体归个类。

贪心大总结正式开始：

### [#](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93%E7%AF%87.html#%E8%B4%AA%E5%BF%83%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80)贪心理论基础 <a href="#tan-xin-li-lun-ji-chu" id="tan-xin-li-lun-ji-chu"></a>

在贪心系列开篇词[关于贪心算法，你该了解这些！ (opens new window)](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)中，我们就讲解了大家对贪心的普遍疑惑。

1. 贪心很简单，就是常识？

跟着一起刷题的录友们就会发现，贪心思路往往很巧妙，并不简单。

2. 贪心有没有固定的套路？

贪心无套路，也没有框架之类的，需要多看多练培养感觉才能想到贪心的思路。

3. 究竟什么题目是贪心呢？

Carl个人认为：如果找出局部最优并可以推出全局最优，就是贪心，如果局部最优都没找出来，就不是贪心，可能是单纯的模拟。（并不是权威解读，一家之辞哈）

但我们也不用过于强调什么题目是贪心，什么不是贪心，那就太学术了，毕竟学会解题就行了。

4. 如何知道局部最优推出全局最优，有数学证明么？

在做贪心题的过程中，如果再来一个数据证明，其实没有必要，手动模拟一下，如果找不出反例，就试试贪心。面试中，代码写出来跑过测试用例即可，或者自己能自圆其说理由就行了

就像是 要用一下 1 + 1 = 2，没有必要再证明一下 1 + 1 究竟为什么等于 2。（例子极端了点，但是这个道理）

相信大家读完[关于贪心算法，你该了解这些！ (opens new window)](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)，就对贪心有了一个基本的认识了。

### [#](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93%E7%AF%87.html#%E8%B4%AA%E5%BF%83%E7%AE%80%E5%8D%95%E9%A2%98)贪心简单题 <a href="#tan-xin-jian-dan-ti" id="tan-xin-jian-dan-ti"></a>

以下三道题目就是简单题，大家会发现贪心感觉就是常识。是的，如下三道题目，就是靠常识，但我都具体分析了局部最优是什么，全局最优是什么，贪心也要贪的有理有据！

* [贪心算法：分发饼干(opens new window)](https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html)
* [贪心算法：K次取反后最大化的数组和(opens new window)](https://programmercarl.com/1005.K%E6%AC%A1%E5%8F%96%E5%8F%8D%E5%90%8E%E6%9C%80%E5%A4%A7%E5%8C%96%E7%9A%84%E6%95%B0%E7%BB%84%E5%92%8C.html)
* [贪心算法：柠檬水找零(opens new window)](https://programmercarl.com/0860.%E6%9F%A0%E6%AA%AC%E6%B0%B4%E6%89%BE%E9%9B%B6.html)

### [#](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93%E7%AF%87.html#%E8%B4%AA%E5%BF%83%E4%B8%AD%E7%AD%89%E9%A2%98)贪心中等题 <a href="#tan-xin-zhong-deng-ti" id="tan-xin-zhong-deng-ti"></a>

贪心中等题，靠常识可能就有点想不出来了。开始初现贪心算法的难度与巧妙之处。

* [贪心算法：摆动序列(opens new window)](https://programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html)
* [贪心算法：单调递增的数字(opens new window)](https://programmercarl.com/0738.%E5%8D%95%E8%B0%83%E9%80%92%E5%A2%9E%E7%9A%84%E6%95%B0%E5%AD%97.html)

#### [#](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93%E7%AF%87.html#%E8%B4%AA%E5%BF%83%E8%A7%A3%E5%86%B3%E8%82%A1%E7%A5%A8%E9%97%AE%E9%A2%98)贪心解决股票问题 <a href="#tan-xin-jie-jue-gu-piao-wen-ti" id="tan-xin-jie-jue-gu-piao-wen-ti"></a>

大家都知道股票系列问题是动规的专长，其实用贪心也可以解决，而且还不止就这两道题目，但这两道比较典型，我就拿来单独说一说

* [贪心算法：买卖股票的最佳时机II(opens new window)](https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII.html)
* [贪心算法：买卖股票的最佳时机含手续费 (opens new window)](https://programmercarl.com/0714.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BA%E5%90%AB%E6%89%8B%E7%BB%AD%E8%B4%B9.html)本题使用贪心算法比较绕，建议后面学习动态规划章节的时候，理解动规就好

#### [#](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93%E7%AF%87.html#%E4%B8%A4%E4%B8%AA%E7%BB%B4%E5%BA%A6%E6%9D%83%E8%A1%A1%E9%97%AE%E9%A2%98)两个维度权衡问题 <a href="#liang-ge-wei-du-quan-heng-wen-ti" id="liang-ge-wei-du-quan-heng-wen-ti"></a>

在出现两个维度相互影响的情况时，两边一起考虑一定会顾此失彼，要先确定一个维度，再确定另一个一个维度。

* [贪心算法：分发糖果(opens new window)](https://programmercarl.com/0135.%E5%88%86%E5%8F%91%E7%B3%96%E6%9E%9C.html)
* [贪心算法：根据身高重建队列(opens new window)](https://programmercarl.com/0406.%E6%A0%B9%E6%8D%AE%E8%BA%AB%E9%AB%98%E9%87%8D%E5%BB%BA%E9%98%9F%E5%88%97.html)

在讲解本题的过程中，还强调了编程语言的重要性，模拟插队的时候，使用C++中的list（链表）替代了vector(动态数组)，效率会高很多。

所以在[贪心算法：根据身高重建队列（续集） (opens new window)](https://programmercarl.com/%E6%A0%B9%E6%8D%AE%E8%BA%AB%E9%AB%98%E9%87%8D%E5%BB%BA%E9%98%9F%E5%88%97%EF%BC%88vector%E5%8E%9F%E7%90%86%E8%AE%B2%E8%A7%A3%EF%BC%89.html)详细讲解了，为什么用list（链表）更快！

**大家也要掌握自己所用的编程语言，理解其内部实现机制，这样才能写出高效的算法！**

### [#](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93%E7%AF%87.html#%E8%B4%AA%E5%BF%83%E9%9A%BE%E9%A2%98)贪心难题 <a href="#tan-xin-nan-ti" id="tan-xin-nan-ti"></a>

这里的题目如果没有接触过，其实是很难想到的，甚至接触过，也一时想不出来，所以题目不要做一遍，要多练！

#### [#](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93%E7%AF%87.html#%E8%B4%AA%E5%BF%83%E8%A7%A3%E5%86%B3%E5%8C%BA%E9%97%B4%E9%97%AE%E9%A2%98)贪心解决区间问题 <a href="#tan-xin-jie-jue-qu-jian-wen-ti" id="tan-xin-jie-jue-qu-jian-wen-ti"></a>

关于区间问题，大家应该印象深刻，有一周我们专门讲解的区间问题，各种覆盖各种去重。

* [贪心算法：跳跃游戏(opens new window)](https://programmercarl.com/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.html)
* [贪心算法：跳跃游戏II(opens new window)](https://programmercarl.com/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.html)
* [贪心算法：用最少数量的箭引爆气球(opens new window)](https://programmercarl.com/0452.%E7%94%A8%E6%9C%80%E5%B0%91%E6%95%B0%E9%87%8F%E7%9A%84%E7%AE%AD%E5%BC%95%E7%88%86%E6%B0%94%E7%90%83.html)
* [贪心算法：无重叠区间(opens new window)](https://programmercarl.com/0435.%E6%97%A0%E9%87%8D%E5%8F%A0%E5%8C%BA%E9%97%B4.html)
* [贪心算法：划分字母区间(opens new window)](https://programmercarl.com/0763.%E5%88%92%E5%88%86%E5%AD%97%E6%AF%8D%E5%8C%BA%E9%97%B4.html)
* [贪心算法：合并区间(opens new window)](https://programmercarl.com/0056.%E5%90%88%E5%B9%B6%E5%8C%BA%E9%97%B4.html)

#### [#](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93%E7%AF%87.html#%E5%85%B6%E4%BB%96%E9%9A%BE%E9%A2%98)其他难题 <a href="#qi-ta-nan-ti" id="qi-ta-nan-ti"></a>

[贪心算法：最大子序和 (opens new window)](https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html)其实是动态规划的题目，但贪心性能更优，很多同学也是第一次发现贪心能比动规更优的题目。

[贪心算法：加油站 (opens new window)](https://programmercarl.com/0134.%E5%8A%A0%E6%B2%B9%E7%AB%99.html)可能以为是一道模拟题，但就算模拟其实也不简单，需要把while用的很娴熟。但其实是可以使用贪心给时间复杂度降低一个数量级。

最后贪心系列压轴题目[贪心算法：我要监控二叉树！ (opens new window)](https://programmercarl.com/0968.%E7%9B%91%E6%8E%A7%E4%BA%8C%E5%8F%89%E6%A0%91.html)，不仅贪心的思路不好想，而且需要对二叉树的操作特别娴熟，这就是典型的交叉类难题了。

### [#](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93%E7%AF%87.html#%E8%B4%AA%E5%BF%83%E6%AF%8F%E5%91%A8%E6%80%BB%E7%BB%93)贪心每周总结 <a href="#tan-xin-mei-zhou-zong-jie" id="tan-xin-mei-zhou-zong-jie"></a>

周总结里会对每周的题目中大家的疑问、相关难点或者笔误之类的进行复盘和总结。

如果大家发现文章哪里有问题，那么在周总结里或者文章评论区一定进行了修正，保证不会因为我的笔误或者理解问题而误导大家，哈哈。

所以周总结一定要看！

* [本周小结！（贪心算法系列一）(opens new window)](https://programmercarl.com/%E5%91%A8%E6%80%BB%E7%BB%93/20201126%E8%B4%AA%E5%BF%83%E5%91%A8%E6%9C%AB%E6%80%BB%E7%BB%93.html)
* [本周小结！（贪心算法系列二）(opens new window)](https://programmercarl.com/%E5%91%A8%E6%80%BB%E7%BB%93/20201203%E8%B4%AA%E5%BF%83%E5%91%A8%E6%9C%AB%E6%80%BB%E7%BB%93.html)
* [本周小结！（贪心算法系列三）(opens new window)](https://programmercarl.com/%E5%91%A8%E6%80%BB%E7%BB%93/20201217%E8%B4%AA%E5%BF%83%E5%91%A8%E6%9C%AB%E6%80%BB%E7%BB%93.html)
* [本周小结！（贪心算法系列四）(opens new window)](https://programmercarl.com/%E5%91%A8%E6%80%BB%E7%BB%93/20201224%E8%B4%AA%E5%BF%83%E5%91%A8%E6%9C%AB%E6%80%BB%E7%BB%93.html)

### [#](https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93%E7%AF%87.html#%E6%80%BB%E7%BB%93)总结 <a href="#zong-jie" id="zong-jie"></a>

贪心专题汇聚为一张图：

![](https://code-thinking-1253855093.file.myqcloud.com/pics/%E8%B4%AA%E5%BF%83%E6%80%BB%E7%BB%93water.png)

这个图是 [代码随想录知识星球 (opens new window)](https://programmercarl.com/other/kstar.html)成员：[海螺人 (opens new window)](https://wx.zsxq.com/dweb2/index/footprint/844412858822412)所画，总结的非常好，分享给大家。

很多没有接触过贪心的同学都会感觉贪心有啥可学的，但只要跟着「代码随想录」坚持下来之后，就会发现，贪心是一种很重要的算法思维而且并不简单，贪心往往妙的出其不意，触不及防！

**回想一下我们刚刚开始讲解贪心的时候，大家会发现自己在坚持中进步了很多！**

这也是「代码随想录」的初衷，只要一路坚持下来，不仅基础扎实，而且进步也是飞速的。

**在这十八道贪心经典题目中，大家可以发现在每一道题目的讲解中，我都是把什么是局部最优，和什么是全局最优说清楚**。

这也是我认为判断这是一道贪心题目的依据，如果找不出局部最优，那可能就是一道模拟题。

