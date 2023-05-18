---
title: 'Feature-Rich Audio Model Inversion for Data-Free Knowledge Distillation Towards General Sound Classification'
authors:
  - Zuheng Kang
  - Yayun He
  - Jianzong Wang
  - Junqing Peng
  - Xiaoyang Qu
  - Jing Xiao
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
 
date: '2023-04-05T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2023 IEEE International Conference on Acoustics, Speech and Signal Processing*
publication_short: In *ICASSP2023* (CCF-B)

abstract: Data-Free Knowledge Distillation (DFKD) has recently attracted growing attention in the academic community, especially with major breakthroughs in computer vision. Despite promising results, the technique has not been well applied to audio and signal processing. Due to the variable duration of audio signals, it has its own unique way of modeling. In this work, we propose feature-rich audio model inversion (FRAMI), a data-free knowledge distillation framework for general sound classification tasks. It first generates high-quality and feature-rich Mel-spectrograms through a feature-invariant contrastive loss. Then, the hidden states before and after the statistics pooling layer are reused when knowledge distillation is performed on these feature-rich samples. Experimental results on the Urbansound8k, ESC-50, and audioMNIST datasets demonstrate that FRAMI can generate feature-rich samples. Meanwhile, the accuracy of the student model is further improved by reusing the hidden state and significantly outperforms the baseline method.




tags:
  - Speech
featured: true

links:
- name: "arXiv"
  url: "https://arxiv.org/abs/2303.07643"
- name: "IEEE"
  url: "https://ieeexplore.ieee.org/document/10096079"
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Feature invariance contrastive inversion overview'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

