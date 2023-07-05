---
title: 'Transfer Ability of Monolingual Wav2vec2.0 for Low-resource Speech Recognition'
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

abstract: Recently, there are several domains that have their own feature extractors, such as ResNet, BERT, and GPT-x, which are widely used for various down-stream tasks. These models are pre-trained on large amounts of unlabeled data by self-supervision. In the speech domain, wav2vec2.0 starts to show its powerful representation ability and feasibility for ultra-low resource speech recognition tasks. This speech feature extractor is pre-trained on the monolingual audiobook corpus, whereas it has not been thoroughly examined in real spoken scenarios and other languages. In this work, we endeavor to transfer the knowledge from the pre-trained monolingual wav2vec2.0 to cross-lingual spoken ASR tasks with less than 20 hours of labeled data. We achieve more than 20% relative improvements in all the six languages compared with previous methods, establishing a strong benchmark on CALLHOME datasets. Compared with supervised pre-training, self-supervision training used in wav2vec2.0 has a better transfer ability. We also find that using coarse-grained modeling units, such as subword or character, usually achieves better results than fine-grained modeling units, such as phone or letter.



tags:
  - ASR
featured: true
links:
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9533587'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Apply wav2vec2.0 to ASR tasks'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

