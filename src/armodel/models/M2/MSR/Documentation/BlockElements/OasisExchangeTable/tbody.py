"""Tbody AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 335)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class Tbody(ARObject):
    """AUTOSAR Tbody."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "valign": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ValignEnum,
        ),  # valign
    }

    def __init__(self) -> None:
        """Initialize Tbody."""
        super().__init__()
        self.valign: Optional[ValignEnum] = None


class TbodyBuilder:
    """Builder for Tbody."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Tbody = Tbody()

    def build(self) -> Tbody:
        """Build and return Tbody object.

        Returns:
            Tbody instance
        """
        # TODO: Add validation
        return self._obj
