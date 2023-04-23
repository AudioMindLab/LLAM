---
widget: slider
weight: 50
active: true
headless: true

design:
  # Slide height is automatic unless you force a specific height (e.g. '400px')
  slide_height: ''
  is_fullscreen: true
  # Automatically transition through slides?
  loop: false
  # Duration of transition between slides (in ms)
  interval: 2000

content:
  slides:
    - title: 👋 Welcome to the group
      content: Take a look at workplaces in our lab...
      align: center
      background:
        position: right
        color: '#666'
        brightness: 0.7
        media: 工位.jpg
    - title: Lab of Large Audio Model
      content: 'Share your knowledge with the group and explore exciting new topics together!'
      align: right
      background:
        position: center
        color: '#333'
        brightness: 0.5
        media: welcome.jpg
      link:
        icon: graduation-cap
        icon_pack: fas
        text: Join Us
        url: ../contact/
---