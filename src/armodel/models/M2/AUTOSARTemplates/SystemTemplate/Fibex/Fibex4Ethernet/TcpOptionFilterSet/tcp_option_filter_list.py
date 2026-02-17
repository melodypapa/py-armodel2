"""TcpOptionFilterList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_TcpOptionFilterSet.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


class TcpOptionFilterList(Identifiable):
    """AUTOSAR TcpOptionFilterList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "allowed_tcp_options": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
        ),  # allowedTcpOptions
    }

    def __init__(self) -> None:
        """Initialize TcpOptionFilterList."""
        super().__init__()
        self.allowed_tcp_options: list[PositiveInteger] = []


class TcpOptionFilterListBuilder:
    """Builder for TcpOptionFilterList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TcpOptionFilterList = TcpOptionFilterList()

    def build(self) -> TcpOptionFilterList:
        """Build and return TcpOptionFilterList object.

        Returns:
            TcpOptionFilterList instance
        """
        # TODO: Add validation
        return self._obj
