"""CouplingPortTrafficClassAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.referrable import (
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class CouplingPortTrafficClassAssignment(Referrable):
    """AUTOSAR CouplingPortTrafficClassAssignment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # priority
        "traffic_class": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # trafficClass
    }

    def __init__(self) -> None:
        """Initialize CouplingPortTrafficClassAssignment."""
        super().__init__()
        self.priority: PositiveInteger = None
        self.traffic_class: Optional[PositiveInteger] = None


class CouplingPortTrafficClassAssignmentBuilder:
    """Builder for CouplingPortTrafficClassAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CouplingPortTrafficClassAssignment = CouplingPortTrafficClassAssignment()

    def build(self) -> CouplingPortTrafficClassAssignment:
        """Build and return CouplingPortTrafficClassAssignment object.

        Returns:
            CouplingPortTrafficClassAssignment instance
        """
        # TODO: Add validation
        return self._obj
