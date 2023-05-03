---
title: 'Large-Scale Transfer Learning for Low-Resource Spoken Language Understanding'
authors:
  - Xueli Jia
  - Jianzong Wang
  - Zhiyong Zhang
  - Ning Cheng
  - Jing Xiao


date: '2020-10-25T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *21th Annual Conference of the International Speech Communication Association*
publication_short: In *INTERSPEECH2020*

abstract: End-to-end Spoken Language Understanding (SLU) models are made increasingly large and complex to achieve the state-of-the-art accuracy. However, the increased complexity of a model can also introduce high risk of over-fitting, which is a major challenge in SLU tasks due to the limitation of available data. In this paper, we propose an attention-based SLU model together with three encoder enhancement strategies to overcome data sparsity challenge. The first strategy focuses on the transfer-learning approach to improve feature extraction capability of the encoder. It is implemented by pre-training the encoder component with a quantity of Automatic Speech Recognition annotated data relying on the standard Transformer architecture and then fine-tuning the SLU model with a small amount of target labelled data. The second strategy adopts multi-task learning strategy, the SLU model integrates the speech recognition model by sharing the same underlying encoder, such that improving robustness and generalization ability. The third strategy, learning from Component Fusion (CF) idea, involves a Bidirectional Encoder Representation from Transformer (BERT) model and aims to boost the capability of the decoder with an auxiliary network. It hence reduces the risk of over-fitting and augments the ability of the underlying encoder, indirectly. Experiments on the FluentAI dataset show that cross-language transfer learning and multi-task strategies have been improved by up to 4.52% and 3.89% respectively, compared to the baseline.


tags:
  - Spoken Language Understanding
featured: true
links:
- name: "ISCA"
  url: 'https://www.isca-speech.org/archive/interspeech_2020/jia20_interspeech.html'
url_pdf: 'https://www.isca-speech.org/archive/pdfs/interspeech_2020/jia20_interspeech.pdf'
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Structures for base model and augmentation strategies'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

