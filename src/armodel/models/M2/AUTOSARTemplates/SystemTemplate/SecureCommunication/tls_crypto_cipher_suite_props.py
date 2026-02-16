"""TlsCryptoCipherSuiteProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class TlsCryptoCipherSuiteProps(Identifiable):
    """AUTOSAR TlsCryptoCipherSuiteProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tcp_ip_tls_use", None, True, False, None),  # tcpIpTlsUse
    ]

    def __init__(self) -> None:
        """Initialize TlsCryptoCipherSuiteProps."""
        super().__init__()
        self.tcp_ip_tls_use: Optional[Boolean] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TlsCryptoCipherSuiteProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsCryptoCipherSuiteProps":
        """Create TlsCryptoCipherSuiteProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TlsCryptoCipherSuiteProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TlsCryptoCipherSuiteProps since parent returns ARObject
        return cast("TlsCryptoCipherSuiteProps", obj)


class TlsCryptoCipherSuitePropsBuilder:
    """Builder for TlsCryptoCipherSuiteProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlsCryptoCipherSuiteProps = TlsCryptoCipherSuiteProps()

    def build(self) -> TlsCryptoCipherSuiteProps:
        """Build and return TlsCryptoCipherSuiteProps object.

        Returns:
            TlsCryptoCipherSuiteProps instance
        """
        # TODO: Add validation
        return self._obj
