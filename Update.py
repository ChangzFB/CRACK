import os,sys



PERINTAH = """
cd $HOME
cd CRACK
mv data $HOME
mv results $HOME
cd
rm -rf CRACK
git clone https://github.com/ChangzFB/CRACK
cd $HOME
mv data CRACK
mv results CRACK
cd DARK-FB
"""

print(" |-->Tunggu Sebentar Sedang Update Script....")
os.system(PERINTAH)
print(' |')
print(' |')
print(' |-->Update Script Sudah Selesai...')
print(' |-->Silahkan Jalankan Perintah Ini : python run.py')
os.sys.exit()

