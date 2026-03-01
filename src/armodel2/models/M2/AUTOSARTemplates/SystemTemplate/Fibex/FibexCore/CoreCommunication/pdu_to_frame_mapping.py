"""PduToFrameMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 346)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ByteOrderEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PduToFrameMapping(Identifiable):
    """AUTOSAR PduToFrameMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PDU-TO-FRAME-MAPPING"


    packing_byte_order: Optional[ByteOrderEnum]
    pdu_ref: Optional[ARRef]
    start_position: Optional[Integer]
    update_indication_bit_position: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "PACKING-BYTE-ORDER": lambda obj, elem: setattr(obj, "packing_byte_order", ByteOrderEnum.deserialize(elem)),
        "PDU-REF": ("_POLYMORPHIC", "pdu_ref", ["GeneralPurposePdu", "IPdu", "NmPdu", "UserDefinedPdu"]),
        "START-POSITION": lambda obj, elem: setattr(obj, "start_position", SerializationHelper.deserialize_by_tag(elem, "Integer")),
        "UPDATE-INDICATION-BIT-POSITION": lambda obj, elem: setattr(obj, "update_indication_bit_position", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize PduToFrameMapping."""
        super().__init__()
        self.packing_byte_order: Optional[ByteOrderEnum] = None
        self.pdu_ref: Optional[ARRef] = None
        self.start_position: Optional[Integer] = None
        self.update_indication_bit_position: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize PduToFrameMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PduToFrameMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize packing_byte_order
        if self.packing_byte_order is not None:
            serialized = SerializationHelper.serialize_item(self.packing_byte_order, "ByteOrderEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PACKING-BYTE-ORDER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_ref
        if self.pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_ref, "Pdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize start_position
        if self.start_position is not None:
            serialized = SerializationHelper.serialize_item(self.start_position, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("START-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize update_indication_bit_position
        if self.update_indication_bit_position is not None:
            serialized = SerializationHelper.serialize_item(self.update_indication_bit_position, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPDATE-INDICATION-BIT-POSITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PduToFrameMapping":
        """Deserialize XML element to PduToFrameMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PduToFrameMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PduToFrameMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PACKING-BYTE-ORDER":
                setattr(obj, "packing_byte_order", ByteOrderEnum.deserialize(child))
            elif tag == "PDU-REF":
                setattr(obj, "pdu_ref", ARRef.deserialize(child))
            elif tag == "START-POSITION":
                setattr(obj, "start_position", SerializationHelper.deserialize_by_tag(child, "Integer"))
            elif tag == "UPDATE-INDICATION-BIT-POSITION":
                setattr(obj, "update_indication_bit_position", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class PduToFrameMappingBuilder(BuilderBase):
    """Builder for PduToFrameMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PduToFrameMapping = PduToFrameMapping()


    def with_packing_byte_order(self, value: Optional[ByteOrderEnum]) -> "PduToFrameMappingBuilder":
        """Set packing_byte_order attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.packing_byte_order = value
        return self

    def with_pdu(self, value: Optional[Pdu]) -> "PduToFrameMappingBuilder":
        """Set pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdu = value
        return self

    def with_start_position(self, value: Optional[Integer]) -> "PduToFrameMappingBuilder":
        """Set start_position attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.start_position = value
        return self

    def with_update_indication_bit_position(self, value: Optional[Integer]) -> "PduToFrameMappingBuilder":
        """Set update_indication_bit_position attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.update_indication_bit_position = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> PduToFrameMapping:
        """Build and return the PduToFrameMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj