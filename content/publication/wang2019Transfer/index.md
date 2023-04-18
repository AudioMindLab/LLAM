---
title: 'Transfer Learning for Music Classification and Regression Tasks Using Artist Tags'
authors:
  - Lei Wang
  - Hongning Zhu
  - Xulong Zhang
  - Shengchen Li
  - Wei Li
date: '2019-12-22T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 7th Conference on Sound and Music Technology*
publication_short: In *CSMT2019*

abstract: In this paper, a transfer learning method that exploits artist tags for general-purpose music feature vector extraction is presented. The feature vector extracted from the last convolutional layer in a deep convolutional neural network (DCNN) trained with artist tags is showed for music classification and regression tasks. Not only are artist tags adequate in the music community, therefore easy to be gathered, but also contain much high-level abstract information about the artists and the music audio released by the artists. To train the network, a dataset containing 33903 30-second clips, annotated with artist tags was created. The model is trained to predict the artist tags from audio content first in the proposed system. Then the model is transferred to extract the features that are used to perform music genre classification and music emotion recognition tasks. The experiment results show that the features learned using artist tags under the context of transfer learning are able to be effectively applied in music genre classification and music emotion recognition tasks.



tags:
  - Music emotion recognition
  - Music genre classification
featured: true

url_pdf: 'https://link.springer.com/chapter/10.1007/978-981-15-2756-2_7'
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'A diagram of framework'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

