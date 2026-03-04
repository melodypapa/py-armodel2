"""SwDataDependency AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 373)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.MSR.AsamHdo.ComputationMethod.compu_generic_math import (
    CompuGenericMath,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwDataDependency(ARObject):
    """AUTOSAR SwDataDependency."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-DATA-DEPENDENCY"


    sw_data: Optional[CompuGenericMath]
    _DESERIALIZE_DISPATCH = {
        "SW-DATA": lambda obj, elem: setattr(obj, "sw_data", SerializationHelper.deserialize_by_tag(elem, "CompuGenericMath")),
    }


    def __init__(self) -> None:
        """Initialize SwDataDependency."""
        super().__init__()
        self.sw_data: Optional[CompuGenericMath] = None

    def serialize(self) -> ET.Element:
        """Serialize SwDataDependency to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwDataDependency, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize sw_data
        if self.sw_data is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data, "CompuGenericMath")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDependency":
        """Deserialize XML element to SwDataDependency object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwDataDependency object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwDataDependency, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "SW-DATA":
                setattr(obj, "sw_data", SerializationHelper.deserialize_by_tag(child, "CompuGenericMath"))

        return obj



class SwDataDependencyBuilder(BuilderBase):
    """Builder for SwDataDependency with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwDataDependency = SwDataDependency()


    def with_sw_data(self, value: Optional[CompuGenericMath]) -> "SwDataDependencyBuilder":
        """Set sw_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_data = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "swData",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwDataDependency:
        """Build and return the SwDataDependency instance with validation."""
        self._validate_instance()
        return self._obj