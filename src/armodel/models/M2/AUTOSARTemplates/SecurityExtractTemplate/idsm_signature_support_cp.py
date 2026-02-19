"""IdsmSignatureSupportCp AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_primitive import (
    CryptoServicePrimitive,
)


class IdsmSignatureSupportCp(ARObject):
    """AUTOSAR IdsmSignatureSupportCp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    authentication: Optional[CryptoServicePrimitive]
    crypto_service_key: Optional[CryptoServiceKey]
    def __init__(self) -> None:
        """Initialize IdsmSignatureSupportCp."""
        super().__init__()
        self.authentication: Optional[CryptoServicePrimitive] = None
        self.crypto_service_key: Optional[CryptoServiceKey] = None
    def serialize(self) -> ET.Element:
        """Serialize IdsmSignatureSupportCp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmSignatureSupportCp":
        """Deserialize XML element to IdsmSignatureSupportCp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmSignatureSupportCp object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

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

        return obj



class IdsmSignatureSupportCpBuilder:
    """Builder for IdsmSignatureSupportCp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmSignatureSupportCp = IdsmSignatureSupportCp()

    def build(self) -> IdsmSignatureSupportCp:
        """Build and return IdsmSignatureSupportCp object.

        Returns:
            IdsmSignatureSupportCp instance
        """
        # TODO: Add validation
        return self._obj
