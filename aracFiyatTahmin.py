import pandas as pd
from sklearn.linear_model import LinearRegression

def arac_fiyat_tahmin(yil,km,motorH,sahip,manuelMi,benzinMi):

    df = pd.read_csv("audiA1.csv")

    # Veriyi işlerken işe yaramayacak sütunlar kaldırıldı
    df = df.drop(columns=["index","href","PPY","MileageRank","PriceRank","PPYRank","Score","PS"])

    # Motor hacminin yanındaki L kaldırıldı ve veri tipi değiştirildi
    # Kategorik engine verisi numerik yapıldı 
    df['Engine'] = df['Engine'].str.replace("L","")
    df['Engine'] = pd.to_numeric(df["Engine"])

    
    # drop_first kullanımının sebebi yakıt türünden 2 tane var biri varsa diğeri yoktur 
    #                                       eğer kaldırılmasaydı gereksiz sütun olacaktı
    df = pd.get_dummies(df,columns=['Type','Transmission','Fuel'], drop_first=True)
    
    y = df['Price(£)'] # Target, Bağımlı değişken
    x = df.drop('Price(£)',axis=1) # bağımsız değişken, target olan price silindi 

    
    lr = LinearRegression()

    # veriler verilip öğretildi
    model = lr.fit(x,y) 
    
    # elde edinilen veriler ile tahmin yapıldı
    fiyat_tahmin = int(model.predict([[yil,km,motorH,sahip,manuelMi,benzinMi]])) 
    
    print(f"\n\nAracinizin tahmini fiyati: {fiyat_tahmin} Pound\n")
    print(f"modelin doğruluk derecesi: {model.score(x,y):.2f}")

def sorgu(girdi):
    if girdi == 1:
        return "evet"
    return "hayir"


yil = int(input('Arac yilini giriniz: '))
kiloMet = int(input('Arac kilometresini giriniz: '))
motor = float(input('Arac motor hacmini giriniz: '))
sahipS = int(input('Arac kacinci el oldugunu giriniz: '))
manuel = int(input('Arac manuel mi? (evet 1 /hayir 0) '))
benzin = int(input('Arac benzinli mi? (evet 1 /hayir 0) '))


arac_fiyat_tahmin(yil,kiloMet,motor,sahipS,manuel,benzin)
print(f"Girilen degerler: \n\tArac yili: {yil} \n\tArac kilometresi: {kiloMet}"
      f"\n\tArac motor hacmi: {motor} \n\tArac kacinci sahibinde: {sahipS}" 
      f"\n\tArac manuel mi {sorgu(manuel)}\n\tArac benzinli mi {sorgu(benzin)}")