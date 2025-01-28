ROOT_PATH = "/media/anwaldt/ANWALDT_DATA/WORK/TEACHING/Online/"

# DEBUG?
NIKOLA_DEBUG=0


# Data about this site
BLOG_AUTHOR = "Henrik von Coler"  # (translatable)
BLOG_TITLE = "RingBuffer"  # (translatable)

# This is the main URL for your site. It will be used
# in a prominent link. Don't forget the protocol (http/https)!
SITE_URL = "http://ringbuffer.org/"

# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "http://hvc.berlin/"
#DEPLOY_COMMANDS = {'default': [
#    'rsync -rav --delete output/ ralsina@lateral.netmanagers.com.ar:/srv/www/lateral',
#    'rdiff-backup output ~/blog-backup',
#    "links -dump 'http://www.twingly.com/ping2?url=lateral.netmanagers.com.ar'",
#]}


BLOG_EMAIL = "contact@hvc.berlin"
BLOG_DESCRIPTION = "RingBuffer"  # (translatable)

#
# Some things in the middle you don't really need to change...



DEFAULT_LANG = "en"


THEME_CONFIG = {
    DEFAULT_LANG: {
        # Show the latest featured post in a large box, with the previewimage as its background.
        'featured_large': False,
        # Show the first (remaining) two featured posts in small boxes.
        'featured_small': False,
        # Show featured posts on mobile.
        'featured_on_mobile': True,
        # Show image in `featured_large` on mobile.
        # `featured_small` displays them only on desktop.
        'featured_large_image_on_mobile': True,
        # Strip HTML from featured post text.
        'featured_strip_html': False,
        # Contents of the sidebar, If empty, the sidebar is not displayed.
        'sidebar': ''
    }
}


EXTRA_HEAD_DATA = """<link rel="stylesheet" href="/assets/hvc/pkgindex.css">"""

POSTS = (
        ("posts/*.rst", "", "post.tmpl"),
        ("posts/*.md", "", "post.tmpl"),
        ("posts/*.txt", "", "post.tmpl"),
        ("posts/*.html", "", "post.tmpl"),
        ("posts/*.ipynb", "", "post.tmpl"),

        (ROOT_PATH+"dsp/posts/*.rst", "dsp", "post.tmpl"),
        (ROOT_PATH+"Sound_Synthesis_Introduction/posts/*.rst", "sound_synthesis_introduction", "post.tmpl"),
        (ROOT_PATH+"Computer_Music_Basics/posts/*.rst", "computer_music_basics", "post.tmpl"),
        (ROOT_PATH+"Sound_Synthesis_in_Faust/posts/*.rst", "faust", "post.tmpl"),
        (ROOT_PATH+"sound_synthesis_cpp/posts/*.rst", "cpp", "post.tmpl"),
        (ROOT_PATH+"Spatial_Audio/posts/*.rst", "spatial_audio", "post.tmpl"),
        (ROOT_PATH+"Music_Interaction_Systems/posts/*.rst", "music_interaction_systems", "post.tmpl")
 )


PAGES = (
    ("pages/*.rst", "", "page.tmpl"),
    ("pages/*.txt", "", "page.tmpl"),
    ("pages/*.html", "", "page.tmpl"),
    ("pages/*.ipynb", "", "page.tmpl"),
)


# Attempt to set global dir

#GLOBAL_CONTEXT = {
#        "JUPYTER_PATH":  "/home/anwaldt/Desktop/Sound_Synthesis_2020/Website/jupyter/",
#        }


COMMENT_SYSTEM = {}

# And to avoid a conflict because blogs try to generate /index.html
# INDEX_PATH = "blog"

# Or you can disable blog indexes altogether:
DISABLE_INDEXES = True

#THEME="cadair"
THEME="bootblog4"

FRONT_INDEX_HEADER = {
    DEFAULT_LANG: ''
}

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
         ##
         #
          ("/computer-music-basics", "Computer Music Basics"),
          ("/dsp", "DSP"),
          ("/sound-synthesis-introduction", "Sound Synthesis Introduction"),
          ("/spatial-audio", "Spatial Audio"),
          ("/music_interaction_systems", "Music Interaction Systems"),
          ("/building-instruments-in-faust", "Faust"),
          ("/sound-synthesis-cpp", "C++"),
          #
          # ("/contact", "Contact"),
    ),
}

INDEX_PATH = "news"
 

IMAGE_FOLDERS = {
                 'images': 'images',
                 '../Computer_Music_Basics/graphics' : 'images/basics',
                 '../dsp/graphics' : 'images/dsp',
                 '../Sound_Synthesis_Introduction/images' : 'images/Sound_Synthesis/',
                 '../Music_Interaction_Systems/images' : 'images/mis',
                 '../Sound_Synthesis_in_Faust/graphics' : 'images/faust',
                 '../sound_synthesis_cpp/graphics' : 'images/cpp',
                 '../Spatial_Audio/images' : 'images/spatial'
                 }

IMAGE_THUMBNAIL_SIZE = 400

SHOW_SOURCELINK = False

FILES_FOLDERS = {
                'files': 'files',
                ROOT_PATH+'Computer_Music_Basics/webaudio': 'files/webaudio',
                ROOT_PATH+'Sound_Synthesis_in_Faust/webaudio': 'files/webaudio/faust',
                ROOT_PATH+'Sound_Synthesis_in_Faust/faust*.dsp': 'files/faust',
                #
                # HTML from jupyter (did copy but was not )
                # ROOT_PATH+'dsp/jupyter': 'jupyter_html/dsp',
                # ROOT_PATH+'Computer_Music_Basics/jupyter': 'jupyter_html/cmb',
                # ROOT_PATH+'Sound_Synthesis_Introduction/jupyter': 'jupyter_html/ssi',
                #
                # BIB stuff:
                ROOT_PATH+'/Spatial_Audio/bibtex': 'bibtex/',
                #
                # audio
                ROOT_PATH+'Sound_Synthesis_Introduction/Audio/': 'audio/sound-synthesis/spectral',
                ROOT_PATH+'dsp/audio': 'files/dsp/audio',
                # video
                ROOT_PATH+'Computer_Music_Basics/videos/': 'files/videos/cmb',
                }

LISTINGS_FOLDERS = {
#        '../Computer_Music_Basics/webaudio':          'listings/webaudio',
#        '../Sound_Synthesis_in_Faust/faust/Physical': 'listings/faust/Physical',
        }


MARKDOWN_EXTENSIONS = ['fenced_code', 'codehilite', 'extra']

## mathjax needs to be configured for handling the $ $ notation from the nbconvert to html
#MATHJAX_CONFIG = True
MATHJAX_CONFIG = """
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
        displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
        processEscapes: true
    },
    displayAlign: 'center', // Change this to 'left' if you want left-aligned equations.
    "HTML-CSS": {
        styles: {'.MathJax_Display': {"margin": 0}}
    }
});
</script>
"""

KATEX_AUTO_RENDER = """
delimiters: [
    {left: "$$", right: "$$", display: true},
    {left: "\\\[", right: "\\\]", display: true},
    {left: "$", right: "$", display: false},
    {left: "\\\(", right: "\\\)", display: false}
]
"""



CONTENT_FOOTER = '''
<center>
<hr>
<br>
</center>
<br>
'''

#CONTENT_FOOTER = '''
#<center>
#<hr>
#<br>
#Contents &copy; Henrik von Coler 2023 - <a href="/contact"> Contact</a>
#</center>
#<br>
#'''


# LATEX STUFF

# Determines how the formulae are rendered. Possibilities:
#  - "latex_formula_image_renderer": renders formulae as graphics and includes them.
#  - "latex_formula_mathjax": inserts MathJax code.
LATEX_FORMULA_RENDERER = "latex_formula_image_renderer"

# When "latex_formula_image_renderer" is selected as the formula renderer,
# the formulae colors and scale can be set here:
#
# The color must be given as an RGB triple with components in range [0, 1].
# Here, (0, 0, 0) is black and (1, 1, 1) is white.
LATEX_FORMULA_COLOR = (0.1, 0.1, 0.1)
#
# The formula scale determines the effective size of the formulae.
# Check what looks good with your theme's main font.
LATEX_FORMULA_SCALE = 1.25
#
# The engine determines the TeX engine used. Must be one of "latex", "luatex" and "xetex".
# Note that "luatex" does not support pstricks formulae.
LATEX_FORMULA_ENGINE = "latex"
