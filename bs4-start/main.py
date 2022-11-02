from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_response = response.text

soup = BeautifulSoup(yc_response, "html.parser")


# all_stories = soup.findAll(name="span", class_="titleline")

all_stories = soup.select(".titleline")
article_titles = []
article_links = []

for article_tag in all_stories:
    article_titles.append(article_tag.select_one("a").getText())
    article_links.append(article_tag.select_one("a").get("href"))

all_scores_text = soup.findAll(name="span", class_="score")
all_scores = [int(score.getText().split(" ")[0]) for score in all_scores_text]

print(all_scores)

for i in range(len(article_titles)):
    print(f"{i} {article_titles[i]} {article_links[i]} {all_scores[i]} ")
