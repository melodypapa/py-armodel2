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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    authentication_ref: Optional[ARRef]
    crypto_service_key_ref: Optional[ARRef]
    crypto_service_queue_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SecOcCryptoServiceMapping."""
        super().__init__()
        self.authentication_ref: Optional[ARRef] = None
        self.crypto_service_key_ref: Optional[ARRef] = None
        self.crypto_service_queue_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SecOcCryptoServiceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SecOcCryptoServiceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize authentication_ref
        if self.authentication_ref is not None:
            serialized = SerializationHelper.serialize_item(self.authentication_ref, "CryptoServicePrimitive")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTHENTICATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_service_key_ref
        if self.crypto_service_key_ref is not None:
            serialized = SerializationHelper.serialize_item(self.crypto_service_key_ref, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-SERVICE-KEY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_service_queue_ref
        if self.crypto_service_queue_ref is not None:
            serialized = SerializationHelper.serialize_item(self.crypto_service_queue_ref, "CryptoServiceQueue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-SERVICE-QUEUE-REF")
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

        # Parse authentication_ref
        child = SerializationHelper.find_child_element(element, "AUTHENTICATION-REF")
        if child is not None:
            authentication_ref_value = ARRef.deserialize(child)
            obj.authentication_ref = authentication_ref_value

        # Parse crypto_service_key_ref
        child = SerializationHelper.find_child_element(element, "CRYPTO-SERVICE-KEY-REF")
        if child is not None:
            crypto_service_key_ref_value = ARRef.deserialize(child)
            obj.crypto_service_key_ref = crypto_service_key_ref_value

        # Parse crypto_service_queue_ref
        child = SerializationHelper.find_child_element(element, "CRYPTO-SERVICE-QUEUE-REF")
        if child is not None:
            crypto_service_queue_ref_value = ARRef.deserialize(child)
            obj.crypto_service_queue_ref = crypto_service_queue_ref_value

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
