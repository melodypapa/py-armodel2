"""FMFeatureMapElement AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 53)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature_map import (
        FMFeatureMap,
    )



class FMFeatureMapElement(Identifiable):
    """AUTOSAR FMFeatureMapElement."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assertions: list[FMFeatureMap]
    conditions: list[FMFeatureMap]
    post_build_variant_refs: list[Any]
    sw_value_set_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize FMFeatureMapElement."""
        super().__init__()
        self.assertions: list[FMFeatureMap] = []
        self.conditions: list[FMFeatureMap] = []
        self.post_build_variant_refs: list[Any] = []
        self.sw_value_set_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize FMFeatureMapElement to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFeatureMapElement, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize assertions (list to container "ASSERTIONS")
        if self.assertions:
            wrapper = ET.Element("ASSERTIONS")
            for item in self.assertions:
                serialized = ARObject._serialize_item(item, "FMFeatureMap")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize conditions (list to container "CONDITIONS")
        if self.conditions:
            wrapper = ET.Element("CONDITIONS")
            for item in self.conditions:
                serialized = ARObject._serialize_item(item, "FMFeatureMap")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize post_build_variant_refs (list to container "POST-BUILD-VARIANT-REFS")
        if self.post_build_variant_refs:
            wrapper = ET.Element("POST-BUILD-VARIANT-REFS")
            for item in self.post_build_variant_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("POST-BUILD-VARIANT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_value_set_refs (list to container "SW-VALUE-SET-REFS")
        if self.sw_value_set_refs:
            wrapper = ET.Element("SW-VALUE-SET-REFS")
            for item in self.sw_value_set_refs:
                serialized = ARObject._serialize_item(item, "SwSystemconstantValueSet")
                if serialized is not None:
                    child_elem = ET.Element("SW-VALUE-SET-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureMapElement":
        """Deserialize XML element to FMFeatureMapElement object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureMapElement object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFeatureMapElement, cls).deserialize(element)

        # Parse assertions (list from container "ASSERTIONS")
        obj.assertions = []
        container = ARObject._find_child_element(element, "ASSERTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.assertions.append(child_value)

        # Parse conditions (list from container "CONDITIONS")
        obj.conditions = []
        container = ARObject._find_child_element(element, "CONDITIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.conditions.append(child_value)

        # Parse post_build_variant_refs (list from container "POST-BUILD-VARIANT-REFS")
        obj.post_build_variant_refs = []
        container = ARObject._find_child_element(element, "POST-BUILD-VARIANT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.post_build_variant_refs.append(child_value)

        # Parse sw_value_set_refs (list from container "SW-VALUE-SET-REFS")
        obj.sw_value_set_refs = []
        container = ARObject._find_child_element(element, "SW-VALUE-SET-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_value_set_refs.append(child_value)

        return obj



class FMFeatureMapElementBuilder:
    """Builder for FMFeatureMapElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureMapElement = FMFeatureMapElement()

    def build(self) -> FMFeatureMapElement:
        """Build and return FMFeatureMapElement object.

        Returns:
            FMFeatureMapElement instance
        """
        # TODO: Add validation
        return self._obj
