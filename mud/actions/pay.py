# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .action import Action2, Action3
from mud.events import PayEvent, PayWithEvent


class PayAction(Action2):
    EVENT = PayEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "pay"


class PayWithAction(Action3):
    EVENT = PayWithEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    RESOLVE_OBJECT2 = "resolve_for_use"
    ACTION = "pay-with"
