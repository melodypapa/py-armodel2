"""ConcreteClassTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 103)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.data_format_element_scope import (
    DataFormatElementScope,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class ConcreteClassTailoring(DataFormatElementScope):
    """AUTOSAR ConcreteClassTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    validation_root: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize ConcreteClassTailoring."""
        super().__init__()
        self.validation_root: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize ConcreteClassTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConcreteClassTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize validation_root
        if self.validation_root is not None:
            serialized = ARObject._serialize_item(self.validation_root, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALIDATION-ROOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConcreteClassTailoring":
        """Deserialize XML element to ConcreteClassTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConcreteClassTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConcreteClassTailoring, cls).deserialize(element)

        # Parse validation_root
        child = ARObject._find_child_element(element, "VALIDATION-ROOT")
        if child is not None:
            validation_root_value = child.text
            obj.validation_root = validation_root_value

        return obj



class ConcreteClassTailoringBuilder:
    """Builder for ConcreteClassTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ConcreteClassTailoring = ConcreteClassTailoring()

    def build(self) -> ConcreteClassTailoring:
        """Build and return ConcreteClassTailoring object.

        Returns:
            ConcreteClassTailoring instance
        """
        # TODO: Add validation
        return self._obj
