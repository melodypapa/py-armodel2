"""DiagnosticOperationCyclePortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 250)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticOperationCyclePortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticOperationCyclePortMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    operation_cycle_ref: Optional[Any]
    swc_flat_service_ref: Optional[Any]
    swc_service: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticOperationCyclePortMapping."""
        super().__init__()
        self.operation_cycle_ref: Optional[Any] = None
        self.swc_flat_service_ref: Optional[Any] = None
        self.swc_service: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticOperationCyclePortMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticOperationCyclePortMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize operation_cycle_ref
        if self.operation_cycle_ref is not None:
            serialized = ARObject._serialize_item(self.operation_cycle_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("OPERATION-CYCLE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_flat_service_ref
        if self.swc_flat_service_ref is not None:
            serialized = ARObject._serialize_item(self.swc_flat_service_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-FLAT-SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_service
        if self.swc_service is not None:
            serialized = ARObject._serialize_item(self.swc_service, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticOperationCyclePortMapping":
        """Deserialize XML element to DiagnosticOperationCyclePortMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticOperationCyclePortMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticOperationCyclePortMapping, cls).deserialize(element)

        # Parse operation_cycle_ref
        child = ARObject._find_child_element(element, "OPERATION-CYCLE-REF")
        if child is not None:
            operation_cycle_ref_value = ARRef.deserialize(child)
            obj.operation_cycle_ref = operation_cycle_ref_value

        # Parse swc_flat_service_ref
        child = ARObject._find_child_element(element, "SWC-FLAT-SERVICE-REF")
        if child is not None:
            swc_flat_service_ref_value = ARRef.deserialize(child)
            obj.swc_flat_service_ref = swc_flat_service_ref_value

        # Parse swc_service
        child = ARObject._find_child_element(element, "SWC-SERVICE")
        if child is not None:
            swc_service_value = child.text
            obj.swc_service = swc_service_value

        return obj



class DiagnosticOperationCyclePortMappingBuilder:
    """Builder for DiagnosticOperationCyclePortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticOperationCyclePortMapping = DiagnosticOperationCyclePortMapping()

    def build(self) -> DiagnosticOperationCyclePortMapping:
        """Build and return DiagnosticOperationCyclePortMapping object.

        Returns:
            DiagnosticOperationCyclePortMapping instance
        """
        # TODO: Add validation
        return self._obj
