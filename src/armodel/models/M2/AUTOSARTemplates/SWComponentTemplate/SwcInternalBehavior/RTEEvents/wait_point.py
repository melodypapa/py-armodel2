"""WaitPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 550)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)


class WaitPoint(Identifiable):
    """AUTOSAR WaitPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "timeout": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # timeout
        "trigger": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RTEEvent,
        ),  # trigger
    }

    def __init__(self) -> None:
        """Initialize WaitPoint."""
        super().__init__()
        self.timeout: Optional[TimeValue] = None
        self.trigger: Optional[RTEEvent] = None


class WaitPointBuilder:
    """Builder for WaitPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: WaitPoint = WaitPoint()

    def build(self) -> WaitPoint:
        """Build and return WaitPoint object.

        Returns:
            WaitPoint instance
        """
        # TODO: Add validation
        return self._obj
