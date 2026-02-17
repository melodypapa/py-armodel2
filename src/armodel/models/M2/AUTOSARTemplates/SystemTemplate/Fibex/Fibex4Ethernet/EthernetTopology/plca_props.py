"""PlcaProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 169)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class PlcaProps(ARObject):
    """AUTOSAR PlcaProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "plca_local_node": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # plcaLocalNode
        "plca_max_burst": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # plcaMaxBurst
    }

    def __init__(self) -> None:
        """Initialize PlcaProps."""
        super().__init__()
        self.plca_local_node: Optional[PositiveInteger] = None
        self.plca_max_burst: Optional[PositiveInteger] = None


class PlcaPropsBuilder:
    """Builder for PlcaProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PlcaProps = PlcaProps()

    def build(self) -> PlcaProps:
        """Build and return PlcaProps object.

        Returns:
            PlcaProps instance
        """
        # TODO: Add validation
        return self._obj
