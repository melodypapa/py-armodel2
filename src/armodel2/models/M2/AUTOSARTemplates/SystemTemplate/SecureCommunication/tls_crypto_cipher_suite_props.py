"""TlsCryptoCipherSuiteProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 563)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class TlsCryptoCipherSuiteProps(Identifiable):
    """AUTOSAR TlsCryptoCipherSuiteProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "TLS-CRYPTO-CIPHER-SUITE-PROPS"


    tcp_ip_tls_use: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "TCP-IP-TLS-USE": lambda obj, elem: setattr(obj, "tcp_ip_tls_use", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize TlsCryptoCipherSuiteProps."""
        super().__init__()
        self.tcp_ip_tls_use: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize TlsCryptoCipherSuiteProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TlsCryptoCipherSuiteProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_ip_tls_use
        if self.tcp_ip_tls_use is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_tls_use, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-TLS-USE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsCryptoCipherSuiteProps":
        """Deserialize XML element to TlsCryptoCipherSuiteProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlsCryptoCipherSuiteProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TlsCryptoCipherSuiteProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TCP-IP-TLS-USE":
                setattr(obj, "tcp_ip_tls_use", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class TlsCryptoCipherSuitePropsBuilder(IdentifiableBuilder):
    """Builder for TlsCryptoCipherSuiteProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TlsCryptoCipherSuiteProps = TlsCryptoCipherSuiteProps()


    def with_tcp_ip_tls_use(self, value: Optional[Boolean]) -> "TlsCryptoCipherSuitePropsBuilder":
        """Set tcp_ip_tls_use attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_tls_use = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tcpIpTlsUse",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> TlsCryptoCipherSuiteProps:
        """Build and return the TlsCryptoCipherSuiteProps instance with validation."""
        self._validate_instance()
        return self._obj