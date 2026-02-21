"""FMFormulaByFeaturesAndSwSystemconsts AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    feature_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize FMFormulaByFeaturesAndSwSystemconsts."""
        super().__init__()
        self.feature_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize FMFormulaByFeaturesAndSwSystemconsts to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FMFormulaByFeaturesAndSwSystemconsts, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize feature_ref
        if self.feature_ref is not None:
            serialized = SerializationHelper.serialize_item(self.feature_ref, "FMFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FEATURE-REF")
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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FMFormulaByFeaturesAndSwSystemconsts, cls).deserialize(element)

        # Parse feature_ref
        child = SerializationHelper.find_child_element(element, "FEATURE-REF")
        if child is not None:
            feature_ref_value = ARRef.deserialize(child)
            obj.feature_ref = feature_ref_value

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
