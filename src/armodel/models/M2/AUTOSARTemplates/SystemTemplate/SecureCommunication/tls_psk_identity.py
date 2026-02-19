"""TlsPskIdentity AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 563)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.crypto_service_key import (
    CryptoServiceKey,
)


class TlsPskIdentity(ARObject):
    """AUTOSAR TlsPskIdentity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    pre_shared_key: Optional[CryptoServiceKey]
    psk_identity: Optional[String]
    psk_identity_hint: Optional[String]
    def __init__(self) -> None:
        """Initialize TlsPskIdentity."""
        super().__init__()
        self.pre_shared_key: Optional[CryptoServiceKey] = None
        self.psk_identity: Optional[String] = None
        self.psk_identity_hint: Optional[String] = None
    def serialize(self) -> ET.Element:
        """Serialize TlsPskIdentity to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize pre_shared_key
        if self.pre_shared_key is not None:
            serialized = ARObject._serialize_item(self.pre_shared_key, "CryptoServiceKey")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRE-SHARED-KEY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize psk_identity
        if self.psk_identity is not None:
            serialized = ARObject._serialize_item(self.psk_identity, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PSK-IDENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize psk_identity_hint
        if self.psk_identity_hint is not None:
            serialized = ARObject._serialize_item(self.psk_identity_hint, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PSK-IDENTITY-HINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlsPskIdentity":
        """Deserialize XML element to TlsPskIdentity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlsPskIdentity object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse pre_shared_key
        child = ARObject._find_child_element(element, "PRE-SHARED-KEY")
        if child is not None:
            pre_shared_key_value = ARObject._deserialize_by_tag(child, "CryptoServiceKey")
            obj.pre_shared_key = pre_shared_key_value

        # Parse psk_identity
        child = ARObject._find_child_element(element, "PSK-IDENTITY")
        if child is not None:
            psk_identity_value = child.text
            obj.psk_identity = psk_identity_value

        # Parse psk_identity_hint
        child = ARObject._find_child_element(element, "PSK-IDENTITY-HINT")
        if child is not None:
            psk_identity_hint_value = child.text
            obj.psk_identity_hint = psk_identity_hint_value

        return obj



class TlsPskIdentityBuilder:
    """Builder for TlsPskIdentity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TlsPskIdentity = TlsPskIdentity()

    def build(self) -> TlsPskIdentity:
        """Build and return TlsPskIdentity object.

        Returns:
            TlsPskIdentity instance
        """
        # TODO: Add validation
        return self._obj
