import zipfile,os.path,csv
def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            # Path traversal defense copied from
            # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                while True:
                    drive, word = os.path.splitdrive(word)
                    head, word = os.path.split(word)
                    if not drive:
                        break
                if word in (os.curdir, os.pardir, ''):
                    continue
                path = os.path.join(path, word)
            #print(ZipInfo.filename)
            #zf.extract(member, path)
            for i in zf.namelist():
                if "monthly" in i:
                    print(i)
                    #zf.open(i)
                    with open(os.path.join(path, i), 'wb') as f:
                        f.write(zf.read(i))
                elif "station" in i:
                    print(i)
                    #zf.open(i)
                    with open(os.path.join('Weather_station/', i), 'wb') as f:
                        f.write(zf.read(i).replace('|',','))
                        #f.write(reader)

loc="Weather_Zipfiles/"
dest_dir="Weather_monthly/"
#dest_dir2="Weather_station/"
for filename in os.listdir(loc):
    if filename.endswith(".zip"):
        unzip(loc+filename, dest_dir)
