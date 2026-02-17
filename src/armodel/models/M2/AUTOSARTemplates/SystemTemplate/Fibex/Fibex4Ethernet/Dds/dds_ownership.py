"""DdsOwnership AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 532)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsOwnershipKindEnum,
)


class DdsOwnership(ARObject):
    """AUTOSAR DdsOwnership."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ownership_kind": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DdsOwnershipKindEnum,
        ),  # ownershipKind
    }

    def __init__(self) -> None:
        """Initialize DdsOwnership."""
        super().__init__()
        self.ownership_kind: Optional[DdsOwnershipKindEnum] = None


class DdsOwnershipBuilder:
    """Builder for DdsOwnership."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DdsOwnership = DdsOwnership()

    def build(self) -> DdsOwnership:
        """Build and return DdsOwnership object.

        Returns:
            DdsOwnership instance
        """
        # TODO: Add validation
        return self._obj
