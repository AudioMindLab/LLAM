---
title: 'A Language Model Based Pseudo-Sample Deliberation for Semi-supervised Speech Recognition'
authors:
  - Cheng Yi
  - Jianzong Wang
  - Ning Cheng
  - Shiyu Zhou
  - Bo Xu
corresponding_author:
    - ''
    - 'Corresponding author'
date: '2021-07-18T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2021 International Joint Conference on Neural Networks*
publication_short: In *IJCNN2021* (CCF-C)

abstract: End-to-end modeling requires tremendous amounts of transcribed speech to achieve an automatic speech recognition (ASR) model with high performance. For low-resource ASR tasks, it is a promising approach to utilize the highly accessible unlabeled speech and text corpus. Previous works have shown that training with pseudo samples, which are the inferring results given the unlabeled speech, can substantially improve the accuracy of a baseline ASR model. Besides the common data filtering to improve pseudo-label quality, we propose an alternative pseudo-sample deliberation method that operates on the output of the ASR model through a pre-trained bidirectional language model (BERT). It fixes the unreasonable tokens in the inference by substitution, which can distill knowledge from the large text corpus. Experiments on Librispeech show that assisted with our fixing operation, self-training on additional unlabeled samples can bridge up to 82.3 % of the gap with the supervised training.


tags:
  - ASR
featured: true
links:
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9533793'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The ASR model structure we used in this work'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

