"""InstantiationTimingEventProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 85)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Composition.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.instantiation_rte_event_props import (
    InstantiationRTEEventProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class InstantiationTimingEventProps(InstantiationRTEEventProps):
    """AUTOSAR InstantiationTimingEventProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "period": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # period
    }

    def __init__(self) -> None:
        """Initialize InstantiationTimingEventProps."""
        super().__init__()
        self.period: Optional[TimeValue] = None


class InstantiationTimingEventPropsBuilder:
    """Builder for InstantiationTimingEventProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstantiationTimingEventProps = InstantiationTimingEventProps()

    def build(self) -> InstantiationTimingEventProps:
        """Build and return InstantiationTimingEventProps object.

        Returns:
            InstantiationTimingEventProps instance
        """
        # TODO: Add validation
        return self._obj
