"""MacSecLocalKayProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import (
    MacSecRoleEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_global_kay_props import (
    MacSecGlobalKayProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.mac_sec_kay_participant import (
    MacSecKayParticipant,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class MacSecLocalKayProps(ARObject):
    """AUTOSAR MacSecLocalKayProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "MAC-SEC-LOCAL-KAY-PROPS"


    destination_mac: Optional[MacAddressString]
    global_kay_props_ref: Optional[ARRef]
    key_server: Optional[PositiveInteger]
    mka_participant_refs: list[ARRef]
    role: Optional[MacSecRoleEnum]
    source_mac: Optional[MacAddressString]
    _DESERIALIZE_DISPATCH = {
        "DESTINATION-MAC": lambda obj, elem: setattr(obj, "destination_mac", SerializationHelper.deserialize_by_tag(elem, "MacAddressString")),
        "GLOBAL-KAY-PROPS-REF": lambda obj, elem: setattr(obj, "global_kay_props_ref", ARRef.deserialize(elem)),
        "KEY-SERVER": lambda obj, elem: setattr(obj, "key_server", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MKA-PARTICIPANT-REFS": lambda obj, elem: obj.mka_participant_refs.append(ARRef.deserialize(elem)),
        "ROLE": lambda obj, elem: setattr(obj, "role", MacSecRoleEnum.deserialize(elem)),
        "SOURCE-MAC": lambda obj, elem: setattr(obj, "source_mac", SerializationHelper.deserialize_by_tag(elem, "MacAddressString")),
    }


    def __init__(self) -> None:
        """Initialize MacSecLocalKayProps."""
        super().__init__()
        self.destination_mac: Optional[MacAddressString] = None
        self.global_kay_props_ref: Optional[ARRef] = None
        self.key_server: Optional[PositiveInteger] = None
        self.mka_participant_refs: list[ARRef] = []
        self.role: Optional[MacSecRoleEnum] = None
        self.source_mac: Optional[MacAddressString] = None

    def serialize(self) -> ET.Element:
        """Serialize MacSecLocalKayProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MacSecLocalKayProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_mac
        if self.destination_mac is not None:
            serialized = SerializationHelper.serialize_item(self.destination_mac, "MacAddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DESTINATION-MAC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_kay_props_ref
        if self.global_kay_props_ref is not None:
            serialized = SerializationHelper.serialize_item(self.global_kay_props_ref, "MacSecGlobalKayProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GLOBAL-KAY-PROPS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize key_server
        if self.key_server is not None:
            serialized = SerializationHelper.serialize_item(self.key_server, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("KEY-SERVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mka_participant_refs (list to container "MKA-PARTICIPANT-REFS")
        if self.mka_participant_refs:
            wrapper = ET.Element("MKA-PARTICIPANT-REFS")
            for item in self.mka_participant_refs:
                serialized = SerializationHelper.serialize_item(item, "MacSecKayParticipant")
                if serialized is not None:
                    child_elem = ET.Element("MKA-PARTICIPANT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize role
        if self.role is not None:
            serialized = SerializationHelper.serialize_item(self.role, "MacSecRoleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize source_mac
        if self.source_mac is not None:
            serialized = SerializationHelper.serialize_item(self.source_mac, "MacAddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOURCE-MAC")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MacSecLocalKayProps":
        """Deserialize XML element to MacSecLocalKayProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MacSecLocalKayProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(MacSecLocalKayProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DESTINATION-MAC":
                setattr(obj, "destination_mac", SerializationHelper.deserialize_by_tag(child, "MacAddressString"))
            elif tag == "GLOBAL-KAY-PROPS-REF":
                setattr(obj, "global_kay_props_ref", ARRef.deserialize(child))
            elif tag == "KEY-SERVER":
                setattr(obj, "key_server", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MKA-PARTICIPANT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.mka_participant_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "MacSecKayParticipant"))
            elif tag == "ROLE":
                setattr(obj, "role", MacSecRoleEnum.deserialize(child))
            elif tag == "SOURCE-MAC":
                setattr(obj, "source_mac", SerializationHelper.deserialize_by_tag(child, "MacAddressString"))

        return obj



class MacSecLocalKayPropsBuilder(BuilderBase):
    """Builder for MacSecLocalKayProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: MacSecLocalKayProps = MacSecLocalKayProps()


    def with_destination_mac(self, value: Optional[MacAddressString]) -> "MacSecLocalKayPropsBuilder":
        """Set destination_mac attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.destination_mac = value
        return self

    def with_global_kay_props(self, value: Optional[MacSecGlobalKayProps]) -> "MacSecLocalKayPropsBuilder":
        """Set global_kay_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.global_kay_props = value
        return self

    def with_key_server(self, value: Optional[PositiveInteger]) -> "MacSecLocalKayPropsBuilder":
        """Set key_server attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.key_server = value
        return self

    def with_mka_participants(self, items: list[MacSecKayParticipant]) -> "MacSecLocalKayPropsBuilder":
        """Set mka_participants list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mka_participants = list(items) if items else []
        return self

    def with_role(self, value: Optional[MacSecRoleEnum]) -> "MacSecLocalKayPropsBuilder":
        """Set role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.role = value
        return self

    def with_source_mac(self, value: Optional[MacAddressString]) -> "MacSecLocalKayPropsBuilder":
        """Set source_mac attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.source_mac = value
        return self


    def add_mka_participant(self, item: MacSecKayParticipant) -> "MacSecLocalKayPropsBuilder":
        """Add a single item to mka_participants list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mka_participants.append(item)
        return self

    def clear_mka_participants(self) -> "MacSecLocalKayPropsBuilder":
        """Clear all items from mka_participants list.

        Returns:
            self for method chaining
        """
        self._obj.mka_participants = []
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


    def build(self) -> MacSecLocalKayProps:
        """Build and return the MacSecLocalKayProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj