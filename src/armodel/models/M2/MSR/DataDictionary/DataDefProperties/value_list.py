"""ValueList AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 350)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 314)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 459)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 222)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)


class ValueList(ARObject):
    """AUTOSAR ValueList."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    v: Optional[Numerical]
    def __init__(self) -> None:
        """Initialize ValueList."""
        super().__init__()
        self.v: Optional[Numerical] = None
    def serialize(self) -> ET.Element:
        """Serialize ValueList to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize v
        if self.v is not None:
            serialized = ARObject._serialize_item(self.v, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("V")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueList":
        """Deserialize XML element to ValueList object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ValueList object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse v
        child = ARObject._find_child_element(element, "V")
        if child is not None:
            v_value = child.text
            obj.v = v_value

        return obj



class ValueListBuilder:
    """Builder for ValueList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueList = ValueList()

    def build(self) -> ValueList:
        """Build and return ValueList object.

        Returns:
            ValueList instance
        """
        # TODO: Add validation
        return self._obj
