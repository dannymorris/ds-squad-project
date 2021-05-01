#Importing libraries
import pandas as pd
import geopandas as gpd
import numpy as np
import os
from os.path import dirname
from geopy.geocoders import Nominatim
import src.zstage.main.config as config
import csv


def filldata():
    # Reading the crime data into a pandas dataframe :
    config.setConfig("Crime")
    crime_df = pd.read_csv(config.inputFile)
    # converting the incident_datetime column into datetime format:
    #crime_df['incident_datetime'] = pd.to_datetime(crime_df['incident_datetime'])
    # Sorting the data by time :
    #crime_df.sort_values('incident_datetime', inplace=True)
    geolocator = Nominatim(user_agent="https://nominatim.openstreetmap.org/search?")
    df = crime_df[crime_df['latitude'].isna()].copy()
    lon_list = []
    lat_list = []
    for (i, j) in enumerate(df['address_1']):
        j = str(j)
        if "Block" in str(j):
            string = j.replace('Block', "") + " Buffalo New York"
        elif "&" in str(j):
            string = j[j.find("&") + 2:] + " Buffalo New York"
        else:
            string = j + " Buffalo New York"
        try:
            location = geolocator.geocode(string)
            lat_list.append(location.latitude)
            lon_list.append(location.longitude)
        except:
            lat_list.append(None)
            lon_list.append(None)

    df['latitude'] = lat_list
    df['longitude'] = lon_list
    crime_df = pd.concat([crime_df[crime_df['latitude'].notna()], df], axis=0)
    # Reading the geojson data provided by https://data.buffalony.gov "https://data.buffalony.gov/Economic-Neighborhood-Development/Neighborhoods/q9bk-zu3p" :
    nbh_polygon = gpd.read_file(f"{dirname(dirname(dirname(os.getcwd())))}\\Neighborhoods_coordinates.geojson")
    pd_polygon = gpd.read_file(f"{dirname(dirname(dirname(os.getcwd())))}\\BPD Districts.geojson")
    cd_polygon = gpd.read_file(f"{dirname(dirname(dirname(os.getcwd())))}\\Council Districts.geojson")
    # Converting the pandas dataframe into a geopandas dataframe(has higher support for geospatial data) :
    gdf = gpd.GeoDataFrame(crime_df, geometry=gpd.points_from_xy(crime_df.longitude, crime_df.latitude))

    # For loop going through all the neighborhoods, checking if each coordinate is in that neighborhood and assigning a boolean:
    for i in range(len(nbh_polygon)):
        # mask looks at the polygon geometry of each neighborhood and maps it :
        mask = (nbh_polygon.loc[i, 'geometry'])
        # This line checks if the coordinates in crime_df are inside the mask  and outputs a boolean list:
        pip_mask_geofence = gdf.within(mask)
        gdf['geofence'] = pip_mask_geofence
        # Replace all values of the new column 'neighborhood'(not neighborhood_1) with the respective neighborhood name from polygon:
        gdf.loc[gdf['geofence'] == True, 'neighborhood_1'] = nbh_polygon['nbhdname'][i]

    gdf.sort_values('incident_datetime', inplace=True)
    gdf.drop('geofence', axis=1, inplace=True)
    # gdf.drop('geometry',axis=1,inplace=True)

    # For loop going through all the neighborhoods, checking if each coordinate is in that neighborhood and assigning a boolean:
    for i in range(len(cd_polygon)):
        # mask looks at the polygon geometry of each neighborhood and maps it :
        mask = (cd_polygon.loc[i, 'geometry'])
        # This line checks if the coordinates in crime_df are inside the mask  and outputs a boolean list:
        pip_mask_geofence = gdf.within(mask)
        gdf['geofence'] = pip_mask_geofence
        # Replace all values of the new column 'neighborhood'(not neighborhood_1) with the respective neighborhood name from polygon:
        gdf.loc[gdf['geofence'] == True, 'council_district_1'] = cd_polygon['councildistrict'][i]

    gdf.sort_values('incident_datetime', inplace=True)
    gdf.drop('geofence', axis=1, inplace=True)
    # gdf.drop('geometry',axis=1,inplace=True)

    # For loop going through all the neighborhoods, checking if each coordinate is in that neighborhood and assigning a boolean:
    for i in range(len(pd_polygon)):
        # mask looks at the polygon geometry of each neighborhood and maps it :
        mask = (pd_polygon.loc[i, 'geometry'])
        # This line checks if the coordinates in crime_df are inside the mask  and outputs a boolean list:
        pip_mask_geofence = gdf.within(mask)
        gdf['geofence'] = pip_mask_geofence
        # Replace all values of the new column 'neighborhood'(not neighborhood_1) with the respective neighborhood name from polygon:
        gdf.loc[gdf['geofence'] == True, 'police_district_1'] = pd_polygon['name'][i]

    gdf.sort_values('incident_datetime', inplace=True)
    gdf.drop('geofence', axis=1, inplace=True)
    gdf.drop('geometry', axis=1, inplace=True)
    gdf.to_csv(f"{dirname(dirname(dirname(os.getcwd())))}\\Crime_Incidents.csv", quotechar='"', index=False, quoting=csv.QUOTE_ALL)


def main():
    filldata()

if __name__ == '__main__':
    main()