---
layout: page
title: Today I Learned
permalink: /TIL
---
I was inspired by [Aditya Lahiri](https://adityalahiri.github.io) to start this section.

With everyday bringing new challenges and problems, it is easy to forget what I've learned yesterday. Hence, this page is here to keep a track of what I'm learning and to make sense of the progress that I make.

This page is specific to my learnings in research/programming, be it in Web D/ML/DL/CV/NLP. Basically, any of the "CS stuff" I do.

I have not been able to update things accurately till 12/25/2020. Post that, I have tried to put up everything.

*****
{% assign sorted = site.tils|sort : 'date'|reverse %}
{% for til in sorted %}

  {% assign content = til.content | strip_newlines %}
  {% if content == "" or content == nil or content == blank or content == "<p>-</p>" %}
    {% continue %}
  {% endif %}
  <h3>{{ til.date | date: "%B %e, %Y" }}</h3>
  <div>
    {{ til.content }}
  </div>  
  {% if forloop.last == false %}
  <hr>
  {% endif %}
{% endfor %}
