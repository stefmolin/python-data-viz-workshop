# About the data

| File | Description | Source |
| --- | --- | --- |
| `earthquakes.geojson` | GeoJSON file of earthquakes occurring in 2020. | [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/) |
| `NYC_subway_daily.csv` | Total entries and exits per day per NYC borough in 2017-2021. This was resampled from the original `NYC_subway_traffic_2017-2021.zip` dataset created through some extensive data wrangling by Kaggle user [Edden](https://www.kaggle.com/eddeng). | [Kaggle](https://www.kaggle.com/eddeng/nyc-subway-traffic-data-20172021?select=NYC_subway_traffic_2017-2021.csv) |
| `stackoverflow_questions.json` | Data collected from the Stack Overflow API's [/search](https://api.stackexchange.com/docs/search) endpoint for a few tags. | Stack Exchange Network |
| `stackoverflow_tag_co_occurrences.csv` | Data from `stackoverflow.csv` transformed to determine co-occurrences of tags (see the [`collection/stackoverflow.ipynb`](./collection/stackoverflow.ipynb) notebook. | Stack Exchange Network |
| `stackoverflow.zip` | Data from `stackoverflow_questions.json` transformed to include Boolean columns indicating whether each question (row) was tagged with each of the libraries in question. | Stack Exchange Network |
| `T100_MARKET_ALL_CARRIER.zip` | 2019 flight statistics for flights to/from the United States. | United States Department of Transportation’s [Bureau of Transportation Statistics](https://www.transtats.bts.gov/DL_SelectFields.asp?gnoyr_VQ=FMF&QO_fu146_anzr=Nv4%20Pn44vr45) |
| `weather.csv` | Daily weather observations for a few U.S. cities in 2020. | [NCDC API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) |

*Note: The code to collect and generate these files can be found in the [collection](./collection) directory where applicable.*
