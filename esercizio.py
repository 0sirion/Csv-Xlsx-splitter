import pandas as pd

def main() :
    
    territorioT= "";

    print('inserici 1 per splittare il file, 2 per ricostituirlo')
    num = input()
    if num == "1" :

        df = pd.read_csv('./csvsource/energia.csv', delimiter=",")

        for i in df.index :
            # print(df["Territorio"][i])
            # print(df[1][i])
            # if df["Territorio"][i] == "Liguria" :
                # break


            if territorioT != df["Territorio"][i]:
                territorioT = df["Territorio"][i]
                df_subset = df.loc[df['Territorio'] == territorioT]
                
                nome_file_csv = "./energiaCsvEstratti/energia_"+ df["Territorio"][i].replace("/","-")+".csv"
                df_subset.to_csv(nome_file_csv, index = 0)

                nome_file_xlsx = "./energiaXlsxEstratti/energia_"+ df["Territorio"][i].replace("/","-")+".xlsx"
                df_subset.to_excel(nome_file_xlsx, index = 0)

    elif num == "2" :
         df = pd.read_csv('./csvsource/energia.csv', delimiter=",")
         territori = df["Territorio"].unique()
         
         df_Ricostruito = pd.DataFrame()

         for name in territori :
             df_temp = pd.read_csv("./energiaCsvEstratti/energia_"+ name.replace("/","-") + ".csv")
             df_Ricostruito = pd.concat([df_Ricostruito , df_temp], axis = 0)
         print(df_Ricostruito)
        
             
    else :
        print('comando non riconosciuto')

        

            

if __name__ == "__main__" :
    main() 