"""DataReceiveErrorEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 543)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)


class DataReceiveErrorEvent(RTEEvent):
    """AUTOSAR DataReceiveErrorEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "data": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=VariableDataPrototype,
        ),  # data
    }

    def __init__(self) -> None:
        """Initialize DataReceiveErrorEvent."""
        super().__init__()
        self.data: Optional[VariableDataPrototype] = None


class DataReceiveErrorEventBuilder:
    """Builder for DataReceiveErrorEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataReceiveErrorEvent = DataReceiveErrorEvent()

    def build(self) -> DataReceiveErrorEvent:
        """Build and return DataReceiveErrorEvent object.

        Returns:
            DataReceiveErrorEvent instance
        """
        # TODO: Add validation
        return self._obj
