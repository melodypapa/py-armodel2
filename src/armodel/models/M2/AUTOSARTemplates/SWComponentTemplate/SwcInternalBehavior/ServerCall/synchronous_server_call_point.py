"""SynchronousServerCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 580)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2074)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServerCall.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
    ServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)


class SynchronousServerCallPoint(ServerCallPoint):
    """AUTOSAR SynchronousServerCallPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "called_from": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ExclusiveAreaNestingOrder,
        ),  # calledFrom
    }

    def __init__(self) -> None:
        """Initialize SynchronousServerCallPoint."""
        super().__init__()
        self.called_from: Optional[ExclusiveAreaNestingOrder] = None


class SynchronousServerCallPointBuilder:
    """Builder for SynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SynchronousServerCallPoint = SynchronousServerCallPoint()

    def build(self) -> SynchronousServerCallPoint:
        """Build and return SynchronousServerCallPoint object.

        Returns:
            SynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
