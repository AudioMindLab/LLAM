---
title: 'Aligntts: Efficient Feed-Forward Text-to-Speech System Without Explicit Alignment'
authors:
  - Zhen Zeng
  - Jianzong Wang
  - Ning Cheng
  - Tian Xia
  - Jing Xiao



date: '2020-05-04T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2020 IEEE International Conference on Acoustics, Speech and Signal Processing*
publication_short: In *ICASSP2020*

abstract: Targeting at both high efficiency and performance, we propose AlignTTS to predict the mel-spectrum in parallel. AlignTTS is based on a Feed-Forward Transformer which generates mel-spectrum from a sequence of characters, and the duration of each character is determined by a duration predictor. Instead of adopting the attention mechanism in Transformer TTS to align text to mel-spectrum, the alignment loss is presented to consider all possible alignments in training by use of dynamic programming. Experiments on the LJSpeech dataset show that our model achieves not only state-of-the-art performance which outperforms Transformer TTS by 0.03 in mean option score (MOS), but also a high efficiency which is more than 50 times faster than real-time.


tags:
  - TTS
featured: true

url_pdf: 'https://ieeexplore.ieee.org/document/9054119'
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Comparison of Alignments'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

