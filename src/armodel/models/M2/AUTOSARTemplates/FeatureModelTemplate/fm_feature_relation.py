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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

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

    feature_refs: list[ARRef]
    restriction: Optional[Any]
    def __init__(self) -> None:
        """Initialize FMFeatureRelation."""
        super().__init__()
        self.feature_refs: list[ARRef] = []
        self.restriction: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize FMFeatureRelation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureRelation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize feature_refs (list to container "FEATURE-REFS")
        if self.feature_refs:
            wrapper = ET.Element("FEATURE-REFS")
            for item in self.feature_refs:
                serialized = SerializationHelper.serialize_item(item, "FMFeature")
                if serialized is not None:
                    child_elem = ET.Element("FEATURE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize restriction
        if self.restriction is not None:
            serialized = SerializationHelper.serialize_item(self.restriction, "Any")
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

        # Parse feature_refs (list from container "FEATURE-REFS")
        obj.feature_refs = []
        container = SerializationHelper.find_child_element(element, "FEATURE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.feature_refs.append(child_value)

        # Parse restriction
        child = SerializationHelper.find_child_element(element, "RESTRICTION")
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
