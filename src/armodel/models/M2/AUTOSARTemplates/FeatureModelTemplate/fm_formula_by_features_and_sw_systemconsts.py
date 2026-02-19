"""FMFormulaByFeaturesAndSwSystemconsts AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)
from abc import ABC, abstractmethod


class FMFormulaByFeaturesAndSwSystemconsts(ARObject, ABC):
    """AUTOSAR FMFormulaByFeaturesAndSwSystemconsts."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    feature: Optional[FMFeature]
    def __init__(self) -> None:
        """Initialize FMFormulaByFeaturesAndSwSystemconsts."""
        super().__init__()
        self.feature: Optional[FMFeature] = None

    def serialize(self) -> ET.Element:
        """Serialize FMFormulaByFeaturesAndSwSystemconsts to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

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
    def deserialize(cls, element: ET.Element) -> "FMFormulaByFeaturesAndSwSystemconsts":
        """Deserialize XML element to FMFormulaByFeaturesAndSwSystemconsts object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FMFormulaByFeaturesAndSwSystemconsts object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse feature
        child = ARObject._find_child_element(element, "FEATURE")
        if child is not None:
            feature_value = ARObject._deserialize_by_tag(child, "FMFeature")
            obj.feature = feature_value

        return obj



class FMFormulaByFeaturesAndSwSystemconstsBuilder:
    """Builder for FMFormulaByFeaturesAndSwSystemconsts."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FMFormulaByFeaturesAndSwSystemconsts = FMFormulaByFeaturesAndSwSystemconsts()

    def build(self) -> FMFormulaByFeaturesAndSwSystemconsts:
        """Build and return FMFormulaByFeaturesAndSwSystemconsts object.

        Returns:
            FMFormulaByFeaturesAndSwSystemconsts instance
        """
        # TODO: Add validation
        return self._obj
