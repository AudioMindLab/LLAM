---
title: 'Uncertainty Calibration for Deep Audio Classifiers'
authors:
  - Tong Ye
  - Shijing Si
  - Jianzong Wang
  - Ning Cheng
  - Jing Xiao

date: '2022-09-18T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *23rd Annual Conference of the International Speech Communication Association*
publication_short: In *INTERSPEECH2022* (CCF-C)

abstract: Although deep Neural Networks (DNNs) have achieved tremendous success in audio classification tasks, their uncertainty calibration are still under-explored. A well-calibrated model should be accurate when it is certain about its prediction and indicate high uncertainty when it is likely to be inaccurate. In this work, we investigate the uncertainty calibration for deep audio classifiers. In particular, we empirically study the performance of popular calibration methods{:}(i) Monte Carlo dropout, (ii) ensemble, (iii) focal loss, and (iv) spectral-normalized Gaussian process (SNGP), on audio classification datasets. To this end, we evaluate (i–iv) for the tasks of environment sound and music genre classification. Results indicate that uncalibrated deep audio classifiers may be over-confident, and SNGP performs the best and is very efficient on the two datasets of this paper.






tags:
  - Speech
featured: true
links:
- name: "ISCA"
  url: 'https://www.isca-speech.org/archive/interspeech_2022/ye22b_interspeech.html'
url_pdf: 'https://www.isca-speech.org/archive/pdfs/interspeech_2022/ye22b_interspeech.pdf'
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Reliability diagrams of the ResNet-50 architecture and four calibration methods'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

