"""PostBuildVariantCriterionValueSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1000)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 56)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 258)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class PostBuildVariantCriterionValueSet(ARElement):
    """AUTOSAR PostBuildVariantCriterionValueSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    post_build_variants: list[Any]
    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterionValueSet."""
        super().__init__()
        self.post_build_variants: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize PostBuildVariantCriterionValueSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PostBuildVariantCriterionValueSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize post_build_variants (list to container "POST-BUILD-VARIANTS")
        if self.post_build_variants:
            wrapper = ET.Element("POST-BUILD-VARIANTS")
            for item in self.post_build_variants:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PostBuildVariantCriterionValueSet":
        """Deserialize XML element to PostBuildVariantCriterionValueSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PostBuildVariantCriterionValueSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PostBuildVariantCriterionValueSet, cls).deserialize(element)

        # Parse post_build_variants (list from container "POST-BUILD-VARIANTS")
        obj.post_build_variants = []
        container = SerializationHelper.find_child_element(element, "POST-BUILD-VARIANTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.post_build_variants.append(child_value)

        return obj



class PostBuildVariantCriterionValueSetBuilder:
    """Builder for PostBuildVariantCriterionValueSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCriterionValueSet = PostBuildVariantCriterionValueSet()

    def build(self) -> PostBuildVariantCriterionValueSet:
        """Build and return PostBuildVariantCriterionValueSet object.

        Returns:
            PostBuildVariantCriterionValueSet instance
        """
        # TODO: Add validation
        return self._obj
