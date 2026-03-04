"""BswDataReceivedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 99)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import BswScheduleEventBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class BswDataReceivedEvent(BswScheduleEvent):
    """AUTOSAR BswDataReceivedEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "BSW-DATA-RECEIVED-EVENT"


    data_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-REF": lambda obj, elem: setattr(obj, "data_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize BswDataReceivedEvent."""
        super().__init__()
        self.data_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswDataReceivedEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswDataReceivedEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_ref
        if self.data_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswDataReceivedEvent":
        """Deserialize XML element to BswDataReceivedEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswDataReceivedEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswDataReceivedEvent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-REF":
                setattr(obj, "data_ref", ARRef.deserialize(child))

        return obj



class BswDataReceivedEventBuilder(BswScheduleEventBuilder):
    """Builder for BswDataReceivedEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswDataReceivedEvent = BswDataReceivedEvent()


    def with_data(self, value: Optional[VariableDataPrototype]) -> "BswDataReceivedEventBuilder":
        """Set data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "data",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> BswDataReceivedEvent:
        """Build and return the BswDataReceivedEvent instance with validation."""
        self._validate_instance()
        return self._obj