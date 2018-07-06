# -*- coding: utf-8 -*-
# Copyright (C) 2014 Denys Duchier, IUT d'Orléans
#==============================================================================

from .go        import GoAction, LeaveAction, EnterAction
from .inspect   import InspectAction
from .look      import LookAction
from .open      import OpenAction, OpenWithAction
from .close     import CloseAction
from .type      import TypeAction
from .take      import TakeAction
from .inventory import InventoryAction
from .light     import LightOnAction, LightOffAction
from .drop      import DropAction, DropInAction
from .push      import PushAction
from .teleport  import TeleportAction
from .play	    import PlayAction
from .read      import ReadAction
from .talk      import TalkAction
from .use       import UseInAction
from .pay       import PayAction, PayWithAction
from .fill      import FillAction, FillWithAction
