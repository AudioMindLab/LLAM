---
title: 'Loss Prediction: End-to-End Active Learning Approach For Speech Recognition'
authors:
  - Jian Luo
  - Jianzong Wang
  - Ning Cheng
  - Jing Xiao



date: '2021-07-18T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2021 International Joint Conference on Neural Networks*
publication_short: In *IJCNN2021*

abstract: End-to-end speech recognition systems usually require huge amounts of labeling resource, while annotating the speech data is complicated and expensive. Active learning is the solution by selecting the most valuable samples for annotation. In this paper, we proposed to use a predicted loss that estimates the uncertainty of the sample. The CTC (Connectionist Temporal Classification) and attention loss are informative for speech recognition since they are computed based on all decoding paths and alignments. We defined an end-to-end active learning pipeline, training an ASR/LP (Automatic Speech Recognition/Loss Prediction) joint model. The proposed approach was validated on an English and a Chinese speech recognition task. The experiments show that our approach achieves competitive results, outperforming random selection, least confidence, and estimated loss method.


tags:
  - ASR
featured: true

url_pdf: 'https://ieeexplore.ieee.org/document/9533839'
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Active Learning Pipeline with Loss Prediction'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

