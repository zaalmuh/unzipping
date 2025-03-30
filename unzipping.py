import os
from glob import glob
import zipfile
import patoolib
import shutil
import sys

if len(sys.argv) > 2:
    print('Pastikan gunakan tanda petik atas untuk membuka dan menutup folder, contoh: unzipping \"C:/Abc\"')
    print(sys.argv[1])
    sys.exit()
folder_path = sys.argv[1]
print(folder_path)

for name in os.listdir(folder_path):
    if 'zip' in name:
        continue
    for path in sorted(glob(f'{folder_path}/{name}/*')):
        if 'rar' in path:
            patoolib.extract_archive(path, outdir=f"{folder_path}/{name}/")
        if 'zip' in path:
            with zipfile.ZipFile(path,"r") as zip_ref:
                zip_ref.extractall(f'{folder_path}/{name}/')
#         else:
#             removed_path = os.path.split(path)
#             removed_path = '/'.join(removed_path)
#             os.chmod(removed_path, 0o777)
#             if os.path.isdir(removed_path):
#                 shutil.rmtree(removed_path)
#                 continue
#             os.remove(removed_path)
print('Semua compressed file telah diekstrak!')