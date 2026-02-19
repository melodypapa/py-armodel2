"""IdsmSignatureSupportAp AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SecurityExtractTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.CryptoDeployment.crypto_key_slot import (
    CryptoKeySlot,
)


class IdsmSignatureSupportAp(ARObject):
    """AUTOSAR IdsmSignatureSupportAp."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    crypto_primitive: String
    key_slot: Optional[CryptoKeySlot]
    def __init__(self) -> None:
        """Initialize IdsmSignatureSupportAp."""
        super().__init__()
        self.crypto_primitive: String = None
        self.key_slot: Optional[CryptoKeySlot] = None
    def serialize(self) -> ET.Element:
        """Serialize IdsmSignatureSupportAp to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize crypto_primitive
        if self.crypto_primitive is not None:
            serialized = ARObject._serialize_item(self.crypto_primitive, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-PRIMITIVE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_slot
        if self.key_slot is not None:
            serialized = ARObject._serialize_item(self.key_slot, "CryptoKeySlot")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SLOT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IdsmSignatureSupportAp":
        """Deserialize XML element to IdsmSignatureSupportAp object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IdsmSignatureSupportAp object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse crypto_primitive
        child = ARObject._find_child_element(element, "CRYPTO-PRIMITIVE")
        if child is not None:
            crypto_primitive_value = child.text
            obj.crypto_primitive = crypto_primitive_value

        # Parse key_slot
        child = ARObject._find_child_element(element, "KEY-SLOT")
        if child is not None:
            key_slot_value = ARObject._deserialize_by_tag(child, "CryptoKeySlot")
            obj.key_slot = key_slot_value

        return obj



class IdsmSignatureSupportApBuilder:
    """Builder for IdsmSignatureSupportAp."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IdsmSignatureSupportAp = IdsmSignatureSupportAp()

    def build(self) -> IdsmSignatureSupportAp:
        """Build and return IdsmSignatureSupportAp object.

        Returns:
            IdsmSignatureSupportAp instance
        """
        # TODO: Add validation
        return self._obj
