# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2

class PlayEvent(Event2):
    NAME = "play"

    def perform(self):
        if not self.object.has_prop("playable"):
            self.fail()
            return self.inform("play.failed")
        self.inform("play")
