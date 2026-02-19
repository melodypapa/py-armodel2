"""DiagnosticProtocol AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 58)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.diagnostic_connection import (
    DiagnosticConnection,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution.diagnostic_service_table import (
    DiagnosticServiceTable,
)


class DiagnosticProtocol(DiagnosticCommonElement):
    """AUTOSAR DiagnosticProtocol."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostics: list[DiagnosticConnection]
    priority: Optional[PositiveInteger]
    protocol_kind: Optional[NameToken]
    send_resp_pend: Optional[Boolean]
    service_table: Optional[DiagnosticServiceTable]
    def __init__(self) -> None:
        """Initialize DiagnosticProtocol."""
        super().__init__()
        self.diagnostics: list[DiagnosticConnection] = []
        self.priority: Optional[PositiveInteger] = None
        self.protocol_kind: Optional[NameToken] = None
        self.send_resp_pend: Optional[Boolean] = None
        self.service_table: Optional[DiagnosticServiceTable] = None
    def serialize(self) -> ET.Element:
        """Serialize DiagnosticProtocol to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticProtocol, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostics (list to container "DIAGNOSTICS")
        if self.diagnostics:
            wrapper = ET.Element("DIAGNOSTICS")
            for item in self.diagnostics:
                serialized = ARObject._serialize_item(item, "DiagnosticConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize priority
        if self.priority is not None:
            serialized = ARObject._serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize protocol_kind
        if self.protocol_kind is not None:
            serialized = ARObject._serialize_item(self.protocol_kind, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROTOCOL-KIND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize send_resp_pend
        if self.send_resp_pend is not None:
            serialized = ARObject._serialize_item(self.send_resp_pend, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SEND-RESP-PEND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_table
        if self.service_table is not None:
            serialized = ARObject._serialize_item(self.service_table, "DiagnosticServiceTable")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-TABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticProtocol":
        """Deserialize XML element to DiagnosticProtocol object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticProtocol object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticProtocol, cls).deserialize(element)

        # Parse diagnostics (list from container "DIAGNOSTICS")
        obj.diagnostics = []
        container = ARObject._find_child_element(element, "DIAGNOSTICS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.diagnostics.append(child_value)

        # Parse priority
        child = ARObject._find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse protocol_kind
        child = ARObject._find_child_element(element, "PROTOCOL-KIND")
        if child is not None:
            protocol_kind_value = child.text
            obj.protocol_kind = protocol_kind_value

        # Parse send_resp_pend
        child = ARObject._find_child_element(element, "SEND-RESP-PEND")
        if child is not None:
            send_resp_pend_value = child.text
            obj.send_resp_pend = send_resp_pend_value

        # Parse service_table
        child = ARObject._find_child_element(element, "SERVICE-TABLE")
        if child is not None:
            service_table_value = ARObject._deserialize_by_tag(child, "DiagnosticServiceTable")
            obj.service_table = service_table_value

        return obj



class DiagnosticProtocolBuilder:
    """Builder for DiagnosticProtocol."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticProtocol = DiagnosticProtocol()

    def build(self) -> DiagnosticProtocol:
        """Build and return DiagnosticProtocol object.

        Returns:
            DiagnosticProtocol instance
        """
        # TODO: Add validation
        return self._obj
