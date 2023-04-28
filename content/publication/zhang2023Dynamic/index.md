---
title: 'Dynamic Alignment Mask CTC: Improved Mask-CTC with Aligned Cross Entropy'
authors:
  - Xulong Zhang
  - Haobin Tang
  - Jianzong Wang
  - Ning Cheng
  - Jian Luo
  - Jing Xiao 
date: '2023-04-17T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2023 IEEE International Conference on Acoustics, Speech and Signal Processing*
publication_short: In *ICASSP2023*

abstract: Because of predicting all the target tokens in parallel, the non-autoregressive models greatly improve the decoding efficiency of speech recognition compared with traditional autoregressive models. In this work, we present dynamic alignment Mask CTC, introducing two methods{:} (1) Aligned Cross Entropy (AXE), finding the monotonic alignment that minimizes the cross-entropy loss through dynamic programming, (2) Dynamic Rectification, creating new training samples by replacing some masks with model predicted tokens. The AXE ignores the absolute position alignment between prediction and ground truth sentence and focuses on tokens matching in relative order. The dynamic rectification method makes the model capable of simulating the non-mask but possible wrong tokens, even if they have high confidence. Our experiments on WSJ dataset demonstrated that not only AXE loss but also the rectification method could improve the WER performance of Mask CTC.



tags:
  - ASR
featured: true
links:
- name: "Arxiv"
  url: 'https://arxiv.org/abs/2303.07687'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Conformer Architecture of Dynamic Alignment Mask CTC with Mask and Dynamic Rectification Methods'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

