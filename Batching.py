import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import Login as Login

#login
driver = Login.driver

# Open file
with open('batching.csv') as file_obj:
      
    # Create reader object by passing the file
    # object to DictReader method
    reader_obj = csv.DictReader(file_obj)
      
    # Iterate over each row in the csv file
    # using reader object
    for row in reader_obj:
        #continue last no batch with check
        if int(row['no_batch'])>61070718:
        
            #url batching
            driver.get("https://sipmen.bps.go.id/regsosek/cetak-box/tambah-generate-box-kab")

            #kabupaten
            pilihKab= driver.find_element(By.ID, "kd_kab")
            selectKab = Select(pilihKab)
            selectKab.select_by_value("07")
            time.sleep(2)
            #kecamatan
            pilihKec= driver.find_element(By.ID, "kd_kec")
            selectKec = Select(pilihKec)
            time.sleep(2)
            selectKec.select_by_value(row["kd_kec"])

            #desa
            pilihDesa= driver.find_element(By.ID, "kd_desa")
            selectDesa = Select(pilihDesa)
            time.sleep(2)
            selectDesa.select_by_value(row["kd_desa"])

            #sls
            pilihSls= driver.find_element(By.ID, "kd_sls")
            selectSls = Select(pilihSls)
            time.sleep(2)
            selectSls.select_by_value(row["kdsls"])

            #tambah ke batching
            addWil = driver.find_element(By.NAME, "add_wilayah")
            time.sleep(2)
            addWil.click()

            #penomoran batching
            noBatch = driver.find_element(By.ID, "no_box_besar")
            noBatch.send_keys(Keys.CONTROL+"A")
            noBatch.send_keys(row["no_batch"])

            #tambah ke batching
            submit = driver.find_element(By.NAME, "simpan")
            submit.click()

            #confirm class = swal2-confirm swal2-styled
            acc = driver.find_element(By.CLASS_NAME, "swal2-confirm")
            acc.click()
            print("kd_kec:"+row["kd_kec"]+" kd_desa:"+row["kd_desa"]+" kdsls:"+row["kdsls"]+" nobatch:"+row["no_batch"])
