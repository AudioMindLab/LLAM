---
title: 'Unidirectional Memory-Self-Attention Transducer for Online Speech Recognition'
authors:
  - Jian Luo
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

abstract: Self-attention models have been successfully applied in end-to-end speech recognition systems, which greatly improve the performance of recognition accuracy. However, such attention-based models cannot be used in online speech recognition, because these models usually have to utilize a whole acoustic sequences as inputs. A common method is restricting the field of attention sights by a fixed left and right window, which makes the computation costs manageable yet also introduces performance degradation. In this paper, we propose Memory-Self-Attention (MSA), which adds history information into the Restricted-Self-Attention unit. MSA only needs localtime features as inputs, and efficiently models long temporal contexts by attending memory states. Meanwhile, recurrent neural network transducer (RNN-T) has proved to be a great approach for online ASR tasks, because the alignments of RNN-T are local and monotonic. We propose a novel network structure, called Memory-Self-Attention (MSA) Transducer. Both encoder and decoder of the MSA Transducer contain the proposed MSA unit. The experiments demonstrate that our proposed models improve WER results than Restricted-Self-Attention models by 13.5% on WSJ and 7.1% on SWBD datasets relatively, and without much computation costs increase.



tags:
  -  ASR
featured: true
links:
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/9413932'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Memory-Self-Attention Transducer'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

