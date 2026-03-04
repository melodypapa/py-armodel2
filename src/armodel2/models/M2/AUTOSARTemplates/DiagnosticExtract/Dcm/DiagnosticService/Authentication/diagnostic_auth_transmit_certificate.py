"""DiagnosticAuthTransmitCertificate AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 100)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_Authentication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import (
    DiagnosticAuthentication,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.Authentication.diagnostic_authentication import DiagnosticAuthenticationBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DiagnosticAuthTransmitCertificate(DiagnosticAuthentication):
    """AUTOSAR DiagnosticAuthTransmitCertificate."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DIAGNOSTIC-AUTH-TRANSMIT-CERTIFICATE"


    certificates: list[Any]
    _DESERIALIZE_DISPATCH = {
        "CERTIFICATES": lambda obj, elem: obj.certificates.append(SerializationHelper.deserialize_by_tag(elem, "any (DiagnosticAuthTransmit)")),
    }


    def __init__(self) -> None:
        """Initialize DiagnosticAuthTransmitCertificate."""
        super().__init__()
        self.certificates: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticAuthTransmitCertificate to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticAuthTransmitCertificate, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize certificates (list to container "CERTIFICATES")
        if self.certificates:
            wrapper = ET.Element("CERTIFICATES")
            for item in self.certificates:
                serialized = SerializationHelper.serialize_item(item, "Any")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CERTIFICATES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.certificates.append(SerializationHelper.deserialize_by_tag(item_elem, "any (DiagnosticAuthTransmit)"))

        return obj



class DiagnosticAuthTransmitCertificateBuilder(DiagnosticAuthenticationBuilder):
    """Builder for DiagnosticAuthTransmitCertificate with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DiagnosticAuthTransmitCertificate = DiagnosticAuthTransmitCertificate()


    def with_certificates(self, items: list[any (DiagnosticAuthTransmit)]) -> "DiagnosticAuthTransmitCertificateBuilder":
        """Set certificates list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.certificates = list(items) if items else []
        return self


    def add_certificate(self, item: any (DiagnosticAuthTransmit)) -> "DiagnosticAuthTransmitCertificateBuilder":
        """Add a single item to certificates list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.certificates.append(item)
        return self

    def clear_certificates(self) -> "DiagnosticAuthTransmitCertificateBuilder":
        """Clear all items from certificates list.

        Returns:
            self for method chaining
        """
        self._obj.certificates = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "certificate",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DiagnosticAuthTransmitCertificate:
        """Build and return the DiagnosticAuthTransmitCertificate instance with validation."""
        self._validate_instance()
        return self._obj