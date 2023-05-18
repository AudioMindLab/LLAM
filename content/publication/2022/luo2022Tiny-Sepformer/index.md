---
title: 'Tiny-Sepformer: A Tiny Time-Domain Transformer Network For Speech Separation'
authors:
  - Jian Luo
  - Jianzong Wang
  - Ning Cheng
  - Edward Xiao
  - Xulong Zhang
  - Jing Xiao
date: '2022-09-18T00:00:00Z'
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *23rd Annual Conference of the International Speech Communication Association*
publication_short: In *Interspeech2022* (CCF-C)

abstract: Time-domain Transformer neural networks have proven their superiority in speech separation tasks. However, these models usually have a large number of network parameters, thus often encountering the problem of GPU memory explosion. In this paper, we proposed Tiny-Sepformer, a tiny version of Transformer network for speech separation. We presented two techniques to reduce the model parameters and memory consumption{:} (1) Convolution-Attention (CA) block, spliting the vanilla Transformer to two paths, multi-head attention and 1D depthwise separable convolution, (2) parameter sharing, sharing the layer parameters within the CA block. In our experiments, Tiny-Sepformer could greatly reduce the model size, and achieves comparable separation performance with vanilla Sepformer on WSJ0-2/3Mix datasets.




tags:
  - Speech
featured: true
links:
- name: "ISCA"
  url: 'https://www.isca-speech.org/archive/interspeech_2022/luo22_interspeech.html'
url_pdf: 'https://www.isca-speech.org/archive/pdfs/interspeech_2022/luo22_interspeech.pdf'
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The Model Architecture of Tiny-Sepformer'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

