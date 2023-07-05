---
title: 'A Practical Singing Voice Detection System Based on GRU-RNN'
authors:
  - Zhigao Chen
  - Xulong Zhang
  - Jin Deng
  - Juanjuan Li
  - Yiliang Jiang
  - Wei Li
corresponding_author:
    - ''
    - ''
    - ''
    - ''
    - ''
    - 'Corresponding author'
date: '2018-11-24T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 6th Conference on Sound and Music Technology*
publication_short: In *CSMT2018* (Best Paper Award)

abstract: In this paper, we present a practical three-step approach for singing voice detection based on a gated recurrent unit (GRU) recurrent neural network (RNN) and the proposed method achieves comparable results to state-of-the-art method. We combine four classic features—namely Mel-frequency Cepstral Coefficients (MFCC), Mel-filter Bank, Linear Predictive Cepstral Coefficients (LPCC), and Chroma. Then, the mixed signal is first preprocessed by singing voice separation (SVS) with the Deep U-Net Convolutional Networks. Long short-term memory (LSTM) and GRU are both proposed to solve the gradient vanish problem in RNN. In our experiments, we set the block duration as 120 ms and 720 ms respectively, and we get comparable or better results than results from state-of-the-art methods, while results on Jamendo are not as good as those from RWC-Pop.


tags:
  - MIR
featured: true

links:
- name: "Springer"
  url: 'https://link.springer.com/chapter/10.1007/978-981-13-8707-4_2'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'A system overview'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

