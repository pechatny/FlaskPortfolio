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
    'css/nivo-slider.css',
    output='gen/packed.css')

js1 = Bundle(
    'js/jquery-1.7.1.min.js',
    'js/jquery-ui-1.8.18.custom.min.js',
    'js/jquery.effects.core.min.js',
    'js/jPreloader/jquery.preloader.min.js',
    output='gen/packed1.js')

js2 = Bundle(
    'js/contact-form/contactform.js',
    'js/pretty/jquery.prettyPhoto.min.js',
    'js/scrollTo/jquery.scrollTo-min.js',
    'js/column-height.js',
    'js/styleswitch.js',
    'js/theme-changer.js',
    'js/custom.js',
    output='gen/packed2.js')


assets.register('js_all', js1)
assets.register('js_all2', js2)

assets.register('css_all', css)


if __name__ == "__main__":
    app.run()

import routes