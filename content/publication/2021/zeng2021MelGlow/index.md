---
title: 'MelGlow: Efficient Waveform Generative Network Based On Location-Variable Convolution'
authors:
  - Zhen Zeng
  - Jianzong Wang
  - Ning Cheng
  - Jing Xiao



date: '2021-01-19T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2021 IEEE Spoken Language Technology Workshop*
publication_short: In *SLT2021*

abstract: Recent neural vocoders usually use a WaveNet-like network to capture the long-term dependencies of the waveform, but a large number of parameters are required to obtain good modeling capabilities. In this paper, an efficient network, named location-variable convolution, is proposed to model the dependencies of waveforms. Different from the use of unified convolution kernels in WaveNet to capture the dependencies of arbitrary waveforms, location-variable convolutions utilizes a kernel predictor to generate multiple sets of convolution kernels based on the melspectrum, where each set of convolution kernels is used to perform convolution operations on the associated waveform intervals. Combining WaveGlow and location-variable convolutions, an efficient vocoder, named MelGlow, is designed. Experiments on the LJSpeech dataset show that MelGlow achieves better performance than WaveGlow at small model sizes, which verifies the effectiveness and potential optimization space of location-variable convolutions.



tags:
  - TTS
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2012.01684'
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9383603'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The architecture'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

