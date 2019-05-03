# XlsToIni
This Python based utility helps you to convert your configuration information from '.xls' in '.ini' file. This utility helps you to maintain your configurations information in xls.  


Format of input file 
Group A, B etc refers to sections in ini file
Colomn names refers to 'key' and values are corrosponding row value. 

Format of output file file:

Keys (properties):

        name=value

Sections:

        [Group A]
        desc=description
        similar for other groups.

To generate '.ini' file from input and output files follow below command

$python iniParser.py <input_file_name> <output_file_name>
In our case input_file_name = ConfigParameterList.xls 
output_file_name = MyConfigs.ini

$python iniParser.py ConfigParameterList.xls MyConfig.ini

Make sure <input_file_name> is placed in same directory level if you are not giving absolute file path. 
