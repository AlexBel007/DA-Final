## Final homework notes ##



### Data sources ###

LV

<https://data.gov.lv/lv>

LT

<https://osp.stat.gov.lt/viesos-duomenu-rinkmenos/-/asset_publisher/i2LnhXkrXAbl/content/-covid-19-duomenys?inheritRedirect=false&redirect=https%3A%2F%2Fosp.stat.gov.lt%2Fviesos-duomenu-rinkmenos%3Fp_p_id%3D101_INSTANCE_i2LnhXkrXAbl%26p_p_lifecycle%3D0%26p_p_state%3Dnormal%26p_p_mode%3Dview%26p_p_col_id%3Dcolumn-1%26p_p_col_pos%3D1%26p_p_col_count%3D2>



Power BI references sources from **D:\Course\DA-FInal\data\**.

Python references sources relatively from *\data\*.

### Dataset processing

Remove unnecessary data columns.

Rename columns with standardized names.

Add index columns to reference rows.

Changed types of data in columns from mixed to whole/decimal number.

Parse dates (LT and LV have different date format in source file)

 

Datasets have cumulative number of recovered patients, no daily numbers.

Add calculated column to provide daily number of recovered patients

 

Add 7 day rolling average for number of new infections to smooth out noise.

 

Extend dataset to provide future dates. Custom made dataset providing dates between 2020-01-01 and 2022-01-01, is used to join to LT and LV datasets.

Create additional column providing average new infection numbers the same day last year for use in forecasting. 

### LV dataset specifics 

Some null values in the beginning of the dataset needed to be replaced with 0

Dataset has daily recovered numbers column and data until about the end of 2020, but 0 afterwards, therefore daily numbers still had to be calculated based on cumulative numbers. 

### LT dataset specifics 

Dataset contained detailed information for each municipality, and also total numbers for the whole country. Only country level rows are needed, the rest were filtered out. 

### Moving average VS raw incidence rate

Daily infection rate numbers are highly dependent on the day of week. There significantly less tests made during weekends, therefore discovered number of infected is usually much less on weekends. On the opposite side, business days see more tests and more discovered cases, especially on Monday, where we see most of the delayed results that were collecting  during weekends. 

This is why cumulative 14 day number is usually used in the industry. For the purpose of this work, 7 day rolling average was used to calculate the number.

Formula   used: **SUM(NewInfections   during last 7 days)/7**    

The same issue is relevant for daily death and recovery rates. 

### Conclusions

 Virus spread is correlating with the spread of general respiratory viruses in the Northern hemisphere. There is a sharp increase starting in fall (not on the chart) with a decline in cases in spring. Lowest number of cases are in summer months when people usually have good immunity and spend time outdoors.

Latvian more so then LT. 

LT has lifted major restrictions in April, that allow travelling between cities resulting in the raise in cases in April-May.

Additionally, Easter celebrations may have added to the raise in both LT and LV

#### Forecast  

Does not take into account spread reduction due to vaccinations or new government restrictions. Potentially predicts worst case scenario based on last years growth coefficients.

