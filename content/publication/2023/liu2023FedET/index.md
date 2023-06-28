---
title: 'FedET: A Communication-Efficient Federated Class-Incremental Learning Framework Based on Enhanced Transformer'
authors:
  - Chenghao Liu
  - Xiaoyang Qu
  - Jianzong Wang
  - Jing Xiao

# author_notes:
#   - 'Equal contribution'
#   - 'Equal contribution'
date: '2023-06-28T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2023 International Joint Conference on Artificial Intelligence*
publication_short: In *IJCAI2023* (CCF-A)

abstract: Federated Learning (FL) has been widely con- cerned for it enables decentralized learning while ensuring data privacy. However, most existing methods unrealistically assume that the classes en- countered by local clients are fixed over time. Af- ter learning new classes, this assumption will make the model’s catastrophic forgetting of old classes significantly severe. Moreover, due to the limi- tation of communication cost, it is challenging to use large-scale models in FL, which will affect the prediction accuracy. To address these chal- lenges, we propose a novel framework, Federated Enhanced Transformer (FedET), which simulta- neously achieves high accuracy and low commu- nication cost. Specifically, FedET uses Enhancer, a tiny module, to absorb and communicate new knowledge, and applies pre-trained Transformers combined with different Enhancers to ensure high precision on various tasks. To address local for- getting caused by new classes of new tasks and global forgetting brought by non-i.i.d class imbal- ance across different local clients, we proposed an Enhancer distillation method to modify the im- balance between old and new knowledge and re- pair the non-i.i.d. problem. Experimental re- sults demonstrate that FedET’s average accuracy on representative benchmark datasets is 14.1% higher than the state-of-the-art method, while FedET saves 90% of the communication cost compared to the previous method.




tags:
  - Other
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2306.15347'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Simple FedET scenario when performing incremental learning'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

