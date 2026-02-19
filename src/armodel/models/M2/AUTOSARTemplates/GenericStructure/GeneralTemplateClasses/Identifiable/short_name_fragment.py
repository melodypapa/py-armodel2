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
    def serialize(self) -> ET.Element:
        """Serialize ShortNameFragment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize fragment
        if self.fragment is not None:
            serialized = ARObject._serialize_item(self.fragment, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAGMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize role
        if self.role is not None:
            serialized = ARObject._serialize_item(self.role, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

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
            fragment_value = ARObject._deserialize_by_tag(child, "Identifier")
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
