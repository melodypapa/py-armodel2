"""EthGlobalTimeManagedCouplingPort AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 874)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.GlobalTime.ETH import (
    GlobalTimePortRoleEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.coupling_port import (
    CouplingPort,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthGlobalTimeManagedCouplingPort(ARObject):
    """AUTOSAR EthGlobalTimeManagedCouplingPort."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    coupling_port_ref: Optional[ARRef]
    global_time_port_role: Optional[GlobalTimePortRoleEnum]
    global_time_tx_period: Optional[TimeValue]
    pdelay_latency: Optional[TimeValue]
    pdelay_request: Optional[TimeValue]
    pdelay_resp_and: Optional[TimeValue]
    pdelay: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EthGlobalTimeManagedCouplingPort."""
        super().__init__()
        self.coupling_port_ref: Optional[ARRef] = None
        self.global_time_port_role: Optional[GlobalTimePortRoleEnum] = None
        self.global_time_tx_period: Optional[TimeValue] = None
        self.pdelay_latency: Optional[TimeValue] = None
        self.pdelay_request: Optional[TimeValue] = None
        self.pdelay_resp_and: Optional[TimeValue] = None
        self.pdelay: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EthGlobalTimeManagedCouplingPort to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthGlobalTimeManagedCouplingPort, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize coupling_port_ref
        if self.coupling_port_ref is not None:
            serialized = SerializationHelper.serialize_item(self.coupling_port_ref, "CouplingPort")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUPLING-PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_time_port_role
        if self.global_time_port_role is not None:
            serialized = SerializationHelper.serialize_item(self.global_time_port_role, "GlobalTimePortRoleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GLOBAL-TIME-PORT-ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize global_time_tx_period
        if self.global_time_tx_period is not None:
            serialized = SerializationHelper.serialize_item(self.global_time_tx_period, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GLOBAL-TIME-TX-PERIOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdelay_latency
        if self.pdelay_latency is not None:
            serialized = SerializationHelper.serialize_item(self.pdelay_latency, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDELAY-LATENCY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdelay_request
        if self.pdelay_request is not None:
            serialized = SerializationHelper.serialize_item(self.pdelay_request, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDELAY-REQUEST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdelay_resp_and
        if self.pdelay_resp_and is not None:
            serialized = SerializationHelper.serialize_item(self.pdelay_resp_and, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDELAY-RESP-AND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdelay
        if self.pdelay is not None:
            serialized = SerializationHelper.serialize_item(self.pdelay, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDELAY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthGlobalTimeManagedCouplingPort":
        """Deserialize XML element to EthGlobalTimeManagedCouplingPort object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthGlobalTimeManagedCouplingPort object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthGlobalTimeManagedCouplingPort, cls).deserialize(element)

        # Parse coupling_port_ref
        child = SerializationHelper.find_child_element(element, "COUPLING-PORT-REF")
        if child is not None:
            coupling_port_ref_value = ARRef.deserialize(child)
            obj.coupling_port_ref = coupling_port_ref_value

        # Parse global_time_port_role
        child = SerializationHelper.find_child_element(element, "GLOBAL-TIME-PORT-ROLE")
        if child is not None:
            global_time_port_role_value = GlobalTimePortRoleEnum.deserialize(child)
            obj.global_time_port_role = global_time_port_role_value

        # Parse global_time_tx_period
        child = SerializationHelper.find_child_element(element, "GLOBAL-TIME-TX-PERIOD")
        if child is not None:
            global_time_tx_period_value = child.text
            obj.global_time_tx_period = global_time_tx_period_value

        # Parse pdelay_latency
        child = SerializationHelper.find_child_element(element, "PDELAY-LATENCY")
        if child is not None:
            pdelay_latency_value = child.text
            obj.pdelay_latency = pdelay_latency_value

        # Parse pdelay_request
        child = SerializationHelper.find_child_element(element, "PDELAY-REQUEST")
        if child is not None:
            pdelay_request_value = child.text
            obj.pdelay_request = pdelay_request_value

        # Parse pdelay_resp_and
        child = SerializationHelper.find_child_element(element, "PDELAY-RESP-AND")
        if child is not None:
            pdelay_resp_and_value = child.text
            obj.pdelay_resp_and = pdelay_resp_and_value

        # Parse pdelay
        child = SerializationHelper.find_child_element(element, "PDELAY")
        if child is not None:
            pdelay_value = child.text
            obj.pdelay = pdelay_value

        return obj



class EthGlobalTimeManagedCouplingPortBuilder(BuilderBase):
    """Builder for EthGlobalTimeManagedCouplingPort with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthGlobalTimeManagedCouplingPort = EthGlobalTimeManagedCouplingPort()


    def with_coupling_port(self, value: Optional[CouplingPort]) -> "EthGlobalTimeManagedCouplingPortBuilder":
        """Set coupling_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.coupling_port = value
        return self

    def with_global_time_port_role(self, value: Optional[GlobalTimePortRoleEnum]) -> "EthGlobalTimeManagedCouplingPortBuilder":
        """Set global_time_port_role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.global_time_port_role = value
        return self

    def with_global_time_tx_period(self, value: Optional[TimeValue]) -> "EthGlobalTimeManagedCouplingPortBuilder":
        """Set global_time_tx_period attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.global_time_tx_period = value
        return self

    def with_pdelay_latency(self, value: Optional[TimeValue]) -> "EthGlobalTimeManagedCouplingPortBuilder":
        """Set pdelay_latency attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdelay_latency = value
        return self

    def with_pdelay_request(self, value: Optional[TimeValue]) -> "EthGlobalTimeManagedCouplingPortBuilder":
        """Set pdelay_request attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdelay_request = value
        return self

    def with_pdelay_resp_and(self, value: Optional[TimeValue]) -> "EthGlobalTimeManagedCouplingPortBuilder":
        """Set pdelay_resp_and attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdelay_resp_and = value
        return self

    def with_pdelay(self, value: Optional[Boolean]) -> "EthGlobalTimeManagedCouplingPortBuilder":
        """Set pdelay attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdelay = value
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


    def build(self) -> EthGlobalTimeManagedCouplingPort:
        """Build and return the EthGlobalTimeManagedCouplingPort instance with validation."""
        self._validate_instance()
        pass
        return self._obj