"""FMFormulaByFeaturesAndAttributes AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 61)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_attribute_def import (
    FMAttributeDef,
)
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)
from abc import ABC, abstractmethod


class FMFormulaByFeaturesAndAttributes(ARObject, ABC):
    """AUTOSAR FMFormulaByFeaturesAndAttributes."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    attribute: Optional[FMAttributeDef]
    feature: Optional[FMFeature]
    def __init__(self) -> None:
        """Initialize FMFormulaByFeaturesAndAttributes."""
        super().__init__()
        self.attribute: Optional[FMAttributeDef] = None
        self.feature: Optional[FMFeature] = None
    def serialize(self) -> ET.Element:
        """Serialize FMFormulaByFeaturesAndAttributes to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize attribute
        if self.attribute is not None:
            serialized = ARObject._serialize_item(self.attribute, "FMAttributeDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATTRIBUTE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize feature
        if self.feature is not None:
            serialized = ARObject._serialize_item(self.feature, "FMFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FEATURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FMFormulaByFeaturesAndAttributes":
        """Deserialize XML element to FMFormulaByFeaturesAndAttributes object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFormulaByFeaturesAndAttributes object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse attribute
        child = ARObject._find_child_element(element, "ATTRIBUTE")
        if child is not None:
            attribute_value = ARObject._deserialize_by_tag(child, "FMAttributeDef")
            obj.attribute = attribute_value

        # Parse feature
        child = ARObject._find_child_element(element, "FEATURE")
        if child is not None:
            feature_value = ARObject._deserialize_by_tag(child, "FMFeature")
            obj.feature = feature_value

        return obj



class FMFormulaByFeaturesAndAttributesBuilder:
    """Builder for FMFormulaByFeaturesAndAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFormulaByFeaturesAndAttributes = FMFormulaByFeaturesAndAttributes()

    def build(self) -> FMFormulaByFeaturesAndAttributes:
        """Build and return FMFormulaByFeaturesAndAttributes object.

        Returns:
            FMFormulaByFeaturesAndAttributes instance
        """
        # TODO: Add validation
        return self._obj
