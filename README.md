# Surfs_up-Analysis

## Overview of the analysis

For this project we have put together a business plan to open a Surf n 'Shake shop. Our goal is to present our idea to investor W. Avy and give him insight into the weather patterns of a specific location on Oahu where we would like to build our shop.

W. Avy knows the importance of analyzing a weather dataset to determine the amount of precipitation levels in a year and identify trends in the data to make the best investment decision. To perform the analysis we use a database saved in SQL that we access through SQLAlchemy and Pandas.

## Surfs_up Results

1) Summary temperature statistics of June

<img src="https://github.com/Jponce25/Surfs_up/blob/48474f35b8d06f34eb21db6d8629ade122919ca0/Images/TempJune.png" width="180">

2) Summary temperature statistics of December 

<img src="https://github.com/Jponce25/Surfs_up/blob/48474f35b8d06f34eb21db6d8629ade122919ca0/Images/TempDecember.png" width="200">

The three main points observed from the analysis:

- The temperature throughout the year is warm and constant. Considering the two sample months June and December the mean temperature for June is 74.9 F and for December it is 71.04 F.

- As expected, the December minimum temperature is lower than the June minimum temperature. Being 56 F in winter (December) and 64 F in summer (June).

- The variation of the data measured through the standard deviation is +/-3.2 for June and +/-3.7 for December.  This allows us to conclude that there is not much variation with respect to the mean and the weather does not vary much throughout the year.

## Surfs_up Summary

From the analysis carried out it can be determined that the temperatures remain constant and warm on Oahu, the temperatures are warm in summer (June) and winter (December), this first analysis allows us to conclude that Oahu is a place viable to start a surf shop.

In order to add two additional queries that allow us to gather more weather data for June and December.

We run a querry to obtain the precipitation for June and December, additionally we plot the temperatures and precipitation of a year to determine the trends and help us make an informed decision.

Summary precipitation statistics

<img src="https://github.com/Jponce25/Surfs_up/blob/48474f35b8d06f34eb21db6d8629ade122919ca0/Images/Precipitation.png" width="690">

Frecuency Plots

<img src="https://github.com/Jponce25/Surfs_up/blob/48474f35b8d06f34eb21db6d8629ade122919ca0/Images/Frequency.png" width="690">

Annual Plots

<img src="https://github.com/Jponce25/Surfs_up/blob/48474f35b8d06f34eb21db6d8629ade122919ca0/Images/AnualPlot.png" width="690">
