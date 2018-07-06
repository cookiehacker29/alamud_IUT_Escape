# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2, Event3

class FillEvent(Event2):
    NAME = "fill"

    def perform(self):
        self.inform("fill")


class FillWithEvent(Event3):
    NAME = "fill-with"

    def perform(self):
        self.inform("fill-with")
