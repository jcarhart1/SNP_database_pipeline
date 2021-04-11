
import urllib3 as urllib
import zipfile2 as zipfile

# download and unzip (wrap in function after testing so that this file can be called with the exe)
url = 'https://api.pharmgkb.org/v1/download/file/data/clinicalAnnotations.zip'
filehandle, _ = urllib.urlretrieve(url)
zip_file_object = zipfile.ZipFile(filehandle, 'r')
first_file = zip_file_object.namelist()[0]
file = zip_file_object.open(first_file)
content = file.read()

# extract to local (db next iteration)
