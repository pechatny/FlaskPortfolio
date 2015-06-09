from flask import Flask

from flask.ext.assets import Environment, Bundle

app = Flask(__name__)
app.config.from_object('config')

assets = Environment(app)

css = Bundle(
    'css/noscript.css',
    'css/reset.css',
    'css/shortcodes.css',
    'css/styles1.css',
    'css/styles2.css',
    'css/styles3.css',
    'css/styles4.css',
    'css/styles5.css',
    'css/styles6.css',
    'css/styles7.css',
    'css/styles8.css',
    'js/pretty/prettyPhoto.css',
    'js/nivo/nivo-slider.css',
    output='gen/packed.css')

js = Bundle(
    'js/jquery-1.7.1.min.js',
    'js/jquery-ui-1.8.18.custom.min.js',
    'js/jquery.effects.core.min.js',
    'js/jPreloader/jquery.preloader.min.js',
    'js/nivo/jquery.nivo.slider.pack.js',
    'js/styleswitch.js',
    'js/theme-changer.js',
    'js/tweet/jquery.tweet.min.js',
    'js/scrollTo/jquery.scrollTo-min.js',
    'js/pretty/jquery.prettyPhoto.min.js',
    'js/maps/jquery.jmapping.min.js',
    'js/maps/vendor/jquery.metadata.min.js',
    'js/maps/vendor/markermanager.min.js',
    'js/maps/vendor/StyledMarker.min.js',
    'js/contact-form/contactform.js',
    'js/column-height.js',
    'js/custom.js',
    output='gen/packed.js')


assets.register('css_all', css)
assets.register('js_all', js)

if __name__ == "__main__":
    app.run()

import routes