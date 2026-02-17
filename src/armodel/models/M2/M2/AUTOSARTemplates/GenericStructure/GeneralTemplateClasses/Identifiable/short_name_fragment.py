"""ShortNameFragment AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    String,
)


class ShortNameFragment(ARObject):
    """AUTOSAR ShortNameFragment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "fragment": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # fragment
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # role
    }

    def __init__(self) -> None:
        """Initialize ShortNameFragment."""
        super().__init__()
        self.fragment: Identifier = None
        self.role: String = None


class ShortNameFragmentBuilder:
    """Builder for ShortNameFragment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ShortNameFragment = ShortNameFragment()

    def build(self) -> ShortNameFragment:
        """Build and return ShortNameFragment object.

        Returns:
            ShortNameFragment instance
        """
        # TODO: Add validation
        return self._obj
