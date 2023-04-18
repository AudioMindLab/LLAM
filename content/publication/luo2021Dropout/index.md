---
title: 'Dropout Regularization for Self-Supervised Learning of Transformer Encoder Speech Representation'
authors:
  - Jian Luo
  - Jianzong Wang
  - Ning Cheng
  - Jing Xiao


date: '2021-08-30T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *22th Annual Conference of the International Speech Communication Association*
publication_short: In *INTERSPEECH2021*

abstract: Predicting the altered acoustic frames is an effective way of self-supervised learning for speech representation. However, it is challenging to prevent the pretrained model from overfitting. In this paper, we proposed to introduce two dropout regularization methods into the pretraining of transformer encoder{:}(1) attention dropout, (2) layer dropout. Both of the two dropout methods encourage the model to utilize global speech information, and avoid just copying local spectrum features when reconstructing the masked frames. We evaluated the proposed methods on phoneme classification and speaker recognition tasks. The experiments demonstrate that our dropout approaches achieve competitive results, and improve the performance of classification accuracy on downstream tasks.



tags:
  - Speech Representation
featured: true

url_pdf: 'https://www.isca-speech.org/archive/interspeech_2021/luo21b_interspeech.html'
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The Transformer Encoder Architecture of SelfSupervised Learning with dropout regularization'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

