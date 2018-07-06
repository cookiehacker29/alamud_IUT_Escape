# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2, Action3
from mud.events import FillEvent, FillWithEvent


class FillAction(Action2):
    EVENT = FillEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "fill"


class FillWithAction(Action3):
    EVENT = FillWithEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    RESOLVE_OBJECT2 = "resolve_for_use"
    ACTION = "fill-with"
