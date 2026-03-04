"""DataReceivedEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 542)

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
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs.r_variable_in_atomic_swc_instance_ref import (
    RVariableInAtomicSwcInstanceRef,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DataReceivedEvent(RTEEvent):
    """AUTOSAR DataReceivedEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-RECEIVED-EVENT"


    data_iref: Optional[RVariableInAtomicSwcInstanceRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-IREF": lambda obj, elem: setattr(obj, "data_iref", SerializationHelper.deserialize_by_tag(elem, "RVariableInAtomicSwcInstanceRef")),
    }


    def __init__(self) -> None:
        """Initialize DataReceivedEvent."""
        super().__init__()
        self.data_iref: Optional[RVariableInAtomicSwcInstanceRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DataReceivedEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataReceivedEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_iref (instance reference with wrapper "DATA-IREF")
        if self.data_iref is not None:
            serialized = SerializationHelper.serialize_item(self.data_iref, "RVariableInAtomicSwcInstanceRef")
            if serialized is not None:
                # Wrap in IREF wrapper element
                iref_wrapper = ET.Element("DATA-IREF")
                # Flatten: append children of serialized element directly to iref wrapper
                for child in serialized:
                    iref_wrapper.append(child)
                elem.append(iref_wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataReceivedEvent":
        """Deserialize XML element to DataReceivedEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataReceivedEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataReceivedEvent, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-IREF":
                setattr(obj, "data_iref", SerializationHelper.deserialize_by_tag(child, "RVariableInAtomicSwcInstanceRef"))

        return obj



class DataReceivedEventBuilder(RTEEventBuilder):
    """Builder for DataReceivedEvent with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataReceivedEvent = DataReceivedEvent()


    def with_data(self, value: Optional[RVariableInAtomicSwcInstanceRef]) -> "DataReceivedEventBuilder":
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


    def build(self) -> DataReceivedEvent:
        """Build and return the DataReceivedEvent instance with validation."""
        self._validate_instance()
        return self._obj