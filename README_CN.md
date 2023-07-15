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
------------------------------------------------------------------------------------------------------------

# ICAA17K数据集 &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>


## 介绍
* 简要版：首个面向图像【色彩】的美学评估数据集，1万7千张左右图像，按色彩搭配的类型进行标注。
* 太长不看版：目前图像美学评估数据集，主要聚焦于图像整体美感的研究，但就色彩这一维度而言，数据集中的样本存在严重的selection bias，例如，在最大的通用美学评估数据集AVA中，有几乎50%的图像，都属于“black and white”类型的样本。少数几个色彩评估数据集，也仅仅考虑图像pattern色彩和谐性的表现，脱离图像语义内容，且色彩种类覆盖范围极其有限。为此，我们构建了首个真正面向图像色彩主观美感评估的数据集，在数据采集时，我们就按照
* 常见的视觉上表现为互补色搭配和单色的30种类型，分别整理归类样张，并进行众包标注。
![ICAA17K dataset](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/bedbe5bc-0144-4714-a47f-94aaeb2951f7) 


## Download
* 你可以从这里下载到数据集和标注分数 [here](https://drive.google.com/file/d/18PDtXiQNqHe8NUFK9jpuAjBp2MxRjRGM/view?pli=1)，如果失效了，记得cue我。
* 百度网盘：链接：待补充



------------------------------------------------------------------------------------------------------------

# 网络结构Delegate Transformer &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>


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



## 其它
* 组内的另一项关于通用美学评估的工作：
+ Shuai He, Yongchang Zhang, Dongxiang Jiang, Rui Xie, Anlong Ming*: "Rethinking Image Aesthetics Assessment: Models, Datasets and Benchmarks.", [[pdf]](https://www.ijcai.org/proceedings/2022/0132.pdf) [[code]](https://github.com/woshidandan/TANet) IJCAI 2022, 人工智能领域顶会.
* 我们实验室的主页：[视觉机器人与智能技术实验室](http://www.mrobotit.cn/Default.aspx)。
* 我的个人主页：[博客](https://xiaohegithub.cn/)，[知乎](https://www.zhihu.com/people/wo-shi-dan-dan-87)。

## 如果你觉得这篇工作对你有帮助，请引用，不要白嫖-_-:
```
@article{heICAA17k,
  title={Delegate Transformer for Image Color Aesthetics Assessment},
  author={He, Shuai and Ming, Anlong and Yaqi, Li and Jinyuan, Sun and ShunTian, Zheng and Huadong, Ma},
  journal={ICCV},
  year={2023},
}
```


