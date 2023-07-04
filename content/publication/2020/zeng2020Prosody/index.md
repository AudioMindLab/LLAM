---
title: 'Prosody Learning Mechanism for Speech Synthesis System Without Text Length Limit'
authors:
  - Zhen Zeng
  - Jianzong Wang
  - Ning Cheng
  - Jing Xiao

date: '2020-10-25T00:00:00Z' # TODO
doi: ''


# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *21th Annual Conference of the International Speech Communication Association*
publication_short: In *INTERSPEECH2020* (CCF-C)

abstract: Recent neural speech synthesis systems have gradually focused on the control of prosody to improve the quality of synthesized speech, but they rarely consider the variability of prosody and the correlation between prosody and semantics together. In this paper, a prosody learning mechanism is proposed to model the prosody of speech based on TTS system, where the prosody information of speech is extracted from the mel-spectrum by a prosody learner and combined with the phoneme sequence to reconstruct the mel-spectrum. Meanwhile, the semantic features of text from the pre-trained language model is introduced to improve the prosody prediction results. In addition, a novel self-attention structure, named as local attention, is proposed to lift this restriction of input text length, where the relative position information of the sequence is modeled by the relative position matrices so that the position encodings is no longer needed. Experiments on English and Mandarin show that speech with more satisfactory prosody has obtained in our model. Especially in Mandarin synthesis, our proposed model outperforms baseline model with a MOS gap of 0.08, and the overall naturalness of the synthesized speech has been significantly improved.


tags:
  - TTS
featured: true
links:
- name: "arXiv"
  url: 'https://arxiv.org/abs/2008.05656'
- name: "ISCA"
  url: 'https://www.isca-speech.org/archive/interspeech_2020/zeng20b_interspeech.html'
url_pdf: 'https://www.isca-speech.org/archive/pdfs/interspeech_2020/zeng20b_interspeech.pdf'
url_code: ''
url_poster: ''
url_slides: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Model Training with Prosody Learning Mechanism and Prosody predictor'
  focal_point: ''
  preview_only: false


---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

