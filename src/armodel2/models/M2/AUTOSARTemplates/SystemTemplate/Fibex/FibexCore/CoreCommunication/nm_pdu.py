"""NmPdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 302)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 342)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import (
    Pdu,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu import PduBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_to_i_pdu_mapping import (
    ISignalToIPduMapping,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class NmPdu(Pdu):
    """AUTOSAR NmPdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NM-PDU"


    i_signal_to_i_pdu_refs: list[ARRef]
    nm_data: Optional[Boolean]
    nm_vote_information: Optional[Boolean]
    unused_bit: Optional[Integer]
    _DESERIALIZE_DISPATCH = {
        "I-SIGNAL-TO-I-PDU-REFS": lambda obj, elem: [obj.i_signal_to_i_pdu_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "NM-DATA": lambda obj, elem: setattr(obj, "nm_data", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "NM-VOTE-INFORMATION": lambda obj, elem: setattr(obj, "nm_vote_information", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "UNUSED-BIT": lambda obj, elem: setattr(obj, "unused_bit", SerializationHelper.deserialize_by_tag(elem, "Integer")),
    }


    def __init__(self) -> None:
        """Initialize NmPdu."""
        super().__init__()
        self.i_signal_to_i_pdu_refs: list[ARRef] = []
        self.nm_data: Optional[Boolean] = None
        self.nm_vote_information: Optional[Boolean] = None
        self.unused_bit: Optional[Integer] = None

    def serialize(self) -> ET.Element:
        """Serialize NmPdu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmPdu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_signal_to_i_pdu_refs (list to container "I-SIGNAL-TO-I-PDU-REFS")
        if self.i_signal_to_i_pdu_refs:
            wrapper = ET.Element("I-SIGNAL-TO-I-PDU-REFS")
            for item in self.i_signal_to_i_pdu_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalToIPduMapping")
                if serialized is not None:
                    child_elem = ET.Element("I-SIGNAL-TO-I-PDU-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nm_data
        if self.nm_data is not None:
            serialized = SerializationHelper.serialize_item(self.nm_data, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-DATA")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_vote_information
        if self.nm_vote_information is not None:
            serialized = SerializationHelper.serialize_item(self.nm_vote_information, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-VOTE-INFORMATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize unused_bit
        if self.unused_bit is not None:
            serialized = SerializationHelper.serialize_item(self.unused_bit, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UNUSED-BIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmPdu":
        """Deserialize XML element to NmPdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmPdu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmPdu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "I-SIGNAL-TO-I-PDU-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.i_signal_to_i_pdu_refs.append(ARRef.deserialize(item_elem))
            elif tag == "NM-DATA":
                setattr(obj, "nm_data", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "NM-VOTE-INFORMATION":
                setattr(obj, "nm_vote_information", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "UNUSED-BIT":
                setattr(obj, "unused_bit", SerializationHelper.deserialize_by_tag(child, "Integer"))

        return obj



class NmPduBuilder(PduBuilder):
    """Builder for NmPdu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NmPdu = NmPdu()


    def with_i_signal_to_i_pdus(self, items: list[ISignalToIPduMapping]) -> "NmPduBuilder":
        """Set i_signal_to_i_pdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_signal_to_i_pdus = list(items) if items else []
        return self

    def with_nm_data(self, value: Optional[Boolean]) -> "NmPduBuilder":
        """Set nm_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_data = value
        return self

    def with_nm_vote_information(self, value: Optional[Boolean]) -> "NmPduBuilder":
        """Set nm_vote_information attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_vote_information = value
        return self

    def with_unused_bit(self, value: Optional[Integer]) -> "NmPduBuilder":
        """Set unused_bit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.unused_bit = value
        return self


    def add_i_signal_to_i_pdu(self, item: ISignalToIPduMapping) -> "NmPduBuilder":
        """Add a single item to i_signal_to_i_pdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_signal_to_i_pdus.append(item)
        return self

    def clear_i_signal_to_i_pdus(self) -> "NmPduBuilder":
        """Clear all items from i_signal_to_i_pdus list.

        Returns:
            self for method chaining
        """
        self._obj.i_signal_to_i_pdus = []
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


    def build(self) -> NmPdu:
        """Build and return the NmPdu instance with validation."""
        self._validate_instance()
        pass
        return self._obj