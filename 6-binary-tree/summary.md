# Summary

## 二叉树：总结篇！（需要掌握的二叉树技能都在这里了） <a href="#er-cha-shu-zong-jie-pian-xu-yao-zhang-wo-de-er-cha-shu-ji-neng-du-zai-zhe-li-le" id="er-cha-shu-zong-jie-pian-xu-yao-zhang-wo-de-er-cha-shu-ji-neng-du-zai-zhe-li-le"></a>

> 力扣二叉树大总结！

不知不觉二叉树已经和我们度过了**三十三天**，[「代码随想录」 (opens new window)](https://img-blog.csdnimg.cn/20200815195519696.png)里已经发了**三十三篇二叉树的文章**，详细讲解了**30+二叉树经典题目**，一直坚持下来的录友们一定会二叉树有深刻理解了。

在每一道二叉树的题目中，我都使用了**递归三部曲**来分析题目，相信大家以后看到二叉树，看到递归，都会想：返回值、参数是什么？终止条件是什么？单层逻辑是什么？

而且**几乎每一道题目我都给出对应的迭代法**，可以用来进一步提高自己。

下面Carl把分析过的题目分门别类，可以帮助新录友循序渐进学习二叉树，也方便老录友面试前快速复习，看到一个标题，就回想一下对应的解题思路，这样很快就可以系统性的复习一遍二叉树了。

公众号的发文顺序，就是循序渐进的，所以如下分类基本就是按照文章发文顺序来的，我再做一个系统性的分类。

### [#](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html#%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80)二叉树的理论基础 <a href="#er-cha-shu-de-li-lun-ji-chu" id="er-cha-shu-de-li-lun-ji-chu"></a>

* [关于二叉树，你该了解这些！ (opens new window)](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)：二叉树的种类、存储方式、遍历方式、定义方式

### [#](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html#%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%81%8D%E5%8E%86%E6%96%B9%E5%BC%8F)二叉树的遍历方式 <a href="#er-cha-shu-de-bian-li-fang-shi" id="er-cha-shu-de-bian-li-fang-shi"></a>

* 深度优先遍历
  * [二叉树：前中后序递归法 (opens new window)](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html)：递归三部曲初次亮相
  * [二叉树：前中后序迭代法（一） (opens new window)](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%BF%AD%E4%BB%A3%E9%81%8D%E5%8E%86.html)：通过栈模拟递归
  * [二叉树：前中后序迭代法（二）统一风格(opens new window)](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E7%BB%9F%E4%B8%80%E8%BF%AD%E4%BB%A3%E6%B3%95.html)
* 广度优先遍历
  * [二叉树的层序遍历 (opens new window)](https://programmercarl.com/0102.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%82%E5%BA%8F%E9%81%8D%E5%8E%86.html)：通过队列模拟

### [#](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html#%E6%B1%82%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E5%B1%9E%E6%80%A7)求二叉树的属性 <a href="#qiu-er-cha-shu-de-shu-xing" id="qiu-er-cha-shu-de-shu-xing"></a>

* [二叉树：是否对称(opens new window)](https://programmercarl.com/0101.%E5%AF%B9%E7%A7%B0%E4%BA%8C%E5%8F%89%E6%A0%91.html)
  * 递归：后序，比较的是根节点的左子树与右子树是不是相互翻转
  * 迭代：使用队列/栈将两个节点顺序放入容器中进行比较
* [二叉树：求最大深度(opens new window)](https://programmercarl.com/0104.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%A4%A7%E6%B7%B1%E5%BA%A6.html)
  * 递归：后序，求根节点最大高度就是最大深度，通过递归函数的返回值做计算树的高度
  * 迭代：层序遍历
* [二叉树：求最小深度(opens new window)](https://programmercarl.com/0111.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E6%B7%B1%E5%BA%A6.html)
  * 递归：后序，求根节点最小高度就是最小深度，注意最小深度的定义
  * 迭代：层序遍历
* [二叉树：求有多少个节点(opens new window)](https://programmercarl.com/0222.%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%8A%82%E7%82%B9%E4%B8%AA%E6%95%B0.html)
  * 递归：后序，通过递归函数的返回值计算节点数量
  * 迭代：层序遍历
* [二叉树：是否平衡(opens new window)](https://programmercarl.com/0110.%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.html)
  * 递归：后序，注意后序求高度和前序求深度，递归过程判断高度差
  * 迭代：效率很低，不推荐
* [二叉树：找所有路径(opens new window)](https://programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html)
  * 递归：前序，方便让父节点指向子节点，涉及回溯处理根节点到叶子的所有路径
  * 迭代：一个栈模拟递归，一个栈来存放对应的遍历路径
* [二叉树：递归中如何隐藏着回溯(opens new window)](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E4%B8%AD%E9%80%92%E5%BD%92%E5%B8%A6%E7%9D%80%E5%9B%9E%E6%BA%AF.html)
  * 详解[二叉树：找所有路径 (opens new window)](https://programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html)中递归如何隐藏着回溯
* [二叉树：求左叶子之和(opens new window)](https://programmercarl.com/0404.%E5%B7%A6%E5%8F%B6%E5%AD%90%E4%B9%8B%E5%92%8C.html)
  * 递归：后序，必须三层约束条件，才能判断是否是左叶子。
  * 迭代：直接模拟后序遍历
* [二叉树：求左下角的值(opens new window)](https://programmercarl.com/0513.%E6%89%BE%E6%A0%91%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%80%BC.html)
  * 递归：顺序无所谓，优先左孩子搜索，同时找深度最大的叶子节点。
  * 迭代：层序遍历找最后一行最左边
* [二叉树：求路径总和(opens new window)](https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html)
  * 递归：顺序无所谓，递归函数返回值为bool类型是为了搜索一条边，没有返回值是搜索整棵树。
  * 迭代：栈里元素不仅要记录节点指针，还要记录从头结点到该节点的路径数值总和

### [#](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html#%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E4%BF%AE%E6%94%B9%E4%B8%8E%E6%9E%84%E9%80%A0)二叉树的修改与构造 <a href="#er-cha-shu-de-xiu-gai-yu-gou-zao" id="er-cha-shu-de-xiu-gai-yu-gou-zao"></a>

* [翻转二叉树(opens new window)](https://programmercarl.com/0226.%E7%BF%BB%E8%BD%AC%E4%BA%8C%E5%8F%89%E6%A0%91.html)
  * 递归：前序，交换左右孩子
  * 迭代：直接模拟前序遍历
* [构造二叉树(opens new window)](https://programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html)
  * 递归：前序，重点在于找分割点，分左右区间构造
  * 迭代：比较复杂，意义不大
* [构造最大的二叉树(opens new window)](https://programmercarl.com/0654.%E6%9C%80%E5%A4%A7%E4%BA%8C%E5%8F%89%E6%A0%91.html)
  * 递归：前序，分割点为数组最大值，分左右区间构造
  * 迭代：比较复杂，意义不大
* [合并两个二叉树(opens new window)](https://programmercarl.com/0617.%E5%90%88%E5%B9%B6%E4%BA%8C%E5%8F%89%E6%A0%91.html)
  * 递归：前序，同时操作两个树的节点，注意合并的规则
  * 迭代：使用队列，类似层序遍历

### [#](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html#%E6%B1%82%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E5%B1%9E%E6%80%A7)求二叉搜索树的属性 <a href="#qiu-er-cha-sou-suo-shu-de-shu-xing" id="qiu-er-cha-sou-suo-shu-de-shu-xing"></a>

* [二叉搜索树中的搜索(opens new window)](https://programmercarl.com/0700.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%90%9C%E7%B4%A2.html)
  * 递归：二叉搜索树的递归是有方向的
  * 迭代：因为有方向，所以迭代法很简单
* [是不是二叉搜索树(opens new window)](https://programmercarl.com/0098.%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html)
  * 递归：中序，相当于变成了判断一个序列是不是递增的
  * 迭代：模拟中序，逻辑相同
* [求二叉搜索树的最小绝对差(opens new window)](https://programmercarl.com/0530.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E7%BB%9D%E5%AF%B9%E5%B7%AE.html)
  * 递归：中序，双指针操作
  * 迭代：模拟中序，逻辑相同
* [求二叉搜索树的众数(opens new window)](https://programmercarl.com/0501.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E4%BC%97%E6%95%B0.html)
  * 递归：中序，清空结果集的技巧，遍历一遍便可求众数集合
  * [二叉搜索树转成累加树(opens new window)](https://programmercarl.com/0538.%E6%8A%8A%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E8%BD%AC%E6%8D%A2%E4%B8%BA%E7%B4%AF%E5%8A%A0%E6%A0%91.html)
  * 递归：中序，双指针操作累加
  * 迭代：模拟中序，逻辑相同

### [#](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html#%E4%BA%8C%E5%8F%89%E6%A0%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88%E9%97%AE%E9%A2%98)二叉树公共祖先问题 <a href="#er-cha-shu-gong-gong-zu-xian-wen-ti" id="er-cha-shu-gong-gong-zu-xian-wen-ti"></a>

* [二叉树的公共祖先问题(opens new window)](https://programmercarl.com/0236.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html)
  * 递归：后序，回溯，找到左子树出现目标值，右子树节点目标值的节点。
  * 迭代：不适合模拟回溯
* [二叉搜索树的公共祖先问题(opens new window)](https://programmercarl.com/0235.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html)
  * 递归：顺序无所谓，如果节点的数值在目标区间就是最近公共祖先
  * 迭代：按序遍历

### [#](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html#%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E4%BF%AE%E6%94%B9%E4%B8%8E%E6%9E%84%E9%80%A0)二叉搜索树的修改与构造 <a href="#er-cha-sou-suo-shu-de-xiu-gai-yu-gou-zao" id="er-cha-sou-suo-shu-de-xiu-gai-yu-gou-zao"></a>

* [二叉搜索树中的插入操作(opens new window)](https://programmercarl.com/0701.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%8F%92%E5%85%A5%E6%93%8D%E4%BD%9C.html)
  * 递归：顺序无所谓，通过递归函数返回值添加节点
  * 迭代：按序遍历，需要记录插入父节点，这样才能做插入操作
* [二叉搜索树中的删除操作(opens new window)](https://programmercarl.com/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html)
  * 递归：前序，想清楚删除非叶子节点的情况
  * 迭代：有序遍历，较复杂
* [修剪二叉搜索树(opens new window)](https://programmercarl.com/0669.%E4%BF%AE%E5%89%AA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html)
  * 递归：前序，通过递归函数返回值删除节点
  * 迭代：有序遍历，较复杂
* [构造二叉搜索树(opens new window)](https://programmercarl.com/0108.%E5%B0%86%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E8%BD%AC%E6%8D%A2%E4%B8%BA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html)
  * 递归：前序，数组中间节点分割
  * 迭代：较复杂，通过三个队列来模拟

### [#](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html#%E9%98%B6%E6%AE%B5%E6%80%BB%E7%BB%93)阶段总结 <a href="#jie-duan-zong-jie" id="jie-duan-zong-jie"></a>

大家以上题目都做过了，也一定要看如下阶段小结。

**每周小结都会对大家的疑问做统一解答，并且对每周的内容进行拓展和补充，所以一定要看，将细碎知识点一网打尽！**

* [本周小结！（二叉树系列一）(opens new window)](https://programmercarl.com/%E5%91%A8%E6%80%BB%E7%BB%93/20200927%E4%BA%8C%E5%8F%89%E6%A0%91%E5%91%A8%E6%9C%AB%E6%80%BB%E7%BB%93.html)
* [本周小结！（二叉树系列二）(opens new window)](https://programmercarl.com/%E5%91%A8%E6%80%BB%E7%BB%93/20201003%E4%BA%8C%E5%8F%89%E6%A0%91%E5%91%A8%E6%9C%AB%E6%80%BB%E7%BB%93.html)
* [本周小结！（二叉树系列三）(opens new window)](https://programmercarl.com/%E5%91%A8%E6%80%BB%E7%BB%93/20201010%E4%BA%8C%E5%8F%89%E6%A0%91%E5%91%A8%E6%9C%AB%E6%80%BB%E7%BB%93.html)
* [本周小结！（二叉树系列四）(opens new window)](https://programmercarl.com/%E5%91%A8%E6%80%BB%E7%BB%93/20201017%E4%BA%8C%E5%8F%89%E6%A0%91%E5%91%A8%E6%9C%AB%E6%80%BB%E7%BB%93.html)

### [#](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html#%E6%9C%80%E5%90%8E%E6%80%BB%E7%BB%93)最后总结 <a href="#zui-hou-zong-jie" id="zui-hou-zong-jie"></a>

**在二叉树题目选择什么遍历顺序是不少同学头疼的事情，我们做了这么多二叉树的题目了，Carl给大家大体分分类**。

* 涉及到二叉树的构造，无论普通二叉树还是二叉搜索树一定前序，都是先构造中节点。
* 求普通二叉树的属性，一般是后序，一般要通过递归函数的返回值做计算。
* 求二叉搜索树的属性，一定是中序了，要不白瞎了有序性了。

注意在普通二叉树的属性中，我用的是一般为后序，例如单纯求深度就用前序，[二叉树：找所有路径(opens new window)](https://programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html)也用了前序，这是为了方便让父节点指向子节点。

所以求普通二叉树的属性还是要具体问题具体分析。

二叉树专题汇聚为一张图：

![](https://code-thinking-1253855093.file.myqcloud.com/pics/20211030125421.png)

这个图是 [代码随想录知识星球 (opens new window)](https://programmercarl.com/other/kstar.html)成员：[青 (opens new window)](https://wx.zsxq.com/dweb2/index/footprint/185251215558842)，所画，总结的非常好，分享给大家。

**最后，二叉树系列就这么完美结束了，估计这应该是最长的系列了，感谢大家33天的坚持与陪伴，接下来我们又要开始新的系列了「回溯算法」！**

### [#](https://programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93%E7%AF%87.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC) <a href="#qi-ta-yu-yan-ban-ben" id="qi-ta-yu-yan-ban-ben"></a>

\
\
