# Inshorts_API
# Inshorts News API [Unofficial]
---
This API is capable of fetching news contents from various sources as gathered by Inshorts app.

---
### Show some :heart: and :star: the repo to support the project

## News Categories

This API supports category wise news. Here is a complete list of all categories.

1. all
2. national //Indian News only
3. business
4. sports
5. world
6. politics
7. technology
8. startup
9. entertainment
10. miscellaneous
11. hatke
12. science
13. automobile

---

## Usage

Make a get request specifying the category of news you want
```
https://inshortsnews.herokuapp.com/{category_name}
```
Example - https://inshortsapi.herokuapp.com/science

---


## Response Format

The response JSON Object looks something like this - 

```JSON
{
  "Articles": [
    {
            "author": "Pragya Swastik",
            "content": "Coronavirus vaccine developed by the UK's Oxford University and AstraZeneca is safe and induces immune reaction, as per preliminary results, medical journal The Lancet said. Trials involving around 1,077 people showed the injection led to them making antibodies and white blood cells that can fight coronavirus. Authors say that further clinical studies, including in older adults, should be done.\n\n",
            "date": "20 Jul 2020,Monday 07:35 pm",
            "image_url": "https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2020/07_jul/20_mon/img_1595253241851_893.jpg",
            "inshort_url": "https://inshorts.com/en/news/coronavirus-vaccine-by-oxford-safe-induces-immune-reaction-preliminary-results-1595253905125",
            "read_more_url": "https://twitter.com/TheLancet/status/1285207186591887360?s=20&utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
            "title": "Coronavirus vaccine by Oxford safe, induces immune reaction, show preliminary results"
        },
        {
            "author": "Pragya Swastik",
            "content": "Sarah Catherine Gilbert, who's leading Oxford University's COVID-19 vaccine candidate, said rolling out vaccine by this year is a possibility but there's no certainty about it. \"We need three things to happen,\" she added. It needs to work in late-stage trials, should be manufactured in large quantities and regulators must agree quickly to license it for emergency use, she added.",
            "date": "21 Jul 2020,Tuesday 03:50 pm",
            "image_url": "https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2020/07_jul/21_tue/img_1595325828978_33.jpg",
            "inshort_url": "https://inshorts.com/en/news/possible-but-not-certain-of-oxford-covid19-vaccine-this-year-lead-developer-1595326839287",
            "read_more_url": "https://in.mobile.reuters.com/article/amp/idINKCN24M0OP?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
            "title": "Possible but not certain of Oxford COVID-19 vaccine this year: Lead developer"
        }
    ],
  "category": "technology",
  "success": true
}
```
---

## Setup

Install all dependencies listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python app.py
    ```
---

#### Star the Repo in case you liked it :)

##Credits

inspired from [Sumanjay](https://github.com/cyberboysumanjay/Inshorts-News-API)
