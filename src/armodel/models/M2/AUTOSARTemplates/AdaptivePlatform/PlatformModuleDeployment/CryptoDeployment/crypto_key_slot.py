"""CryptoKeySlot AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_CryptoDeployment.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    String,
)


class CryptoKeySlot(Identifiable):
    """AUTOSAR CryptoKeySlot."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allocate_shadow_copy: Optional[Boolean]
    crypto_alg_id: Optional[String]
    crypto_object_type: Optional[CryptoObjectTypeEnum]
    key_slot_allowed_modification: Optional[CryptoKeySlotAllowedModification]
    key_slot_content_allowed_usages: list[CryptoKeySlotContentAllowedUsage]
    slot_capacity: Optional[PositiveInteger]
    slot_type: Optional[CryptoKeySlotTypeEnum]
    def __init__(self) -> None:
        """Initialize CryptoKeySlot."""
        super().__init__()
        self.allocate_shadow_copy: Optional[Boolean] = None
        self.crypto_alg_id: Optional[String] = None
        self.crypto_object_type: Optional[CryptoObjectTypeEnum] = None
        self.key_slot_allowed_modification: Optional[CryptoKeySlotAllowedModification] = None
        self.key_slot_content_allowed_usages: list[CryptoKeySlotContentAllowedUsage] = []
        self.slot_capacity: Optional[PositiveInteger] = None
        self.slot_type: Optional[CryptoKeySlotTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize CryptoKeySlot to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CryptoKeySlot, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allocate_shadow_copy
        if self.allocate_shadow_copy is not None:
            serialized = ARObject._serialize_item(self.allocate_shadow_copy, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALLOCATE-SHADOW-COPY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_alg_id
        if self.crypto_alg_id is not None:
            serialized = ARObject._serialize_item(self.crypto_alg_id, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-ALG-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize crypto_object_type
        if self.crypto_object_type is not None:
            serialized = ARObject._serialize_item(self.crypto_object_type, "CryptoObjectTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CRYPTO-OBJECT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_slot_allowed_modification
        if self.key_slot_allowed_modification is not None:
            serialized = ARObject._serialize_item(self.key_slot_allowed_modification, "CryptoKeySlotAllowedModification")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SLOT-ALLOWED-MODIFICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_slot_content_allowed_usages (list to container "KEY-SLOT-CONTENT-ALLOWED-USAGES")
        if self.key_slot_content_allowed_usages:
            wrapper = ET.Element("KEY-SLOT-CONTENT-ALLOWED-USAGES")
            for item in self.key_slot_content_allowed_usages:
                serialized = ARObject._serialize_item(item, "CryptoKeySlotContentAllowedUsage")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize slot_capacity
        if self.slot_capacity is not None:
            serialized = ARObject._serialize_item(self.slot_capacity, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLOT-CAPACITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize slot_type
        if self.slot_type is not None:
            serialized = ARObject._serialize_item(self.slot_type, "CryptoKeySlotTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SLOT-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CryptoKeySlot":
        """Deserialize XML element to CryptoKeySlot object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CryptoKeySlot object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CryptoKeySlot, cls).deserialize(element)

        # Parse allocate_shadow_copy
        child = ARObject._find_child_element(element, "ALLOCATE-SHADOW-COPY")
        if child is not None:
            allocate_shadow_copy_value = child.text
            obj.allocate_shadow_copy = allocate_shadow_copy_value

        # Parse crypto_alg_id
        child = ARObject._find_child_element(element, "CRYPTO-ALG-ID")
        if child is not None:
            crypto_alg_id_value = child.text
            obj.crypto_alg_id = crypto_alg_id_value

        # Parse crypto_object_type
        child = ARObject._find_child_element(element, "CRYPTO-OBJECT-TYPE")
        if child is not None:
            crypto_object_type_value = ARObject._deserialize_by_tag(child, "CryptoObjectTypeEnum")
            obj.crypto_object_type = crypto_object_type_value

        # Parse key_slot_allowed_modification
        child = ARObject._find_child_element(element, "KEY-SLOT-ALLOWED-MODIFICATION")
        if child is not None:
            key_slot_allowed_modification_value = ARObject._deserialize_by_tag(child, "CryptoKeySlotAllowedModification")
            obj.key_slot_allowed_modification = key_slot_allowed_modification_value

        # Parse key_slot_content_allowed_usages (list from container "KEY-SLOT-CONTENT-ALLOWED-USAGES")
        obj.key_slot_content_allowed_usages = []
        container = ARObject._find_child_element(element, "KEY-SLOT-CONTENT-ALLOWED-USAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.key_slot_content_allowed_usages.append(child_value)

        # Parse slot_capacity
        child = ARObject._find_child_element(element, "SLOT-CAPACITY")
        if child is not None:
            slot_capacity_value = child.text
            obj.slot_capacity = slot_capacity_value

        # Parse slot_type
        child = ARObject._find_child_element(element, "SLOT-TYPE")
        if child is not None:
            slot_type_value = ARObject._deserialize_by_tag(child, "CryptoKeySlotTypeEnum")
            obj.slot_type = slot_type_value

        return obj



class CryptoKeySlotBuilder:
    """Builder for CryptoKeySlot."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CryptoKeySlot = CryptoKeySlot()

    def build(self) -> CryptoKeySlot:
        """Build and return CryptoKeySlot object.

        Returns:
            CryptoKeySlot instance
        """
        # TODO: Add validation
        return self._obj
