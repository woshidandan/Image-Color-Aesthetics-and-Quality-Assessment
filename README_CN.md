[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Framework](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&logo=PyTorch&logoColor=white)](https://pytorch.org/)

这是我们组在ICCV 2023关于图像色彩美学评估最新的一篇工作: 

<div align="center">
<h1>
<b>
Delegate Transformer for Image Color Aesthetics Assessment
</b>
</h1>
<h4>
<b>
Shuai He, Anlong Ming, Yaqi Li, Jinyuan Sun, ShunTian Zheng, Huadong Ma
    
Beijing University of Posts and Telecommunications
</b>
</h4>
</div>

因我个人热衷于开源，希望更多的小伙伴关注到这篇工作，故额外写了一篇中文的介绍，不要忘记给我们一个小星星哦，Star一下吧！
<!-- ![ICAA17K dataset](https://user-images.githubusercontent.com/15050507/164587655-4af0b519-7213-4f29-b378-5dfc51dfab83.png)
![Performance](https://user-images.githubusercontent.com/15050507/164587663-043a76d8-5d1b-417e-856d-2320fbe26836.png) -->
------------------------------------------------------------------------------------------------------------

# ICAA17K数据集 &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>


## 介绍
* 简要版：首个面向图像【色彩】的美学评估数据集，1万7千张左右图像，按色彩搭配的类型进行标注。
* 太长不看版：目前图像美学评估数据集，主要聚焦于图像整体美感的研究，但就色彩这一维度而言，数据集中的样本存在严重的selection bias，例如，在最大的通用美学评估数据集AVA中，有几乎50%的图像，都属于“black and white”类型的样本。少数几个色彩评估数据集，也仅仅考虑图像pattern色彩和谐性的表现，脱离图像语义内容，且色彩种类覆盖范围极其有限。为此，我们构建了首个真正面向图像色彩主观美感评估的数据集，在数据采集时，我们就按照
* 常见的视觉上表现为互补色搭配和单色的30种类型，分别整理归类样张，并进行众包标注。
<div align="center">
![ICAA17K dataset](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/bedbe5bc-0144-4714-a47f-94aaeb2951f7) 
</div>

## Download
* 你可以从这里下载到数据集和标注分数 [here]([https://drive.google.com/drive/folders/1b2D9LeeG5XZzhEa8ldnIZjGh0IHadHhU?usp=sharing](https://drive.google.com/file/d/18PDtXiQNqHe8NUFK9jpuAjBp2MxRjRGM/view?pli=1))，如果失效了，记得cue我。
* 百度网盘：链接：待补充

------------------------------------------------------------------------------------------------------------

# 网络结构Delegate Transformer &nbsp;<a href=""><img width="48" src="docs/release_icon.png"></a>


## 介绍
* 简要版：魔改可变形transformer，搭配色彩空间划分理论。
* 太长不看版：待补充。
* 色彩美感评估领域，此前工作为空白，我们索性把所有发布了开源代码的工作都自己跑了一遍（不得不吐槽一句，IAA领域，大部分工作不开源就算了，少数开源做的是相当的差，希望我们组的工作，能撑撑牌面），确立相关指标，发布了一个目前最全的benchmark。
![网络结构](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/7cb28baf-65c0-41fe-a5a0-7d0078a3e8cc)

![Benchmark](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/e555a052-1a7c-45cb-af96-8808577ca930)


## 代码环境
* pandas==0.22.0
* nni==1.8
* requests==2.18.4
* torchvision==0.8.2+cu101
* numpy==1.13.3
* scipy==0.19.1
* tqdm==4.43.0
* torch==1.7.1+cu101
* scikit_learn==1.0.2
* tensorboardX==2.5

## 如何训练和测试
* 炼丹是一个痛苦的过程，特别是像TANet这种的多分支网络，每个分支若设置相同的学习率，训练起来无法达到最优的性能，若单独手工设置各分支学习率，耗时又耗力，所以这里面我们用了微软的自动调参工具[nni](https://github.com/microsoft/nni)，网上有很多nni相关的[使用教程](https://blog.csdn.net/weixin_43653494/article/details/101039198)，强烈推荐同学们使用这个工具，不仅能自动调参，还能替代TensorBoard对训练过程的各项指标可视化。
* 如果你安装好了nni之后，训练时请配置好config.yml和超参数文件search_space.json，然后运行nnictl create --config config.yml -p 8999，训练的可视化后台可以在本地的http://127.0.0.1:8999 或 http://172.17.0.3:8999 看到。
* 如果你不想用这个工具训练或测试，只需要将代码中类似于param_group['lr']这样的超参数的中括号都改为param_group.lr就可以了。
* PS：FLICKR-AES这个数据集上train的工作可能不会公开，因为目前和一个公司合作，相关的模型已经嵌入进系统中，有一些保密的需求。

## 其它
* 事实上，以TAD66K为起点，后续还有很多工作可以尝试，即使是我们自己发布的TANet，性能也远未达到上限，因为TAD66K每个主题都对应了不同的评分规则，任务难度更大，这点可以在SRCC这种的指标上看出，目前只有0.513，有兴趣的同学，可以继续加油，把指标刷上去。
* 我们实验室的主页：[视觉机器人与智能技术实验室](http://www.mrobotit.cn/Default.aspx)。
* 我的个人主页：[博客](https://xiaohegithub.cn/)，[知乎](https://www.zhihu.com/people/wo-shi-dan-dan-87)。

## 如果你觉得这篇工作对你有帮助，请引用，不要白嫖-_-:
```
@article{herethinking,
  title={Rethinking Image Aesthetics Assessment: Models, Datasets and Benchmarks},
  author={He, Shuai and Zhang, Yongchang and Xie, Rui and Jiang, Dongxiang and Ming, Anlong},
  journal={IJCAI},
  year={2022},
}
```

## 快来尝试一下吧!
https://user-images.githubusercontent.com/15050507/164580816-f98d1dd9-50a0-47b7-b992-2f0374e8a418.mp4

https://user-images.githubusercontent.com/15050507/164580823-4ea8ff91-825b-43dc-a421-f75455e549ae.mp4

https://user-images.githubusercontent.com/15050507/164580840-b7f5624f-486d-46e6-9dd4-efaa92dde09c.mp4


