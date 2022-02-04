#!/usr/bin/env python
# coding: utf-8

# In[ ]:


freshwater_home = [
    'Largemouth bass'
    , 'Smallmouth bass'
    , 'Spotted bass'
    , 'Striped bass'
    , 'Black crappie'
    , 'White crappie'
    , 'Yellow perch'
    , 'Warmouth'
    , 'Green sunfish'
    , 'Bluegill'
    , 'Redear sunfish'
    , 'Pumpkinseed'
    , 'Blue catfish'
    , 'Channel catfish'
    , 'Flathead catfish'
    , 'Brown bullhead'
    , 'Black bullhead'
    , 'Yellow bullhead'
    , 'Longnose gar'
    , 'Northern snakehead'
    , 'Common carp'
    , 'Crucian carp'
    , 'Grass carp'
    , 'American shad'
    , 'Gizzard shad'
    , 'Hickory shad'
    , 'Blueback shad'
]

freshwater_exotic = [
    'Butterfly peacock bass'
    , 'Mexican mojarra'
]

saltwater_carolina = [
    'Summer flounder'
    , 'Southern flounder'
    , 'Red drum'
    , 'Spotted seatrout'
    , 'Inshore lizardfish'
    , 'Houndfish'
    , 'Pinfish'
    , 'Atlantic croaker'
    , 'Southern kingfish'
    , 'Black sea bass'
    , 'Scup'
    , 'Crevalle jack'
    , 'Gag'
    , 'Clearnose skate'
]

saltwater_exotic = [
    'Mangrove red snapper'
    , 'Mangrove snapper'
    , 'Yellowtail snapper'
    , 'Schoolmaster'
    , 'White grunt'
    , 'Hairy blenny'
]

saltwater_rogue = [
    'Atlantic cod'
]

def get_all():
    return freshwater_home + freshwater_exotic + saltwater_carolina + saltwater_exotic + saltwater_rogue

