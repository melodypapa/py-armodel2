"""IdsmSignatureSupportCp AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    authentication_ref: Optional[ARRef]
    crypto_service_key_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize IdsmSignatureSupportCp."""
        super().__init__()
        self.authentication_ref: Optional[ARRef] = None
        self.crypto_service_key_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize IdsmSignatureSupportCp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize authentication_ref
        if self.authentication_ref is not None:
            serialized = ARObject._serialize_item(self.authentication_ref, "CryptoServicePrimitive")
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
            serialized = ARObject._serialize_item(self.crypto_service_key_ref, "CryptoServiceKey")
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

        # Parse authentication_ref
        child = ARObject._find_child_element(element, "AUTHENTICATION-REF")
        if child is not None:
            authentication_ref_value = ARRef.deserialize(child)
            obj.authentication_ref = authentication_ref_value

        # Parse crypto_service_key_ref
        child = ARObject._find_child_element(element, "CRYPTO-SERVICE-KEY-REF")
        if child is not None:
            crypto_service_key_ref_value = ARRef.deserialize(child)
            obj.crypto_service_key_ref = crypto_service_key_ref_value

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
