"""FMFormulaByFeaturesAndSwSystemconsts AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 63)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_FeatureModelTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.FeatureModelTemplate.fm_feature import (
    FMFeature,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "FEATURE-REF": lambda obj, elem: setattr(obj, "feature_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize FMFormulaByFeaturesAndSwSystemconsts."""
        super().__init__()
        self.feature_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize FMFormulaByFeaturesAndSwSystemconsts to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "FEATURE-REF":
                setattr(obj, "feature_ref", ARRef.deserialize(child))

        return obj



class FMFormulaByFeaturesAndSwSystemconstsBuilder(BuilderBase, ABC):
    """Builder for FMFormulaByFeaturesAndSwSystemconsts with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FMFormulaByFeaturesAndSwSystemconsts = FMFormulaByFeaturesAndSwSystemconsts()


    def with_feature(self, value: Optional[FMFeature]) -> "FMFormulaByFeaturesAndSwSystemconstsBuilder":
        """Set feature attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'feature' is required and cannot be None")
        self._obj.feature = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "feature",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> FMFormulaByFeaturesAndSwSystemconsts:
        """Build and return the FMFormulaByFeaturesAndSwSystemconsts instance (abstract)."""
        raise NotImplementedError