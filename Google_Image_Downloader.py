from google_images_search import GoogleImagesSearch

# you can provide API key and CX using arguments,
# or you can set environment variables: GCS_DEVELOPER_KEY, GCS_CX
API_KEY= ' '
CX = ' '

gis = GoogleImagesSearch(API_KEY,CX)

#Define download destination:
Download_destination='D:\Pictures'

# Define search params:
_search_params = {
    'q': 'cute puppy', # Search Query
    'num': 150, # Amount of pics to download
    'safe': 'high', # Safe search level
    'fileType': 'jpg', # File type
}


# this will search, download and resize:
gis.search(search_params=_search_params, path_to_dir=Download_destination)
