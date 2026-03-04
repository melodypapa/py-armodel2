"""AccessCount AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_AccessCount.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AccessCount(ARObject):
    """AUTOSAR AccessCount."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ACCESS-COUNT"


    access_point_ref: Optional[ARRef]
    value: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ACCESS-POINT-REF": ("_POLYMORPHIC", "access_point_ref", ["AsynchronousServerCallPoint", "AsynchronousServerCallResultPoint", "ExternalTriggeringPointIdent", "InternalTriggeringPoint", "ModeAccessPointIdent", "ModeSwitchPoint", "ParameterAccess", "ServerCallPoint", "SynchronousServerCallPoint", "VariableAccess"]),
        "VALUE": lambda obj, elem: setattr(obj, "value", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize AccessCount."""
        super().__init__()
        self.access_point_ref: Optional[ARRef] = None
        self.value: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize AccessCount to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AccessCount, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access_point_ref
        if self.access_point_ref is not None:
            serialized = SerializationHelper.serialize_item(self.access_point_ref, "AbstractAccessPoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACCESS-POINT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize value
        if self.value is not None:
            serialized = SerializationHelper.serialize_item(self.value, "PositiveInteger")
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
    def deserialize(cls, element: ET.Element) -> "AccessCount":
        """Deserialize XML element to AccessCount object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AccessCount object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AccessCount, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ACCESS-POINT-REF":
                setattr(obj, "access_point_ref", ARRef.deserialize(child))
            elif tag == "VALUE":
                setattr(obj, "value", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class AccessCountBuilder(BuilderBase):
    """Builder for AccessCount with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AccessCount = AccessCount()


    def with_access_point(self, value: Optional[AbstractAccessPoint]) -> "AccessCountBuilder":
        """Set access_point attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.access_point = value
        return self

    def with_value(self, value: Optional[PositiveInteger]) -> "AccessCountBuilder":
        """Set value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.value = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "accessPoint",
        "value",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> AccessCount:
        """Build and return the AccessCount instance with validation."""
        self._validate_instance()
        return self._obj