---
title: 'Learning Speech Representations with Flexible Hidden Feature Dimensions'
authors:
  - Huaizhen Tang
  - Xulong Zhang
  - Jianzong Wang
  - Ning Cheng
  - Jing Xiao 
date: '2023-04-17T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2023 IEEE International Conference on Acoustics, Speech and Signal Processing*
publication_short: In *ICASSP2023*

abstract: Non-parallel many-to-many voice conversion is a kind of style transfer task in speech. Recently, AutoVC has been applied in this field as a popular solution, as it can achieve distribution-matching style transfer by training only the re- construction loss. However, in order to strike a good balance between timbre disentanglement and sound quality, AutoVC requires imposing very strict constraints on the dimension- ality of the latent representation. This constraint affects the quality of the converted speech while making it challenging to apply to other datasets directly. This paper proposes a new voice conversion framework that uses only one encoder to obtain timbre and content information by partitioning the latent space in the channel dimension. Furthermore, two different types of classifiers and two additional reconstruc- tion losses are proposed to ensure that different parts of the latent space contain only separated content and timbre in- formation, respectively. Experiments on the VCTK dataset show that the proposed model achieves state-of-the-art re- sults in terms of the naturalness and similarity of converted speech. In addition, we experimentally show that for different division proportions of latent space, the content and timbre information will always be well separated.



tags:
  - TTS
featured: true

url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The framework of the proposed Model'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

