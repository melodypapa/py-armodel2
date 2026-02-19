"""ValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 333)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 433)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2076)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from abc import ABC, abstractmethod


class ValueSpecification(ARObject, ABC):
    """AUTOSAR ValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize ValueSpecification."""
        super().__init__()
        self.short_label: Optional[Identifier] = None
    def serialize(self) -> ET.Element:
        """Serialize ValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize short_label
        if self.short_label is not None:
            serialized = ARObject._serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ValueSpecification":
        """Deserialize XML element to ValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ValueSpecification object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        return obj



class ValueSpecificationBuilder:
    """Builder for ValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ValueSpecification = ValueSpecification()

    def build(self) -> ValueSpecification:
        """Build and return ValueSpecification object.

        Returns:
            ValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
