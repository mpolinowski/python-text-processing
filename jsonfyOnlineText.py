import requests
import re
from bs4 import BeautifulSoup

url = 'https://wiki.instar.com/en/Outdoor_Cameras/IN-9408_WQHD/'
title = 'IN-9408 WQHD :: Product Overview'
camera_series = '["1440p Cameras", "Outdoor Cameras"]'
article_type = 'User Manual'
link = '/Outdoor_Cameras/IN-9408_WQHD/'
chapter = 'Outdoor Cameras'
tags = '["IN-9408 WQHD", "INSTAR", "products", "1440p series", "Indoor Cameras", "IP camera", "web cam", "overview"]'
image = '/en/images/Search/P_SearchThumb_IN-9408HD.webp'
imagesquare = '/en/images/Search/TOC_Icons/Wiki_Tiles_P-IN-9408HD_white.webp'
short = 'IN-9408 WQHD - Product Overview'
abstract = 'The IN-9408 WQHD with a SONY STARVIS Images Sensor and a 5 megapixel video resolution.'

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

content = soup.find('div', attrs={'id': 'gatsby-focus-wrapper'}).text
# replace quotation marks
replaced_content = content.replace('"', ' ')
# strip multiple-space character
single_space = re.sub('\s+',' ',replaced_content)


json_template = """{
    "title": "ARTICLE_TITLE",
    "series": ARTICLE_SERIES,
    "type": "ARTICLE_TYPE",
    "description": "ARTICLE_BODY",
    "sublink1": "ARTICLE_URL",
    "chapter": "ARTICLE_CHAPTER",
    "tags": ARTICLE_TAGS,
    "image": "ARTICLE_IMAGE",
    "imagesquare": "ARTICLE_SQUAREIMAGE",
    "short": "ARTICLE_SHORT",
    "abstract": "ARTICLE_ABSTRACT"
}"""


add_body = json_template.replace('ARTICLE_BODY', single_space)
add_title = add_body.replace('ARTICLE_TITLE', title)
add_series = add_title.replace('ARTICLE_SERIES', camera_series)
add_type = add_series.replace('ARTICLE_TYPE', article_type)
add_url = add_type.replace('ARTICLE_URL', link)
add_chapter = add_url.replace('ARTICLE_CHAPTER', chapter)
add_tags = add_chapter.replace('ARTICLE_TAGS', tags)
add_image = add_tags.replace('ARTICLE_IMAGE', image)
add_imagesquare = add_image.replace('ARTICLE_SQUAREIMAGE', imagesquare)
add_short = add_imagesquare.replace('ARTICLE_SHORT', short)
add_abstract = add_short.replace('ARTICLE_ABSTRACT', abstract)


with open('elasticsearch/article.json', 'w') as file:
    file.write(add_abstract)