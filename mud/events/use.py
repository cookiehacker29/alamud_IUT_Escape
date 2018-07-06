# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2, Event3


class UseInEvent(Event3):
    NAME = "use-in"

    def perform(self):
        if not self.object2.is_container():
            self.add_prop("object2-not-container")
            return self.use_in_failure()
        if self.object not in self.actor:
            self.add_prop("object-not-in-inventory")
            return self.use_in_failure()
        if not self.get_datum("use-in.data-driven"):
            self.object.move_to(self.object2)
        self.inform("use-in")

    def use_in_failure(self):
        self.fail()
        self.inform("use-in.failed")
