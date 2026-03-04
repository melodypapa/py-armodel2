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

    _XML_TAG = "I-SIGNAL-PORT"


    data_filter: Optional[DataFilter]
    dds_qos_profile_ref: Optional[ARRef]
    first_timeout: Optional[TimeValue]
    handle_invalid_enum: Optional[HandleInvalidEnum]
    timeout: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "DATA-FILTER": lambda obj, elem: setattr(obj, "data_filter", SerializationHelper.deserialize_by_tag(elem, "DataFilter")),
        "DDS-QOS-PROFILE-REF": lambda obj, elem: setattr(obj, "dds_qos_profile_ref", ARRef.deserialize(elem)),
        "FIRST-TIMEOUT": lambda obj, elem: setattr(obj, "first_timeout", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "HANDLE-INVALID-ENUM": lambda obj, elem: setattr(obj, "handle_invalid_enum", HandleInvalidEnum.deserialize(elem)),
        "TIMEOUT": lambda obj, elem: setattr(obj, "timeout", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-FILTER":
                setattr(obj, "data_filter", SerializationHelper.deserialize_by_tag(child, "DataFilter"))
            elif tag == "DDS-QOS-PROFILE-REF":
                setattr(obj, "dds_qos_profile_ref", ARRef.deserialize(child))
            elif tag == "FIRST-TIMEOUT":
                setattr(obj, "first_timeout", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "HANDLE-INVALID-ENUM":
                setattr(obj, "handle_invalid_enum", HandleInvalidEnum.deserialize(child))
            elif tag == "TIMEOUT":
                setattr(obj, "timeout", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

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



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataFilter",
        "ddsQosProfile",
        "firstTimeout",
        "handleInvalidEnum",
        "timeout",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ISignalPort:
        """Build and return the ISignalPort instance with validation."""
        self._validate_instance()
        return self._obj