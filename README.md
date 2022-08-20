## [ActivityWatch meets jupyter-notebooks](https://github.com/dentropy/aw-experiments)


The purpose of this repo is to showcase the various ways I queried my [ActivityWatch](https://github.com/ActivityWatch/activitywatch).

My goal is to generate a graph of the websites I go to the most similar to the ['Top Browser Domains' feature](https://github.com/ActivityWatch/aw-webui/commit/8f443bc1e258c54f1838994e0f1f79e254d86d6a) but like [another person I can not get it working.](https://github.com/ActivityWatch/aw-webui/issues/357). I look forward to whenever 0.12.0 get's released. To view the production jupyter notebook click [here](https://nbviewer.org/github/dentropy/aw-experiments/blob/main/Production.ipynb)

## Queries:

* Domain Name Queries
  * Extract all domain names and sort by most visited and then put on a bar graph
  * Find number of unique domain names
  * Find total number of websites visited
  * Find most visited URLs
    * Option to specify by site
* Time Based Queries
  * Average number of events on weekdays verses weekend
  * Total Duration per
    * Total
    * Bucket
    * Website Domain Name
    * App
  * Number of events per hour visualized as a heatmap by month

## Explanation of files

The production notebook has the results of everything in the practice folder. To view it click [here](https://nbviewer.org/github/dentropy/aw-experiments/blob/main/Production.ipynb) and here is a link to the actual [notebook](https://github.com/dentropy/aw-experiments/blob/main/Production.ipynb)

*Story of what is in the practice folder*

First I coppiced the sqlite database from [the data directory](https://docs.activitywatch.net/en/latest/directories.html#data-directory) and played with it within [QueryCrafting.ipynb](https://github.com/dentropy/aw-experiments/blob/main/practice/QueryCrafting.ipynb) and [GraphingUp.ipynb](https://github.com/dentropy/aw-experiments/blob/main/practice/GraphingUp.ipynb). Inside [QueryCrafting.ipynb](https://github.com/dentropy/aw-experiments/blob/main/practice/QueryCrafting.ipynb) I wrote and troubleshooted a query get all the domain names and group them distinctly. I then used the query from [QueryCrafting.ipynb](./QueryCrafting.ipynb) inside [GraphingUp.ipynb](https://github.com/dentropy/aw-experiments/blob/main/practice/QueryCrafting.ipynb) to generate a graph using [plotly](https://plotly.com/python/bar-charts/).

While troubleshooting ['Top Browser Domains' feature](https://github.com/ActivityWatch/aw-webui/commit/8f443bc1e258c54f1838994e0f1f79e254d86d6a) I realized [ActivityWatch](https://github.com/ActivityWatch/activitywatch) has an [API](https://docs.activitywatch.net/en/stable/api.html) I can just strait up query rather than pulling from the sqlite file. So that's what I did in [UsingAW-API.ipynb](https://github.com/dentropy/aw-experiments/blob/main/practice/UsingAW-API.ipynb) Turns out you can load the events strait into a pandas dataframe and play with it from there which I thought was pretty awesome.

## Requirements

* Python
* pip packages used
  * pandas
  * jupyterlab
  * plotly
  * ipython-sql
* Activity watch sqlite database

## Setup

``` bash
git clone https://github.com/dentropy/aw-experiments.git
cd aw-experiments
python3 -m venv env
source env/bin/activate
pip install -r ./requirements.txt
jupyter lab .
```

## Next Steps

* Find most visited URLs
  * Narrow by specific website
* Learn [Querying Data](https://docs.activitywatch.net/en/latest/examples/querying-data.html)
