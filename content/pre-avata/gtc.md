---
# A Demo section created with the Blank widget.
# Any elements can be added in the body: https://wowchemy.com/docs/writing-markdown-latex/
# Add more sections by duplicating this file and customizing to your requirements.

# widget: hero # See https://wowchemy.com/docs/page-builder/

# Providing only the video ID as an unnamed parameter
# {{< youtube-enhanced G44Lkj7XDsA >}}

# Providing only the video ID as the named id parameter
# {{< youtube-enhanced id="G44Lkj7XDsA" >}}

# Providing values for named id, title, and start parameters
{{< youtube-enhanced id="G44Lkj7XDsA" title="Hugo Introduction" start="5" >}}


headless: true # This file represents a page section.
weight: 10 # Order that this section will appear.
title: |
  Demo of Pre-Avata on GTC


design:
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns: '1'
  # Add custom styles
  css_style:
  css_class:
---


{{ $id := .Get "id" | default (.Get 0) }}
{{ $start := .Get "start" | default 0 }}
{{ $title := .Get "title" | default "YouTube Video" }}

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube-nocookie.com/embed/{{ $id }}?rel=0&start={{ $start }}"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
          allowfullscreen="" title="{{ $title }}"></iframe>
</div>


<h2>GTC 2022</h2>
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/G44Lkj7XDsA"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
          allowfullscreen="" title="YouTube Video"></iframe>
</div>

<h2>GTC 2023</h2>
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe src="https://www.youtube.com/embed/G44Lkj7XDsA"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
          allowfullscreen="" title="YouTube Video"></iframe>
</div>