"""NmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 674)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_coordinator import (
        NmCoordinator,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class NmEcu(Identifiable):
    """AUTOSAR NmEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "NM-ECU"


    bus_dependent_nm_ecus: list[BusspecificNmEcu]
    ecu_instance_ref: Optional[ARRef]
    nm_bus_synchronization: Optional[Any]
    nm_com_control_enabled: Optional[Boolean]
    nm_coordinator: Optional[NmCoordinator]
    nm_cycletime: Optional[TimeValue]
    nm_pdu_rx_indication: Optional[Any]
    nm_remote_sleep_ind: Optional[Any]
    nm_state_change: Optional[Boolean]
    nm_user_data_enabled: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "BUS-DEPENDENT-NM-ECUS": ("_POLYMORPHIC_LIST", "bus_dependent_nm_ecus", ["CanNmEcu", "FlexrayNmEcu", "J1939NmEcu", "UdpNmEcu"]),
        "ECU-INSTANCE-REF": lambda obj, elem: setattr(obj, "ecu_instance_ref", ARRef.deserialize(elem)),
        "NM-BUS-SYNCHRONIZATION": lambda obj, elem: setattr(obj, "nm_bus_synchronization", SerializationHelper.deserialize_by_tag(elem, "any (BooleanEnabled)")),
        "NM-COM-CONTROL-ENABLED": lambda obj, elem: setattr(obj, "nm_com_control_enabled", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "NM-COORDINATOR": lambda obj, elem: setattr(obj, "nm_coordinator", SerializationHelper.deserialize_by_tag(elem, "NmCoordinator")),
        "NM-CYCLETIME": lambda obj, elem: setattr(obj, "nm_cycletime", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "NM-PDU-RX-INDICATION": lambda obj, elem: setattr(obj, "nm_pdu_rx_indication", SerializationHelper.deserialize_by_tag(elem, "any (BooleanEnabled)")),
        "NM-REMOTE-SLEEP-IND": lambda obj, elem: setattr(obj, "nm_remote_sleep_ind", SerializationHelper.deserialize_by_tag(elem, "any (BooleanEnabled)")),
        "NM-STATE-CHANGE": lambda obj, elem: setattr(obj, "nm_state_change", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "NM-USER-DATA-ENABLED": lambda obj, elem: setattr(obj, "nm_user_data_enabled", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize NmEcu."""
        super().__init__()
        self.bus_dependent_nm_ecus: list[BusspecificNmEcu] = []
        self.ecu_instance_ref: Optional[ARRef] = None
        self.nm_bus_synchronization: Optional[Any] = None
        self.nm_com_control_enabled: Optional[Boolean] = None
        self.nm_coordinator: Optional[NmCoordinator] = None
        self.nm_cycletime: Optional[TimeValue] = None
        self.nm_pdu_rx_indication: Optional[Any] = None
        self.nm_remote_sleep_ind: Optional[Any] = None
        self.nm_state_change: Optional[Boolean] = None
        self.nm_user_data_enabled: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize NmEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NmEcu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bus_dependent_nm_ecus (list to container "BUS-DEPENDENT-NM-ECUS")
        if self.bus_dependent_nm_ecus:
            wrapper = ET.Element("BUS-DEPENDENT-NM-ECUS")
            for item in self.bus_dependent_nm_ecus:
                serialized = SerializationHelper.serialize_item(item, "BusspecificNmEcu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize ecu_instance_ref
        if self.ecu_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_instance_ref, "EcuInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_bus_synchronization
        if self.nm_bus_synchronization is not None:
            serialized = SerializationHelper.serialize_item(self.nm_bus_synchronization, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-BUS-SYNCHRONIZATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_com_control_enabled
        if self.nm_com_control_enabled is not None:
            serialized = SerializationHelper.serialize_item(self.nm_com_control_enabled, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-COM-CONTROL-ENABLED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_coordinator
        if self.nm_coordinator is not None:
            serialized = SerializationHelper.serialize_item(self.nm_coordinator, "NmCoordinator")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-COORDINATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_cycletime
        if self.nm_cycletime is not None:
            serialized = SerializationHelper.serialize_item(self.nm_cycletime, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-CYCLETIME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_pdu_rx_indication
        if self.nm_pdu_rx_indication is not None:
            serialized = SerializationHelper.serialize_item(self.nm_pdu_rx_indication, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-PDU-RX-INDICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_remote_sleep_ind
        if self.nm_remote_sleep_ind is not None:
            serialized = SerializationHelper.serialize_item(self.nm_remote_sleep_ind, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-REMOTE-SLEEP-IND")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_state_change
        if self.nm_state_change is not None:
            serialized = SerializationHelper.serialize_item(self.nm_state_change, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-STATE-CHANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize nm_user_data_enabled
        if self.nm_user_data_enabled is not None:
            serialized = SerializationHelper.serialize_item(self.nm_user_data_enabled, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NM-USER-DATA-ENABLED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NmEcu":
        """Deserialize XML element to NmEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NmEcu object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NmEcu, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "BUS-DEPENDENT-NM-ECUS":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "CAN-NM-ECU":
                        obj.bus_dependent_nm_ecus.append(SerializationHelper.deserialize_by_tag(child[0], "CanNmEcu"))
                    elif concrete_tag == "FLEXRAY-NM-ECU":
                        obj.bus_dependent_nm_ecus.append(SerializationHelper.deserialize_by_tag(child[0], "FlexrayNmEcu"))
                    elif concrete_tag == "J1939-NM-ECU":
                        obj.bus_dependent_nm_ecus.append(SerializationHelper.deserialize_by_tag(child[0], "J1939NmEcu"))
                    elif concrete_tag == "UDP-NM-ECU":
                        obj.bus_dependent_nm_ecus.append(SerializationHelper.deserialize_by_tag(child[0], "UdpNmEcu"))
            elif tag == "ECU-INSTANCE-REF":
                setattr(obj, "ecu_instance_ref", ARRef.deserialize(child))
            elif tag == "NM-BUS-SYNCHRONIZATION":
                setattr(obj, "nm_bus_synchronization", SerializationHelper.deserialize_by_tag(child, "any (BooleanEnabled)"))
            elif tag == "NM-COM-CONTROL-ENABLED":
                setattr(obj, "nm_com_control_enabled", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "NM-COORDINATOR":
                setattr(obj, "nm_coordinator", SerializationHelper.deserialize_by_tag(child, "NmCoordinator"))
            elif tag == "NM-CYCLETIME":
                setattr(obj, "nm_cycletime", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "NM-PDU-RX-INDICATION":
                setattr(obj, "nm_pdu_rx_indication", SerializationHelper.deserialize_by_tag(child, "any (BooleanEnabled)"))
            elif tag == "NM-REMOTE-SLEEP-IND":
                setattr(obj, "nm_remote_sleep_ind", SerializationHelper.deserialize_by_tag(child, "any (BooleanEnabled)"))
            elif tag == "NM-STATE-CHANGE":
                setattr(obj, "nm_state_change", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "NM-USER-DATA-ENABLED":
                setattr(obj, "nm_user_data_enabled", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class NmEcuBuilder(IdentifiableBuilder):
    """Builder for NmEcu with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NmEcu = NmEcu()


    def with_bus_dependent_nm_ecus(self, items: list[BusspecificNmEcu]) -> "NmEcuBuilder":
        """Set bus_dependent_nm_ecus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.bus_dependent_nm_ecus = list(items) if items else []
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> "NmEcuBuilder":
        """Set ecu_instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_instance = value
        return self

    def with_nm_bus_synchronization(self, value: Optional[any (BooleanEnabled)]) -> "NmEcuBuilder":
        """Set nm_bus_synchronization attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_bus_synchronization = value
        return self

    def with_nm_com_control_enabled(self, value: Optional[Boolean]) -> "NmEcuBuilder":
        """Set nm_com_control_enabled attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_com_control_enabled = value
        return self

    def with_nm_coordinator(self, value: Optional[NmCoordinator]) -> "NmEcuBuilder":
        """Set nm_coordinator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_coordinator = value
        return self

    def with_nm_cycletime(self, value: Optional[TimeValue]) -> "NmEcuBuilder":
        """Set nm_cycletime attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_cycletime = value
        return self

    def with_nm_pdu_rx_indication(self, value: Optional[any (BooleanEnabled)]) -> "NmEcuBuilder":
        """Set nm_pdu_rx_indication attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_pdu_rx_indication = value
        return self

    def with_nm_remote_sleep_ind(self, value: Optional[any (BooleanEnabled)]) -> "NmEcuBuilder":
        """Set nm_remote_sleep_ind attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_remote_sleep_ind = value
        return self

    def with_nm_state_change(self, value: Optional[Boolean]) -> "NmEcuBuilder":
        """Set nm_state_change attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_state_change = value
        return self

    def with_nm_user_data_enabled(self, value: Optional[Boolean]) -> "NmEcuBuilder":
        """Set nm_user_data_enabled attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.nm_user_data_enabled = value
        return self


    def add_bus_dependent_nm_ecu(self, item: BusspecificNmEcu) -> "NmEcuBuilder":
        """Add a single item to bus_dependent_nm_ecus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.bus_dependent_nm_ecus.append(item)
        return self

    def clear_bus_dependent_nm_ecus(self) -> "NmEcuBuilder":
        """Clear all items from bus_dependent_nm_ecus list.

        Returns:
            self for method chaining
        """
        self._obj.bus_dependent_nm_ecus = []
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


    def build(self) -> NmEcu:
        """Build and return the NmEcu instance with validation."""
        self._validate_instance()
        pass
        return self._obj