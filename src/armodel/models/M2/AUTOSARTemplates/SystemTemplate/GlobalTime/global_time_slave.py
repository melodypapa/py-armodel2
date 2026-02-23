"""GlobalTimeSlave AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 860)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from abc import ABC, abstractmethod
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class GlobalTimeSlave(Identifiable, ABC):
    """AUTOSAR GlobalTimeSlave."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    communication_connector_ref: Optional[ARRef]
    follow_up_timeout_value: Optional[TimeValue]
    icv_verification: Optional[Any]
    time_leap_future: Optional[TimeValue]
    time_leap: Optional[PositiveInteger]
    time_leap_past: Optional[TimeValue]
    def __init__(self) -> None:
        """Initialize GlobalTimeSlave."""
        super().__init__()
        self.communication_connector_ref: Optional[ARRef] = None
        self.follow_up_timeout_value: Optional[TimeValue] = None
        self.icv_verification: Optional[Any] = None
        self.time_leap_future: Optional[TimeValue] = None
        self.time_leap: Optional[PositiveInteger] = None
        self.time_leap_past: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize GlobalTimeSlave to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(GlobalTimeSlave, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_connector_ref
        if self.communication_connector_ref is not None:
            serialized = SerializationHelper.serialize_item(self.communication_connector_ref, "CommunicationConnector")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CONNECTOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize follow_up_timeout_value
        if self.follow_up_timeout_value is not None:
            serialized = SerializationHelper.serialize_item(self.follow_up_timeout_value, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FOLLOW-UP-TIMEOUT-VALUE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize icv_verification
        if self.icv_verification is not None:
            serialized = SerializationHelper.serialize_item(self.icv_verification, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ICV-VERIFICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_leap_future
        if self.time_leap_future is not None:
            serialized = SerializationHelper.serialize_item(self.time_leap_future, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-LEAP-FUTURE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_leap
        if self.time_leap is not None:
            serialized = SerializationHelper.serialize_item(self.time_leap, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-LEAP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize time_leap_past
        if self.time_leap_past is not None:
            serialized = SerializationHelper.serialize_item(self.time_leap_past, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIME-LEAP-PAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "GlobalTimeSlave":
        """Deserialize XML element to GlobalTimeSlave object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized GlobalTimeSlave object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(GlobalTimeSlave, cls).deserialize(element)

        # Parse communication_connector_ref
        child = SerializationHelper.find_child_element(element, "COMMUNICATION-CONNECTOR-REF")
        if child is not None:
            communication_connector_ref_value = ARRef.deserialize(child)
            obj.communication_connector_ref = communication_connector_ref_value

        # Parse follow_up_timeout_value
        child = SerializationHelper.find_child_element(element, "FOLLOW-UP-TIMEOUT-VALUE")
        if child is not None:
            follow_up_timeout_value_value = child.text
            obj.follow_up_timeout_value = follow_up_timeout_value_value

        # Parse icv_verification
        child = SerializationHelper.find_child_element(element, "ICV-VERIFICATION")
        if child is not None:
            icv_verification_value = child.text
            obj.icv_verification = icv_verification_value

        # Parse time_leap_future
        child = SerializationHelper.find_child_element(element, "TIME-LEAP-FUTURE")
        if child is not None:
            time_leap_future_value = child.text
            obj.time_leap_future = time_leap_future_value

        # Parse time_leap
        child = SerializationHelper.find_child_element(element, "TIME-LEAP")
        if child is not None:
            time_leap_value = child.text
            obj.time_leap = time_leap_value

        # Parse time_leap_past
        child = SerializationHelper.find_child_element(element, "TIME-LEAP-PAST")
        if child is not None:
            time_leap_past_value = child.text
            obj.time_leap_past = time_leap_past_value

        return obj



class GlobalTimeSlaveBuilder(IdentifiableBuilder):
    """Builder for GlobalTimeSlave with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: GlobalTimeSlave = GlobalTimeSlave()


    def with_communication_connector(self, value: Optional[CommunicationConnector]) -> "GlobalTimeSlaveBuilder":
        """Set communication_connector attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.communication_connector = value
        return self

    def with_follow_up_timeout_value(self, value: Optional[TimeValue]) -> "GlobalTimeSlaveBuilder":
        """Set follow_up_timeout_value attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.follow_up_timeout_value = value
        return self

    def with_icv_verification(self, value: Optional[any (GlobalTimeIcv)]) -> "GlobalTimeSlaveBuilder":
        """Set icv_verification attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.icv_verification = value
        return self

    def with_time_leap_future(self, value: Optional[TimeValue]) -> "GlobalTimeSlaveBuilder":
        """Set time_leap_future attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_leap_future = value
        return self

    def with_time_leap(self, value: Optional[PositiveInteger]) -> "GlobalTimeSlaveBuilder":
        """Set time_leap attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_leap = value
        return self

    def with_time_leap_past(self, value: Optional[TimeValue]) -> "GlobalTimeSlaveBuilder":
        """Set time_leap_past attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.time_leap_past = value
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


    @abstractmethod
    def build(self) -> GlobalTimeSlave:
        """Build and return the GlobalTimeSlave instance (abstract)."""
        raise NotImplementedError