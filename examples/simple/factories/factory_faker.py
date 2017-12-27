# coding=utf-8

from __future__ import unicode_literals

from django.core.files.base import File

from factory import Faker as OriginalFaker

from faker import Faker as FakerFaker
from faker.generator import random
from faker.providers import BaseProvider
from faker.providers.phone_number import Provider as PhoneNumberProvider
from faker.providers.person.nl_NL import Provider as PersonProvider

from .files import get_temporary_file

__all__ = ('Faker',)


class Faker(OriginalFaker):
    """Override to change the default locale."""

    _DEFAULT_LOCALE = 'nl_NL'


class SpacelessPostalcodeProvider(BaseProvider):
    """Spaceless postal code provider."""

    def postcode_spaceless(self):
        """Spaceless postal code."""
        return self.bothify('%###??').upper()


class NLPhoneNumberProvider(PhoneNumberProvider):
    """Phone number provider `compatible django.contrib.localflavor.nl`."""
    # NLPhoneNumberField validates with max=12
    formats = ('### ### ####',
               '##########',
               '###-#######',
               '+31#########')


class NLPersonProvider(PersonProvider):
    """Person data provider.

    Overridden to make it compatible with our database model.
    """
    last_names = [n for n in PersonProvider.last_names if len(n) <= 30]


class PyStrWithPrefixProvider(BaseProvider):
    """pystr with prefix provider."""

    @classmethod
    def pystr_with_prefix(cls, min_chars=None, max_chars=20, prefix=''):
        """ Generates a random string of upper and lowercase letters.

        :type min_chars: int
        :type max_chars: int
        :return: String. Random of random length between min and max
            characters.
        """
        if min_chars is None:
            return "".join(cls.random_letter() for i in range(max_chars))
        else:
            assert (max_chars >= min_chars), "Maximum length must be " \
                                             "greater than or equal to " \
                                             "minium length"
            pystr = "".join(
                cls.random_letter()
                for i
                in range(0, random.randint(min_chars, max_chars))
            )
            return "%s%s" % (prefix, pystr)


class LoremWithPrefixProvider(BaseProvider):
    """Lorem with prefix provider."""

    @classmethod
    def word_with_prefix(cls):
        """
        Generate a random word
        :example 'lorem'
        """
        return cls.random_element(cls.word_list)

    @classmethod
    def words_with_prefix(cls, nb=3):
        """
        Generate an array of random words
        :example array('Lorem', 'ipsum', 'dolor')
        :param nb how many words to return
        """
        return [cls.word_with_prefix() for _ in range(0, nb)]

    @classmethod
    def sentence_with_prefix(cls, nb_words=6, variable_nb_words=True,
                             prefix=''):
        """Generate a random sentence.

        :example: 'Lorem ipsum dolor sit amet.'.
        :param nb_words around how many words the sentence should contain
        :param variable_nb_words set to false if you want exactly $nbWords
            returned, otherwise $nbWords may vary by +/-40% with a minimum
            of 1.
        """
        if nb_words <= 0:
            return ''

        if variable_nb_words:
            nb_words = cls.randomize_nb_elements(nb_words)

        words = cls.words_with_prefix(nb_words)
        words[0] = words[0].title()

        sentence = " ".join(words) + '.'

        return "%s%s" % (prefix, sentence)


class DjangoFile(BaseProvider):
    """Image file provider."""

    @classmethod
    def django_file(cls, extension=None):
        """ Generates a random image file.

        :return: File object.
        """

        fake = FakerFaker()
        django_file = get_temporary_file(fake.file_name(extension=extension))
        return File(django_file)


Faker.add_provider(SpacelessPostalcodeProvider)
Faker.add_provider(NLPhoneNumberProvider)
Faker.add_provider(NLPersonProvider, locale='nl_NL')
Faker.add_provider(PyStrWithPrefixProvider, locale='la')
Faker.add_provider(LoremWithPrefixProvider, locale='la')
Faker.add_provider(DjangoFile)
