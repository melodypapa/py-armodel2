"""J1939TpPg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 625)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class J1939TpPg(ARObject):
    """AUTOSAR J1939TpPg."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    direct_pdu_ref: Optional[ARRef]
    pgn: Optional[Integer]
    requestable: Optional[Boolean]
    sdu_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize J1939TpPg."""
        super().__init__()
        self.direct_pdu_ref: Optional[ARRef] = None
        self.pgn: Optional[Integer] = None
        self.requestable: Optional[Boolean] = None
        self.sdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize J1939TpPg to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939TpPg, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direct_pdu_ref
        if self.direct_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.direct_pdu_ref, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECT-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pgn
        if self.pgn is not None:
            serialized = SerializationHelper.serialize_item(self.pgn, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PGN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requestable
        if self.requestable is not None:
            serialized = SerializationHelper.serialize_item(self.requestable, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUESTABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdu_refs (list to container "SDU-REFS")
        if self.sdu_refs:
            wrapper = ET.Element("SDU-REFS")
            for item in self.sdu_refs:
                serialized = SerializationHelper.serialize_item(item, "IPdu")
                if serialized is not None:
                    child_elem = ET.Element("SDU-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpPg":
        """Deserialize XML element to J1939TpPg object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpPg object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939TpPg, cls).deserialize(element)

        # Parse direct_pdu_ref
        child = SerializationHelper.find_child_element(element, "DIRECT-PDU-REF")
        if child is not None:
            direct_pdu_ref_value = ARRef.deserialize(child)
            obj.direct_pdu_ref = direct_pdu_ref_value

        # Parse pgn
        child = SerializationHelper.find_child_element(element, "PGN")
        if child is not None:
            pgn_value = child.text
            obj.pgn = pgn_value

        # Parse requestable
        child = SerializationHelper.find_child_element(element, "REQUESTABLE")
        if child is not None:
            requestable_value = child.text
            obj.requestable = requestable_value

        # Parse sdu_refs (list from container "SDU-REFS")
        obj.sdu_refs = []
        container = SerializationHelper.find_child_element(element, "SDU-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdu_refs.append(child_value)

        return obj



class J1939TpPgBuilder(BuilderBase):
    """Builder for J1939TpPg with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: J1939TpPg = J1939TpPg()


    def with_direct_pdu(self, value: Optional[NPdu]) -> "J1939TpPgBuilder":
        """Set direct_pdu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.direct_pdu = value
        return self

    def with_pgn(self, value: Optional[Integer]) -> "J1939TpPgBuilder":
        """Set pgn attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pgn = value
        return self

    def with_requestable(self, value: Optional[Boolean]) -> "J1939TpPgBuilder":
        """Set requestable attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.requestable = value
        return self

    def with_sdus(self, items: list[IPdu]) -> "J1939TpPgBuilder":
        """Set sdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sdus = list(items) if items else []
        return self


    def add_sdu(self, item: IPdu) -> "J1939TpPgBuilder":
        """Add a single item to sdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sdus.append(item)
        return self

    def clear_sdus(self) -> "J1939TpPgBuilder":
        """Clear all items from sdus list.

        Returns:
            self for method chaining
        """
        self._obj.sdus = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> J1939TpPg:
        """Build and return the J1939TpPg instance with validation."""
        self._validate_instance()
        pass
        return self._obj