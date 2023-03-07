import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import Login as Login

#login
driver = Login.driver

# Open file
with open('pengolahan.csv') as file_obj:
      
    # Create reader object by passing the file
    # object to DictReader method
    reader_obj = csv.DictReader(file_obj)
      
    # Iterate over each row in the csv file
    # using reader object
    for row in reader_obj:
        #continue last no batch with check
        #17-1 935-2
        if int(row['penerima'])==2:
            #url pengolahan
            driver.get("https://sipmen.bps.go.id/regsosek/sipmen-terima-kab-pengolahan/tambah-generate-box-kab")

            #kabupaten
            pilihKab= driver.find_element(By.ID, "kd_kab")
            selectKab = Select(pilihKab)
            selectKab.select_by_value("07")
            time.sleep(1)

            #petugas
            s = driver.find_element(By.ID, "select2-petugas-container")
            s.click()
            petugas = ["Widya Ardianti","Etty Solekhah","Lidia Espita Agata","Anggiat Roy Silalahi"]
            id_petugas=int(row['penerima'])
            s1 = driver.find_element(By.CLASS_NAME, "select2-search__field")
            s1.send_keys(petugas[id_petugas-1])
            time.sleep(1)
            s1.send_keys(Keys.ENTER)

            #nobatch select2-no_box_besar-container
            s2 = driver.find_element(By.ID, "select2-no_box_besar-container")
            s2.click()
            nobatch = row['no_batch']
            s3 = driver.find_element(By.CLASS_NAME, "select2-search__field")
            s3.send_keys(nobatch)
            time.sleep(1)
            s3.send_keys(Keys.ENTER)

            #tambah box
            addWil = driver.find_element(By.NAME, "add_wilayah")
            addWil.click()
            time.sleep(2)

            #simpan
            submit = driver.find_element(By.ID, "simpan1")
            submit.click()
            print(row["no_batch"]+"--"+row["penerima"])