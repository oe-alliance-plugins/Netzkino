from setuptools import setup
import setup_translate

pkg = 'Extensions.Netzkino'
setup(name='enigma2-plugin-extensions-netzkino',
       version='3.0',
       description='Zugriff auf Netzkino',
       package_dir={pkg: 'Netzkino'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'logo.png', 'maintainer.info', 'keymap.xml', 'skin_FHD.xml', 'skin_HD.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
