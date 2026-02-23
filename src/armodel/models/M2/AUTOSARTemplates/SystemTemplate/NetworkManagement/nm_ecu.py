"""NmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 674)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.busspecific_nm_ecu import (
    BusspecificNmEcu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_coordinator import (
        NmCoordinator,
    )



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class NmEcu(Identifiable):
    """AUTOSAR NmEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

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
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Parse bus_dependent_nm_ecus (list from container "BUS-DEPENDENT-NM-ECUS")
        obj.bus_dependent_nm_ecus = []
        container = SerializationHelper.find_child_element(element, "BUS-DEPENDENT-NM-ECUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.bus_dependent_nm_ecus.append(child_value)

        # Parse ecu_instance_ref
        child = SerializationHelper.find_child_element(element, "ECU-INSTANCE-REF")
        if child is not None:
            ecu_instance_ref_value = ARRef.deserialize(child)
            obj.ecu_instance_ref = ecu_instance_ref_value

        # Parse nm_bus_synchronization
        child = SerializationHelper.find_child_element(element, "NM-BUS-SYNCHRONIZATION")
        if child is not None:
            nm_bus_synchronization_value = child.text
            obj.nm_bus_synchronization = nm_bus_synchronization_value

        # Parse nm_com_control_enabled
        child = SerializationHelper.find_child_element(element, "NM-COM-CONTROL-ENABLED")
        if child is not None:
            nm_com_control_enabled_value = child.text
            obj.nm_com_control_enabled = nm_com_control_enabled_value

        # Parse nm_coordinator
        child = SerializationHelper.find_child_element(element, "NM-COORDINATOR")
        if child is not None:
            nm_coordinator_value = SerializationHelper.deserialize_by_tag(child, "NmCoordinator")
            obj.nm_coordinator = nm_coordinator_value

        # Parse nm_cycletime
        child = SerializationHelper.find_child_element(element, "NM-CYCLETIME")
        if child is not None:
            nm_cycletime_value = child.text
            obj.nm_cycletime = nm_cycletime_value

        # Parse nm_pdu_rx_indication
        child = SerializationHelper.find_child_element(element, "NM-PDU-RX-INDICATION")
        if child is not None:
            nm_pdu_rx_indication_value = child.text
            obj.nm_pdu_rx_indication = nm_pdu_rx_indication_value

        # Parse nm_remote_sleep_ind
        child = SerializationHelper.find_child_element(element, "NM-REMOTE-SLEEP-IND")
        if child is not None:
            nm_remote_sleep_ind_value = child.text
            obj.nm_remote_sleep_ind = nm_remote_sleep_ind_value

        # Parse nm_state_change
        child = SerializationHelper.find_child_element(element, "NM-STATE-CHANGE")
        if child is not None:
            nm_state_change_value = child.text
            obj.nm_state_change = nm_state_change_value

        # Parse nm_user_data_enabled
        child = SerializationHelper.find_child_element(element, "NM-USER-DATA-ENABLED")
        if child is not None:
            nm_user_data_enabled_value = child.text
            obj.nm_user_data_enabled = nm_user_data_enabled_value

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


    def build(self) -> NmEcu:
        """Build and return the NmEcu instance with validation."""
        self._validate_instance()
        pass
        return self._obj