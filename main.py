import internal
import scraper
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
  }
  remix_artist = {
    'remix_artist_name': page_info['remix_artist_name'],
    'remix_artist_ocremix_url': page_info['remix_artist_ocremix_url'],
  }
  remix_original_song = {
    'original_song_title': page_info['original_song_title'],
    'original_song_ocremix_url': page_info['original_song_ocremix_url'],
  }
  original_artist = {
    'original_artist_name': page_info['original_artist_name'],
    'original_artist_ocremix_url': page_info['original_artist_ocremix_url'],
  }
  videogame = {
    'videogame_title': page_info['videogame_title'],
    'videogame_ocremix_url': page_info['videogame_ocremix_url'],
    # 'videogame_console': page_info.videogame_console,
  }
  internal.log_info(remix)

consume_ocremix_remix("OCR04280")
