---
title: 'MetaSID: Singer Identification with Domain Adaptation for Metaverse'
authors:
  - Xulong Zhang
  - Jianzong Wang
  - Ning Cheng
  - Jing Xiao
date: '2022-07-18T00:00:00Z'
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2022 International Joint Conference on Neural Networks*
publication_short: In *IJCNN2022* (CCF-C)

abstract: Metaverse has stretched the real world into unlimited space. There will be more live concerts in Metaverse. The task of singer identification is to identify the song belongs to which singer. However, there has been a tough problem in singer identification, which is the different live effects. The studio version is different from the live version, the data distribution of the training set and the test set are different, and the performance of the classifier decreases. This paper proposes the use of the domain adaptation method to solve the live effect in singer identification. Three methods of domain adaptation combined with Convolutional Recurrent Neural Network (CRNN) are designed, which are Maximum Mean Discrepancy (MMD), gradient reversal (Revgrad), and Contrastive Adaptation Network (CAN). MMD is a distance-based method, which adds domain loss. Revgrad is based on the idea that learned features can represent different domain samples. CAN is based on class adaptation, it takes into account the correspondence between the categories of the source domain and target domain. Experimental results on the public dataset of Artist20 show that CRNN-MMD leads to an improvement over the baseline CRNN by 0.14. The CRNN-RevGrad outperforms the baseline by 0.21. The CRNN-CAN achieved state of the art with the F1 measure value of 0.83 on album split.


tags:
  - MIR
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2205.11821'
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9892793'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The network architecture of the proposed three methods'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

