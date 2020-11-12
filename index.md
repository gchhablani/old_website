---
layout: default
title: Gunjan Chhablani
permalink: /
---

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<div style="float:none;overflow:hidden">

    <p style="white-space:nowrap">
      <img class="cover" style = "float:left;" src="images/mypicture_1.jpg" alt="A picture of me from 2019, clicked at a restaurant called 'Bay 15' in Goa, India." title ="A picture of myself from 2019, clicked at a restaurant called 'Bay 15' in Goa, India.">
    </p>

    <p class="title">
        <!-- <a href="https://www.oracle.com/in/index.html">
          <img class = "orglogo" src="images/oraclelogo.png">
        </a><br> -->
        <ul class="affiliations">
          <li>
            Application Developer<br>
            Oracle<br>
            Hyderabad, India
          </li>
        </ul>


    </p>
</div>


****

## Bio ##
Information about me. Coming Soon!

*****
## Projects ##

<div class="posts">
  {% for project in site.projects %}
    <article class="post">

      <h3><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></h3>

      <div class="entry">
        {{ project.content }}
      </div>

      <!-- <a href="{{ site.baseurl }}{{ project.url }}" class="read-more">Read More</a> -->
    </article>
  {% endfor %}
</div>
