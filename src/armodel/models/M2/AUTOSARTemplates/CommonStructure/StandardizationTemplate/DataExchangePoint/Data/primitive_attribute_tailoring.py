"""PrimitiveAttributeTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data import (
    DefaultValueApplicationStrategyEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.value_restriction_with_severity import (
    ValueRestrictionWithSeverity,
)


class PrimitiveAttributeTailoring(AttributeTailoring):
    """AUTOSAR PrimitiveAttributeTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    default_value: Optional[DefaultValueApplicationStrategyEnum]
    sub_attributes: list[Any]
    value_restriction_with_severity: Optional[ValueRestrictionWithSeverity]
    def __init__(self) -> None:
        """Initialize PrimitiveAttributeTailoring."""
        super().__init__()
        self.default_value: Optional[DefaultValueApplicationStrategyEnum] = None
        self.sub_attributes: list[Any] = []
        self.value_restriction_with_severity: Optional[ValueRestrictionWithSeverity] = None
    def serialize(self) -> ET.Element:
        """Serialize PrimitiveAttributeTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PrimitiveAttributeTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize default_value
        if self.default_value is not None:
            serialized = ARObject._serialize_item(self.default_value, "DefaultValueApplicationStrategyEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFAULT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sub_attributes (list to container "SUB-ATTRIBUTES")
        if self.sub_attributes:
            wrapper = ET.Element("SUB-ATTRIBUTES")
            for item in self.sub_attributes:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize value_restriction_with_severity
        if self.value_restriction_with_severity is not None:
            serialized = ARObject._serialize_item(self.value_restriction_with_severity, "ValueRestrictionWithSeverity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE-RESTRICTION-WITH-SEVERITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PrimitiveAttributeTailoring":
        """Deserialize XML element to PrimitiveAttributeTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PrimitiveAttributeTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PrimitiveAttributeTailoring, cls).deserialize(element)

        # Parse default_value
        child = ARObject._find_child_element(element, "DEFAULT-VALUE")
        if child is not None:
            default_value_value = DefaultValueApplicationStrategyEnum.deserialize(child)
            obj.default_value = default_value_value

        # Parse sub_attributes (list from container "SUB-ATTRIBUTES")
        obj.sub_attributes = []
        container = ARObject._find_child_element(element, "SUB-ATTRIBUTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sub_attributes.append(child_value)

        # Parse value_restriction_with_severity
        child = ARObject._find_child_element(element, "VALUE-RESTRICTION-WITH-SEVERITY")
        if child is not None:
            value_restriction_with_severity_value = ARObject._deserialize_by_tag(child, "ValueRestrictionWithSeverity")
            obj.value_restriction_with_severity = value_restriction_with_severity_value

        return obj



class PrimitiveAttributeTailoringBuilder:
    """Builder for PrimitiveAttributeTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PrimitiveAttributeTailoring = PrimitiveAttributeTailoring()

    def build(self) -> PrimitiveAttributeTailoring:
        """Build and return PrimitiveAttributeTailoring object.

        Returns:
            PrimitiveAttributeTailoring instance
        """
        # TODO: Add validation
        return self._obj
