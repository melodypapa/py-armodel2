"""FlexrayAbsolutelyScheduledTiming AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 423)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Flexray_FlexrayCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_cycle import (
    CommunicationCycle,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayAbsolutelyScheduledTiming(ARObject):
    """AUTOSAR FlexrayAbsolutelyScheduledTiming."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-ABSOLUTELY-SCHEDULED-TIMING"


    communication_cycle_cycle: Optional[CommunicationCycle]
    slot_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "COMMUNICATION-CYCLE-CYCLE": ("_POLYMORPHIC", "communication_cycle_cycle", ["CycleCounter", "CycleRepetition"]),
        "SLOT-ID": lambda obj, elem: setattr(obj, "slot_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize FlexrayAbsolutelyScheduledTiming."""
        super().__init__()
        self.communication_cycle_cycle: Optional[CommunicationCycle] = None
        self.slot_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayAbsolutelyScheduledTiming to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayAbsolutelyScheduledTiming, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_cycle_cycle
        if self.communication_cycle_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.communication_cycle_cycle, "CommunicationCycle")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CYCLE-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slot_id
        if self.slot_id is not None:
            serialized = SerializationHelper.serialize_item(self.slot_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLOT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayAbsolutelyScheduledTiming":
        """Deserialize XML element to FlexrayAbsolutelyScheduledTiming object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayAbsolutelyScheduledTiming object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayAbsolutelyScheduledTiming, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMMUNICATION-CYCLE-CYCLE":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "CYCLE-COUNTER":
                        setattr(obj, "communication_cycle_cycle", SerializationHelper.deserialize_by_tag(child[0], "CycleCounter"))
                    elif concrete_tag == "CYCLE-REPETITION":
                        setattr(obj, "communication_cycle_cycle", SerializationHelper.deserialize_by_tag(child[0], "CycleRepetition"))
            elif tag == "SLOT-ID":
                setattr(obj, "slot_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class FlexrayAbsolutelyScheduledTimingBuilder(BuilderBase):
    """Builder for FlexrayAbsolutelyScheduledTiming with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayAbsolutelyScheduledTiming = FlexrayAbsolutelyScheduledTiming()


    def with_communication_cycle_cycle(self, value: Optional[CommunicationCycle]) -> "FlexrayAbsolutelyScheduledTimingBuilder":
        """Set communication_cycle_cycle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'communication_cycle_cycle' is required and cannot be None")
        self._obj.communication_cycle_cycle = value
        return self

    def with_slot_id(self, value: Optional[PositiveInteger]) -> "FlexrayAbsolutelyScheduledTimingBuilder":
        """Set slot_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'slot_id' is required and cannot be None")
        self._obj.slot_id = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "communicationCycleCycle",
        "slotID",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> FlexrayAbsolutelyScheduledTiming:
        """Build and return the FlexrayAbsolutelyScheduledTiming instance with validation."""
        self._validate_instance()
        return self._obj