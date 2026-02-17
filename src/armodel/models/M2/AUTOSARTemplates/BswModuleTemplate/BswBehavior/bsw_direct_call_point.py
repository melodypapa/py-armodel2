"""BswDirectCallPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 78)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)


class BswDirectCallPoint(BswModuleCallPoint):
    """AUTOSAR BswDirectCallPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "called_entry": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleEntry,
        ),  # calledEntry
        "called_from": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ExclusiveAreaNestingOrder,
        ),  # calledFrom
    }

    def __init__(self) -> None:
        """Initialize BswDirectCallPoint."""
        super().__init__()
        self.called_entry: Optional[BswModuleEntry] = None
        self.called_from: Optional[ExclusiveAreaNestingOrder] = None


class BswDirectCallPointBuilder:
    """Builder for BswDirectCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswDirectCallPoint = BswDirectCallPoint()

    def build(self) -> BswDirectCallPoint:
        """Build and return BswDirectCallPoint object.

        Returns:
            BswDirectCallPoint instance
        """
        # TODO: Add validation
        return self._obj
