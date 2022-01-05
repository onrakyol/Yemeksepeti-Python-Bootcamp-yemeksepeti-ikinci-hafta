import csv, json
import os.path
import pandas as pd
from csv import writer
from tabulate import tabulate

class FileTool:
    def __init__(self, path, fields = []):
        self.path = path
        self.fields = fields

    def showfile(self): # This function shows file contents on console.
        with open(self.path, "r", encoding="UTF-8") as f:            
            print(tabulate(f))
        return self.path       
    
    def create_file(self): # This function create a new file.
        check = os.path.exists(self.path)
        if check:
            print("İşlem yapmak istediğiniz dosya sistemde mevcut.")
        else:
            print("İşlem yapmak istediğiniz dosya oluşturuldu.")
            with open(path, 'w', encoding='utf-8') as file:
                writer = csv.writer(file)
                fields = [i for i in input("Veri girişi yapınız: ").split()]
                writer.writerow(fields)                

    def csv_to_json(self): # This function convert '.csv' file to '.json' file.
        df = pd.read_csv(self.path,sep = ";")        
        df = df.reset_index().to_json(path.replace(".csv", ".json"), orient='records')        
        print("İstediğiniz dosya JSON formatına dönüştürüldü.")

    def search(self): # This function search data in file.
        search_ = input("Aramak istediğiniz sözcüğü giriniz: ")
        with open(self.path, 'r') as f:
            for line in f.readlines():
                if search_ in line:
                    print(line)

    def add(self): # This function add new data in file.
        txt = [i for i in input("Lütfen eklemek istediğiniz veriyi yazınız: ").split("\n")]
        with open(self.path, 'a', newline='') as f:  
            writer_object = writer(f)
            writer_object.writerow(txt)  
            f.close()

    def delete(self): # This function delete data in file.
        deleted_ = input("Silmek istediğiniz veriyi giriniz: ")
        with open(self.path, 'r+') as f:
            lines = f.readlines()
            for line in lines:
                if line.strip("\n") != deleted_:
                    f.write(line)
    
    def update(self): # This function change data in file.
        f1 = open(self.path,'r')
        f1 = ''.join([i for i in f1]).replace("{}".format(input("Değiştirmek istediğiniz veriyi giriniz :")), "{}".format(input("Yeni veriyi giriniz: ")))
        f2 = open(self.path,'w')
        f2.writelines(f1)
        f2.close()            

    def merge_file(self): # This function merge two files.
      mevcut_dizin = os.getcwd()
      file_list = os.listdir(mevcut_dizin)
      print("Aşağıda birleştirebileceğiniz dosyaların listesi mevcuttur.")
      for i in file_list:
        if i.endswith(".csv"):
          print(i)
      file1 = file2 = ""
      with open(self.path) as f:
        file1 = f.read()
      
      with open("{}".format(input("Birleştirilmesini istediğiniz dosya adını giriniz: "))) as f:
        file2 = f.read()

        file1 += "\n"
        file1 += file2

      with open("{}.csv".format(input("Yeni dosya adını giriniz: ")), "w") as f:
        f.write(file1)

    def Menu(self): # This function is menu.
        print("Lütfen aşağıdaki menüden bir seçim yapınız.")        
        while True:
            choice = input("""
1- Ara,
2- Ekle,
3- Sil,
4- Güncelle,
5- Yeni "csv" dosyası oluştur,
6- "csv" dosyasını "json" dosyasına dönüştür,
7- Dosyayı göster,
8- Dosya birleştir,
9- Çıkış yap
Gerçekleştirmek istediğiniz işlemin başındaki numarayı yazınız: """)
            if choice == '1':
                self.search()
            elif choice == '2':
                self.add()
            elif choice == '3':
                self.delete()
            elif choice == '4':
                self.update()
            elif choice == '5':
                self.create_file()
            elif choice == '6':
                self.csv_to_json()
            elif choice == '7':
                self.showfile()
            elif choice == '8':
                self.merge_file()
            elif choice == '9':
                break                
            else:
                print("Geçersiz veri girişi!!!")

path = input("İşlem yapmak istediğiniz dosyanın adını giriniz: ")
FileTool(path).Menu()