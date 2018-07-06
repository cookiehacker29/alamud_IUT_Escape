# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .event import Event2, Event3

class PayEvent(Event2):
    NAME = "pay"

    def perform(self):
        self.inform("pay")


class PayWithEvent(Event3):
    NAME = "pay-with"

    def perform(self):
        self.inform("pay-with")
