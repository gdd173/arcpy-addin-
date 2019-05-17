#!/usr/bin/python
# -*- coding: utf-8 -*-

import arcpy
import json

def GetPoint():
    with open(r'E:\first_addin_picture\farm.txt', 'r') as f:
        farm_point = json.loads(f.read())
    return farm_point

def Farmpoint_polygon(farm_point):
    polygonGeometryList = []
    for farm_point_list in farm_point:

        array = arcpy.Array()
        for dict in farm_point_list:
            point = arcpy.Point()
            point.X = dict['X']
            point.Y = dict['Y']
            array.append(point)
        polygon = arcpy.Polygon(array)
        print(array.count)

        polygonGeometryList.append(polygon)
    print(len(polygonGeometryList))
    arcpy.CopyFeatures_management(polygonGeometryList, r'E:\first_addin_picture\polygon\house\farm.shp')
