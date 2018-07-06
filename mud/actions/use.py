# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2, Action3
from mud.events import UseInEvent

class UseInAction(Action3):
    EVENT = UseInEvent
    RESOLVE_OBJECT = "resolve_for_use"
    RESOLVE_OBJECT2 = "resolve_for_operate"
    ACTION = "use-in"
