import time, ssl

from urllib.request import urlopen, URLError, HTTPError

from .web import generateWebRequest

def get_next_image_url_from_html( htmlString ):

  s = htmlString

  # class existing on all image containers in the search results
  img_identifier = s.find('rg_di')

  if img_identifier >= 0:
    # extract url for full image
    meta_data_start = s.find('"class="rg_meta"')
    img_url_start = s.find('"ou"', meta_data_start + 1)
    remaining_html = s.find(',"ow"', img_url_start + 1)
    img_url = str(s[img_url_start + 6:remaining_html - 1])

    return img_url, remaining_html

  return "no_links", 0

def get_all_imgage_urls_from_html( htmlString, limit=-1 ):

  # hard limit; only ~100 images are displayed per image search
  limit = 100 if int(limit) < 0 else int(limit)

  img_urls = []

  while len(img_urls) < limit:
    img_url, remaining_html = get_next_image_url_from_html(htmlString)

    if img_url == "no_links":
      break
    else:
      img_urls.append(img_url)
      time.sleep(0.1)
      htmlString = htmlString[remaining_html:]

  return img_urls

def download_images( imgURLs, target_directory = "downloads", delay = 0, start_index = 0 ):

  errorCount = 0

  for i in range(len(imgURLs)):
    imgURL = imgURLs[i]

    try:
        image_name = str(imgURL[(imgURL.rfind('/')) + 1:]).lower()

        if ".jpg" in image_name:
          file_extension = ".jpg"

        elif ".png" in image_name:
          file_extension = ".png"

        elif ".jpeg" in image_name:
          file_extension = ".jpeg"

        elif ".svg" in image_name:
          file_extension = ".svg"

        else:
          file_extension = ".jpg"

        # current image number
        i_with_leading_zeros = ("{:0"+str(len(str(len(imgURLs))))+"}").format(start_index + i + 1)

        file_name = "image-" + i_with_leading_zeros

        output_file = open(target_directory + "/" + file_name + file_extension, 'wb')

        req = generateWebRequest(imgURL)
        img = urlopen(req, None, 15).read()

        output_file.write(img)
        output_file.close()

        print("completed ====> " + str(start_index + i + 1) + ". " + image_name)

    except HTTPError as e:
        errorCount += 1
        print("HTTPError on image " + str(start_index + i + 1))
        print(str(e))

    except URLError as e:
        errorCount += 1
        print("URLError on image " + str(start_index + i + 1))
        print(str(e))

    except IOError:
        errorCount += 1
        print("IOError on image " + str(start_index + i + 1))

    except ssl.CertificateError as e:
        errorCount += 1
        print("CertificateError on image " + str(start_index + i + 1))
        print(str(e))

    if int(delay) > 0:
        time.sleep(int(delay))

  return errorCount


def get_next_match_from_html (htmlString):
  N_COLUMNS = 11

  s = htmlString

  # class existing on all match row containers in the search results
  row_identifier = s.find('data1')

  if row_identifier >= 0:
    match_data = []

    cursor_pos = row_identifier

    for _ in range(N_COLUMNS):    
      # extract text string from td element
      td_start = s.find('<td', cursor_pos)
      column_data_start = s.find('>', td_start + 1)
      column_data_end = s.find('</td', column_data_start + 1)

      td_string = s[(column_data_start + 1) : column_data_end]
      td_sub_element_end = td_string.find('>')

      if (td_sub_element_end >= 0):
        td_sub_data_end = td_string.find('<', td_sub_element_end)
        td_string = td_string[td_sub_element_end + 1 : td_sub_data_end]

      match_data.append(str(td_string))
      cursor_pos = column_data_end

    remaining_html = s[cursor_pos:]

    return match_data, remaining_html

  return [], ""
  
def get_match_data (htmlString):
  matches = []

  while True:
    match_data, remaining_html = get_next_match_from_html(htmlString)

    if len(match_data) == 0 or len(remaining_html) == 0:
      break
    else:
      matches.append(match_data)
      time.sleep(0.1)
      htmlString = remaining_html

  return matches