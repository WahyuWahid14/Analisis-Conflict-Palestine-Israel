import pandas as pd
import numpy as np
import mysql.connector
import matplotlib.pyplot as plt
# plt.style.use('_mpl-gallery')


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='palestin',
                                         user='root',
                                         password='')

except mysql.connector.Error as e:
    print("error pada connection", e)

print("Connection Berjalan Lancar")

## VISUALISASI ##

# 1
# def diagram_garis(Query_sql):
#     Query_sql = "SELECT YEAR(date_of_death) AS tahun, COUNT(date_of_event) AS jumlah_kematian FROM conflict_palestin_israel GROUP BY YEAR(date_of_death);"
#     cursor = connection.cursor()
#     cursor.execute(Query_sql)
#     records = cursor.fetchall()

#     jumlah = []
#     bulan = []
#     # tahun = []
#     for i in range(len(records)):
#         jumlah.append(int(records[i][0]))
#         bulan.append(records[i][1])
  
#         # tahun.append(records[i][2])
    
#     # fig, ax = plt.subplots()
#     # ax.plot( jumlah)    
#     # ax.plot( bulan)
#     # # ax.legend()
    
#     plt.plot(jumlah, bulan, '-o') 
#     plt.xlabel(" Tahun ") 
#     plt.ylabel(" Jumlah Kematian ") 
#     plt.title(" TREN KEMATIAN PALESTINA VS ISRAEL ") 
#     plt.show()
#     plt.show()
# inputan = int(input("Masukkan angka 1 : "))
# print(f"Menamilkan grafik garis yang menampilkan jumlah resep obat per bulan selama tahun ini.\n {diagram_garis(inputan)}")

# def bar_chart(Query_sql):
#     Query_sql = "SELECT YEAR(date_of_death) AS tahun, COUNT(date_of_event) AS jumlah_kematian FROM conflict_palestin_israel GROUP BY YEAR(date_of_death);"
#     cursor = connection.cursor()
#     cursor.execute(Query_sql)
#     records = cursor.fetchall()

#     tahun = []
#     jumlah = []
#     # tahun = []
#     for i in range(len(records)):
#         tahun.append(str(records[i][0]))
#         jumlah.append(records[i][1])


#     plt.barh(tahun, jumlah, height = 0.8)  
#     plt.xlabel('Jumlah Kematian')
#     plt.ylabel('Tahun')
#     plt.title('Grafik Jumlah Kematian per Tahun')
#     plt.show()
# inputan = int(input("Masukkan angka 1 : "))
# print(f"Menamilkan grafik garis yang menampilkan jumlah resep obat per bulan selama tahun ini.\n {bar_chart(inputan)}")


# 2
# **Diagram Lingkaran**
def pie_chart(kategori, ukuran_jumlah):

        labels = kategori
        sizes = ukuran_jumlah

        fig, ax = plt.subplots()

        ax.pie(sizes, labels=labels, autopct='%1.1f%%')

        plt.legend(loc = 'upper right')

        jadi = plt.show()

        return jadi

Query_sql = "SELECT CASE WHEN age BETWEEN 0 AND 12 THEN 'Anak-anak' WHEN age BETWEEN 13 AND 18 THEN 'Remaja' WHEN age BETWEEN 19 AND 50 THEN 'Dewasa Pertengahan' ELSE 'Lansia' END AS kelompok_usia, COUNT(*) AS jumlah_kematian_individu FROM conflict_palestin_israel GROUP BY kelompok_usia ORDER BY jumlah_kematian_individu DESC;"
cursor = connection.cursor()
cursor.execute(Query_sql)
records = cursor.fetchall()

kelompok_usia = []
jumlah = []
# tahun = []
for i in range(len(records)):
    kelompok_usia.append(str(records[i][0]))
    jumlah.append(records[i][1])

pie_chart(kelompok_usia, jumlah)


