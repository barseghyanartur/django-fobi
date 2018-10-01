import os
import sys

from distutils.version import LooseVersion
from setuptools import setup, find_packages

version = '0.13.7'

# ***************************************************************************
# ************************** Python version *********************************
# ***************************************************************************
PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3
LTE_PY26 = PY2 and (7 > sys.version_info[1])
PYPY = hasattr(sys, 'pypy_translation_info')

# ***************************************************************************
# ************************** Django version *********************************
# ***************************************************************************
DJANGO_INSTALLED = False
try:
    import django
    DJANGO_INSTALLED = True

    LOOSE_DJANGO_VERSION = LooseVersion(django.get_version())
    LOOSE_DJANGO_MINOR_VERSION = LooseVersion(
        '.'.join([str(i) for i in LOOSE_DJANGO_VERSION.version[0:2]])
    )

    # Loose versions
    LOOSE_VERSIONS = (
        '1.4', '1.5', '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '2.0', '2.1',
        '2.2', '3.0'
    )

    for v in LOOSE_VERSIONS:
        var_name = 'LOOSE_VERSION_{0}'.format(v.replace('.', '_'))
        globals()[var_name] = LooseVersion(v)

    # Exact versions
    EXACT_VERSIONS = LOOSE_VERSIONS[:-1]

    for i, v in enumerate(EXACT_VERSIONS):
        l_cur = globals()['LOOSE_VERSION_{0}' \
                          ''.format(LOOSE_VERSIONS[i].replace('.', '_'))]
        l_nxt = globals()['LOOSE_VERSION_{0}' \
                          ''.format(LOOSE_VERSIONS[i + 1].replace('.', '_'))]
        var_name = 'DJANGO_{0}'.format(v.replace('.', '_'))
        globals()[var_name] = (l_cur <= LOOSE_DJANGO_VERSION < l_nxt)

    # LTE list
    LTE_VERSIONS = LOOSE_VERSIONS[:-1]

    for i, v in enumerate(EXACT_VERSIONS):
        l_cur = globals()['LOOSE_VERSION_{0}' \
                          ''.format(LOOSE_VERSIONS[i].replace('.', '_'))]
        var_name = 'DJANGO_LTE_{0}'.format(v.replace('.', '_'))
        globals()[var_name] = (LOOSE_DJANGO_MINOR_VERSION <= l_cur)

    # GTE list
    GTE_VERSIONS = LOOSE_VERSIONS[:-1]

    for i, v in enumerate(EXACT_VERSIONS):
        l_cur = globals()['LOOSE_VERSION_{0}' \
                          ''.format(LOOSE_VERSIONS[i].replace('.', '_'))]
        var_name = 'DJANGO_GTE_{0}'.format(v.replace('.', '_'))
        globals()[var_name] = (
            LOOSE_DJANGO_MINOR_VERSION >= l_cur
        )

except Exception as err:
    pass

# ***************************************************************************
# ***************************************************************************
# ***************************************************************************

try:
    readme = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
    screenshots = open(
        os.path.join(os.path.dirname(__file__), 'docs/screenshots.rst.distrib')
    ).read()
    screenshots = screenshots.replace(
        '.. image:: _static',
        '.. figure:: https://github.com/barseghyanartur/django-fobi/raw/'
        'master/docs/_static'
    )
except:
    readme = ''
    screenshots = ''

template_dirs = [
    # Core templates
    "src/fobi/templates/fobi",

    # Bootstrap 3
    "src/fobi/contrib/themes/bootstrap3/templates/bootstrap3",

    # Foundation 5
    "src/fobi/contrib/themes/foundation5/templates/foundation5",

    # DB Store widget for Foundation 5
    "src/fobi/contrib/themes/foundation5/widgets/form_handlers/"
    "db_store_foundation5_widget",

    # Simple
    "src/fobi/contrib/themes/simple/templates/simple",

    # djangocms_admin_style_theme
    "src/fobi/contrib/themes/djangocms_admin_style_theme/templates/"
    "djangocms_admin_style_theme",

    # DjangoCMS integration
    "src/fobi/contrib/apps/djangocms_integration/templates/"
    "djangocms_integration",

    # FeinCMS integration
    # "src/fobi/contrib/apps/feincms_integration/templates/"
    # "feincms_integration",

    # Mezzanine integration
    "src/fobi/contrib/apps/mezzanine_integration/templates/"
    "mezzanine_integration",

    # Wagtail integration
    "src/fobi/contrib/apps/wagtail_integration/templates/"
    "wagtail_integration",

    # Content image
    "src/fobi/contrib/plugins/form_elements/content/content_image/"
    "templates/content_image",

    # Content image URL
    "src/fobi/contrib/plugins/form_elements/content/content_image_url/"
    "templates/content_image_url",

    # DB Store
    "src/fobi/contrib/plugins/form_handlers/db_store/templates/db_store",

    # Mail
    "src/fobi/contrib/plugins/form_handlers/mail/templates/mail",

    # Http re-post
    "src/fobi/contrib/plugins/form_handlers/http_repost/templates/"
    "http_repost",

    # MailChimp importer
    "src/fobi/contrib/plugins/form_importers/mailchimp_importer/templates/"
    "mailchimp_importer",
]

static_dirs = [
    # Core static
    "src/fobi/static",

    # Bootstrap3
    "src/fobi/contrib/themes/bootstrap3/static",

    # Bootstrap3 datetime widget
    "src/fobi/contrib/themes/bootstrap3/widgets/form_elements/"
    "datetime_bootstrap3_widget/static",

    # Bootstrap3 date widget
    "src/fobi/contrib/themes/bootstrap3/widgets/form_elements/"
    "date_bootstrap3_widget/static",

    # Bootstrap3 slider widget
    "src/fobi/contrib/themes/bootstrap3/widgets/form_elements/"
    "slider_bootstrap3_widget/static",

    # Foundation5
    "src/fobi/contrib/themes/foundation5/static",

    # Foundation5 datetime widget
    "src/fobi/contrib/themes/foundation5/widgets/form_elements/"
    "datetime_foundation5_widget/static",

    # Foundation5 date widget
    "src/fobi/contrib/themes/foundation5/widgets/form_elements/"
    "date_foundation5_widget/static",

    # Simple
    "src/fobi/contrib/themes/simple/static",

    # djangocms_admin_style_theme
    "src/fobi/contrib/themes/djangocms_admin_style_theme/static",

    # DB Store
    "src/fobi/contrib/plugins/form_handlers/db_store/static",

    # Dummy
    "src/fobi/contrib/plugins/form_elements/test/dummy/static",

    # Markdown widget
    "src/fobi/reusable/markdown_widget/static",
    "src/fobi/contrib/plugins/form_elements/content/content_markdown/static",

    # Invisible reCAPTCHA
    "src/fobi/contrib/plugins/form_elements/security/invisible_recaptcha/static",
]

locale_dirs = [
    "src/fobi/locale/nl",
    "src/fobi/locale/ru",
    "src/fobi/locale/de",
]

templates = []
static_files = []
locale_files = []

for template_dir in template_dirs:
    templates += [os.path.join(template_dir, f)
                  for f
                  in os.listdir(template_dir)]

for static_dir in static_dirs:
    static_files += [os.path.join(static_dir, f)
                     for f
                     in os.listdir(static_dir)]

for locale_dir in locale_dirs:
    locale_files += [os.path.join(locale_dir, f)
                     for f
                     in os.listdir(locale_dir)]

dependency_links = []

install_requires = []
# If certain version of Django is already installed, choose version agnostic
# dependencies.
if DJANGO_INSTALLED:
    if DJANGO_1_5 or DJANGO_1_6 or DJANGO_1_7:
        install_requires = [
            'bleach',
            'django-autoslug-iplweb>=1.9.4',
            'django-nine>=0.1.13',
            'django-nonefield>=0.1',
            'Pillow>=2.0.0',
            'requests>=1.0.0',
            'six>=1.9',
            'Unidecode>=0.04.1',
            'vishap>=0.1.5,<2.0',
        ]

    elif DJANGO_1_8:
        install_requires = [
            'bleach',
            'django-autoslug-iplweb>=1.9.4',
            'django-formtools>=1.0',
            'django-nine>=0.1.13',
            'django-nonefield>=0.1',
            'Pillow>=2.0.0',
            'requests>=1.0.0',
            'six>=1.9',
            'Unidecode>=0.04.1',
            'vishap>=0.1.5,<2.0',
        ]
    elif DJANGO_1_9:
        install_requires = [
            'bleach',
            'django-autoslug-iplweb>=1.9.4',
            'django-formtools>=1.0',
            'django-nine>=0.1.13',
            'django-nonefield>=0.1',
            'Pillow>=2.0.0',
            'requests>=1.0.0',
            'six>=1.9',
            'Unidecode>=0.04.1',
            'vishap>=0.1.5,<2.0',
        ]
    elif DJANGO_1_10:
        install_requires = [
            'bleach',
            'django-autoslug-iplweb>=1.9.4',
            'django-formtools>=1.0',
            'django-nine>=0.1.13',
            'django-nonefield>=0.1',
            'Pillow>=2.0.0',
            'requests>=1.0.0',
            'six>=1.9',
            'Unidecode>=0.04.1',
            'vishap>=0.1.5,<2.0',
        ]
    elif DJANGO_1_11:
        install_requires = [
            'bleach',
            'django-autoslug-iplweb>=1.9.4',
            'django-formtools>=2.0',
            'django-nine>=0.1.13',
            'django-nonefield>=0.1',
            'Pillow>=2.0.0',
            'requests>=1.0.0',
            'six>=1.9',
            'Unidecode>=0.04.1',
            'vishap>=0.1.5,<2.0',
        ]
        # dependency_links.append(
        #     'https://github.com/django/django-formtools/archive/master.tar.gz'
        #     '#egg=django-formtools'
        # )
    elif DJANGO_2_0:
        install_requires = [
            'bleach',
            'django-autoslug-iplweb>=1.9.4',
            'django-formtools>=2.0',
            'django-nine>=0.1.13',
            'django-nonefield>=0.3',
            'Pillow>=2.0.0',
            'requests>=1.0.0',
            'six>=1.9',
            'Unidecode>=0.04.1',
            'vishap>=0.1.5,<2.0',
        ]
        # dependency_links.append(
        #     'https://github.com/django/django-formtools/archive/master.tar.gz'
        #     '#egg=django-formtools'
        # )

# Fall back to the latest dependencies
if not install_requires:
    install_requires = [
        'bleach',
        'django-autoslug-iplweb>=1.9.4',
        'django-formtools>=2.0',
        'django-nine>=0.1.13',
        'django-nonefield>=0.1',
        'Pillow>=2.0.0',
        'requests>=1.0.0',
        'six>=1.9',
        'Unidecode>=0.04.1',
        'vishap>=0.1.5,<2.0',
    ]

# There are also conditional PY3/PY2 requirements. Scroll down to see them.

tests_require = [
    'selenium',
    'Faker',
    # 'factory_boy',
    # 'fake-factory',
    # 'Pillow',
    # 'pytest',
    # 'pytest-django',
    # 'pytest-cov',
    # 'tox',
]

if PY3:
    install_requires.append('simplejson>=3.0.0')  # When using Python 3
    if DJANGO_INSTALLED and not DJANGO_1_11:
        install_requires.append('easy-thumbnails>=2.3')
    else:
        install_requires.append('easy-thumbnails>=2.4.1')
        # dependency_links.append(
        #     'https://github.com/SmileyChris/easy-thumbnails/archive/'
        #     'master.tar.gz'
        #     '#egg=easy-thumbnails'
        # )
else:
    install_requires.append('simplejson>=2.1.0')  # When using Python 2.*
    install_requires.append('ordereddict>=1.1')
    if DJANGO_INSTALLED and not DJANGO_1_11:
        install_requires.append('easy-thumbnails>=1.4')
    else:
        install_requires.append('easy-thumbnails>=2.4.1')
        # dependency_links.append(
        #     'https://github.com/SmileyChris/easy-thumbnails/archive/'
        #     'master.tar.gz'
        #     '#egg=easy-thumbnails'
        # )

# if PYPY:
#     install_requires.remove('Pillow>=2.0.0')

setup(
    name='django-fobi',
    version=version,
    description="Form generator/builder application for Django done right: "
                "customisable, modular, user- and developer- friendly.",
    long_description="{0}{1}".format(readme, screenshots),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Environment :: Web Environment",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "License :: OSI Approved :: GNU Lesser General Public License v2 or "
        "later (LGPLv2+)",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
    ],
    keywords="django, form generator, form builder, visual form designer, "
             "user generated forms",
    author='Artur Barseghyan',
    author_email='artur.barseghyan@gmail.com',
    url='https://github.com/barseghyanartur/django-fobi/',
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    license='GPL 2.0/LGPL 2.1',
    install_requires=install_requires,
    tests_require=tests_require,
    dependency_links=dependency_links,
    package_data={
        'fobi': templates + static_files + locale_files
    },
    include_package_data=True,
)
