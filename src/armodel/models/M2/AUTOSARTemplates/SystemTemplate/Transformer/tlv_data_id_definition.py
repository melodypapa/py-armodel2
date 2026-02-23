"""TlvDataIdDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 830)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.argument_data_prototype import (
    ArgumentDataPrototype,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.abstract_implementation_data_type import (
        AbstractImplementationDataType,
    )



class TlvDataIdDefinition(ARObject):
    """AUTOSAR TlvDataIdDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    id: Optional[PositiveInteger]
    tlv_argument_ref: Optional[ARRef]
    tlv_ref: Optional[ARRef]
    tlv_record_ref: Optional[Any]
    def __init__(self) -> None:
        """Initialize TlvDataIdDefinition."""
        super().__init__()
        self.id: Optional[PositiveInteger] = None
        self.tlv_argument_ref: Optional[ARRef] = None
        self.tlv_ref: Optional[ARRef] = None
        self.tlv_record_ref: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TlvDataIdDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TlvDataIdDefinition, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize id
        if self.id is not None:
            serialized = SerializationHelper.serialize_item(self.id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tlv_argument_ref
        if self.tlv_argument_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tlv_argument_ref, "ArgumentDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TLV-ARGUMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tlv_ref
        if self.tlv_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tlv_ref, "AbstractImplementationDataType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TLV-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tlv_record_ref
        if self.tlv_record_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tlv_record_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TLV-RECORD-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TlvDataIdDefinition":
        """Deserialize XML element to TlvDataIdDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TlvDataIdDefinition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TlvDataIdDefinition, cls).deserialize(element)

        # Parse id
        child = SerializationHelper.find_child_element(element, "ID")
        if child is not None:
            id_value = child.text
            obj.id = id_value

        # Parse tlv_argument_ref
        child = SerializationHelper.find_child_element(element, "TLV-ARGUMENT-REF")
        if child is not None:
            tlv_argument_ref_value = ARRef.deserialize(child)
            obj.tlv_argument_ref = tlv_argument_ref_value

        # Parse tlv_ref
        child = SerializationHelper.find_child_element(element, "TLV-REF")
        if child is not None:
            tlv_ref_value = ARRef.deserialize(child)
            obj.tlv_ref = tlv_ref_value

        # Parse tlv_record_ref
        child = SerializationHelper.find_child_element(element, "TLV-RECORD-REF")
        if child is not None:
            tlv_record_ref_value = ARRef.deserialize(child)
            obj.tlv_record_ref = tlv_record_ref_value

        return obj



class TlvDataIdDefinitionBuilder(BuilderBase):
    """Builder for TlvDataIdDefinition with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: TlvDataIdDefinition = TlvDataIdDefinition()


    def with_id(self, value: Optional[PositiveInteger]) -> "TlvDataIdDefinitionBuilder":
        """Set id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.id = value
        return self

    def with_tlv_argument(self, value: Optional[ArgumentDataPrototype]) -> "TlvDataIdDefinitionBuilder":
        """Set tlv_argument attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tlv_argument = value
        return self

    def with_tlv(self, value: Optional[AbstractImplementationDataType]) -> "TlvDataIdDefinitionBuilder":
        """Set tlv attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tlv = value
        return self

    def with_tlv_record(self, value: Optional[any (ApplicationRecord)]) -> "TlvDataIdDefinitionBuilder":
        """Set tlv_record attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tlv_record = value
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


    def build(self) -> TlvDataIdDefinition:
        """Build and return the TlvDataIdDefinition instance with validation."""
        self._validate_instance()
        pass
        return self._obj