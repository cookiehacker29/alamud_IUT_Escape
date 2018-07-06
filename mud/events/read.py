# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2

class ReadEvent(Event2):
    NAME = "read"

    def perform(self):
        if not self.object.has_prop("readable"):
            self.fail()
            return self.inform("read.failed")
        self.inform("read")
