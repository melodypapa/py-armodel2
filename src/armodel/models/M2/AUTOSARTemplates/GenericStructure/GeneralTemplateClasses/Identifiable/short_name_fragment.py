"""ShortNameFragment AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_Identifiable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    String,
)


class ShortNameFragment(ARObject):
    """AUTOSAR ShortNameFragment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    fragment: Identifier
    role: String
    def __init__(self) -> None:
        """Initialize ShortNameFragment."""
        super().__init__()
        self.fragment: Identifier = None
        self.role: String = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ShortNameFragment":
        """Deserialize XML element to ShortNameFragment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ShortNameFragment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse fragment
        child = ARObject._find_child_element(element, "FRAGMENT")
        if child is not None:
            fragment_value = child.text
            obj.fragment = fragment_value

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = child.text
            obj.role = role_value

        return obj



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
