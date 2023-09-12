[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Framework](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&logo=PyTorch&logoColor=white)](https://pytorch.org/)

这是我们组在ICCV 2023关于图像色彩美学评估最新的一篇工作: 

<div align="center">
<h1>
<b>
Thinking Image Color Aesthetics Assessment: Models, Datasets and Benchmarks
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
* 简要版：首个面向图像【色彩】的美学评估数据集，1万7千张左右图像，按色彩搭配的类型进行标注。
* 太长不看版：目前存在的一些图像美学评估数据集在色彩覆盖的种类范围上存在不足，而且也存在严重的样本偏差问题。例如，AVA数据集中大约有一半左右的图像主要是黑白色。因此，这些数据集无法用于训练图像色彩评估模型。为了解决这个问题，我们基于十二色环理论，并结合主色调和辅色调的划分，从15种对比色和15种单色中采集了数据，以确保数据的多样性，并防止产生样本偏差。在进行数据标注的过程中，我们采用了预标注的方法，以避免数据标注产生长尾效应（例如，所有图像都被标注为色彩特别好或特别差的情况）。首先，我们利用经典的色环理论对图像进行和谐性打分，然后利用从网站爬取的样本中提取的浏览量和喜爱量等信息生成粗糙的评分。接着，我们将这两部分评分结合起来，筛选出各分段数量均衡的待标注样本，然后交由标注人员进行打分（不过还是会有长尾效应，因为我们发现标注人员喜欢偷懒，标累的时候，倾向于直接给一个中间的评分-_-!）。


![ICAA17K dataset](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/bedbe5bc-0144-4714-a47f-94aaeb2951f7) 


## Download
* 你可以从这里下载到数据集和标注分数 [谷歌网盘](https://drive.google.com/file/d/18PDtXiQNqHe8NUFK9jpuAjBp2MxRjRGM/view?pli=1)，如果失效了，记得cue我。
* 百度网盘：链接：https://pan.baidu.com/s/1dKDEaiUQ6s6m_Gl5AkIbzg?pwd=8888 
提取码：8888



------------------------------------------------------------------------------------------------------------

# 网络结构Delegate Transformer &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>
* 简要版：魔改可变形transformer，搭配色彩空间划分理论。
* 太长不看版：传统的色彩评估方法主要基于数理统计，通过分析图像中像素的色彩分布来判断色彩的和谐性，但无法考虑到语义内容的影响。我们的研究主要从人眼视觉系统的色彩空间理论出发。这个理论的核心观点是，人类在评价图像色彩时通常将其划分为主色调和辅色调。主色调直接决定了图像的色彩美感，并影响了图像所表达的情感（例如，当画面的主色调是红色时，通常给人一种充满热情和活力的感觉）；而辅色调则间接影响了色彩的呈现效果（例如，在绿叶的衬托下，红色的花朵更能展现美感）。因此，我们的目标是让网络能够感知当前图像的两个关键信息：1.主色调和辅色调分别是什么；2.如何进行色调的划分。在我们的研究中，我们采用了可变形Transformer来设置图像的兴趣点，并根据这些兴趣点来划分不同的色调空间（注意，我们基于语义级别而非像素级别来定义兴趣点）。为了学习色调空间的划分方式，我们提出了一种基于概率统计的色调划分模块，能够自适应地学习色调空间的中心位置和空间宽度。**关于训练权重**：因为目前项目原因，暂时权重不能公开（过段时间肯定开源），不过训练代码都有，大家可以自己训练一个吧。

* 色彩美感评估领域，此前工作为空白，我们索性把所有发布了开源代码的工作都自己跑了一遍（不得不吐槽一句，IAA领域，大部分工作不开源就算了，少数开源做的是相当的差，希望我们组的工作，能撑撑牌面），确立相关指标，发布了一个目前最全的benchmark。
![网络结构](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/7cb28baf-65c0-41fe-a5a0-7d0078a3e8cc)

![Benchmark](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/e555a052-1a7c-45cb-af96-8808577ca930)


# 代码环境
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

# 怎么使用代码
* **注意**: 在ICAA17K或SPAQ上训练之前, 请加载在AVA数据集上的预训练权重，以确保你获得一个好的开始：[link](https://drive.google.com/file/d/1kTwGn2f075iEFi3XrmGRGjgBCEpiNiv9/view?usp=sharing),你也可以自己pre-train一个。
* 我们用了微软的自动调参工具[nni](https://github.com/microsoft/nni)，网上有很多nni相关的[使用教程](https://blog.csdn.net/weixin_43653494/article/details/101039198)，强烈推荐同学们使用这个工具，不仅能自动调参，还能替代TensorBoard对训练过程的各项指标可视化。
* 如果你安装好了nni之后，训练时请配置好config.yml和超参数文件search_space.json，然后运行nnictl create --config config.yml -p 8999，训练的可视化后台可以在本地的http://127.0.0.1:8999 或 http://172.17.0.3:8999 看到。
* 如果你不想用这个工具训练或测试，只需要将代码中类似于param_group['lr']这样的超参数的中括号都改为param_group.lr就可以了。


# 如果你觉得这篇工作对你有帮助，请引用，不要白嫖-_-:
```
@article{hethinking,
  title={Thinking Image Color Aesthetics Assessment: Models, Datasets and Benchmarks},
  author={He, Shuai and Ming, Anlong and Yaqi, Li and Jinyuan, Sun and ShunTian, Zheng and Huadong, Ma},
  journal={ICCV},
  year={2023},
}
```

# 组内其它同类型工作:
+ "EAT: An Enhancer for Aesthetics-Oriented Transformers.", [[pdf]](https://github.com/woshidandan/Image-Aesthetics-Assessment/blob/main/Paper_ID_847_EAT%20An%20Enhancer%20for%20Aesthetics-Oriented%20Transformers.pdf) [[code]](https://github.com/woshidandan/Image-Aesthetics-Assessment/tree/main) ACMMM2023.
+ "Rethinking Image Aesthetics Assessment: Models, Datasets and Benchmarks.", [[pdf]](https://www.ijcai.org/proceedings/2022/0132.pdf) [[code]](https://github.com/woshidandan/TANet) IJCAI 2022.

# 其它
* 我们实验室的主页：[视觉机器人与智能技术实验室](http://www.mrobotit.cn/Default.aspx)。
* 我的个人主页：[博客](https://xiaohegithub.cn/)，[知乎](https://www.zhihu.com/people/wo-shi-dan-dan-87)。


