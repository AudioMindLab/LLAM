---
title: 'Shoggoth: Towards Efficient Edge-Cloud Collaborative Real-Time Video Inference via Adaptive Online Learning'
authors:
  - Liang Wang 
  - Kai Lu
  - Nan Zhang
  - Xiaoyang Qu
  - Jianzong Wang
  - Jiguang Wan
  - Guokuan Li
  - Jing Xiao
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
date: '2023-06-27T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *60th ACM/IEEE Design Automation Conference*
publication_short: In *DAC2023* (CCF-A)

abstract:   This paper proposes Shoggoth, an efficient edge-cloud collaborative architecture, for boosting inference performance on real-time video of changing scenes. Shoggoth uses online knowledge distillation to improve the accuracy of models suffering from data drift and offloads the labeling process to the cloud, alleviating constrained resources of edge devices. At the edge, we design adaptive training using small batches to adapt models under limited computing power, and adaptive sampling of training frames for robustness and reducing bandwidth. The evaluations on the realistic dataset show 15%–20% model accuracy improvement compared to the edge-only strategy and fewer network costs than the cloud-only strategy.



tags:
  - Other
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2306.15333'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Shoggoth system overview'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

