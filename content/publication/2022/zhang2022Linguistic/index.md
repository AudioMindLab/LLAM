---
title: 'Linguistic-Enhanced Transformer with CTC Embedding for Speech Recognition'
authors:
  - Xulong Zhang
  - Jianzong Wang
  - Ning Cheng
  - Mengyuan Zhao
  - Zhiyong Zhang
  - Jing Xiao 
date: '2022-12-14T00:00:00Z'
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *18th International Conference on Mobility, Sensing and Networking*
publication_short: In *MSN2022* (CCF-C)

abstract: The recent emergence of joint CTC-Attention model shows significant improvement in automatic speech recognition (ASR). The improvement largely lies in the modeling of linguistic information by decoder. The decoder joint-optimized with an acoustic encoder renders the language model from ground-truth sequences in an auto-regressive manner during training. However, the training corpus of the decoder is limited to the speech transcriptions, which is far less than the corpus needed to train an acceptable language model. This leads to poor robustness of decoder. To alleviate this problem, we propose linguistic-enhanced transformer, which introduces refined CTC information to decoder during training process, so that the decoder can be more robust. Our experiments on AISHELL-1 speech corpus show that the character error rate (CER) is relatively reduced by up to 7 %. We also find that in joint CTC-Attention ASR model, decoder is more sensitive to linguistic information than acoustic information.




tags:
  - ASR
featured: true
links:
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/10076600'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Diagram of the semi-supervised learning method based on backbone network'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

