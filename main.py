import internal
import scraper
import csv

def consume_ocremix_remix(ocremixid: str):
  page_url = f"https://ocremix.org/remix/{ocremixid}"
  internal.log_info(f"GET to /parse with {ocremixid}")
  try:
      page_info = scraper.scrape_remix_page(page_url)
  except:
      internal.log_error(f"Failed to get page {page_url}")
      return None

  remix = {
    'remix_youtube_url': page_info['remix_youtube_url'],
    'ocremix_remix_url': page_info['ocremix_remix_url'],
    'remix_title': page_info['remix_title'],
    'ocremix_remix_id': ocremixid,
    'remix_artist_name': page_info['remix_artist_name'],
    'remix_artist_ocremix_url': page_info['remix_artist_ocremix_url'],
    'original_song_title': page_info['original_song_title'],
    'original_song_ocremix_url': page_info['original_song_ocremix_url'],
    'original_artist_name': page_info['original_artist_name'],
    'original_artist_ocremix_url': page_info['original_artist_ocremix_url'],
    'videogame_title': page_info['videogame_title'],
    'videogame_ocremix_url': page_info['videogame_ocremix_url'],
    # 'videogame_console': page_info.videogame_console,
  }
  internal.log_info(remix)
  return remix


def write_remix_to_csv(ocremix):
    with open('test_1.csv', mode='a') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([
            ocremix[ 'remix_youtube_url' ],
            ocremix[ 'ocremix_remix_url'],
            ocremix[ 'remix_title'],
            ocremix[ 'ocremix_remix_id'],
            ocremix[ 'remix_artist_name'],
            ocremix[ 'remix_artist_ocremix_url'],
            ocremix[ 'original_song_title'],
            ocremix[ 'original_song_ocremix_url'],
            ocremix[ 'original_artist_name'],
            ocremix[ 'original_artist_ocremix_url'],
            ocremix[ 'videogame_title'],
            ocremix[ 'videogame_ocremix_url'],
            ])

for i in range(100000):
    print(str(i).zfill(5))
    internal.log_info(f"Crafting id for i={i}")
    ocremix_id = f"OCR{str(i).zfill(5)}"
    internal.log_info(f"Resulting id: {ocremix_id}")
    remix = consume_ocremix_remix(ocremix_id)
    if remix is not None:
        internal.log_info(f"Invoking write_remix_to_csv for {remix['ocremix_remix_url']}")
        write_remix_to_csv(remix)
    else:
        internal.log_info(f"Failed to collect remix {ocremix_id}")

write_remix_to_csv(consume_ocremix_remix("OCR04280"))
