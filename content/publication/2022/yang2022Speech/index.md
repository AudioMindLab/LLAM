---
title: 'Speech Representation Disentanglement with Adversarial Mutual Information Learning for One-shot Voice Conversion'
authors:
  - SiCheng Yang
  - Methawee Tantrawenith
  - Haolin Zhuang
  - Zhiyong Wu
  - Aolan Sun
  - Jianzong Wang
  - Ning Cheng
  - Huaizhen Tang
  - Xintao Zhao
  - Jie Wang
  - Helen Meng


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

abstract: One-shot voice conversion (VC) with only a single target-speaker speech for reference has become a new research direction. Existing works generally disentangle timbre, while information about pitch, rhythm and content is still mixed together. To perform one-shot VC effectively with further disentangling these speech components, we employ random resampling for pitch and content encoder and use the variational contrastive log-ratio upper bound of mutual information and gradient reversal layer based adversarial mutual information learning to ensure the different parts of the latent space containing only the desired disentanglement during training. Experiments on the VCTK dataset show the model is a state-of-the-art one-shot VC framework in terms of naturalness and intellgibility of converted speech. In addition, we can transfer style of one-shot VC on timbre, pitch and rhythm separately by speech representation disentanglement. Our code, pre-trained models and demo are available at https://im1eon.github.io/IS2022-SRDVC/.


tags:
  - Voice Conversion
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2208.08757'
- name: "ISCA"
  url: 'https://www.isca-speech.org/archive/interspeech_2022/yang22f_interspeech.html'
- name: "DEMO"
  url: 'https://im1eon.github.io/IS2022-SRDVC/'
url_pdf: 'https://www.isca-speech.org/archive/pdfs/interspeech_2022/yang22f_interspeech.pdf'
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Framework of proposed model'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

