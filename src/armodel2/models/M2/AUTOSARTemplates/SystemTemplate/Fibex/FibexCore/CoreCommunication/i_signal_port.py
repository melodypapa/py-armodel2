"""ISignalPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 305)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import CommConnectorPortBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleInvalidEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Filter.data_filter import (
    DataFilter,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_qos_profile import (
    DdsCpQosProfile,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ISignalPort(CommConnectorPort):
    """AUTOSAR ISignalPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_filter: Optional[DataFilter]
    dds_qos_profile_ref: Optional[ARRef]
    first_timeout: Optional[TimeValue]
    handle_invalid_enum: Optional[HandleInvalidEnum]
    timeout: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize ISignalPort."""
        super().__init__()
        self.data_filter: Optional[DataFilter] = None
        self.dds_qos_profile_ref: Optional[ARRef] = None
        self.first_timeout: Optional[TimeValue] = None
        self.handle_invalid_enum: Optional[HandleInvalidEnum] = None
        self.timeout: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize ISignalPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ISignalPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_filter
        if self.data_filter is not None:
            serialized = SerializationHelper.serialize_item(self.data_filter, "DataFilter")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-FILTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dds_qos_profile_ref
        if self.dds_qos_profile_ref is not None:
            serialized = SerializationHelper.serialize_item(self.dds_qos_profile_ref, "DdsCpQosProfile")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DDS-QOS-PROFILE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize first_timeout
        if self.first_timeout is not None:
            serialized = SerializationHelper.serialize_item(self.first_timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FIRST-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_invalid_enum
        if self.handle_invalid_enum is not None:
            serialized = SerializationHelper.serialize_item(self.handle_invalid_enum, "HandleInvalidEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-INVALID-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout
        if self.timeout is not None:
            serialized = SerializationHelper.serialize_item(self.timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ISignalPort":
        """Deserialize XML element to ISignalPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ISignalPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ISignalPort, cls).deserialize(element)

        # Parse data_filter
        child = SerializationHelper.find_child_element(element, "DATA-FILTER")
        if child is not None:
            data_filter_value = SerializationHelper.deserialize_by_tag(child, "DataFilter")
            obj.data_filter = data_filter_value

        # Parse dds_qos_profile_ref
        child = SerializationHelper.find_child_element(element, "DDS-QOS-PROFILE-REF")
        if child is not None:
            dds_qos_profile_ref_value = ARRef.deserialize(child)
            obj.dds_qos_profile_ref = dds_qos_profile_ref_value

        # Parse first_timeout
        child = SerializationHelper.find_child_element(element, "FIRST-TIMEOUT")
        if child is not None:
            first_timeout_value = child.text
            obj.first_timeout = first_timeout_value

        # Parse handle_invalid_enum
        child = SerializationHelper.find_child_element(element, "HANDLE-INVALID-ENUM")
        if child is not None:
            handle_invalid_enum_value = HandleInvalidEnum.deserialize(child)
            obj.handle_invalid_enum = handle_invalid_enum_value

        # Parse timeout
        child = SerializationHelper.find_child_element(element, "TIMEOUT")
        if child is not None:
            timeout_value = child.text
            obj.timeout = timeout_value

        return obj



class ISignalPortBuilder(CommConnectorPortBuilder):
    """Builder for ISignalPort with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ISignalPort = ISignalPort()


    def with_data_filter(self, value: Optional[DataFilter]) -> "ISignalPortBuilder":
        """Set data_filter attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_filter = value
        return self

    def with_dds_qos_profile(self, value: Optional[DdsCpQosProfile]) -> "ISignalPortBuilder":
        """Set dds_qos_profile attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dds_qos_profile = value
        return self

    def with_first_timeout(self, value: Optional[TimeValue]) -> "ISignalPortBuilder":
        """Set first_timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.first_timeout = value
        return self

    def with_handle_invalid_enum(self, value: Optional[HandleInvalidEnum]) -> "ISignalPortBuilder":
        """Set handle_invalid_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_invalid_enum = value
        return self

    def with_timeout(self, value: Optional[TimeValue]) -> "ISignalPortBuilder":
        """Set timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.timeout = value
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


    def build(self) -> ISignalPort:
        """Build and return the ISignalPort instance with validation."""
        self._validate_instance()
        pass
        return self._obj