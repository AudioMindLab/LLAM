---
title: 'Adapitch: Adaption Multi-Speaker Text-to-Speech Conditioned on Pitch Disentangling with Untranscribed Data'
authors:
  - Xulong Zhang
  - Jianzong Wang
  - Ning Cheng
  - Jing Xiao 
date: '2022-12-14T00:00:00Z'
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *18th International Conference on Mobility, Sensing and Networking*
publication_short: In *MSN2022* (CCF-C)

abstract: In this paper, we proposed Adapitch, a multi-speaker TTS method that makes adaptation of the supervised module with untranscribed data. We design two self supervised modules to train the text encoder and mel decoder separately with untranscribed data to enhance the representation of text and mel. To better handle the prosody information in a synthesized voice, a supervised TTS module is designed conditioned on content disentangling of pitch, text, and speaker. The training phase was separated into two parts, pretrained and fixed the text encoder and mel decoder with unsupervised mode, then the supervised mode on the disentanglement of TTS. Experiment results show that the Adaptich achieved much better quality than baseline methods.




tags:
  - TTS
featured: true
links:
- name: "IEEE"
  url: 'https://ieeexplore.ieee.org/document/10076635'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The overview of the proposed text-to-speech method'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

