"""DiagnosticCommunicationManagerNeeds AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 248)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 779)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds.diagnostic_capability_element import (
    DiagnosticCapabilityElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DiagnosticCommunicationManagerNeeds(DiagnosticCapabilityElement):
    """AUTOSAR DiagnosticCommunicationManagerNeeds."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    service_request: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticCommunicationManagerNeeds."""
        super().__init__()
        self.service_request: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticCommunicationManagerNeeds to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticCommunicationManagerNeeds, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize service_request
        if self.service_request is not None:
            serialized = SerializationHelper.serialize_item(self.service_request, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-REQUEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticCommunicationManagerNeeds":
        """Deserialize XML element to DiagnosticCommunicationManagerNeeds object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticCommunicationManagerNeeds object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticCommunicationManagerNeeds, cls).deserialize(element)

        # Parse service_request
        child = SerializationHelper.find_child_element(element, "SERVICE-REQUEST")
        if child is not None:
            service_request_value = child.text
            obj.service_request = service_request_value

        return obj



class DiagnosticCommunicationManagerNeedsBuilder:
    """Builder for DiagnosticCommunicationManagerNeeds."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticCommunicationManagerNeeds = DiagnosticCommunicationManagerNeeds()

    def build(self) -> DiagnosticCommunicationManagerNeeds:
        """Build and return DiagnosticCommunicationManagerNeeds object.

        Returns:
            DiagnosticCommunicationManagerNeeds instance
        """
        # TODO: Add validation
        return self._obj
