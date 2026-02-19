"""FMFeatureSelection AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 40)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_value import (
    FMAttributeValue,
)


class FMFeatureSelection(Identifiable):
    """AUTOSAR FMFeatureSelection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attribute_values: list[FMAttributeValue]
    def __init__(self) -> None:
        """Initialize FMFeatureSelection."""
        super().__init__()
        self.attribute_values: list[FMAttributeValue] = []
    def serialize(self) -> ET.Element:
        """Serialize FMFeatureSelection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureSelection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attribute_values (list to container "ATTRIBUTE-VALUES")
        if self.attribute_values:
            wrapper = ET.Element("ATTRIBUTE-VALUES")
            for item in self.attribute_values:
                serialized = ARObject._serialize_item(item, "FMAttributeValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureSelection":
        """Deserialize XML element to FMFeatureSelection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureSelection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureSelection, cls).deserialize(element)

        # Parse attribute_values (list from container "ATTRIBUTE-VALUES")
        obj.attribute_values = []
        container = ARObject._find_child_element(element, "ATTRIBUTE-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.attribute_values.append(child_value)

        return obj



class FMFeatureSelectionBuilder:
    """Builder for FMFeatureSelection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureSelection = FMFeatureSelection()

    def build(self) -> FMFeatureSelection:
        """Build and return FMFeatureSelection object.

        Returns:
            FMFeatureSelection instance
        """
        # TODO: Add validation
        return self._obj
