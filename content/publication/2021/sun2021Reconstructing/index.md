---
title: 'Reconstructing Dual Learning for Neural Voice Conversion Using Relatively Few Samples'
authors:
  - Aolan Sun
  - Jianzong Wang
  - Ning Cheng
  - Methawee Tantrawenith
  - Zhiyong Wu
  - Helen Meng
  - Edward Xiao
  - Jing Xiao
corresponding_author:
    - ''
    - 'Corresponding author'
date: '2021-12-13T00:00:00Z'
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2021 IEEE Automatic Speech Recognition and Understanding Workshop*
publication_short: In *ASRU2021*

abstract: This paper introduces a dual learning system for neural voice conversion (DualVC) using relatively few samples based on the symmetry of the speech conversion task. The system contains a pair of sequence-to-sequence neural networks that have the same structure but are trained in opposite directions. The objective function of the dual model training is the sum of paired conversion loss and reconstruction loss during the dual training circle. The models in the two directions are trained alternately to guide each other by the corresponding reconstruction loss. Furthermore, curriculum learning techniques are used to load models in existing fields into the current task to accelerate the rapid iteration and convergence of the model. The experiment on the voice conversion task with the proposed DualVC and curriculum learning strategy obtained a comparable naturalness and similarity with only a 30% dataset than the BaseVC model trained on the full dataset.



tags:
  - Voice Conversion
featured: true
links:
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9687965'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Dual voice conversion mechanism'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

