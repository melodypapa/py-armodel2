"""DiagnosticAuthTransmitCertificateMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 242)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticAuthTransmitCertificateMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticAuthTransmitCertificateMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crypto_service_refs: list[Any]
    service_instance_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificateMapping."""
        super().__init__()
        self.crypto_service_refs: list[Any] = []
        self.service_instance_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAuthTransmitCertificateMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAuthTransmitCertificateMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize crypto_service_refs (list to container "CRYPTO-SERVICE-REFS")
        if self.crypto_service_refs:
            wrapper = ET.Element("CRYPTO-SERVICE-REFS")
            for item in self.crypto_service_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("CRYPTO-SERVICE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_instance_ref
        if self.service_instance_ref is not None:
            serialized = ARObject._serialize_item(self.service_instance_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthTransmitCertificateMapping":
        """Deserialize XML element to DiagnosticAuthTransmitCertificateMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthTransmitCertificateMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAuthTransmitCertificateMapping, cls).deserialize(element)

        # Parse crypto_service_refs (list from container "CRYPTO-SERVICE-REFS")
        obj.crypto_service_refs = []
        container = ARObject._find_child_element(element, "CRYPTO-SERVICE-REFS")
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
                    obj.crypto_service_refs.append(child_value)

        # Parse service_instance_ref
        child = ARObject._find_child_element(element, "SERVICE-INSTANCE-REF")
        if child is not None:
            service_instance_ref_value = ARRef.deserialize(child)
            obj.service_instance_ref = service_instance_ref_value

        return obj



class DiagnosticAuthTransmitCertificateMappingBuilder:
    """Builder for DiagnosticAuthTransmitCertificateMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthTransmitCertificateMapping = DiagnosticAuthTransmitCertificateMapping()

    def build(self) -> DiagnosticAuthTransmitCertificateMapping:
        """Build and return DiagnosticAuthTransmitCertificateMapping object.

        Returns:
            DiagnosticAuthTransmitCertificateMapping instance
        """
        # TODO: Add validation
        return self._obj
