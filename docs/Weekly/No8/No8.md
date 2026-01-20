## 📖好文章

* 📄[如何写对 Flutter centerSlice](https://juejin.cn/post/7324501285624561727)
* 📄[着色器预热？为什么 Flutter 需要？为什么原生 App 不需要？那 Compose 呢？Impeller 呢？](https://juejin.cn/post/7385942645232828442)
* 📄[Flutter Keys： 你的终极指南，让 widget 世界更快乐](https://juejin.cn/post/7356240651039948815)

## 🔨好工具

**PlantUML**

https://plantuml.com/zh/

PlantUML是一个通用性很强的工具，可以快速、直接地创建各种图表。利用简单直观的语言，用户可以毫不费力地绘制各种类型的图表。


**scre.io**

https://scre.io/

`chrome`屏幕录制插件，支持桌面以及标签页录制。最主要是这个工具是免费，缺点输出视频格式是`webm`格式。不过可以用`Python`脚本转码成为`mp4`格式，转码脚本工具推荐使用`ffmpeg`。 由于默认转码帧率存在问题导出`mp4`耗时很长且时长也有问题，因此可用以下指令导出。

```
ffmpeg -fflags +genpts -i 1.webm -r 24 1.mp4
```


