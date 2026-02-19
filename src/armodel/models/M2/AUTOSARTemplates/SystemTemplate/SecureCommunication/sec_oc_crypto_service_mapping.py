"""SecOcCryptoServiceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 375)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_mapping import (
    CryptoServiceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_queue import (
    CryptoServiceQueue,
)


class SecOcCryptoServiceMapping(CryptoServiceMapping):
    """AUTOSAR SecOcCryptoServiceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication: Optional[CryptoServicePrimitive]
    crypto_service_key: Optional[CryptoServiceKey]
    crypto_service_queue: Optional[CryptoServiceQueue]
    def __init__(self) -> None:
        """Initialize SecOcCryptoServiceMapping."""
        super().__init__()
        self.authentication: Optional[CryptoServicePrimitive] = None
        self.crypto_service_key: Optional[CryptoServiceKey] = None
        self.crypto_service_queue: Optional[CryptoServiceQueue] = None

    def serialize(self) -> ET.Element:
        """Serialize SecOcCryptoServiceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecOcCryptoServiceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentication
        if self.authentication is not None:
            serialized = ARObject._serialize_item(self.authentication, "CryptoServicePrimitive")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTHENTICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_service_key
        if self.crypto_service_key is not None:
            serialized = ARObject._serialize_item(self.crypto_service_key, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-SERVICE-KEY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_service_queue
        if self.crypto_service_queue is not None:
            serialized = ARObject._serialize_item(self.crypto_service_queue, "CryptoServiceQueue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-SERVICE-QUEUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SecOcCryptoServiceMapping":
        """Deserialize XML element to SecOcCryptoServiceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SecOcCryptoServiceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SecOcCryptoServiceMapping, cls).deserialize(element)

        # Parse authentication
        child = ARObject._find_child_element(element, "AUTHENTICATION")
        if child is not None:
            authentication_value = ARObject._deserialize_by_tag(child, "CryptoServicePrimitive")
            obj.authentication = authentication_value

        # Parse crypto_service_key
        child = ARObject._find_child_element(element, "CRYPTO-SERVICE-KEY")
        if child is not None:
            crypto_service_key_value = ARObject._deserialize_by_tag(child, "CryptoServiceKey")
            obj.crypto_service_key = crypto_service_key_value

        # Parse crypto_service_queue
        child = ARObject._find_child_element(element, "CRYPTO-SERVICE-QUEUE")
        if child is not None:
            crypto_service_queue_value = ARObject._deserialize_by_tag(child, "CryptoServiceQueue")
            obj.crypto_service_queue = crypto_service_queue_value

        return obj



class SecOcCryptoServiceMappingBuilder:
    """Builder for SecOcCryptoServiceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SecOcCryptoServiceMapping = SecOcCryptoServiceMapping()

    def build(self) -> SecOcCryptoServiceMapping:
        """Build and return SecOcCryptoServiceMapping object.

        Returns:
            SecOcCryptoServiceMapping instance
        """
        # TODO: Add validation
        return self._obj
