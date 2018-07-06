# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .effect import Effect2, Effect3
from mud.events import PayEvent, PayWithEvent

class PayEffect(Effect2):
    EVENT = PayEvent

class PayWithEffect(Effect3):
    EVENT = PayWithEvent
