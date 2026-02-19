"""SoAdRoutingGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2057)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ObsoleteModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    EventGroupControlTypeEnum,
)


class SoAdRoutingGroup(FibexElement):
    """AUTOSAR SoAdRoutingGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    event_group_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SoAdRoutingGroup."""
        super().__init__()
        self.event_group_ref: Optional[ARRef] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoAdRoutingGroup":
        """Deserialize XML element to SoAdRoutingGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SoAdRoutingGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SoAdRoutingGroup, cls).deserialize(element)

        # Parse event_group_ref
        child = ARObject._find_child_element(element, "EVENT-GROUP")
        if child is not None:
            event_group_ref_value = EventGroupControlTypeEnum.deserialize(child)
            obj.event_group_ref = event_group_ref_value

        return obj



class SoAdRoutingGroupBuilder:
    """Builder for SoAdRoutingGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoAdRoutingGroup = SoAdRoutingGroup()

    def build(self) -> SoAdRoutingGroup:
        """Build and return SoAdRoutingGroup object.

        Returns:
            SoAdRoutingGroup instance
        """
        # TODO: Add validation
        return self._obj
