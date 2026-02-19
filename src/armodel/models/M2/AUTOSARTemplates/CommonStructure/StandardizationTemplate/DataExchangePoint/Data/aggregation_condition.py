"""AggregationCondition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_condition import (
    AttributeCondition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.aggregation_tailoring import (
    AggregationTailoring,
)


class AggregationCondition(AttributeCondition):
    """AUTOSAR AggregationCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    aggregation: AggregationTailoring
    def __init__(self) -> None:
        """Initialize AggregationCondition."""
        super().__init__()
        self.aggregation: AggregationTailoring = None
    def serialize(self) -> ET.Element:
        """Serialize AggregationCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AggregationCondition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize aggregation
        if self.aggregation is not None:
            serialized = ARObject._serialize_item(self.aggregation, "AggregationTailoring")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AGGREGATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AggregationCondition":
        """Deserialize XML element to AggregationCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AggregationCondition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AggregationCondition, cls).deserialize(element)

        # Parse aggregation
        child = ARObject._find_child_element(element, "AGGREGATION")
        if child is not None:
            aggregation_value = ARObject._deserialize_by_tag(child, "AggregationTailoring")
            obj.aggregation = aggregation_value

        return obj



class AggregationConditionBuilder:
    """Builder for AggregationCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AggregationCondition = AggregationCondition()

    def build(self) -> AggregationCondition:
        """Build and return AggregationCondition object.

        Returns:
            AggregationCondition instance
        """
        # TODO: Add validation
        return self._obj
