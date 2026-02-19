"""FMFeatureMap AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map_element import (
        FMFeatureMapElement,
    )



class FMFeatureMap(ARElement):
    """AUTOSAR FMFeatureMap."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mappings: list[FMFeatureMapElement]
    def __init__(self) -> None:
        """Initialize FMFeatureMap."""
        super().__init__()
        self.mappings: list[FMFeatureMapElement] = []
    def serialize(self) -> ET.Element:
        """Serialize FMFeatureMap to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureMap, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mappings (list to container "MAPPINGS")
        if self.mappings:
            wrapper = ET.Element("MAPPINGS")
            for item in self.mappings:
                serialized = ARObject._serialize_item(item, "FMFeatureMapElement")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureMap":
        """Deserialize XML element to FMFeatureMap object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureMap object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureMap, cls).deserialize(element)

        # Parse mappings (list from container "MAPPINGS")
        obj.mappings = []
        container = ARObject._find_child_element(element, "MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mappings.append(child_value)

        return obj



class FMFeatureMapBuilder:
    """Builder for FMFeatureMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMap = FMFeatureMap()

    def build(self) -> FMFeatureMap:
        """Build and return FMFeatureMap object.

        Returns:
            FMFeatureMap instance
        """
        # TODO: Add validation
        return self._obj
