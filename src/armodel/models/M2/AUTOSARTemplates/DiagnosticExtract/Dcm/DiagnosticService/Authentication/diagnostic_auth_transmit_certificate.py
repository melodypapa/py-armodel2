"""DiagnosticAuthTransmitCertificate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_Authentication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class DiagnosticAuthTransmitCertificate(DiagnosticAuthentication):
    """AUTOSAR DiagnosticAuthTransmitCertificate."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    certificates: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificate."""
        super().__init__()
        self.certificates: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAuthTransmitCertificate to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAuthTransmitCertificate, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize certificates (list to container "CERTIFICATES")
        if self.certificates:
            wrapper = ET.Element("CERTIFICATES")
            for item in self.certificates:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticAuthTransmitCertificate":
        """Deserialize XML element to DiagnosticAuthTransmitCertificate object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticAuthTransmitCertificate object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticAuthTransmitCertificate, cls).deserialize(element)

        # Parse certificates (list from container "CERTIFICATES")
        obj.certificates = []
        container = ARObject._find_child_element(element, "CERTIFICATES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.certificates.append(child_value)

        return obj



class DiagnosticAuthTransmitCertificateBuilder:
    """Builder for DiagnosticAuthTransmitCertificate."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticAuthTransmitCertificate = DiagnosticAuthTransmitCertificate()

    def build(self) -> DiagnosticAuthTransmitCertificate:
        """Build and return DiagnosticAuthTransmitCertificate object.

        Returns:
            DiagnosticAuthTransmitCertificate instance
        """
        # TODO: Add validation
        return self._obj
