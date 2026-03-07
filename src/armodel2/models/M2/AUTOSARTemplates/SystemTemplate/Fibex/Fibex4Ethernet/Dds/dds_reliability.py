"""DdsReliability AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 534)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import (
    DdsReliabilityKindEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Float,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsReliability(ARObject):
    """AUTOSAR DdsReliability."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-RELIABILITY"


    reliability_kind: Optional[DdsReliabilityKindEnum]
    reliability_max: Optional[Float]
    _DESERIALIZE_DISPATCH = {
        "RELIABILITY-KIND": lambda obj, elem: setattr(obj, "reliability_kind", DdsReliabilityKindEnum.deserialize(elem)),
        "RELIABILITY-MAX": lambda obj, elem: setattr(obj, "reliability_max", SerializationHelper.deserialize_by_tag(elem, "Float")),
    }


    def __init__(self) -> None:
        """Initialize DdsReliability."""
        super().__init__()
        self.reliability_kind: Optional[DdsReliabilityKindEnum] = None
        self.reliability_max: Optional[Float] = None

    def serialize(self) -> ET.Element:
        """Serialize DdsReliability to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsReliability, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize reliability_kind
        if self.reliability_kind is not None:
            serialized = SerializationHelper.serialize_item(self.reliability_kind, "DdsReliabilityKindEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELIABILITY-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize reliability_max
        if self.reliability_max is not None:
            serialized = SerializationHelper.serialize_item(self.reliability_max, "Float")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RELIABILITY-MAX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DdsReliability":
        """Deserialize XML element to DdsReliability object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsReliability object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsReliability, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "RELIABILITY-KIND":
                setattr(obj, "reliability_kind", DdsReliabilityKindEnum.deserialize(child))
            elif tag == "RELIABILITY-MAX":
                setattr(obj, "reliability_max", SerializationHelper.deserialize_by_tag(child, "Float"))

        return obj



class DdsReliabilityBuilder(BuilderBase):
    """Builder for DdsReliability with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsReliability = DdsReliability()


    def with_reliability_kind(self, value: Optional[DdsReliabilityKindEnum]) -> "DdsReliabilityBuilder":
        """Set reliability_kind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'reliability_kind' is required and cannot be None")
        self._obj.reliability_kind = value
        return self

    def with_reliability_max(self, value: Optional[Float]) -> "DdsReliabilityBuilder":
        """Set reliability_max attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'reliability_max' is required and cannot be None")
        self._obj.reliability_max = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "reliabilityKind",
        "reliabilityMax",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DdsReliability:
        """Build and return the DdsReliability instance with validation."""
        self._validate_instance()
        return self._obj