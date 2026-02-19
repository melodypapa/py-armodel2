"""SwitchStreamFilterActionDestPortModification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 140)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)


class SwitchStreamFilterActionDestPortModification(Identifiable):
    """AUTOSAR SwitchStreamFilterActionDestPortModification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    egress_ports: list[CouplingPort]
    modification: Optional[Any]
    def __init__(self) -> None:
        """Initialize SwitchStreamFilterActionDestPortModification."""
        super().__init__()
        self.egress_ports: list[CouplingPort] = []
        self.modification: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwitchStreamFilterActionDestPortModification":
        """Deserialize XML element to SwitchStreamFilterActionDestPortModification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwitchStreamFilterActionDestPortModification object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwitchStreamFilterActionDestPortModification, cls).deserialize(element)

        # Parse egress_ports (list from container "EGRESS-PORTS")
        obj.egress_ports = []
        container = ARObject._find_child_element(element, "EGRESS-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.egress_ports.append(child_value)

        # Parse modification
        child = ARObject._find_child_element(element, "MODIFICATION")
        if child is not None:
            modification_value = child.text
            obj.modification = modification_value

        return obj



class SwitchStreamFilterActionDestPortModificationBuilder:
    """Builder for SwitchStreamFilterActionDestPortModification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwitchStreamFilterActionDestPortModification = SwitchStreamFilterActionDestPortModification()

    def build(self) -> SwitchStreamFilterActionDestPortModification:
        """Build and return SwitchStreamFilterActionDestPortModification object.

        Returns:
            SwitchStreamFilterActionDestPortModification instance
        """
        # TODO: Add validation
        return self._obj
