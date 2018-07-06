# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2
from mud.events import PlayEvent

class PlayAction(Action2):
    EVENT = PlayEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "play"
