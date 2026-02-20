"""PostBuildVariantCriterionValue AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 305)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 77)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 258)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.Documentation.Annotation.annotation import (
    Annotation,
)


class PostBuildVariantCriterionValue(ARObject):
    """AUTOSAR PostBuildVariantCriterionValue."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    annotations: list[Annotation]
    value: Integer
    variant_criterion_ref: Any
    def __init__(self) -> None:
        """Initialize PostBuildVariantCriterionValue."""
        super().__init__()
        self.annotations: list[Annotation] = []
        self.value: Integer = None
        self.variant_criterion_ref: Any = None

    def serialize(self) -> ET.Element:
        """Serialize PostBuildVariantCriterionValue to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize annotations (list to container "ANNOTATIONS")
        if self.annotations:
            wrapper = ET.Element("ANNOTATIONS")
            for item in self.annotations:
                serialized = ARObject._serialize_item(item, "Annotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize value
        if self.value is not None:
            serialized = ARObject._serialize_item(self.value, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variant_criterion_ref
        if self.variant_criterion_ref is not None:
            serialized = ARObject._serialize_item(self.variant_criterion_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIANT-CRITERION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PostBuildVariantCriterionValue":
        """Deserialize XML element to PostBuildVariantCriterionValue object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PostBuildVariantCriterionValue object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse annotations (list from container "ANNOTATIONS")
        obj.annotations = []
        container = ARObject._find_child_element(element, "ANNOTATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.annotations.append(child_value)

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        # Parse variant_criterion_ref
        child = ARObject._find_child_element(element, "VARIANT-CRITERION-REF")
        if child is not None:
            variant_criterion_ref_value = ARRef.deserialize(child)
            obj.variant_criterion_ref = variant_criterion_ref_value

        return obj



class PostBuildVariantCriterionValueBuilder:
    """Builder for PostBuildVariantCriterionValue."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCriterionValue = PostBuildVariantCriterionValue()

    def build(self) -> PostBuildVariantCriterionValue:
        """Build and return PostBuildVariantCriterionValue object.

        Returns:
            PostBuildVariantCriterionValue instance
        """
        # TODO: Add validation
        return self._obj
