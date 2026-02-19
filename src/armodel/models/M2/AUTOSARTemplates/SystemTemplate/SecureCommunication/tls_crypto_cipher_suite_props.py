"""TlsCryptoCipherSuiteProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 563)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class TlsCryptoCipherSuiteProps(Identifiable):
    """AUTOSAR TlsCryptoCipherSuiteProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_ip_tls_use: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize TlsCryptoCipherSuiteProps."""
        super().__init__()
        self.tcp_ip_tls_use: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize TlsCryptoCipherSuiteProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TlsCryptoCipherSuiteProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_ip_tls_use
        if self.tcp_ip_tls_use is not None:
            serialized = ARObject._serialize_item(self.tcp_ip_tls_use, "Boolean")
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

        # Parse tcp_ip_tls_use
        child = ARObject._find_child_element(element, "TCP-IP-TLS-USE")
        if child is not None:
            tcp_ip_tls_use_value = child.text
            obj.tcp_ip_tls_use = tcp_ip_tls_use_value

        return obj



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
