# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run Instructions](README.md#run-instructions)


# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

In this repo, I am creating a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.


# Approach

Given the file input and output locations, I first read in the input file header, and search for specific fields containing status, occupation, and state information. After I get the indices for those fields, I read the file line by line to check if the application status is __`CERTIFIED`__. If it is, that application's work state and SOC would contribute to the total certified application number, and it would be stored in a dictionary to represent the number of times that the state or SOC has appeared.

After processing all the data inside the file, I sort the dictionary items and take its first 10 items. And then I write them into the output files prepended by the required header.


# Run Instructions

Running the script `run.sh` would produce the correct output in the `output/` folder.

