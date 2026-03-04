"""BswTriggerDirectImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswTriggerDirectImplementation(ARObject):
    """AUTOSAR BswTriggerDirectImplementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-TRIGGER-DIRECT-IMPLEMENTATION"


    cat2_isr: Optional[Identifier]
    mastered_trigger_ref: Optional[ARRef]
    task: Optional[Identifier]
    _DESERIALIZE_DISPATCH = {
        "CAT2-ISR": lambda obj, elem: setattr(obj, "cat2_isr", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "MASTERED-TRIGGER-REF": lambda obj, elem: setattr(obj, "mastered_trigger_ref", ARRef.deserialize(elem)),
        "TASK": lambda obj, elem: setattr(obj, "task", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
    }


    def __init__(self) -> None:
        """Initialize BswTriggerDirectImplementation."""
        super().__init__()
        self.cat2_isr: Optional[Identifier] = None
        self.mastered_trigger_ref: Optional[ARRef] = None
        self.task: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize BswTriggerDirectImplementation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswTriggerDirectImplementation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cat2_isr
        if self.cat2_isr is not None:
            serialized = SerializationHelper.serialize_item(self.cat2_isr, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAT2-ISR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mastered_trigger_ref
        if self.mastered_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mastered_trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASTERED-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize task
        if self.task is not None:
            serialized = SerializationHelper.serialize_item(self.task, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswTriggerDirectImplementation":
        """Deserialize XML element to BswTriggerDirectImplementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswTriggerDirectImplementation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswTriggerDirectImplementation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CAT2-ISR":
                setattr(obj, "cat2_isr", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "MASTERED-TRIGGER-REF":
                setattr(obj, "mastered_trigger_ref", ARRef.deserialize(child))
            elif tag == "TASK":
                setattr(obj, "task", SerializationHelper.deserialize_by_tag(child, "Identifier"))

        return obj



class BswTriggerDirectImplementationBuilder(BuilderBase):
    """Builder for BswTriggerDirectImplementation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswTriggerDirectImplementation = BswTriggerDirectImplementation()


    def with_cat2_isr(self, value: Optional[Identifier]) -> "BswTriggerDirectImplementationBuilder":
        """Set cat2_isr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.cat2_isr = value
        return self

    def with_mastered_trigger(self, value: Optional[Trigger]) -> "BswTriggerDirectImplementationBuilder":
        """Set mastered_trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mastered_trigger = value
        return self

    def with_task(self, value: Optional[Identifier]) -> "BswTriggerDirectImplementationBuilder":
        """Set task attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.task = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "cat2Isr",
        "masteredTrigger",
        "task",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswTriggerDirectImplementation:
        """Build and return the BswTriggerDirectImplementation instance with validation."""
        self._validate_instance()
        return self._obj