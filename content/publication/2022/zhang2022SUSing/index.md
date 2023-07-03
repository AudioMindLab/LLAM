---
title: 'SUSing: SU-net for Singing Voice Synthesis'
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

abstract: Singing voice synthesis is a generative task that involves multi-dimensional control of the singing model, including lyrics, pitch, and duration, and includes the timbre of the singer and singing skills such as vibrato. In this paper, we proposed SU-net for singing voice synthesis named SUSing. Synthesizing singing voice is treated as a translation task between lyrics and music score and spectrum. The lyrics and music score information is encoded into a two-dimensional feature representation through the convolution layer. The two-dimensional feature and its frequency spectrum are mapped to the target spectrum in an autoregressive manner through a SU-net network. Within the SU-net the stripe pooling method is used to replace the alternate global pooling method to learn the vertical frequency relationship in the spectrum and the changes of frequency in the time domain. The experimental results on the public dataset Kiritan show that the proposed method can synthesize more natural singing voices.


tags:
  - MIR
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2205.11841'
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9892111'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'An overview of the proposed method of SU-net for singing voice synthesis'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

