---
title: 'SVVAD: Personal Voice Activity Detection for Speaker Verification'
authors:
  - Zuheng Kang
  - Jianzong Wang
  - Junqing Peng
  - Jing Xiao 
# author_notes:
#   - 'Equal contribution'
#   - 'Equal contribution'
date: '2023-05-19T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *24th Annual Conference of the International Speech Communication Association*
publication_short: In *interspeech2023* (CCF-C)

abstract: Voice activity detection (VAD) improves the performance of speaker verification (SV) by preserving speech segments and attenuating the effects of non-speech. However, this scheme is not ideal{:} (1) it fails in noisy environments or multi-speaker conversations; (2) it is trained based on inaccurate human-assigned labels. To address this, we propose a speaker verification-based voice activity detection (SVVAD) framework that can adapt the speech features according to which are most informative for SV. To achieve this, we introduce a label-free training method with triplet-like losses that completely avoids the performance degradation of SV due to incorrect human labeling. Extensive experiments show that SVVAD significantly outperforms the baseline in terms of equal error rate (EER) under conditions where other speakers are mixed at different ratios. Moreover, the decision boundaries reveal the importance of the different parts of speech, which are largely consistent with human judgments.


tags:
  - Speech
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2305.19581'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'The network architecture of SVVAD backbone'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

