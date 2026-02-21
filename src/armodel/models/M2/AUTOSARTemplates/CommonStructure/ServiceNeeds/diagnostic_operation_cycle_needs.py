"""DiagnosticOperationCycleNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 761)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticOperationCycleNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticOperationCycleNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation_cycle: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticOperationCycleNeeds."""
        super().__init__()
        self.operation_cycle: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticOperationCycleNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticOperationCycleNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operation_cycle
        if self.operation_cycle is not None:
            serialized = SerializationHelper.serialize_item(self.operation_cycle, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION-CYCLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticOperationCycleNeeds":
        """Deserialize XML element to DiagnosticOperationCycleNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticOperationCycleNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticOperationCycleNeeds, cls).deserialize(element)

        # Parse operation_cycle
        child = SerializationHelper.find_child_element(element, "OPERATION-CYCLE")
        if child is not None:
            operation_cycle_value = child.text
            obj.operation_cycle = operation_cycle_value

        return obj



class DiagnosticOperationCycleNeedsBuilder:
    """Builder for DiagnosticOperationCycleNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCycleNeeds = DiagnosticOperationCycleNeeds()

    def build(self) -> DiagnosticOperationCycleNeeds:
        """Build and return DiagnosticOperationCycleNeeds object.

        Returns:
            DiagnosticOperationCycleNeeds instance
        """
        # TODO: Add validation
        return self._obj
