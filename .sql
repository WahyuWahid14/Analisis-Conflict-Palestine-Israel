USE palestin;

SELECT * FROM conflict_palestin_israel;

# 1
SELECT YEAR(date_of_death) AS tahun, COUNT(date_of_event) AS jumlah_kematian FROM conflict_palestin_israel 
GROUP BY YEAR(date_of_death)
;
 
SELECT MIN(date_of_death), MAX(date_of_death) FROM conflict_palestin_israel;


SELECT age, gender, citizenship FROM conflict_palestin_israel;

# 2
# usia(age)
SELECT
CASE
    WHEN age BETWEEN 0 AND 12 THEN 'Anak-anak'
    WHEN age BETWEEN 13 AND 18 THEN 'Remaja'
    WHEN age BETWEEN 19 AND 50 THEN 'Dewasa Pertengahan'
    ELSE 'Lansia'
  END AS kelompok_usia,
  COUNT(*) AS jumlah_kematian_individu
FROM conflict_palestin_israel
GROUP BY kelompok_usia
ORDER BY jumlah_kematian_individu DESC;
# Jenis Kelamin
SELECT gender, COUNT(gender) AS jumlah_kematian FROM conflict_palestin_israel
GROUP BY gender
ORDER BY jumlah_kematian DESC;
# kewarganegaraan
SELECT citizenship, COUNT(citizenship) AS jumlah_kematian_individu FROM conflict_palestin_israel
GROUP BY citizenship
ORDER BY jumlah_kematian_individu DESC;
 

# 3
SELECT event_location, event_location_district, event_location_region, COUNT(date_of_death) AS jumlah_kematian
FROM conflict_palestin_israel
GROUP BY event_location, event_location_district, event_location_region;

SELECT event_location, COUNT(date_of_death) AS jumlah_kematian
FROM conflict_palestin_israel
GROUP BY event_location
ORDER BY jumlah_kematian DESC;


# 4
SELECT type_of_injury, killed_by, event_location, COUNT(*) AS jumlah_kasus_kematian, notes
FROM conflict_palestin_israel
GROUP BY event_location
ORDER BY jumlah_kasus_kematian DESC;


# 5
SELECT  type_of_injury, COUNT(*) AS jumlah_kasus_kematian
FROM conflict_palestin_israel
GROUP BY type_of_injury
ORDER BY jumlah_kasus_kematian DESC;
SELECT type_of_injury, killed_by, event_location, COUNT(*) AS jumlah_kasus_kematian
FROM conflict_palestin_israel
GROUP BY type_of_injury, killed_by
ORDER BY jumlah_kasus_kematian DESC;


# 6
SELECT ammunition, notes, COUNT(name) AS jumlah_kasus_kematian
FROM conflict_palestin_israel
GROUP BY ammunition;

SELECT ammunition, COUNT(ammunition) AS jumlah_senjata
FROM conflict_palestin_israel
GROUP BY ammunition;

# 7
SELECT name, age, gender, citizenship, place_of_residence
FROM conflict_palestin_israel;


SELECT place_of_residence_district AS daerah_tempat_tinggal,COUNT(place_of_residence_district) as jumlah_kematian
FROM conflict_palestin_israel
GROUP BY place_of_residence_district;


SELECT place_of_residence_district ,COUNT(*) AS jumlah FROM conflict_palestin_israel
GROUP BY place_of_residence_district;