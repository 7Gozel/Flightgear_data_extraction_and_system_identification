# Flightgear_data_extraction_and_system_identification

Storing Flightgear data to .csv file then estimating lateral stability and control derivatives of Cessna172

In the protocol.xml file add path where you want your .csv file to be located between:

   filename>
   
   /filename
   
(It is recommended to use /AppData/Roaming/flightgear.org/Export/example.csv)

Add protocol.xml to the same folder with fgfs.exe then run the Flightgear. From Settings-->Additional settings type: --config=protocol.xml

This will log flight data to given .csv file, default set to 1000 (1 second) can be lowered for lower dt 

System identification was done using simple least squares, data interpolation was applied to output from Flightgear to enrich the data.
