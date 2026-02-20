"""PrimitiveAttributeCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 104)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class PrimitiveAttributeCondition(AttributeCondition):
    """AUTOSAR PrimitiveAttributeCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attribute: Any
    def __init__(self) -> None:
        """Initialize PrimitiveAttributeCondition."""
        super().__init__()
        self.attribute: Any = None

    def serialize(self) -> ET.Element:
        """Serialize PrimitiveAttributeCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PrimitiveAttributeCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attribute
        if self.attribute is not None:
            serialized = ARObject._serialize_item(self.attribute, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATTRIBUTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PrimitiveAttributeCondition":
        """Deserialize XML element to PrimitiveAttributeCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PrimitiveAttributeCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PrimitiveAttributeCondition, cls).deserialize(element)

        # Parse attribute
        child = ARObject._find_child_element(element, "ATTRIBUTE")
        if child is not None:
            attribute_value = child.text
            obj.attribute = attribute_value

        return obj



class PrimitiveAttributeConditionBuilder:
    """Builder for PrimitiveAttributeCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PrimitiveAttributeCondition = PrimitiveAttributeCondition()

    def build(self) -> PrimitiveAttributeCondition:
        """Build and return PrimitiveAttributeCondition object.

        Returns:
            PrimitiveAttributeCondition instance
        """
        # TODO: Add validation
        return self._obj
