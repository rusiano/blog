---
date:
  created: 2020-01-12
# links:
#   - Homepage: index.md#project-layout
#   - Blog index: blog/index.md
#   - External links:
#     - Material documentation: https://squidfunk.github.io/mkdocs-material
categories:
  - TIFO
tags:
  - today I found out
  - dataset
  - airbnb
  - madrid

---

# Madrid Airbnb dataset: few findings
<!-- more -->

Some of you may know that I've been teaching Python for Data Science for the last 3 months. During the tedious quest for relevant datasets to practice with Pandas, I eventually found very interesting data about hashtag#Airbnb listings in several cities around the world. hashtag#Madrid was among those cities so I decided to use those data for my course. While preparing questions for my students I also did my own analysis and I created a Kaggle kernel out of it. Since this week the course has come to an end I feel it's the right time to share it.

Few alarming facts and figures I discovered:
- Bed-N-Breakfast days are over: more than 60% of the listings are for entire homes/apartments;
- Centro is flooding with tourists: the city center (Centro) is completely packed with Airbnbs as it has 47% of all the listings in the city and a density of almost 1800 listings per km2;
- High risk of speculation: 20% of the hosts have multiple listings for rent which means they possibly run businesses and do not live in the property; even worse, if we look at hosts that rent an entire home then 80% of them have at least another entire property put up for rent!

Have a look at the kernel on Kaggle [here](https://bit.ly/35Kl1ol).