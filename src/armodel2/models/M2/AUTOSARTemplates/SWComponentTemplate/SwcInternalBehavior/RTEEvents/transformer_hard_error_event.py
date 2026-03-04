"""TransformerHardErrorEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 546)

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
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TransformerHardErrorEvent(RTEEvent):
    """AUTOSAR TransformerHardErrorEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TRANSFORMER-HARD-ERROR-EVENT"


    operation: Optional[ClientServerOperation]
    required_trigger_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "OPERATION": lambda obj, elem: setattr(obj, "operation", SerializationHelper.deserialize_by_tag(elem, "ClientServerOperation")),
        "REQUIRED-TRIGGER-REF": lambda obj, elem: setattr(obj, "required_trigger_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize TransformerHardErrorEvent."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
        self.required_trigger_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize TransformerHardErrorEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TransformerHardErrorEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operation
        if self.operation is not None:
            serialized = SerializationHelper.serialize_item(self.operation, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize required_trigger_ref
        if self.required_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.required_trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRED-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformerHardErrorEvent":
        """Deserialize XML element to TransformerHardErrorEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformerHardErrorEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransformerHardErrorEvent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "OPERATION":
                setattr(obj, "operation", SerializationHelper.deserialize_by_tag(child, "ClientServerOperation"))
            elif tag == "REQUIRED-TRIGGER-REF":
                setattr(obj, "required_trigger_ref", ARRef.deserialize(child))

        return obj



class TransformerHardErrorEventBuilder(RTEEventBuilder):
    """Builder for TransformerHardErrorEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TransformerHardErrorEvent = TransformerHardErrorEvent()


    def with_operation(self, value: Optional[ClientServerOperation]) -> "TransformerHardErrorEventBuilder":
        """Set operation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.operation = value
        return self

    def with_required_trigger(self, value: Optional[Trigger]) -> "TransformerHardErrorEventBuilder":
        """Set required_trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.required_trigger = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "operation",
        "requiredTrigger",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TransformerHardErrorEvent:
        """Build and return the TransformerHardErrorEvent instance with validation."""
        self._validate_instance()
        return self._obj