# lern-solr
lern-solr

## start
````
C:\solr-8.2.0>.\bin\solr start
````````

## stop
````
C:\solr-8.2.0>.\bin\solr stop  -all
````

## memory
````
SOLR_JAVA_MEM="-Xms10g -Xmx10g"
````
## change datadir

## When starting up Solr, I can include this parameter:
````
data.dir=C:/foo/bar/my_new_data_directory/
````

## Then in solrconfig.xml, I can prefix my data directory with the parameter set during startup:
````
<dataDir>${solr.data.dir:}core1</dataDir>
````
