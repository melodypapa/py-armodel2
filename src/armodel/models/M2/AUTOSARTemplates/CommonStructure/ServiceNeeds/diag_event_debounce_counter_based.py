"""DiagEventDebounceCounterBased AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 259)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 196)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 757)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diag_event_debounce_algorithm import (
    DiagEventDebounceAlgorithm,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class DiagEventDebounceCounterBased(DiagEventDebounceAlgorithm):
    """AUTOSAR DiagEventDebounceCounterBased."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    counter_based: Optional[Integer]
    counter: Optional[Integer]
    counter_failed: Optional[Integer]
    counter_jump: Optional[Integer]
    counter_jump_up: Optional[Integer]
    counter_passed: Optional[Integer]
    def __init__(self) -> None:
        """Initialize DiagEventDebounceCounterBased."""
        super().__init__()
        self.counter_based: Optional[Integer] = None
        self.counter: Optional[Integer] = None
        self.counter_failed: Optional[Integer] = None
        self.counter_jump: Optional[Integer] = None
        self.counter_jump_up: Optional[Integer] = None
        self.counter_passed: Optional[Integer] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagEventDebounceCounterBased to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagEventDebounceCounterBased, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize counter_based
        if self.counter_based is not None:
            serialized = ARObject._serialize_item(self.counter_based, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-BASED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter
        if self.counter is not None:
            serialized = ARObject._serialize_item(self.counter, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_failed
        if self.counter_failed is not None:
            serialized = ARObject._serialize_item(self.counter_failed, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-FAILED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_jump
        if self.counter_jump is not None:
            serialized = ARObject._serialize_item(self.counter_jump, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-JUMP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_jump_up
        if self.counter_jump_up is not None:
            serialized = ARObject._serialize_item(self.counter_jump_up, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-JUMP-UP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize counter_passed
        if self.counter_passed is not None:
            serialized = ARObject._serialize_item(self.counter_passed, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNTER-PASSED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagEventDebounceCounterBased":
        """Deserialize XML element to DiagEventDebounceCounterBased object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagEventDebounceCounterBased object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagEventDebounceCounterBased, cls).deserialize(element)

        # Parse counter_based
        child = ARObject._find_child_element(element, "COUNTER-BASED")
        if child is not None:
            counter_based_value = child.text
            obj.counter_based = counter_based_value

        # Parse counter
        child = ARObject._find_child_element(element, "COUNTER")
        if child is not None:
            counter_value = child.text
            obj.counter = counter_value

        # Parse counter_failed
        child = ARObject._find_child_element(element, "COUNTER-FAILED")
        if child is not None:
            counter_failed_value = child.text
            obj.counter_failed = counter_failed_value

        # Parse counter_jump
        child = ARObject._find_child_element(element, "COUNTER-JUMP")
        if child is not None:
            counter_jump_value = child.text
            obj.counter_jump = counter_jump_value

        # Parse counter_jump_up
        child = ARObject._find_child_element(element, "COUNTER-JUMP-UP")
        if child is not None:
            counter_jump_up_value = child.text
            obj.counter_jump_up = counter_jump_up_value

        # Parse counter_passed
        child = ARObject._find_child_element(element, "COUNTER-PASSED")
        if child is not None:
            counter_passed_value = child.text
            obj.counter_passed = counter_passed_value

        return obj



class DiagEventDebounceCounterBasedBuilder:
    """Builder for DiagEventDebounceCounterBased."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagEventDebounceCounterBased = DiagEventDebounceCounterBased()

    def build(self) -> DiagEventDebounceCounterBased:
        """Build and return DiagEventDebounceCounterBased object.

        Returns:
            DiagEventDebounceCounterBased instance
        """
        # TODO: Add validation
        return self._obj
