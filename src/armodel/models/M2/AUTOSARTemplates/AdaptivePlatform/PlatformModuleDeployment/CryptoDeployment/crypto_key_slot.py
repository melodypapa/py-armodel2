"""CryptoKeySlot AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_CryptoDeployment.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
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

    allocate_shadow: Optional[Boolean]
    crypto_alg_id: Optional[String]
    crypto_object_type_enum: Optional[Any]
    key_slot_allowed: Optional[Any]
    key_slot_contents: list[Any]
    slot_capacity: Optional[PositiveInteger]
    slot_type: Optional[Any]
    def __init__(self) -> None:
        """Initialize CryptoKeySlot."""
        super().__init__()
        self.allocate_shadow: Optional[Boolean] = None
        self.crypto_alg_id: Optional[String] = None
        self.crypto_object_type_enum: Optional[Any] = None
        self.key_slot_allowed: Optional[Any] = None
        self.key_slot_contents: list[Any] = []
        self.slot_capacity: Optional[PositiveInteger] = None
        self.slot_type: Optional[Any] = None
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

        # Parse allocate_shadow
        child = ARObject._find_child_element(element, "ALLOCATE-SHADOW")
        if child is not None:
            allocate_shadow_value = child.text
            obj.allocate_shadow = allocate_shadow_value

        # Parse crypto_alg_id
        child = ARObject._find_child_element(element, "CRYPTO-ALG-ID")
        if child is not None:
            crypto_alg_id_value = child.text
            obj.crypto_alg_id = crypto_alg_id_value

        # Parse crypto_object_type_enum
        child = ARObject._find_child_element(element, "CRYPTO-OBJECT-TYPE-ENUM")
        if child is not None:
            crypto_object_type_enum_value = child.text
            obj.crypto_object_type_enum = crypto_object_type_enum_value

        # Parse key_slot_allowed
        child = ARObject._find_child_element(element, "KEY-SLOT-ALLOWED")
        if child is not None:
            key_slot_allowed_value = child.text
            obj.key_slot_allowed = key_slot_allowed_value

        # Parse key_slot_contents (list from container "KEY-SLOT-CONTENTS")
        obj.key_slot_contents = []
        container = ARObject._find_child_element(element, "KEY-SLOT-CONTENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.key_slot_contents.append(child_value)

        # Parse slot_capacity
        child = ARObject._find_child_element(element, "SLOT-CAPACITY")
        if child is not None:
            slot_capacity_value = child.text
            obj.slot_capacity = slot_capacity_value

        # Parse slot_type
        child = ARObject._find_child_element(element, "SLOT-TYPE")
        if child is not None:
            slot_type_value = child.text
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
