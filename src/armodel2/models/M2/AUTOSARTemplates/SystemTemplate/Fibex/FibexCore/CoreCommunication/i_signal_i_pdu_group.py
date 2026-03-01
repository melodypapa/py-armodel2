"""ISignalIPduGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 316)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 350)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import FibexElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_signal_i_pdu import (
    ISignalIPdu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.nm_pdu import (
    NmPdu,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ISignalIPduGroup(FibexElement):
    """AUTOSAR ISignalIPduGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "I-SIGNAL-I-PDU-GROUP"


    communication: Optional[String]
    contained_refs: list[ARRef]
    i_signal_i_pdu_refs: list[ARRef]
    nm_pdu_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COMMUNICATION": lambda obj, elem: setattr(obj, "communication", SerializationHelper.deserialize_by_tag(elem, "String")),
        "CONTAINED-REFS": lambda obj, elem: obj.contained_refs.append(ARRef.deserialize(elem)),
        "I-SIGNAL-I-PDU-REFS": lambda obj, elem: obj.i_signal_i_pdu_refs.append(ARRef.deserialize(elem)),
        "NM-PDU-REFS": lambda obj, elem: obj.nm_pdu_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize ISignalIPduGroup."""
        super().__init__()
        self.communication: Optional[String] = None
        self.contained_refs: list[ARRef] = []
        self.i_signal_i_pdu_refs: list[ARRef] = []
        self.nm_pdu_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ISignalIPduGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalIPduGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication
        if self.communication is not None:
            serialized = SerializationHelper.serialize_item(self.communication, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize contained_refs (list to container "CONTAINED-REFS")
        if self.contained_refs:
            wrapper = ET.Element("CONTAINED-REFS")
            for item in self.contained_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalIPduGroup")
                if serialized is not None:
                    child_elem = ET.Element("CONTAINED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize i_signal_i_pdu_refs (list to container "I-SIGNAL-I-PDU-REFS")
        if self.i_signal_i_pdu_refs:
            wrapper = ET.Element("I-SIGNAL-I-PDU-REFS")
            for item in self.i_signal_i_pdu_refs:
                serialized = SerializationHelper.serialize_item(item, "ISignalIPdu")
                if serialized is not None:
                    child_elem = ET.Element("I-SIGNAL-I-PDU-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nm_pdu_refs (list to container "NM-PDU-REFS")
        if self.nm_pdu_refs:
            wrapper = ET.Element("NM-PDU-REFS")
            for item in self.nm_pdu_refs:
                serialized = SerializationHelper.serialize_item(item, "NmPdu")
                if serialized is not None:
                    child_elem = ET.Element("NM-PDU-REF")
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
    def deserialize(cls, element: ET.Element) -> "ISignalIPduGroup":
        """Deserialize XML element to ISignalIPduGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalIPduGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalIPduGroup, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMMUNICATION":
                setattr(obj, "communication", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "CONTAINED-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.contained_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ISignalIPduGroup"))
            elif tag == "I-SIGNAL-I-PDU-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.i_signal_i_pdu_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ISignalIPdu"))
            elif tag == "NM-PDU-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.nm_pdu_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "NmPdu"))

        return obj



class ISignalIPduGroupBuilder(FibexElementBuilder):
    """Builder for ISignalIPduGroup with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ISignalIPduGroup = ISignalIPduGroup()


    def with_communication(self, value: Optional[String]) -> "ISignalIPduGroupBuilder":
        """Set communication attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.communication = value
        return self

    def with_containeds(self, items: list[ISignalIPduGroup]) -> "ISignalIPduGroupBuilder":
        """Set containeds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.containeds = list(items) if items else []
        return self

    def with_i_signal_i_pdus(self, items: list[ISignalIPdu]) -> "ISignalIPduGroupBuilder":
        """Set i_signal_i_pdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_signal_i_pdus = list(items) if items else []
        return self

    def with_nm_pdus(self, items: list[NmPdu]) -> "ISignalIPduGroupBuilder":
        """Set nm_pdus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nm_pdus = list(items) if items else []
        return self


    def add_contained(self, item: ISignalIPduGroup) -> "ISignalIPduGroupBuilder":
        """Add a single item to containeds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.containeds.append(item)
        return self

    def clear_containeds(self) -> "ISignalIPduGroupBuilder":
        """Clear all items from containeds list.

        Returns:
            self for method chaining
        """
        self._obj.containeds = []
        return self

    def add_i_signal_i_pdu(self, item: ISignalIPdu) -> "ISignalIPduGroupBuilder":
        """Add a single item to i_signal_i_pdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_signal_i_pdus.append(item)
        return self

    def clear_i_signal_i_pdus(self) -> "ISignalIPduGroupBuilder":
        """Clear all items from i_signal_i_pdus list.

        Returns:
            self for method chaining
        """
        self._obj.i_signal_i_pdus = []
        return self

    def add_nm_pdu(self, item: NmPdu) -> "ISignalIPduGroupBuilder":
        """Add a single item to nm_pdus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nm_pdus.append(item)
        return self

    def clear_nm_pdus(self) -> "ISignalIPduGroupBuilder":
        """Clear all items from nm_pdus list.

        Returns:
            self for method chaining
        """
        self._obj.nm_pdus = []
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


    def build(self) -> ISignalIPduGroup:
        """Build and return the ISignalIPduGroup instance with validation."""
        self._validate_instance()
        pass
        return self._obj