---
title: 'Multi-Quartznet: Multi-Resolution Convolution for Speech Recognition with Multi-Layer Feature Fusion'
authors:
  - Jian Luo
  - Jianzong Wang
  - Ning Cheng
  - Guilin Jiang
  - Jing Xiao

corresponding_author:
    - ''
    - 'Corresponding author'

date: '2021-01-19T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2021 IEEE Spoken Language Technology Workshop*
publication_short: In *SLT2021*

abstract: In this paper, we propose an end-to-end speech recognition network based on Nvidia's previous QuartzNet [1] model. We try to promote the model performance, and design three components{:} (1) Multi-Resolution Convolution Module, re-places the original 1D time-channel separable convolution with multi-stream convolutions. Each stream has a unique dilated stride on convolutional operations. (2) Channel-Wise Attention Module, calculates the attention weight of each convolutional stream by spatial channel-wise pooling. (3) Multi-Layer Feature Fusion Module, reweights each convolutional block by global multi-layer feature maps. Our experiments demonstrate that Multi-QuartzNet model achieves CER 6.77% on AISHELL-1 data set, which outperforms original QuartzNet and is close to state-of-art result.


tags:
  - ASR
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2011.13090'
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9383532'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Multi-QuartzNet Model Architecture'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

