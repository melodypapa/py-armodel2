"""TlsCryptoServiceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 559)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_mapping import (
    CryptoServiceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.tls_crypto_cipher_suite import (
    TlsCryptoCipherSuite,
)


class TlsCryptoServiceMapping(CryptoServiceMapping):
    """AUTOSAR TlsCryptoServiceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    key_exchange_refs: list[ARRef]
    tls_cipher_suites: list[TlsCryptoCipherSuite]
    use_client: Optional[Boolean]
    use_security: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize TlsCryptoServiceMapping."""
        super().__init__()
        self.key_exchange_refs: list[ARRef] = []
        self.tls_cipher_suites: list[TlsCryptoCipherSuite] = []
        self.use_client: Optional[Boolean] = None
        self.use_security: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize TlsCryptoServiceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TlsCryptoServiceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize key_exchange_refs (list to container "KEY-EXCHANGE-REFS")
        if self.key_exchange_refs:
            wrapper = ET.Element("KEY-EXCHANGE-REFS")
            for item in self.key_exchange_refs:
                serialized = ARObject._serialize_item(item, "CryptoServicePrimitive")
                if serialized is not None:
                    child_elem = ET.Element("KEY-EXCHANGE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tls_cipher_suites (list to container "TLS-CIPHER-SUITES")
        if self.tls_cipher_suites:
            wrapper = ET.Element("TLS-CIPHER-SUITES")
            for item in self.tls_cipher_suites:
                serialized = ARObject._serialize_item(item, "TlsCryptoCipherSuite")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize use_client
        if self.use_client is not None:
            serialized = ARObject._serialize_item(self.use_client, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-CLIENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_security
        if self.use_security is not None:
            serialized = ARObject._serialize_item(self.use_security, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-SECURITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsCryptoServiceMapping":
        """Deserialize XML element to TlsCryptoServiceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlsCryptoServiceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TlsCryptoServiceMapping, cls).deserialize(element)

        # Parse key_exchange_refs (list from container "KEY-EXCHANGE-REFS")
        obj.key_exchange_refs = []
        container = ARObject._find_child_element(element, "KEY-EXCHANGE-REFS")
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
                    obj.key_exchange_refs.append(child_value)

        # Parse tls_cipher_suites (list from container "TLS-CIPHER-SUITES")
        obj.tls_cipher_suites = []
        container = ARObject._find_child_element(element, "TLS-CIPHER-SUITES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tls_cipher_suites.append(child_value)

        # Parse use_client
        child = ARObject._find_child_element(element, "USE-CLIENT")
        if child is not None:
            use_client_value = child.text
            obj.use_client = use_client_value

        # Parse use_security
        child = ARObject._find_child_element(element, "USE-SECURITY")
        if child is not None:
            use_security_value = child.text
            obj.use_security = use_security_value

        return obj



class TlsCryptoServiceMappingBuilder:
    """Builder for TlsCryptoServiceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlsCryptoServiceMapping = TlsCryptoServiceMapping()

    def build(self) -> TlsCryptoServiceMapping:
        """Build and return TlsCryptoServiceMapping object.

        Returns:
            TlsCryptoServiceMapping instance
        """
        # TODO: Add validation
        return self._obj
