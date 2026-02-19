"""IndexedArrayElement AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 237)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class IndexedArrayElement(ARObject):
    """AUTOSAR IndexedArrayElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application_array: Optional[Any]
    implementation: Optional[Any]
    index: Optional[Integer]
    def __init__(self) -> None:
        """Initialize IndexedArrayElement."""
        super().__init__()
        self.application_array: Optional[Any] = None
        self.implementation: Optional[Any] = None
        self.index: Optional[Integer] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndexedArrayElement":
        """Deserialize XML element to IndexedArrayElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IndexedArrayElement object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse application_array
        child = ARObject._find_child_element(element, "APPLICATION-ARRAY")
        if child is not None:
            application_array_value = child.text
            obj.application_array = application_array_value

        # Parse implementation
        child = ARObject._find_child_element(element, "IMPLEMENTATION")
        if child is not None:
            implementation_value = child.text
            obj.implementation = implementation_value

        # Parse index
        child = ARObject._find_child_element(element, "INDEX")
        if child is not None:
            index_value = child.text
            obj.index = index_value

        return obj



class IndexedArrayElementBuilder:
    """Builder for IndexedArrayElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IndexedArrayElement = IndexedArrayElement()

    def build(self) -> IndexedArrayElement:
        """Build and return IndexedArrayElement object.

        Returns:
            IndexedArrayElement instance
        """
        # TODO: Add validation
        return self._obj
