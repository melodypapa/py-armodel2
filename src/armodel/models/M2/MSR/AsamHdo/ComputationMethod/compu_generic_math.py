"""CompuGenericMath AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 374)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PrimitiveIdentifier,
)


class CompuGenericMath(ARObject):
    """AUTOSAR CompuGenericMath."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    level: Optional[PrimitiveIdentifier]
    def __init__(self) -> None:
        """Initialize CompuGenericMath."""
        super().__init__()
        self.level: Optional[PrimitiveIdentifier] = None

    def serialize(self) -> ET.Element:
        """Serialize CompuGenericMath to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize level
        if self.level is not None:
            serialized = ARObject._serialize_item(self.level, "PrimitiveIdentifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LEVEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuGenericMath":
        """Deserialize XML element to CompuGenericMath object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuGenericMath object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse level
        child = ARObject._find_child_element(element, "LEVEL")
        if child is not None:
            level_value = child.text
            obj.level = level_value

        return obj



class CompuGenericMathBuilder:
    """Builder for CompuGenericMath."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuGenericMath = CompuGenericMath()

    def build(self) -> CompuGenericMath:
        """Build and return CompuGenericMath object.

        Returns:
            CompuGenericMath instance
        """
        # TODO: Add validation
        return self._obj
