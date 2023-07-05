---
title: 'DRVC: A Framework of Any-to-Any Voice Conversion with Self-Supervised Learning'
authors:
  - Qiqi Wang
  - Xulong Zhang
  - Jianzong Wang
  - Ning Cheng
  - Jing Xiao
corresponding_author:
    - ''
    - ''
    - 'Corresponding author'
date: '2022-05-23T00:00:00Z'
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2022 IEEE International Conference on Acoustics, Speech and Signal Processing*
publication_short: In *ICASSP2022* (CCF-B)

abstract: Any-to-any voice conversion problem aims to convert voices for source and target speakers, which are out of the training data. Previous works wildly utilize the disentangle-based models. The disentangle-based model assumes the speech consists of content and speaker style information and aims to untangle them to change the style information for conversion. Previous works focus on reducing the dimension of speech to get the content information. But the size is hard to determine to lead to the untangle overlapping problem. We propose the Disentangled Representation Voice Conversion (DRVC) model to address the issue. DRVC model is an end-to-end self-supervised model consisting of the content encoder, timbre encoder, and generator. Instead of the previous work for reducing speech size to get content, we propose a cycle for restricting the disentanglement by the Cycle Reconstruct Loss and Same Loss. The experiments show there is an improvement for converted speech on quality and voice similarity.


tags:
  - Voice Conversion
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2202.10976'
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9747434'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: 'https://sigport.org/sites/default/files/docs/DRVC-presentation.pdf'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Architecture of the Disentangled Representation Voice
Conversion (DRVC) model'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

