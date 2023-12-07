[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Framework](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?&logo=PyTorch&logoColor=white)](https://pytorch.org/)

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

[[国内的小伙伴请看更详细的中文说明]](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/blob/main/README_CN.md)This repo contains the official implementation and the new dataset ICAA17K of the **ICCV 2023** paper.
 [[Our refined model of this work]](https://github.com/woshidandan/Refine-for-ICAA/blob/main/README.md)

# Largest Color-oriented Dataset: ICAA17K &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>
* Existing IAA datasets primarily focus on evaluating the holistic quality of images and lack of detailed color annotations, with limited color types or combinations. Specifically, these datasets exhibit serious selection bias. e.g., about 50% images of the AVA dataset are “black and white” images, which outnumber other colors by 10 to 100 times, and the PCCD and SPAQ datasets have few images of “pink” and “violet” colors. Therefore, these IAA datasets are not suitable for ICAA tasks and cannot support the generalization of ICAA models well. To address the above issue, we try to develop a specialized and color-oriented dataset the first time. To the best of our knowledge, our ICAA17K dataset is the largest, as well as most densely annotated ICAA dataset with a diverse range of color types and image collection devices. You can **download** dataset and label from [google drive](https://drive.google.com/file/d/18PDtXiQNqHe8NUFK9jpuAjBp2MxRjRGM/view?pli=1), or **download** from：[baidu drive](https://pan.baidu.com/s/1dKDEaiUQ6s6m_Gl5AkIbzg?pwd=8888) 

![ICAA17K dataset](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/bedbe5bc-0144-4714-a47f-94aaeb2951f7) 


# Delegate Transformer &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>
* Traditional quantization methods are based on statistical quantitative information of image pixels, ignoring how spatial and semantic content affect color aesthetics. Although these methods can give qualitative analysis results, they cannot quantify the aesthetic differences brought about by a tiny change in color. Data-driven methods typically extract holistic aesthetic features and lack of prior color knowledge, which take themselves harder to perceive the spatial distribution and composition of different colors in an image, then leading to diffuse attention against perceiving color space. On the other hand, they cannot assign different attention weights based on color importance, which leads to in poor fine-grained perception for color. The proposed Delegate Transformer learns to segment color space from dedicated deformable attention rather than static pixel values, and thus captures spatial information of color. Furthermore, different color spaces are assigned different levels of attention by the Delegate Transformer, which exactly matches human behavior for color space segmentation. Note: Because of the current project reasons, our weights can not be made public (please wait.), but the training code are available, you can train one yourself. Download weights from: [google drive](https://drive.google.com/drive/folders/1plWBu2nZw8BcIcjfq833zdzZ0Pk0L4Ug?usp=sharing).

![网络结构](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/7cb28baf-65c0-41fe-a5a0-7d0078a3e8cc)

# Largest Benchmark of Image Color Aesthetics Assessment &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>
* Previously, there was no benchmark designed for subjective color aesthetics assessment. Based on ICAA17K, we release two large-scale benchmarks of 15 methods for ICAA, the most comprehensive one thus far based on two datasets, SPAQ and ICAA17K.
![Benchmark](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/e555a052-1a7c-45cb-af96-8808577ca930)

# Environment Installation
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

# How to Run the Code
* **Note**: before train on ICAA17K or SPAQ, please load the pre-trained weights on the AVA, you can download the weights from [link](https://drive.google.com/file/d/1kTwGn2f075iEFi3XrmGRGjgBCEpiNiv9/view?usp=sharing),or you can pre-train by yourself.
* We used the hyperparameter tuning tool [nni](https://github.com/microsoft/nni), maybe you should know how to use this tool first (it will only take a few minutes of your time), because our training and testing will be in this tool.
* Train or test, please run: nnictl create --config config.yml -p 8999
* The Web UI urls are: http://127.0.0.1:8999 or http://172.17.0.3:8999
* Note: nni is not necessary, if you don't want to use this tool, just make simple modifications to our code, such as changing param_group['lr'] to param_group.lr, etc.

# If you find our work is useful, pleaes cite our paper:
```
@article{hethinking,
  title={Thinking Image Color Aesthetics Assessment: Models, Datasets and Benchmarks},
  author={He, Shuai and Ming, Anlong and Yaqi, Li and Jinyuan, Sun and ShunTian, Zheng and Huadong, Ma},
  journal={ICCV},
  year={2023},
}
```

# Our other works:
+ "EAT: An Enhancer for Aesthetics-Oriented Transformers.", [[pdf]](https://github.com/woshidandan/Image-Aesthetics-Assessment/blob/main/Paper_ID_847_EAT%20An%20Enhancer%20for%20Aesthetics-Oriented%20Transformers.pdf) [[code]](https://github.com/woshidandan/Image-Aesthetics-Assessment/tree/main) ACMMM2023.
+ "Rethinking Image Aesthetics Assessment: Models, Datasets and Benchmarks.", [[pdf]](https://www.ijcai.org/proceedings/2022/0132.pdf) [[code]](https://github.com/woshidandan/TANet) IJCAI 2022.
