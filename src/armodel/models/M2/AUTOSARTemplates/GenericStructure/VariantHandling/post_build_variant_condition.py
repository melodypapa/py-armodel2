"""PostBuildVariantCondition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 614)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 76)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 232)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class PostBuildVariantCondition(ARObject):
    """AUTOSAR PostBuildVariantCondition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    matching: Any
    value: Integer
    def __init__(self) -> None:
        """Initialize PostBuildVariantCondition."""
        super().__init__()
        self.matching: Any = None
        self.value: Integer = None
    def serialize(self) -> ET.Element:
        """Serialize PostBuildVariantCondition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize matching
        if self.matching is not None:
            serialized = ARObject._serialize_item(self.matching, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MATCHING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PostBuildVariantCondition":
        """Deserialize XML element to PostBuildVariantCondition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PostBuildVariantCondition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse matching
        child = ARObject._find_child_element(element, "MATCHING")
        if child is not None:
            matching_value = child.text
            obj.matching = matching_value

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        return obj



class PostBuildVariantConditionBuilder:
    """Builder for PostBuildVariantCondition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PostBuildVariantCondition = PostBuildVariantCondition()

    def build(self) -> PostBuildVariantCondition:
        """Build and return PostBuildVariantCondition object.

        Returns:
            PostBuildVariantCondition instance
        """
        # TODO: Add validation
        return self._obj
