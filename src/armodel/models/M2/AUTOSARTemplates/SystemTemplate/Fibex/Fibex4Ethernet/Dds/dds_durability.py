"""DdsDurability AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 530)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject


class DdsDurability(ARObject):
    """AUTOSAR DdsDurability."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "durability_kind": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsDurabilityKindEnum,
        ),  # durabilityKind
    }

    def __init__(self) -> None:
        """Initialize DdsDurability."""
        super().__init__()
        self.durability_kind: Optional[DdsDurabilityKindEnum] = None


class DdsDurabilityBuilder:
    """Builder for DdsDurability."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsDurability = DdsDurability()

    def build(self) -> DdsDurability:
        """Build and return DdsDurability object.

        Returns:
            DdsDurability instance
        """
        # TODO: Add validation
        return self._obj
