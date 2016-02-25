import webbrowser
import os
import re

# Styles and scripting for the page

# Note the sized up YT vids, with extra parameters (like
# removing related videos) for a more cinematic feel

main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Sagar's Top 6 Media</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: #464646;
            font-family: serif;
        }
        #trailer .modal-dialog {
            margin-top: 100px;
            width: 960px;
            height: 720px;
        }
        .hanging-close {
            position: absolute;
            top: -13px;
            right: -13px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .media-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            color: #ABAAAA;
        }
        .media-tile:hover {
            background-color: #7F7E7E;
            cursor: pointer;
            color: #464646;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: #464646;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click',
                       '.hanging-close, .modal-backdrop, .modal',
                       function (event) {
            // Remove the src so the player itself gets removed, as this is
            // the only reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.media-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var parametersYouTube = '?autoplay=1&html5=1&controls=1'
                                  + '&disablekb=1&modestbranding=1'
                                  + '&rel=0&showinfo=0'
            var sourceUrl = 'http://www.youtube.com/embed/'
                          + trailerYouTubeId
                          + parametersYouTube;
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the media when the page loads
        $(document).ready(function () {
          $('.media-tile').hide().first().show("medium", function showNext() {
            $(this).next("div").show("medium", showNext);
          });
        });
    </script>
</head>
'''


# Main page layout + extra navbar links
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close"
           data-dismiss="modal" aria-hidden="true">
            <img src="https://goo.gl/jYv1iy"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="{movie_link}">Top 6 Movies</a>
            <a class="navbar-brand" href="{game_link}">Top 6 Games</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {media_tiles}
    </div>
  </body>
</html>
'''


# Template for each movie/game tile
media_tile_content = '''
<div class="col-md-6 col-lg-4 media-tile text-center"
 data-trailer-youtube-id="{trailer_youtube_id}"
 data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{media_title}</h2>
</div>
'''


# This function is subordinate to render_content()
def create_media_tiles_content(media):
    # The HTML content for this section of the page
    content = ''

    # 1st half == grabbing the YT ID for each movie or game
    for item in media:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', item.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', item.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        # 2nd half == Filling in cover art for each movie or game, appending
        # each one to the previous to make a monster-sized 'content' var
        content += media_tile_content.format(
            media_title=item.title,
            poster_image_url=item.poster_image_url,
            trailer_youtube_id=trailer_youtube_id)

    return content  # This sends ALL media tiles back


# This function is subordinate to main()
def render_content(media, holder):
    # Easier to understand and remember if I replicate the 'name'
    # variable here rather than set as global variable at top of file
    name = media[0].__class__.__name__.lower()

    # This fills in the guts of the site with all media tiles, plus the
    # two navbar links, which need to be on each page for, well, navigation
    rendered_content = main_page_content.format(
        media_tiles=create_media_tiles_content(media),
        movie_link=holder['movie']['url'],
        game_link=holder['game']['url'])

    # Recreates the page each time, closing it when complete
    holder[name]['output_file'].write(main_page_head + rendered_content)
    holder[name]['output_file'].close()

    return  # No need to send holder back, as it hasn't been changed


# This function is subordinate to main()
def build_dict(media, holder):
    # Defining critical variables
    name = media[0].__class__.__name__.lower()
    output_file = open(name + '.html', 'w')
    url = 'file://' + os.path.abspath(output_file.name)

    # Placing those vars in a dict of dicts for easy (and,
    # more importantly, simple) access later on.
    holder[name] = {}
    holder[name]['output_file'] = output_file
    holder[name]['url'] = url
    return holder


# The big mama function
def main(movies, games):
    # Set up dict outside build_dict function so it keeps growing
    holder = {}
    build_dict(movies, holder)
    build_dict(games, holder)

    # Need two calls to create two separate pages
    render_content(movies, holder)
    render_content(games, holder)

    # The site is now built. This last line just uses our good friend
    # webbrowser to open it in a new tab, defaulting to the movies page
    webbrowser.open(holder['movie']['url'], new=2)
