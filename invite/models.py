# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from django.db import models
from django.template.defaultfilters import slugify
from . import images


JOLTEON = "Jolteon"
FLAREON = "Flareon"
VAPOREON = "Vaporeon"

pokemon_choices = (
    (JOLTEON, JOLTEON),
    (FLAREON, FLAREON),
    (VAPOREON, VAPOREON),
)


OPPRETTET = "Opprettet"
INVITERT = "Invitert"
KOMMER = "Kommer"
KOMMER_IKKE = "Kommer ikke"

status_choices = (
    (OPPRETTET, OPPRETTET),
    (INVITERT, INVITERT),
    (KOMMER, KOMMER),
    (KOMMER_IKKE, KOMMER_IKKE),
)


def pick_random_pokemon():
    return random.sample(pokemon_choices, 1)


class Invite(models.Model):
    name = models.CharField(max_length=255, help_text='Navnet til den som er invitert')
    pokemon = models.CharField(max_length=32, choices=pokemon_choices, default=pick_random_pokemon, help_text='Velg en av de tre pokemonene')  # noqa
    status = models.CharField(max_length=32, choices=status_choices, default=OPPRETTET, help_text='Status på invitasjonen')  # noqa

    def __str__(self):
        return 'Invitasjon til {} ({})'.format(self.name, self.pokemon)

    def slug(self):
        return slugify(self.name)

    @property
    def image(self):
        if self.pokemon == JOLTEON:
            return images.JOLTEON
        elif self.pokemon == FLAREON:
            return images.FLAREON
        elif self.pokemon == VAPOREON:
            return images.VAPOREON
