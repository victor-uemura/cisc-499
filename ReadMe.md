# CISC 499: Geolocation of authors in White Supremacist forums

This is an overview of the code provided in this repo

## Structure

The original data is located in the ./relevantData folder.

The ./cliff-api-client folder is from [here](https://github.com/mediacloud/cliff-api-client). You will need to set up a CLIFF server in docker if you want to run the code. You can set that up [here](https://cliff.mediacloud.org/).

The ./GeoLite2-City_20210202 folder is used to map IP addresses. Documentation for this service is [here](https://dev.maxmind.com/geoip/geoip2/geolite2/).

## Added Files

### one.py

This script takes the original messages and removes tags and puts messages into one line saves new CSV in ./cleanData folder

./relevantInfo/core_message_posts.csv --> ./cleanData/clean_core_message_posts.csv

#### The next files are located in the ./cliff-api-client folder
### two.py

Takes untagged messages and splits them by sentence and then looks for location identifiers. put all statements w locations into a new sheet.

Side note: At the beginning of the project edited two.py a few times so the input file for two.py is not consistent with the output file of one.py.

/processedData/messages.xlsx --> targeted_messages.xlsx

### three.py

Takes location messages and only takes those with keywords indicating they are useful to their location.

targeted_messages.xlsx --> final_targeted_messages.xlsx

The manual check was done on this spreadsheet.

### four.py

Takes messages and makes sure location is counted once per author.

final_targeted_messages.xlsx --> author_location.xlsx

### five.py

Create a spreadsheet with country, state, and city counts

author_location.xlsx --> cities.xlsx, states.xlsx, countries.xlsx

### ips.py

Reads members CSV file and then creates a spreadsheet with country and city counts.

## Visuals

Files with a datawrapper prefix and .csv suffix were used for the maps and graphs. You can see these below.

### Countries Capita Map

[here](https://datawrapper.dwcdn.net/qcCGX/2/)

### Countries Count Map

[here](https://datawrapper.dwcdn.net/ARLgd/2/)

### Countries Chart

[here](https://datawrapper.dwcdn.net/Hyyz3/3/)

### Countries IP Map

[here](https://datawrapper.dwcdn.net/fE7QI/3/)

### States Capita Map

[here](https://datawrapper.dwcdn.net/R5e5d/1/)

### States Count Map

[here](https://datawrapper.dwcdn.net/4fraB/4/)

### States Chart

[here](https://datawrapper.dwcdn.net/C5AZX/1/)
