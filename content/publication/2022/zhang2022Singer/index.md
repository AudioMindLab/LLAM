---
title: 'Singer Identification for Metaverse with Timbral and Middle-Level Perceptual Features'
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

abstract: Metaverse is an interactive world that combines reality and virtuality, where participants can be virtual avatars. Anyone can hold a concert in a virtual concert hall, and users can quickly identify the real singer behind the virtual idol through the singer identification. Most singer identification methods are processed using the frame-level features. However, expect the singer's timbre, the music frame includes music information, such as melodiousness, rhythm, and tonal. It means the music information is noise for using frame-level features to identify the singers. In this paper, instead of only the frame-level features, we propose to use another two features that address this problem. Middle-level feature, which represents the music's melodiousness, rhythmic stability, and tonal stability, and is able to capture the perceptual features of music. The timbre feature, which is used in speaker identification, represents the singers' voice features. Furthermore, we propose a convolutional recurrent neural network (CRNN) to combine three features for singer identification. The model firstly fuses the frame-level feature and timbre feature and then combines middle-level features to the mix features. In experiments, the proposed method achieves comparable performance on an average F1 score of 0.81 on the benchmark dataset of Artist20, which significantly improves related works.


tags:
  - MIR
featured: true
links:
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9892657'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The architecture of the proposed SID model'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

