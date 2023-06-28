---
title: 'On the Calibration and Uncertainty with Pólya-Gamma Augmentation for Dialog Retrieval Models'
authors:
  - Tong Ye
  - Shijing Si
  - Jianzong Wang
  - Ning Cheng
  - Zhitao Li
  - Jing Xiao

# author_notes:
#   - 'Equal contribution'
#   - 'Equal contribution'
date: '2023-06-26T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *Thirty-Seventh AAAI Conference on Artificial Intelligence*
publication_short: In *AAAI2023* (CCF-A)

abstract: Deep neural retrieval models have amply demonstrated their power but estimating the reliability of their predictions remains challenging. Most dialog response retrieval models output a single score for a response on how relevant it is to a given question. However, the bad calibration of deep neural network results in various uncertainty for the single score such that the unreliable predictions always misinform user decisions. To investigate these issues, we present an efficient calibration and uncertainty estimation framework PG-DRR for dialog response retrieval models which adds a Gaussian Process layer to a deterministic deep neural network and recovers conjugacy for tractable posterior inference by Pólya-Gamma augmentation. Finally, PG-DRR achieves the lowest empirical calibration error (ECE) in the in-domain datasets and the distributional shift task while keeping R10@1 and MAP performance.




tags:
  - Other
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2303.08606'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'An illustration of PG-DRR prediction models for dialog response retrieval'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

