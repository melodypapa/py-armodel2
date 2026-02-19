"""AggregationTailoring AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 113)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.attribute_tailoring import (
    AttributeTailoring,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Data.class_tailoring import (
    ClassTailoring,
)


class AggregationTailoring(AttributeTailoring):
    """AUTOSAR AggregationTailoring."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    type_tailorings: list[ClassTailoring]
    def __init__(self) -> None:
        """Initialize AggregationTailoring."""
        super().__init__()
        self.type_tailorings: list[ClassTailoring] = []
    def serialize(self) -> ET.Element:
        """Serialize AggregationTailoring to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AggregationTailoring, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize type_tailorings (list to container "TYPE-TAILORINGS")
        if self.type_tailorings:
            wrapper = ET.Element("TYPE-TAILORINGS")
            for item in self.type_tailorings:
                serialized = ARObject._serialize_item(item, "ClassTailoring")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AggregationTailoring":
        """Deserialize XML element to AggregationTailoring object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AggregationTailoring object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AggregationTailoring, cls).deserialize(element)

        # Parse type_tailorings (list from container "TYPE-TAILORINGS")
        obj.type_tailorings = []
        container = ARObject._find_child_element(element, "TYPE-TAILORINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.type_tailorings.append(child_value)

        return obj



class AggregationTailoringBuilder:
    """Builder for AggregationTailoring."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AggregationTailoring = AggregationTailoring()

    def build(self) -> AggregationTailoring:
        """Build and return AggregationTailoring object.

        Returns:
            AggregationTailoring instance
        """
        # TODO: Add validation
        return self._obj
