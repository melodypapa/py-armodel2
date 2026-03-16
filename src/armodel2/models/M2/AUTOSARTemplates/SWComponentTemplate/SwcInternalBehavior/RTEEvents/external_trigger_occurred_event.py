"""ExternalTriggerOccurredEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 545)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_RTEEvents.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import RTEEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.r_trigger_in_atomic_swc_instance_ref import (
    RTriggerInAtomicSwcInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ExternalTriggerOccurredEvent(RTEEvent):
    """AUTOSAR ExternalTriggerOccurredEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "EXTERNAL-TRIGGER-OCCURRED-EVENT"


    trigger_iref: Optional[RTriggerInAtomicSwcInstanceRef]
    _DESERIALIZE_DISPATCH = {
        "TRIGGER-IREF": lambda obj, elem: setattr(obj, "trigger_iref", SerializationHelper.deserialize_by_tag(elem, "RTriggerInAtomicSwcInstanceRef")),
    }


    def __init__(self) -> None:
        """Initialize ExternalTriggerOccurredEvent."""
        super().__init__()
        self.trigger_iref: Optional[RTriggerInAtomicSwcInstanceRef] = None

    def serialize(self) -> ET.Element:
        """Serialize ExternalTriggerOccurredEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExternalTriggerOccurredEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize trigger_iref (instance reference with wrapper "TRIGGER-IREF")
        if self.trigger_iref is not None:
            serialized = SerializationHelper.serialize_item(self.trigger_iref, "RTriggerInAtomicSwcInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("TRIGGER-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExternalTriggerOccurredEvent":
        """Deserialize XML element to ExternalTriggerOccurredEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExternalTriggerOccurredEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExternalTriggerOccurredEvent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TRIGGER-IREF":
                setattr(obj, "trigger_iref", SerializationHelper.deserialize_by_tag(child, "RTriggerInAtomicSwcInstanceRef"))

        return obj



class ExternalTriggerOccurredEventBuilder(RTEEventBuilder):
    """Builder for ExternalTriggerOccurredEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ExternalTriggerOccurredEvent = ExternalTriggerOccurredEvent()


    def with_trigger(self, value: Optional[RTriggerInAtomicSwcInstanceRef]) -> "ExternalTriggerOccurredEventBuilder":
        """Set trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'trigger' is required and cannot be None")
        self._obj.trigger = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "trigger",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ExternalTriggerOccurredEvent:
        """Build and return the ExternalTriggerOccurredEvent instance with validation."""
        self._validate_instance()
        return self._obj