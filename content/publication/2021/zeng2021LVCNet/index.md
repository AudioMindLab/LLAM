---
title: 'LVCNet: Efficient Condition-Dependent Modeling Network for Waveform Generation'
authors:
  - Zhen Zeng
  - Jianzong Wang
  - Ning Cheng
  - Jing Xiao



date: '2021-06-06T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *2021 IEEE International Conference on Acoustics, Speech and Signal Processing*
publication_short: In *ICASSP2021* (CCF-B)

abstract: In this paper, we propose a novel conditional convolution network, named location-variable convolution, to model the dependencies of the waveform sequence. Different from the use of unified convolution kernels in WaveNet to capture the dependencies of arbitrary waveform, the location-variable convolution uses convolution kernels with different coefficients to perform convolution operations on different waveform intervals, where the coefficients of kernels is predicted according to conditioning acoustic features, such as Mel-spectrograms. Based on location-variable convolutions, we design LVCNet for waveform generation, and apply it in Parallel WaveGAN to design more efficient vocoder. Experiments on the LJSpeech dataset show that our proposed model achieves a four-fold increase in synthesis speed compared to the original Parallel WaveGAN without any degradation in sound quality, which verifies the effectiveness of location-variable convolutions.




tags:
  -  TTS
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2102.10815'
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9414710'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The architecture of LVCNet'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

