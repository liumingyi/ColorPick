## 颜色选择器

![](/Users/liumingyi/Documents/Projects-Python/PickColor/pic_colors.jpeg)

点击相应的颜色即可复制颜色代码。

颜色来源于 [Google Material Color](https://material.io/design/color/the-color-system.html#tools-for-picking-colors)

Link：https://material.io/design/color/the-color-system.html#tools-for-picking-colors

---

使用 py2app 将Python脚本为 .app 应用。

期间遇到一个小插曲，生成的 .app 一直不可用。

最后找到这个[回答](https://stackoverflow.com/questions/45493029/valueerror-character-u6573552f-py2aap)

Link：https://stackoverflow.com/questions/45493029/valueerror-character-u6573552f-py2aap

说是 py2app 0.14 的问题，换成 0.13 就好了。而此时已经更新到 0.17，于是从0.17往下尝试一直到 0.13 ，才成功。 :（  

Why ???


