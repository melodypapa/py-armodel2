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

    functional_request_refs: list[ARRef]
    periodic_response_uudt_refs: list[ARRef]
    physical_request_ref: Optional[ARRef]
    response_ref: Optional[ARRef]
    response_on_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize DiagnosticConnection."""
        super().__init__()
        self.functional_request_refs: list[ARRef] = []
        self.periodic_response_uudt_refs: list[ARRef] = []
        self.physical_request_ref: Optional[ARRef] = None
        self.response_ref: Optional[ARRef] = None
        self.response_on_ref: Optional[ARRef] = None

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

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize functional_request_refs (list to container "FUNCTIONAL-REQUEST-REFS")
        if self.functional_request_refs:
            wrapper = ET.Element("FUNCTIONAL-REQUEST-REFS")
            for item in self.functional_request_refs:
                serialized = ARObject._serialize_item(item, "TpConnectionIdent")
                if serialized is not None:
                    child_elem = ET.Element("FUNCTIONAL-REQUEST-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize periodic_response_uudt_refs (list to container "PERIODIC-RESPONSE-UUDT-REFS")
        if self.periodic_response_uudt_refs:
            wrapper = ET.Element("PERIODIC-RESPONSE-UUDT-REFS")
            for item in self.periodic_response_uudt_refs:
                serialized = ARObject._serialize_item(item, "PduTriggering")
                if serialized is not None:
                    child_elem = ET.Element("PERIODIC-RESPONSE-UUDT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize physical_request_ref
        if self.physical_request_ref is not None:
            serialized = ARObject._serialize_item(self.physical_request_ref, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PHYSICAL-REQUEST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_ref
        if self.response_ref is not None:
            serialized = ARObject._serialize_item(self.response_ref, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize response_on_ref
        if self.response_on_ref is not None:
            serialized = ARObject._serialize_item(self.response_on_ref, "TpConnectionIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESPONSE-ON-REF")
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

        # Parse functional_request_refs (list from container "FUNCTIONAL-REQUEST-REFS")
        obj.functional_request_refs = []
        container = ARObject._find_child_element(element, "FUNCTIONAL-REQUEST-REFS")
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
                    obj.functional_request_refs.append(child_value)

        # Parse periodic_response_uudt_refs (list from container "PERIODIC-RESPONSE-UUDT-REFS")
        obj.periodic_response_uudt_refs = []
        container = ARObject._find_child_element(element, "PERIODIC-RESPONSE-UUDT-REFS")
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
                    obj.periodic_response_uudt_refs.append(child_value)

        # Parse physical_request_ref
        child = ARObject._find_child_element(element, "PHYSICAL-REQUEST-REF")
        if child is not None:
            physical_request_ref_value = ARRef.deserialize(child)
            obj.physical_request_ref = physical_request_ref_value

        # Parse response_ref
        child = ARObject._find_child_element(element, "RESPONSE-REF")
        if child is not None:
            response_ref_value = ARRef.deserialize(child)
            obj.response_ref = response_ref_value

        # Parse response_on_ref
        child = ARObject._find_child_element(element, "RESPONSE-ON-REF")
        if child is not None:
            response_on_ref_value = ARRef.deserialize(child)
            obj.response_on_ref = response_on_ref_value

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
