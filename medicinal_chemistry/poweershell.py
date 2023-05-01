import os

path = r"C:\Users\OPERATOR\Desktop\Studia\SKN organ\Dokowanie\photoswitche\QM4"
dir_list = os.listdir(path)
for x in  dir_list:
        if x.endswith('mol2'):
                with open (f"C:\\Users\\OPERATOR\\Desktop\\Studia\\SKN organ\\Dokowanie\\photoswitche\\QM4\\{x}") as plik:
                    tekst = plik.read()
                    print(f'obabel {x}', f' -O {x}'.replace('mol2', 'pdbqt'))
print('Done')
