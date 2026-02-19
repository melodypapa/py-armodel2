"""DiagnosticEventPortMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 249)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_sw_mapping import (
    DiagnosticSwMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class DiagnosticEventPortMapping(DiagnosticSwMapping):
    """AUTOSAR DiagnosticEventPortMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_service: Optional[Any]
    diagnostic_event: Optional[DiagnosticEvent]
    swc_flat_service: Optional[Any]
    swc_service: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticEventPortMapping."""
        super().__init__()
        self.bsw_service: Optional[Any] = None
        self.diagnostic_event: Optional[DiagnosticEvent] = None
        self.swc_flat_service: Optional[Any] = None
        self.swc_service: Optional[Any] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticEventPortMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticEventPortMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_service
        if self.bsw_service is not None:
            serialized = ARObject._serialize_item(self.bsw_service, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-SERVICE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize diagnostic_event
        if self.diagnostic_event is not None:
            serialized = ARObject._serialize_item(self.diagnostic_event, "DiagnosticEvent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIAGNOSTIC-EVENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_flat_service
        if self.swc_flat_service is not None:
            serialized = ARObject._serialize_item(self.swc_flat_service, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-FLAT-SERVICE")
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
    def deserialize(cls, element: ET.Element) -> "DiagnosticEventPortMapping":
        """Deserialize XML element to DiagnosticEventPortMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticEventPortMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticEventPortMapping, cls).deserialize(element)

        # Parse bsw_service
        child = ARObject._find_child_element(element, "BSW-SERVICE")
        if child is not None:
            bsw_service_value = child.text
            obj.bsw_service = bsw_service_value

        # Parse diagnostic_event
        child = ARObject._find_child_element(element, "DIAGNOSTIC-EVENT")
        if child is not None:
            diagnostic_event_value = ARObject._deserialize_by_tag(child, "DiagnosticEvent")
            obj.diagnostic_event = diagnostic_event_value

        # Parse swc_flat_service
        child = ARObject._find_child_element(element, "SWC-FLAT-SERVICE")
        if child is not None:
            swc_flat_service_value = child.text
            obj.swc_flat_service = swc_flat_service_value

        # Parse swc_service
        child = ARObject._find_child_element(element, "SWC-SERVICE")
        if child is not None:
            swc_service_value = child.text
            obj.swc_service = swc_service_value

        return obj



class DiagnosticEventPortMappingBuilder:
    """Builder for DiagnosticEventPortMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticEventPortMapping = DiagnosticEventPortMapping()

    def build(self) -> DiagnosticEventPortMapping:
        """Build and return DiagnosticEventPortMapping object.

        Returns:
            DiagnosticEventPortMapping instance
        """
        # TODO: Add validation
        return self._obj
