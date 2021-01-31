---
layout: default
title: Gunjan Chhablani
permalink: /
---

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

<div style="float:none;overflow:hidden">

    <p>
      <img class="cover" src="images/mypicture_1.jpg" alt="Happy times @ Bay 15, Goa, India." title ="Happy times @ Bay 15, Goa, India.">
    </p>



      <p class="title">
          <ul class="affiliations">
            {% for affiliation in site.affiliations %}

            <li>
                <div>
                  <div>
                  <a href = "{{ affiliation.link }}">
                    <img src="{{ affiliation.logo }}">
                  </a>
                  </div>


                  <span>
                  {{ affiliation.role }}<br>
                  {{ affiliation.organization }}<br>
                  {{ affiliation.location }}
                  </span>
                </div>

            </li>
           {% endfor %}
          </ul>
      </p>

</div>


****

## Bio ##

Hello there! I am Gunjan Chhablani, a recently graduated undergrad from [BITS Pilani Goa](https://bits-pilani.ac.in/), with a B.E. in Computer Science. I am currently working as an Applications Engineer at [Oracle, India](https://www.oracle.com/in/index.html) where I work on developing web applications for Human Capital Management. 

Prior to this, I spent a wonderful semester at [University of Pittsburgh, Medical Center](https://www.upmc.com/) for my undergraduate thesis where I was advised by [Dr. Kunal Dansingani](http://ophthalmology.pitt.edu/people/kunal-k-dansingani-mbbs-ma-frcophth) and [Dr. Shan Suthaharan](https://sites.google.com/uncg.edu/shan-suthaharan/home?authuser=0). My work focussed on analysing a novel weight initialization technique and its performance on choroid segmentation in OCT Scans.

Apart from that, I am highly interested in deep learning and its applications and use my personal time to work on research projects. My broad research interests include - computer vision, biomedical image analysis, natural language processing, and multi-modal learning.

In the little "personal" time that I get, I love reading self-help books, going out for a stroll, and listening to music/podcasts. I am also big on binge-watching and have watched over 40 TV shows.

I'm always up for collaboration, so if you're interesting in working with me, I would be immensely pleased to hear from you. :)


-----

## News ##

[Jan 2021] I participated in SemEval-2021 Task-5 [Toxic Spans Detection](https://sites.google.com/view/toxicspans). GitHub and paper coming soon!

[Jan 2021] I participated in SemEval-2021 Task-4 [Reading Comprehension of Abstract Meaning](https://competitions.codalab.org/competitions/26153). GitHub and paper coming soon!

[Jan 2021] I participated in [ML Reproducibility Challenge 2020](https://paperswithcode.com/rc2020). GitHub and Report coming soon!

-----

## Projects ##

<div class="posts">
  {% for project in site.projects %}
    <article class="post">
    <h3><a href="{{ site.baseurl }}{{ project.url }}">{{ project.title }}</a></h3>

    <div class="projectinfo">
      {% assign mentorsize = project.mentors | size %}
      {% if mentorsize !=0 %}
        <i> Mentor(s):
          {% for mentor in project.mentors %}
          <a href = "{{ mentor.link }}">{{ mentor.name }}</a>,
          {% endfor %}
        </i>
      {% endif %}

      {% assign domainsize = project.domains | size %}
      {% if domainsize !=0 %}
          <i> Domain(s):
            {% for domain in project.domains %}
            {{ domain }}
              {% if forloop.last == false %}, {% endif %}
            {% endfor %}
          </i>

      {% endif %}
    </div>

    {% if project.codelink %}
       <a class="code" href="{{ project.codelink }}"> Code </a>
    {% endif %}



    {% if project.image %}
    <figure>
      <img src = "{{ project.image }}" title="{{ project.hovercaption}}" style="width:70%;height:auto;">
      <figcaption>{{ project.caption }}</figcaption>
    </figure>
    {% endif %}



    <div class="entry">
      {{ project.content }}
    </div>

      <!-- <a href="{{ site.baseurl }}{{ project.url }}" class="read-more">Read More</a> -->
    </article>
  {% endfor %}
</div>
