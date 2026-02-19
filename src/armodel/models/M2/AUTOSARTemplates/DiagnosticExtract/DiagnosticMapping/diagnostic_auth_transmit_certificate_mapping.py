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


class DiagnosticAuthTransmitCertificateMapping(DiagnosticMapping):
    """AUTOSAR DiagnosticAuthTransmitCertificateMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crypto_services: list[Any]
    service_instance: Optional[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificateMapping."""
        super().__init__()
        self.crypto_services: list[Any] = []
        self.service_instance: Optional[Any] = None
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

        # Parse crypto_services (list from container "CRYPTO-SERVICES")
        obj.crypto_services = []
        container = ARObject._find_child_element(element, "CRYPTO-SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.crypto_services.append(child_value)

        # Parse service_instance
        child = ARObject._find_child_element(element, "SERVICE-INSTANCE")
        if child is not None:
            service_instance_value = child.text
            obj.service_instance = service_instance_value

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
