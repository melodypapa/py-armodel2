"""FMFeatureRelation AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
        FMFeature,
    )



class FMFeatureRelation(Identifiable):
    """AUTOSAR FMFeatureRelation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    features: list[FMFeature]
    restriction: Optional[Any]
    def __init__(self) -> None:
        """Initialize FMFeatureRelation."""
        super().__init__()
        self.features: list[FMFeature] = []
        self.restriction: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize FMFeatureRelation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureRelation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize features (list to container "FEATURES")
        if self.features:
            wrapper = ET.Element("FEATURES")
            for item in self.features:
                serialized = ARObject._serialize_item(item, "FMFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize restriction
        if self.restriction is not None:
            serialized = ARObject._serialize_item(self.restriction, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESTRICTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureRelation":
        """Deserialize XML element to FMFeatureRelation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureRelation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureRelation, cls).deserialize(element)

        # Parse features (list from container "FEATURES")
        obj.features = []
        container = ARObject._find_child_element(element, "FEATURES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.features.append(child_value)

        # Parse restriction
        child = ARObject._find_child_element(element, "RESTRICTION")
        if child is not None:
            restriction_value = child.text
            obj.restriction = restriction_value

        return obj



class FMFeatureRelationBuilder:
    """Builder for FMFeatureRelation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureRelation = FMFeatureRelation()

    def build(self) -> FMFeatureRelation:
        """Build and return FMFeatureRelation object.

        Returns:
            FMFeatureRelation instance
        """
        # TODO: Add validation
        return self._obj
