"""EOCExecutableEntityRefGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 119)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_ExecutionOrderConstraint.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint.eoc_executable_entity_ref_abstract import (
    EOCExecutableEntityRefAbstract,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import (
    LetDataExchangeParadigmEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description_event import (
    TimingDescriptionEvent,
)


class EOCExecutableEntityRefGroup(EOCExecutableEntityRefAbstract):
    """AUTOSAR EOCExecutableEntityRefGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    let_data_exchange: Optional[LetDataExchangeParadigmEnum]
    let_interval_refs: list[ARRef]
    max_cycle: Optional[PositiveInteger]
    max_cycles: Optional[Integer]
    max_slots: Optional[Integer]
    max_slots_per: Optional[PositiveInteger]
    nested_element_refs: list[Any]
    successor_refs: list[Any]
    triggering_event_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize EOCExecutableEntityRefGroup."""
        super().__init__()
        self.let_data_exchange: Optional[LetDataExchangeParadigmEnum] = None
        self.let_interval_refs: list[ARRef] = []
        self.max_cycle: Optional[PositiveInteger] = None
        self.max_cycles: Optional[Integer] = None
        self.max_slots: Optional[Integer] = None
        self.max_slots_per: Optional[PositiveInteger] = None
        self.nested_element_refs: list[Any] = []
        self.successor_refs: list[Any] = []
        self.triggering_event_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize EOCExecutableEntityRefGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EOCExecutableEntityRefGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize let_data_exchange
        if self.let_data_exchange is not None:
            serialized = ARObject._serialize_item(self.let_data_exchange, "LetDataExchangeParadigmEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LET-DATA-EXCHANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize let_interval_refs (list to container "LET-INTERVAL-REFS")
        if self.let_interval_refs:
            wrapper = ET.Element("LET-INTERVAL-REFS")
            for item in self.let_interval_refs:
                serialized = ARObject._serialize_item(item, "TimingDescriptionEvent")
                if serialized is not None:
                    child_elem = ET.Element("LET-INTERVAL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize max_cycle
        if self.max_cycle is not None:
            serialized = ARObject._serialize_item(self.max_cycle, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_cycles
        if self.max_cycles is not None:
            serialized = ARObject._serialize_item(self.max_cycles, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-CYCLES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_slots
        if self.max_slots is not None:
            serialized = ARObject._serialize_item(self.max_slots, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SLOTS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_slots_per
        if self.max_slots_per is not None:
            serialized = ARObject._serialize_item(self.max_slots_per, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-SLOTS-PER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nested_element_refs (list to container "NESTED-ELEMENT-REFS")
        if self.nested_element_refs:
            wrapper = ET.Element("NESTED-ELEMENT-REFS")
            for item in self.nested_element_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("NESTED-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize successor_refs (list to container "SUCCESSOR-REFS")
        if self.successor_refs:
            wrapper = ET.Element("SUCCESSOR-REFS")
            for item in self.successor_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("SUCCESSOR-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize triggering_event_ref
        if self.triggering_event_ref is not None:
            serialized = ARObject._serialize_item(self.triggering_event_ref, "TimingDescriptionEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGERING-EVENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EOCExecutableEntityRefGroup":
        """Deserialize XML element to EOCExecutableEntityRefGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EOCExecutableEntityRefGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EOCExecutableEntityRefGroup, cls).deserialize(element)

        # Parse let_data_exchange
        child = ARObject._find_child_element(element, "LET-DATA-EXCHANGE")
        if child is not None:
            let_data_exchange_value = LetDataExchangeParadigmEnum.deserialize(child)
            obj.let_data_exchange = let_data_exchange_value

        # Parse let_interval_refs (list from container "LET-INTERVAL-REFS")
        obj.let_interval_refs = []
        container = ARObject._find_child_element(element, "LET-INTERVAL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.let_interval_refs.append(child_value)

        # Parse max_cycle
        child = ARObject._find_child_element(element, "MAX-CYCLE")
        if child is not None:
            max_cycle_value = child.text
            obj.max_cycle = max_cycle_value

        # Parse max_cycles
        child = ARObject._find_child_element(element, "MAX-CYCLES")
        if child is not None:
            max_cycles_value = child.text
            obj.max_cycles = max_cycles_value

        # Parse max_slots
        child = ARObject._find_child_element(element, "MAX-SLOTS")
        if child is not None:
            max_slots_value = child.text
            obj.max_slots = max_slots_value

        # Parse max_slots_per
        child = ARObject._find_child_element(element, "MAX-SLOTS-PER")
        if child is not None:
            max_slots_per_value = child.text
            obj.max_slots_per = max_slots_per_value

        # Parse nested_element_refs (list from container "NESTED-ELEMENT-REFS")
        obj.nested_element_refs = []
        container = ARObject._find_child_element(element, "NESTED-ELEMENT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nested_element_refs.append(child_value)

        # Parse successor_refs (list from container "SUCCESSOR-REFS")
        obj.successor_refs = []
        container = ARObject._find_child_element(element, "SUCCESSOR-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.successor_refs.append(child_value)

        # Parse triggering_event_ref
        child = ARObject._find_child_element(element, "TRIGGERING-EVENT-REF")
        if child is not None:
            triggering_event_ref_value = ARRef.deserialize(child)
            obj.triggering_event_ref = triggering_event_ref_value

        return obj



class EOCExecutableEntityRefGroupBuilder:
    """Builder for EOCExecutableEntityRefGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EOCExecutableEntityRefGroup = EOCExecutableEntityRefGroup()

    def build(self) -> EOCExecutableEntityRefGroup:
        """Build and return EOCExecutableEntityRefGroup object.

        Returns:
            EOCExecutableEntityRefGroup instance
        """
        # TODO: Add validation
        return self._obj
