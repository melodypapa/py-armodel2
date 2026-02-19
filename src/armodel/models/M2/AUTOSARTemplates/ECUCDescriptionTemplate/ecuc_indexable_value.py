"""EcucIndexableValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 110)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from abc import ABC, abstractmethod


class EcucIndexableValue(ARObject, ABC):
    """AUTOSAR EcucIndexableValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    index: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize EcucIndexableValue."""
        super().__init__()
        self.index: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize EcucIndexableValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize index
        if self.index is not None:
            serialized = ARObject._serialize_item(self.index, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucIndexableValue":
        """Deserialize XML element to EcucIndexableValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucIndexableValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse index
        child = ARObject._find_child_element(element, "INDEX")
        if child is not None:
            index_value = child.text
            obj.index = index_value

        return obj



class EcucIndexableValueBuilder:
    """Builder for EcucIndexableValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucIndexableValue = EcucIndexableValue()

    def build(self) -> EcucIndexableValue:
        """Build and return EcucIndexableValue object.

        Returns:
            EcucIndexableValue instance
        """
        # TODO: Add validation
        return self._obj
