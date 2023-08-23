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

# Largest Color-oriented Dataset: ICAA17K &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>
* Existing IAA datasets primarily focus on evaluating the holistic quality of images and lack of detailed color annotations, with limited color types or combinations. Specifically, these datasets exhibit serious selection bias. e.g., about 50% images of the AVA dataset are “black and white” images, which outnumber other colors by 10 to 100 times, and the PCCD and SPAQ datasets have few images of “pink” and “violet” colors. Therefore, these IAA datasets are not suitable for ICAA tasks and cannot support the generalization of ICAA models well. To address the above issue, we try to develop a specialized and color-oriented dataset the first time. To the best of our knowledge, our ICAA17K dataset is the largest, as well as most densely annotated ICAA dataset with a diverse range of color types and image collection devices.

![ICAA17K dataset](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/bedbe5bc-0144-4714-a47f-94aaeb2951f7) 


## Download
* you can download dataset and label from [google drive](https://drive.google.com/file/d/18PDtXiQNqHe8NUFK9jpuAjBp2MxRjRGM/view?pli=1).
* or download from：[baidu drive](https://pan.baidu.com/s/1dKDEaiUQ6s6m_Gl5AkIbzg?pwd=8888) 

# Delegate Transformer &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>
* Traditional quantization methods are based on statistical quantitative information of image pixels, ignoring how spatial and semantic content affect color aesthetics. Although these methods can give qualitative analysis results, they cannot quantify the aesthetic differences brought about by a tiny change in color. Data-driven methods typically extract holistic aesthetic features and lack of prior color knowledge, which take themselves harder to perceive the spatial distribution and composition of different colors in an image, then leading to diffuse attention against perceiving color space. On the other hand, they cannot assign different attention weights based on color importance, which leads to in poor fine-grained perception for color. The proposed Delegate Transformer learns to segment color space from dedicated deformable attention rather than static pixel values, and thus captures spatial information of color. Furthermore, different color spaces are assigned different levels of attention by the Delegate Transformer, which exactly matches human behavior for color space segmentation.

![网络结构](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/7cb28baf-65c0-41fe-a5a0-7d0078a3e8cc)

# Largest Benchmark of Image Color Aesthetics Assessment &nbsp;<a href=""><img width="48" src="https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/94354c2b-c70e-4d31-bc40-4a2c76d671ff"></a>
* Previously, there was no benchmark designed for subjective color aesthetics assessment. Based on ICAA17K, we release two large-scale benchmarks of 15 methods for ICAA, the most comprehensive one thus far based on two datasets, SPAQ and ICAA17K.
![Benchmark](https://github.com/woshidandan/Image-Color-Aesthetics-Assessment/assets/15050507/e555a052-1a7c-45cb-af96-8808577ca930)
