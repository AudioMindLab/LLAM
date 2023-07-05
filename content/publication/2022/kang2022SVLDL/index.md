---
title: 'SVLDL: Improved Speaker Age Estimation Using Selective Variance Label Distribution Learning'
authors:
  - Zuheng Kang
  - Jianzong Wang
  - Junqing Peng
  - Jing Xiao
corresponding_author:
    - ''
    - 'Corresponding author' 
date: '2022-12-31T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2022 IEEE Spoken Language Technology Workshop*
publication_short: In *SLT2022*

abstract: Estimating age from a single speech is a classic and challenging topic. Although Label Distribution Learning (LDL) can represent adjacent indistinguishable ages well, the uncertainty of the age estimate for each utterance varies from person to person, i.e., the variance of the age distribution is different. To address this issue, we propose selective variance label distribution learning (SVLDL) method to adapt the variance of different age distributions. Furthermore, the model uses WavLM as the speech feature extractor and adds the auxiliary task of gender recognition to further improve the performance. Two tricks are applied on the loss function to enhance the robustness of the age estimation and improve the quality of the fitted age distribution. Extensive experiments show that the model achieves state-of-the-art performance on all aspects of the NIST SRE08-10 and a real-world datasets.




tags:
  - Speech
featured: true

links:
- name: "IEEE"
  url: "https://ieeexplore.ieee.org/document/10023124"
- name: "arXiv"
  url: "https://arxiv.org/abs/2210.09524"
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Network topology of the SVLDL framework'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

