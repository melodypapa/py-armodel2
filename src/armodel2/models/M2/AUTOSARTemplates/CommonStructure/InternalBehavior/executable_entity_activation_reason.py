"""ExecutableEntityActivationReason AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 315)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 538)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import ImplementationPropsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ExecutableEntityActivationReason(ImplementationProps):
    """AUTOSAR ExecutableEntityActivationReason."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "EXECUTABLE-ENTITY-ACTIVATION-REASON"


    bit_position: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "BIT-POSITION": lambda obj, elem: setattr(obj, "bit_position", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize ExecutableEntityActivationReason."""
        super().__init__()
        self.bit_position: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ExecutableEntityActivationReason to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExecutableEntityActivationReason, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bit_position
        if self.bit_position is not None:
            serialized = SerializationHelper.serialize_item(self.bit_position, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BIT-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutableEntityActivationReason":
        """Deserialize XML element to ExecutableEntityActivationReason object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutableEntityActivationReason object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExecutableEntityActivationReason, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BIT-POSITION":
                setattr(obj, "bit_position", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class ExecutableEntityActivationReasonBuilder(ImplementationPropsBuilder):
    """Builder for ExecutableEntityActivationReason with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ExecutableEntityActivationReason = ExecutableEntityActivationReason()


    def with_bit_position(self, value: Optional[PositiveInteger]) -> "ExecutableEntityActivationReasonBuilder":
        """Set bit_position attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'bit_position' is required and cannot be None")
        self._obj.bit_position = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "bitPosition",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ExecutableEntityActivationReason:
        """Build and return the ExecutableEntityActivationReason instance with validation."""
        self._validate_instance()
        return self._obj