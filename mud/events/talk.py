# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2

class TalkEvent(Event2):
    NAME = "talk"

    def perform(self):
        if not self.object.has_prop("talkable"):
            self.fail()
            return self.inform("talk.failed")
        self.inform("talk")
