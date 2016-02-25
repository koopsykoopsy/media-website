import media
import top6

prototype_movie = ['title',
                   'synopsis',
                   'poster_image_url',
                   'trailer_youtube_url',
                   'genre',
                   'release_year',
                   'rotten_tomatoes_score',
                   'director',
                   'leads']

prototype_game = ['title',
                  'synopsis',
                  'poster_image_url',
                  'trailer_youtube_url',
                  'genre',
                  'release_year',
                  'ign_score',
                  'studio',
                  'protagonist']

# MOVIES - long strings pulled out for PEP8 Compliance

hot_fuzz_synopsis = """
As a former London constable, Nicholas Angel (Simon Pegg) finds it
difficult to adapt to his new assignment in the sleepy British village
of Sandford. Not only does he miss the excitement of the big city, but
he also has a well-meaning oaf (Nick Frost) for a partner. However, when
a series of grisly accidents rocks Sandford, Nick smells something rotten
in the idyllic village."""

hot_fuzz_poster = """https://westcovmedia.files.wordpress.com/2013/09/
hot-fuzz1.jpg"""

hot_fuzz_yt = 'https://www.youtube.com/watch?v=ayTnvVpj9t4'

hot_fuzz = media.Movie('Hot Fuzz',
                       hot_fuzz_synopsis,
                       hot_fuzz_poster,
                       hot_fuzz_yt,
                       'Comedy, Action, Mystery',
                       2007,
                       91,
                       'Edgar Wright',
                       'Simon Pegg, Nick Frost')

wall_e_synopsis = """
WALL-E, short for Waste Allocation Load Lifter Earth-class, is
the last robot left on Earth. He spends his days tidying up the planet,
one piece of garbage at a time. But during 700 years, WALL-E has
developed a personality, and he's more than a little lonely. Then he
spots EVE (Elissa Knight), a sleek and shapely probe sent back to Earth
on a scanning mission. Smitten WALL-E embarks on his greatest adventure
yet when he follows EVE across the galaxy."""

wall_e_poster = """http://www.pixartalk.com/wp-content/uploads/2009/06/
wallefinal.jpg"""

wall_e_yt = 'https://www.youtube.com/watch?v=ZisWjdjs-gM'

wall_e = media.Movie('WALL-E',
                     wall_e_synopsis,
                     wall_e_poster,
                     wall_e_yt,
                     'Animation, Sci-Fi, Adventure, Silent',
                     2008,
                     96,
                     'Andrew Stanton',
                     'Ben Burtt, Elissa Knight')

the_shining_synopsis = """
Jack Torrance (Jack Nicholson) becomes winter caretaker at the isolated
Overlook Hotel in Colorado, hoping to cure his writer's block. He settles
in along with his wife, Wendy (Shelley Duvall), and his son, Danny (Danny
Lloyd), who is plagued by psychic premonitions. As Jack's writing goes
nowhere and Danny's visions become more disturbing, Jack discovers the
hotel's dark secrets and begins to unravel into a homicidal maniac hell-
bent on terrorizing his family."""

the_shining_poster = """http://thefilmstage.com/wp-content/uploads/2014/
08/saul-bass-the-shining-film-poster-1.jpg"""

the_shining_yt = 'https://www.youtube.com/watch?v=5Cb3ik6zP2I'

the_shining = media.Movie('The Shining',
                          the_shining_synopsis,
                          the_shining_poster,
                          the_shining_yt,
                          'Horror, Thriller, Suspense, Classic',
                          1980,
                          89,
                          'Stanley Kubrick',
                          'Jack Nicholson, Shelley Duvall')

twelve_angry_men_synopsis = """
Following the closing arguments in a murder trial, the 12 members of the
jury must deliberate, with a guilty verdict meaning death for the accused,
an inner-city teen. As the dozen men try to reach a unanimous decision
while sequestered in a room, one juror (Henry Fonda) casts considerable
doubt on elements of the case. Personal issues soon rise to the surface,
and conflict threatens to derail the delicate process that will decide one
boy's fate."""

twelve_angry_men_poster = """http://www.classichollywoodcentral.com/
wp-content/uploads/2015/11/12-Angry-Men-poster.jpg"""

twelve_angry_men_yt = 'https://www.youtube.com/watch?v=A7CBKT0PWFA'

twelve_angry_men = media.Movie('12 Angry Men',
                               twelve_angry_men_synopsis,
                               twelve_angry_men_poster,
                               twelve_angry_men_yt,
                               'Drama, Mystery, Classic',
                               1957,
                               100,
                               'Sidney Lumet',
                               'Henry Fonda')

psycho_synopsis = """
"Phoenix secretary Marion Crane (Janet Leigh), on the lam after stealing
$40,000 from her employer in order to run away with her boyfriend, Sam
Loomis (John Gavin), is overcome by exhaustion during a heavy rainstorm.
Traveling on the back roads to avoid the police, she stops for the night
at the ramshackle Bates Motel and meets the polite but highly strung
proprietor Norman Bates (Anthony Perkins), a young man with an interest
in taxidermy and a difficult relationship with his mother."""

psycho_poster = """http://www.michaelbransonsmith.net/blog/wp-content/
uploads/2012/08/pyscho-animated-movie-poster.gif"""

psycho_yt = 'https://www.youtube.com/watch?v=NG3-GlvKPcg'

psycho = media.Movie('Psycho',
                     psycho_synopsis,
                     psycho_poster,
                     psycho_yt,
                     'Horror, Thriller, Suspense, Classic',
                     1960,
                     96,
                     'Alfred Hitchcock',
                     'Anthony Perkins, Janet Leigh')

the_princess_bride_synopsis = """
A fairy tale adventure about a beautiful young woman and her one true love.
He must find her after a long separation and save her. They must battle the
evils of the mythical kingdom of Florin to be reunited with each other. Based
on the William Goldman novel "The Princess Bride" which earned its own loyal
audience."""

the_princess_bride_poster = """http://4.bp.blogspot.com/-T-6ghqniotI/
UESuh8MPc4I/AAAAAAAAM4g/UHcs1M_u5Vw/s1600/The+Princess+Bride+(1987)+5
.jpg"""

the_princess_bride_yt = 'https://www.youtube.com/watch?v=VYgcrny2hRs'

the_princess_bride = media.Movie('The Princess Bride',
                                 the_princess_bride_synopsis,
                                 the_princess_bride_poster,
                                 the_princess_bride_yt,
                                 'Fantasy, Adventure, Comedy, Family, Classic',
                                 1987,
                                 97,
                                 'Rob Reiner',
                                 'Robin Wright, Cary Elwes')

# GAMES - long strings pulled out for PEP8 Compliance

mass_effect_2_synopsis = """
Once again stepping into the role of the heroic Commander Shepard, gamers
command their crew on a suicide mission in space. Players must assemble their
squad from amongst the galaxy's most powerful mystics, geniuses, and convicts
and lead them on a suicide mission to discover why humans are vanishing from
the galaxy. The success of the mission hinges on the squad recruited and their
loyalty to the mission. Shepard's future depends on it."""

mass_effect_2_poster = """http://ia.media-imdb.com/images/M/
MV5BMjE4MTQwMjM1N15BMl5BanBnXkFtZTcwNjMzNjc2Mw@@._V1_SX640_SY720_.jpg"""

mass_effect_2_yt = 'https://www.youtube.com/watch?v=PHCA8tK117c'

mass_effect_2 = media.Game('Mass Effect 2',
                           mass_effect_2_synopsis,
                           mass_effect_2_poster,
                           mass_effect_2_yt,
                           'Sci-Fi, RPG, Adventure',
                           2010,
                           96,
                           'Bioware',
                           'Commander Shepard')

grim_fandango_synopsis = """
Based on various legends of Mexican folklore, Grim Fandango is packed to the
hilt with dancing skeletons, crime, romance, and much more. You play Manny
Calavera, a mid-level worker at the Department of Death (the DOD) who's trying
to work off his sins in life so that he can get to his final reward. As a
reaper, Manny frees incoming souls from their shrouds, finds out what kind of
underworld travel packages their goodness in life has earned them, and then
sends them on their way. Unfortunately, business hasn't been very good for
Manny of late. As the game begins, Calavera is told that he must sell a
premium travel package to a soul or lose his job. In his search, Manny
uncovers a hideous plot, a beautiful woman, and a crew of loyal friends (not
necessarily in that order)."""

grim_fandango_poster = 'http://i.imgur.com/fpUbQ.jpg'

grim_fandango_yt = 'https://www.youtube.com/watch?v=hV1NBHL9Fa4'

grim_fandango = media.Game('Grim Fandango',
                           grim_fandango_synopsis,
                           grim_fandango_poster,
                           grim_fandango_yt,
                           'Adventure, Mystery',
                           1998,
                           94,
                           'LucasArts',
                           'Manny Calavera')

eighty_days_synopsis = """
Playing as Phileas Fogg's loyal valet, Passepartout, you must balance your
master's health, your finances, and the time, as you choose your own path
from city to city all the way around the world. Bribe your way onto early
departures, but don't let yourself go bankrupt or you'll be sleeping rough
and begging for aid! Trade items for profit, and collect the equipment for
the conditions you'll face: but too much luggage will slow you down... Every
city and journey is narrated via an interactive story where you control every
action. Will your choices speed you up - or lead you into disaster? Will you
earn Fogg's trust and respect? Will you uncover the secrets and short-cuts
that can shave days off your time? Murder, romance, rebellion and intrigue
await!"""

eighty_days_poster = 'https://pbs.twimg.com/media/B6NFOKYIYAA1H9-.png'

eighty_days_yt = 'https://www.youtube.com/watch?v=NzR3GED4P7g'

eighty_days = media.Game('80 Days',
                         eighty_days_synopsis,
                         eighty_days_poster,
                         eighty_days_yt,
                         'Adventure',
                         2014,
                         90,
                         'Inkle',
                         'Passepartout')

majoras_mask_synopsis = """
Majora's Mask features vintage Legend of Zelda gameplay with a three-day
twist, including all the swordplay, boomerang throwing and clever puzzles
introduced into the 3D realm by Ocarina of Time. Time passes as you explore
the overworld -- but each minute truly counts in Termina. If you don't save
someone on the first day, it may be too late on the next. There are no time-
outs in Majora's Mask. After 72 (game time) hours, the world ends because an
evil, grinning moon crashes into the planet. There is of course Link's compact
time machine: the Ocarina. But Link can only jump backwards to the first day
of his adventure, which means pretty much everything he accomplished since
then is effectively erased. How do you stop the world from ending when there
is no way to explore everything in three days and if all you do becomes
meaningless anyway the moment you travel back in time?"""

majoras_mask_poster = """http://img01.deviantart.net/563f/i/2015/113/9/1/
majora_s_mask__fan_poster__by_image_six-d5oub5b.jpg"""

majoras_mask_yt = 'https://www.youtube.com/watch?v=Hj6cXziHpjQ'

majoras_mask = media.Game("The Legend of Zelda: Majora's Mask",
                          majoras_mask_synopsis,
                          majoras_mask_poster,
                          majoras_mask_yt,
                          'Action-Adventure',
                          2000,
                          99,
                          'Nintendo',
                          'Link')

red_dead_redemption_synopsis = """
Red Dead Redemption is a Western epic, set at the turn of the 20th century
when the lawless and chaotic badlands began to give way to the expanding reach
of government and the spread of the Industrial Age. A follow up to the 2004
hit Red Dead Revolver, this game tells the story of former outlaw John
Marston, taking players on a great adventure across the American frontier."""

red_dead_redemption_poster = """http://orig10.deviantart.net/7c29/f/2014/
045/4/b/red_dead_redemption_stylised_poster_by_rosshoolie-d76ge7w.jpg"""

red_dead_redemption_yt = 'https://www.youtube.com/watch?v=PD24MkbHQrc'

red_dead_redemption = media.Game('Red Dead Redemption',
                                 red_dead_redemption_synopsis,
                                 red_dead_redemption_poster,
                                 red_dead_redemption_yt,
                                 'Action',
                                 2010,
                                 97,
                                 'Rockstar Games',
                                 'John Marston')

portal_synopsis = """
A unique take on puzzle gameplay by the makers of Half-Life. Portal is a new
type of single player game that changes how players approach, manipulate, and
surmise the possibilities in a given environment in a manner similar to how
the Gravity Gun changed our approach to how an object may be leveraged in any
given situation."""

portal_poster = """http://samplereality.com/gmu/portal/archive/files/
896b074ebe325e7f4c099c4f828b743d.jpg"""

portal_yt = 'https://www.youtube.com/watch?v=ujYcnO0sIks'

portal = media.Game('Portal',
                    portal_synopsis,
                    portal_poster,
                    portal_yt,
                    'Puzzle',
                    2007,
                    82,
                    'Valve, Nuclear Monkey Software',
                    'Chell')

# Collecting the media items and ordering them as media tiles will be displayed

movies = [the_princess_bride, hot_fuzz, the_shining,
          twelve_angry_men, psycho, wall_e]

games = [grim_fandango, eighty_days, majoras_mask,
         portal, mass_effect_2, red_dead_redemption]

# top6.main() takes the Media objects, ordered as above, creates HTML files,
# slots in the Media objects appropriately, and opens the files in the browser
top6.main(movies, games)
