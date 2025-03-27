import os
import shutil

first_string = 'gefeliciteerd_met_je_25ste_verjaardag!'

folder_path = os.path.join(*[x for x in first_string])

# os.makedirs(folder_path)


shutil.copy(r'C:\Users\caspe\Downloads\cadeautje.jpg', folder_path)

second_string = 'wat_zal_er_toch_inzittennnnn'

folder_path = os.path.join(*[x for x in second_string])

os.makedirs(folder_path)

shutil.copy(r'C:\Users\caspe\Documents\verrassing.txt', folder_path)
