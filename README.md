[![Netlify Status](https://api.netlify.com/api/v1/badges/56f03cd8-425b-4487-9b8e-eb15f379e6f7/deploy-status)](https://app.netlify.com/sites/llam/deploys)


# From bib file generate publication
``` bash
pip3 install academic==0.5.1
academic import --bibtex my_publications.bib
academic import --bibtex my_publications.bib --publication-dir content/zh/publication/
```

>https://github.com/wowchemy/hugo-academic-cli