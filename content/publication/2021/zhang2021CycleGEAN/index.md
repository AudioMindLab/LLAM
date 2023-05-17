---
title: 'CycleGEAN: Cycle Generative Enhanced Adversarial Network for Voice Conversion'
authors:
  - Xulong Zhang
  - Jianzong Wang
  - Ning Cheng
  - Edward Xiao
  - Jing Xiao
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

abstract: Cycle Generative Adversarial Network (CycleGAN) for voice conversion (VC) task only used discriminators to identify whether the input voice is generated or real. It means the confrontational does not check the similarity with the target voice, leading the generated voice not much similar to the target. In this paper, instead of vocal checking, we propose to enhance the confrontation to target similarity checking that addresses this problem. A Cycle Generative Enhanced Adversarial Network (CycleGEAN) was introduced to make the original two discriminators to target classifier and non-target classifier. The target classifier aims to identify whether the target speaks the input voice or not. Similarly, the non-target classifier identifies the non-target voice. Furthermore, we add a gradient reversal layer with different operations for target and non-target. Then in each GAN, we used both classifiers. One is the discriminator, and the other is trained for using in another GAN. In experiments, the proposed method compare to CycleGAN improves Mean Opinion Score (MOS) of 0.1 and Voice Similarity Score (VSS) of 0.2 on the Voice Conversion Challenge 2018 (VCC2018) dataset.


tags:
  - Voice Conversion
featured: true
links:
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9687948'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The architecture of the Cycle Generative Enhanced Adversarial Network'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

