---
title: 'Investigation of Singing Voice Separation for Singing Voice Detection in Polyphonic Music'
authors:
  - Yifu Sun
  - Xulong Zhang
  - Xi Chen
  - Yi Yu
  - Wei Li
date: '2022-09-01T00:00:00Z'
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 9th Conference on Sound and Music Technology*
publication_short: In *CSMT2022* (Best Paper Award)

abstract: Singing voice detection (SVD), to recognize vocal parts in the song, is an essential task in music information retrieval (MIR). The task remains challenging since singing voice varies and intertwines with the accompaniment music, especially for some complicated polyphonic music such as choral music recordings. To address this problem, we investigate singing voice detection while discarding the interference from the accompaniment. The proposed SVD has two steps{:} i. The singing voice separation (SVS) technique is first utilized to filter out the singing voice’s potential part coarsely. ii. Upon the continuity of vocal in the time domain, Long-term Recurrent Convolutional Networks (LRCN) is used to learn compositional features. Moreover, to eliminate the outliers, we choose to use a median filter for time-domain smoothing. Experimental results show that the proposed method outperforms the existing state-of-the-art works on two public datasets, the Jamendo Corpus and the RWC pop dataset.




tags:
  - MIR
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2004.04040'
- name: "Springer"
  url: 'https://link.springer.com/chapter/10.1007/978-981-19-4703-2_7'
url_pdf: ''
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Singing voice separation method in the green dashed block and the U-Net model in the blue dashed block'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

