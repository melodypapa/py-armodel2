"""ModeSwitchEventTriggeredActivity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.swc_mode_switch_event import (
    SwcModeSwitchEvent,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ModeSwitchEventTriggeredActivity(ARObject):
    """AUTOSAR ModeSwitchEventTriggeredActivity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MODE-SWITCH-EVENT-TRIGGERED-ACTIVITY"


    role: Optional[Identifier]
    swc_mode_switch_event_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "ROLE": lambda obj, elem: setattr(obj, "role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "SWC-MODE-SWITCH-EVENT-REF": lambda obj, elem: setattr(obj, "swc_mode_switch_event_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ModeSwitchEventTriggeredActivity."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.swc_mode_switch_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ModeSwitchEventTriggeredActivity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ModeSwitchEventTriggeredActivity, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize role
        if self.role is not None:
            serialized = SerializationHelper.serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_mode_switch_event_ref
        if self.swc_mode_switch_event_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_mode_switch_event_ref, "SwcModeSwitchEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-MODE-SWITCH-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeSwitchEventTriggeredActivity":
        """Deserialize XML element to ModeSwitchEventTriggeredActivity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeSwitchEventTriggeredActivity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeSwitchEventTriggeredActivity, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ROLE":
                setattr(obj, "role", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "SWC-MODE-SWITCH-EVENT-REF":
                setattr(obj, "swc_mode_switch_event_ref", ARRef.deserialize(child))

        return obj



class ModeSwitchEventTriggeredActivityBuilder(BuilderBase):
    """Builder for ModeSwitchEventTriggeredActivity with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ModeSwitchEventTriggeredActivity = ModeSwitchEventTriggeredActivity()


    def with_role(self, value: Optional[Identifier]) -> "ModeSwitchEventTriggeredActivityBuilder":
        """Set role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'role' is required and cannot be None")
        self._obj.role = value
        return self

    def with_swc_mode_switch_event(self, value: Optional[SwcModeSwitchEvent]) -> "ModeSwitchEventTriggeredActivityBuilder":
        """Set swc_mode_switch_event attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'swc_mode_switch_event' is required and cannot be None")
        self._obj.swc_mode_switch_event = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "role",
        "swcModeSwitchEvent",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ModeSwitchEventTriggeredActivity:
        """Build and return the ModeSwitchEventTriggeredActivity instance with validation."""
        self._validate_instance()
        return self._obj