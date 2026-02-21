"""FMFeatureDecomposition AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 27)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CategoryString,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)


class FMFeatureDecomposition(ARObject):
    """AUTOSAR FMFeatureDecomposition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    category: Optional[CategoryString]
    feature_refs: list[ARRef]
    max: Optional[PositiveInteger]
    min: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize FMFeatureDecomposition."""
        super().__init__()
        self.category: Optional[CategoryString] = None
        self.feature_refs: list[ARRef] = []
        self.max: Optional[PositiveInteger] = None
        self.min: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize FMFeatureDecomposition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize category
        if self.category is not None:
            serialized = SerializationHelper.serialize_item(self.category, "CategoryString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CATEGORY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize max
        if self.max is not None:
            serialized = SerializationHelper.serialize_item(self.max, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize min
        if self.min is not None:
            serialized = SerializationHelper.serialize_item(self.min, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFeatureDecomposition":
        """Deserialize XML element to FMFeatureDecomposition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFeatureDecomposition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse category
        child = SerializationHelper.find_child_element(element, "CATEGORY")
        if child is not None:
            category_value = child.text
            obj.category = category_value

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

        # Parse max
        child = SerializationHelper.find_child_element(element, "MAX")
        if child is not None:
            max_value = child.text
            obj.max = max_value

        # Parse min
        child = SerializationHelper.find_child_element(element, "MIN")
        if child is not None:
            min_value = child.text
            obj.min = min_value

        return obj



class FMFeatureDecompositionBuilder:
    """Builder for FMFeatureDecomposition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFeatureDecomposition = FMFeatureDecomposition()

    def build(self) -> FMFeatureDecomposition:
        """Build and return FMFeatureDecomposition object.

        Returns:
            FMFeatureDecomposition instance
        """
        # TODO: Add validation
        return self._obj
