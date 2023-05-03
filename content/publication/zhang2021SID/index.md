---
title: 'Singer Identification Using Deep Timbre Feature Learning with KNN-NET'
authors:
  - Xulong Zhang
  - Jiale Qian
  - Yi Yu
  - Yifu Sun
  - Wei Li
date: '2021-06-06T00:00:00Z'
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2021 IEEE International Conference on Acoustics, Speech and Signal Processing*
publication_short: In *ICASSP2021*

abstract: In this paper, we study the issue of automatic singer identification (SID) in popular music recordings, which aims to recognize who sang a given piece of song. The main challenge for this investigation lies in the fact that a singer's singing voice changes and intertwines with the signal of background accompaniment in time domain. To handle this challenge, we propose the KNN-Net for SID, which is a deep neural network model with the goal of learning local timbre feature representation from the mixture of singer voice and background music. Unlike other deep neural networks using the softmax layer as the output layer, we instead utilize the KNN as a more interpretable layer to output target singer labels. Moreover, attention mechanism is first introduced to highlight crucial timbre features for SID. Experiments on the existing artist20 dataset show that the proposed approach outperforms the state-of-the-art method by 4%. We also create singer32 and singer60 datasets consisting of Chinese pop music to evaluate the reliability of the proposed method. The more extensive experiments additionally indicate that our proposed model achieves a significant performance improvement compared to the state-of-the-art methods.


tags:
  - Singer Identification
featured: true
links:
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9413774'
url_pdf: ''
url_code: 'https://gitlab.com/exp_codes/tut-attention'
url_poster: ''
url_slides: ''
url_dataset: 'https://zenodo.org/record/3531980#.ZEyBwOxByeA'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The overview of the proposed deep network architecture for singer identification'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

