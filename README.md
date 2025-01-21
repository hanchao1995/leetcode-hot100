# leetcode-hot100
督促自己刷题找工作~

[TOC]
## 1. 两数之和 
[题目](https://leetcode.cn/problems/two-sum/?envType=study-plan-v2&envId=top-100-liked) [代码](./code/1.py) 
* 从列表中索引特定元素，返回下标：[list].index()
* 思路简单，只需遍历列表元素，索引target - 当前元素的值是否存在于列表
* 题目要求不能重复使用元素，故要考虑当前遍历元素恰好等于target一半的情况
* 相比于判断列表是否存在2个相同元素，从当前元素以后的子列表nums[i+1:]中索引更加方便，因为其不可能存在于nums[:i+1] (若存在就会在前面返回答案了)

## 49. 字母异位词分组
[题目](https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked) [代码](./code/49.py)

* 字母异位，但是字母个数是不变的，因此很容易想到基于个数的统计来确定同组单词
* 因为只包含小写字母，所以只需要统计26各字母上的个数
* 对于异位词，因为不同排序会对应同一组统计数据，即多对一的方式，因此想到用字典的一个key去统计多个异位词
* 注意，在生成key的字符串时，注意以分隔符隔开，否则当出现10的倍数时会重复，比如 ["bdddddddddd","bbbbbbbbbbc"] → [01010 01010] （只统计到D） 