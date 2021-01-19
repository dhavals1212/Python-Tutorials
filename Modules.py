import converters
#The import command practically imports the converters module entirely for use in this file.

from converters import lbs_to_kg
#The use of from requires the file name afterward.
#And afterward again, import will import specific function from that module. Here lbs_to_kg.

print(lbs_to_kg(500))
#After already importing, it doesn't need the object attribute.

print(converters.kg_to_lbs(56))
#Here, it will call the function of kg to lbs and convert 56 kg to lbs and print it.

