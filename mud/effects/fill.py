# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .effect import Effect2, Effect3
from mud.events import FillEvent, FillWithEvent

class FillEffect(Effect2):
    EVENT = FillEvent

class FillWithEffect(Effect3):
    EVENT = FillWithEvent
