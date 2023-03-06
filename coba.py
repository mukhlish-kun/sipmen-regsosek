import csv
  
# Open file
with open('batching.csv') as file_obj:
      
    # Create reader object by passing the file
    # object to DictReader method
    reader_obj = csv.DictReader(file_obj)
      
    # Iterate over each row in the csv file
    # using reader object
    for row in reader_obj:
        if int(row['no_batch'])<61070002:
            print(row['kd_kec'])