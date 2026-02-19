"""DiagnosticConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 60)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 632)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DiagnosticConnection.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection_ident import (
    TpConnectionIdent,
)


class DiagnosticConnection(ARElement):
    """AUTOSAR DiagnosticConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    functional_requests: list[TpConnectionIdent]
    periodic_response_uudt_refs: list[ARRef]
    physical_request: Optional[TpConnectionIdent]
    response: Optional[TpConnectionIdent]
    response_on: Optional[TpConnectionIdent]
    def __init__(self) -> None:
        """Initialize DiagnosticConnection."""
        super().__init__()
        self.functional_requests: list[TpConnectionIdent] = []
        self.periodic_response_uudt_refs: list[ARRef] = []
        self.physical_request: Optional[TpConnectionIdent] = None
        self.response: Optional[TpConnectionIdent] = None
        self.response_on: Optional[TpConnectionIdent] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize functional_requests (list to container "FUNCTIONAL-REQUESTS")
        if self.functional_requests:
            wrapper = ET.Element("FUNCTIONAL-REQUESTS")
            for item in self.functional_requests:
                serialized = ARObject._serialize_item(item, "TpConnectionIdent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize periodic_response_uudt_refs (list to container "PERIODIC-RESPONSE-UUDTS")
        if self.periodic_response_uudt_refs:
            wrapper = ET.Element("PERIODIC-RESPONSE-UUDTS")
            for item in self.periodic_response_uudt_refs:
                serialized = ARObject._serialize_item(item, "PduTriggering")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_request
        if self.physical_request is not None:
            serialized = ARObject._serialize_item(self.physical_request, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-REQUEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response
        if self.response is not None:
            serialized = ARObject._serialize_item(self.response, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_on
        if self.response_on is not None:
            serialized = ARObject._serialize_item(self.response_on, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-ON")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticConnection":
        """Deserialize XML element to DiagnosticConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticConnection, cls).deserialize(element)

        # Parse functional_requests (list from container "FUNCTIONAL-REQUESTS")
        obj.functional_requests = []
        container = ARObject._find_child_element(element, "FUNCTIONAL-REQUESTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.functional_requests.append(child_value)

        # Parse periodic_response_uudt_refs (list from container "PERIODIC-RESPONSE-UUDTS")
        obj.periodic_response_uudt_refs = []
        container = ARObject._find_child_element(element, "PERIODIC-RESPONSE-UUDTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.periodic_response_uudt_refs.append(child_value)

        # Parse physical_request
        child = ARObject._find_child_element(element, "PHYSICAL-REQUEST")
        if child is not None:
            physical_request_value = ARObject._deserialize_by_tag(child, "TpConnectionIdent")
            obj.physical_request = physical_request_value

        # Parse response
        child = ARObject._find_child_element(element, "RESPONSE")
        if child is not None:
            response_value = ARObject._deserialize_by_tag(child, "TpConnectionIdent")
            obj.response = response_value

        # Parse response_on
        child = ARObject._find_child_element(element, "RESPONSE-ON")
        if child is not None:
            response_on_value = ARObject._deserialize_by_tag(child, "TpConnectionIdent")
            obj.response_on = response_on_value

        return obj



class DiagnosticConnectionBuilder:
    """Builder for DiagnosticConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticConnection = DiagnosticConnection()

    def build(self) -> DiagnosticConnection:
        """Build and return DiagnosticConnection object.

        Returns:
            DiagnosticConnection instance
        """
        # TODO: Add validation
        return self._obj
