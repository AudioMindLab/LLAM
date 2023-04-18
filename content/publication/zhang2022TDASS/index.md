---
title: 'TDASS: Target Domain Adaptation Speech Synthesis Framework for Multi-speaker Low-Resource TTS'
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
publication_short: In *IJCNN2022*

abstract: Recently, synthesizing personalized speech by text-to-speech (TTS) application is highly demanded. But the previous TTS models require a mass of target speaker speeches for training. It is a high-cost task, and hard to record lots of utterances from the target speaker. Data augmentation of the speeches is a solution but leads to the low-quality synthesis speech problem. Some multi-speaker TTS models are proposed to address the issue. But the quantity of utterances of each speaker imbalance leads to the voice similarity problem. We propose the Target Domain Adaptation Speech Synthesis Network (TDASS) to address these issues. Based on the backbone of the Tacotron2 model, which is the high-quality TTS model, TDASS introduces a self-interested classifier for reducing the non-target influence. Besides, a special gradient reversal layer with different operations for target and non-target is added to the classifier. We evaluate the model on a Chinese speech corpus, the experiments show the proposed method outperforms the baseline method in terms of voice quality and voice similarity.


tags:
  - TTS
featured: true

url_pdf: https://ieeexplore.ieee.org/document/9892596
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The architecture of the Target Domain Adaptation Speech Synthesis Network (TDASS)'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

