"""DiagnosticServiceTable AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 59)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_common_element import (
    DiagnosticCommonElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.diagnostic_connection import (
    DiagnosticConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)


class DiagnosticServiceTable(DiagnosticCommonElement):
    """AUTOSAR DiagnosticServiceTable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    diagnostic_refs: list[ARRef]
    ecu_instance_ref: Optional[ARRef]
    protocol_kind: Optional[NameToken]
    service_instance_refs: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticServiceTable."""
        super().__init__()
        self.diagnostic_refs: list[ARRef] = []
        self.ecu_instance_ref: Optional[ARRef] = None
        self.protocol_kind: Optional[NameToken] = None
        self.service_instance_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticServiceTable to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticServiceTable, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize diagnostic_refs (list to container "DIAGNOSTIC-REFS")
        if self.diagnostic_refs:
            wrapper = ET.Element("DIAGNOSTIC-REFS")
            for item in self.diagnostic_refs:
                serialized = ARObject._serialize_item(item, "DiagnosticConnection")
                if serialized is not None:
                    child_elem = ET.Element("DIAGNOSTIC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = ARObject._serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
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

        # Serialize service_instance_refs (list to container "SERVICE-INSTANCE-REFS")
        if self.service_instance_refs:
            wrapper = ET.Element("SERVICE-INSTANCE-REFS")
            for item in self.service_instance_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("SERVICE-INSTANCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticServiceTable":
        """Deserialize XML element to DiagnosticServiceTable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticServiceTable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticServiceTable, cls).deserialize(element)

        # Parse diagnostic_refs (list from container "DIAGNOSTIC-REFS")
        obj.diagnostic_refs = []
        container = ARObject._find_child_element(element, "DIAGNOSTIC-REFS")
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
                    obj.diagnostic_refs.append(child_value)

        # Parse ecu_instance_ref
        child = ARObject._find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        # Parse protocol_kind
        child = ARObject._find_child_element(element, "PROTOCOL-KIND")
        if child is not None:
            protocol_kind_value = child.text
            obj.protocol_kind = protocol_kind_value

        # Parse service_instance_refs (list from container "SERVICE-INSTANCE-REFS")
        obj.service_instance_refs = []
        container = ARObject._find_child_element(element, "SERVICE-INSTANCE-REFS")
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
                    obj.service_instance_refs.append(child_value)

        return obj



class DiagnosticServiceTableBuilder:
    """Builder for DiagnosticServiceTable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticServiceTable = DiagnosticServiceTable()

    def build(self) -> DiagnosticServiceTable:
        """Build and return DiagnosticServiceTable object.

        Returns:
            DiagnosticServiceTable instance
        """
        # TODO: Add validation
        return self._obj
