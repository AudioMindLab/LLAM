---
title: 'Investigation of Music Emotion Recognition Based on Segmented Semi-Supervised Learning'
authors:
  - Yifu Sun
  - Xulong Zhang
  - Jianzong Wang
  - Ning Cheng
  - Kaiyu Hu
  - Jing Xiao 
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
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

abstract: The production and annotation of music datasets requires very specialized background knowledge, which is difficult for most people to complete. Therefore, the number of annotated music samples is at a premium for Music Information Retrieval (MIR) tasks. Recently, segment-based methods for emotion-related tasks have been proposed, which train backbone networks on shorter segments instead of entire audio clips, thereby naturally augmenting training samples without requiring additional resources. However, when training at the segment level, segment labels are the major problem. The most commonly used method is that segment inherits the label of the clip containing it, but as we all know, music emotion is not constant during the whole clip. Doing so will introduce label noise and make the training overfit easily. To handle the noisy label issue, we propose a semi-supervised self-learning method and achieve better results than previous methods.



tags:
  - MIR
featured: true
# links:
# - name: "arXiv"
#   url: 'https://arxiv.org/abs/2304.11547'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Flow chart for our proposed method'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

