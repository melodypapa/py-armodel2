"""CommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 54)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.classes.json"""

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    PncGatewayTypeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.comm_connector_port import (
    CommConnectorPort,
)


class CommunicationConnector(Identifiable, ABC):
    """AUTOSAR CommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    comm_controller_ref: Optional[Any]
    create_ecu: Optional[Boolean]
    dynamic_pnc_to: Optional[Boolean]
    ecu_comm_ports: list[CommConnectorPort]
    pnc_filter_arrays: list[PositiveInteger]
    pnc_gateway_type_enum: Optional[PncGatewayTypeEnum]
    def __init__(self) -> None:
        """Initialize CommunicationConnector."""
        super().__init__()
        self.comm_controller_ref: Optional[Any] = None
        self.create_ecu: Optional[Boolean] = None
        self.dynamic_pnc_to: Optional[Boolean] = None
        self.ecu_comm_ports: list[CommConnectorPort] = []
        self.pnc_filter_arrays: list[PositiveInteger] = []
        self.pnc_gateway_type_enum: Optional[PncGatewayTypeEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize CommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CommunicationConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize comm_controller_ref
        if self.comm_controller_ref is not None:
            serialized = SerializationHelper.serialize_item(self.comm_controller_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMM-CONTROLLER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize create_ecu
        if self.create_ecu is not None:
            serialized = SerializationHelper.serialize_item(self.create_ecu, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CREATE-ECU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dynamic_pnc_to
        if self.dynamic_pnc_to is not None:
            serialized = SerializationHelper.serialize_item(self.dynamic_pnc_to, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-PNC-TO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecu_comm_ports (list to container "ECU-COMM-PORTS")
        if self.ecu_comm_ports:
            wrapper = ET.Element("ECU-COMM-PORTS")
            for item in self.ecu_comm_ports:
                serialized = SerializationHelper.serialize_item(item, "CommConnectorPort")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_filter_arrays (list to container "PNC-FILTER-ARRAYS")
        if self.pnc_filter_arrays:
            wrapper = ET.Element("PNC-FILTER-ARRAYS")
            for item in self.pnc_filter_arrays:
                serialized = SerializationHelper.serialize_item(item, "PositiveInteger")
                if serialized is not None:
                    child_elem = ET.Element("PNC-FILTER-ARRAY")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pnc_gateway_type_enum
        if self.pnc_gateway_type_enum is not None:
            serialized = SerializationHelper.serialize_item(self.pnc_gateway_type_enum, "PncGatewayTypeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PNC-GATEWAY-TYPE-ENUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CommunicationConnector":
        """Deserialize XML element to CommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CommunicationConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CommunicationConnector, cls).deserialize(element)

        # Parse comm_controller_ref
        child = SerializationHelper.find_child_element(element, "COMM-CONTROLLER-REF")
        if child is not None:
            comm_controller_ref_value = ARRef.deserialize(child)
            obj.comm_controller_ref = comm_controller_ref_value

        # Parse create_ecu
        child = SerializationHelper.find_child_element(element, "CREATE-ECU")
        if child is not None:
            create_ecu_value = child.text
            obj.create_ecu = create_ecu_value

        # Parse dynamic_pnc_to
        child = SerializationHelper.find_child_element(element, "DYNAMIC-PNC-TO")
        if child is not None:
            dynamic_pnc_to_value = child.text
            obj.dynamic_pnc_to = dynamic_pnc_to_value

        # Parse ecu_comm_ports (list from container "ECU-COMM-PORTS")
        obj.ecu_comm_ports = []
        container = SerializationHelper.find_child_element(element, "ECU-COMM-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.ecu_comm_ports.append(child_value)

        # Parse pnc_filter_arrays (list from container "PNC-FILTER-ARRAYS")
        obj.pnc_filter_arrays = []
        container = SerializationHelper.find_child_element(element, "PNC-FILTER-ARRAYS")
        if container is not None:
            for child in container:
                # Extract primitive value (PositiveInteger) as text
                child_value = child.text
                if child_value is not None:
                    obj.pnc_filter_arrays.append(child_value)

        # Parse pnc_gateway_type_enum
        child = SerializationHelper.find_child_element(element, "PNC-GATEWAY-TYPE-ENUM")
        if child is not None:
            pnc_gateway_type_enum_value = PncGatewayTypeEnum.deserialize(child)
            obj.pnc_gateway_type_enum = pnc_gateway_type_enum_value

        return obj



class CommunicationConnectorBuilder(IdentifiableBuilder):
    """Builder for CommunicationConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: CommunicationConnector = CommunicationConnector()


    def with_comm_controller(self, value: Optional[any (Communication)]) -> "CommunicationConnectorBuilder":
        """Set comm_controller attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.comm_controller = value
        return self

    def with_create_ecu(self, value: Optional[Boolean]) -> "CommunicationConnectorBuilder":
        """Set create_ecu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.create_ecu = value
        return self

    def with_dynamic_pnc_to(self, value: Optional[Boolean]) -> "CommunicationConnectorBuilder":
        """Set dynamic_pnc_to attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dynamic_pnc_to = value
        return self

    def with_ecu_comm_ports(self, items: list[CommConnectorPort]) -> "CommunicationConnectorBuilder":
        """Set ecu_comm_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.ecu_comm_ports = list(items) if items else []
        return self

    def with_pnc_filter_arrays(self, items: list[PositiveInteger]) -> "CommunicationConnectorBuilder":
        """Set pnc_filter_arrays list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pnc_filter_arrays = list(items) if items else []
        return self

    def with_pnc_gateway_type_enum(self, value: Optional[PncGatewayTypeEnum]) -> "CommunicationConnectorBuilder":
        """Set pnc_gateway_type_enum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pnc_gateway_type_enum = value
        return self


    def add_ecu_comm_port(self, item: CommConnectorPort) -> "CommunicationConnectorBuilder":
        """Add a single item to ecu_comm_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.ecu_comm_ports.append(item)
        return self

    def clear_ecu_comm_ports(self) -> "CommunicationConnectorBuilder":
        """Clear all items from ecu_comm_ports list.

        Returns:
            self for method chaining
        """
        self._obj.ecu_comm_ports = []
        return self

    def add_pnc_filter_array(self, item: PositiveInteger) -> "CommunicationConnectorBuilder":
        """Add a single item to pnc_filter_arrays list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pnc_filter_arrays.append(item)
        return self

    def clear_pnc_filter_arrays(self) -> "CommunicationConnectorBuilder":
        """Clear all items from pnc_filter_arrays list.

        Returns:
            self for method chaining
        """
        self._obj.pnc_filter_arrays = []
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
    def build(self) -> CommunicationConnector:
        """Build and return the CommunicationConnector instance (abstract)."""
        raise NotImplementedError