#pip install google_images_download

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

#maximum limit is 100 else need chromedriver
arguments = {"keywords":"search keywords","limit":100,"print_urls":True, "chromedriver":'\..'}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
