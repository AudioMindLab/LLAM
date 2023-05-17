---
title: 'MDCNN-SID: Multi-scale Dilated Convolution Network for Singer Identification'
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

abstract: Most singer identification methods are processed in the frequency domain, which potentially leads to information loss during the spectral transformation. In this paper, instead of the frequency domain, we propose an end-to-end architecture that addresses this problem in the waveform domain. An en-coder based on Multi-scale Dilated Convolution Neural Networks (MDCNN) was introduced to generate wave embedding from the raw audio signal. Specifically, dilated convolution layers are used in the proposed method to enlarge the receptive field, aiming to extract song-level features. Furthermore, skip connection in the backbone network integrates the multi-resolution acoustic features learned by the stack of convolution layers. Then, the obtained wave embedding is passed into the following networks for singer identification. In experiments, the proposed method achieves comparable performance on the benchmark dataset of Artist20, which significantly improves related works.


tags:
  - MIR
featured: true
links:
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9892338'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Overview of the MDCNN-based deep model architecture'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

