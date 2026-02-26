"""PortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 326)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 304)
  - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (page 62)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 66)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2047)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 236)
  - AUTOSAR_FO_TPS_ARXMLSerializationRules.pdf (page 30)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 48)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 76)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 458)
  - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (page 33)
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 65)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.client_server_annotation import (
    ClientServerAnnotation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.delegated_port_annotation import (
    DelegatedPortAnnotation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.mode_port_annotation import (
    ModePortAnnotation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.nv_data_port_annotation import (
    NvDataPortAnnotation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.parameter_port_annotation import (
    ParameterPortAnnotation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.trigger_port_annotation import (
    TriggerPortAnnotation,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.ApplicationAttributes.io_hw_abstraction_server_annotation import (
        IoHwAbstractionServerAnnotation,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PortPrototype(Identifiable, ABC):
    """AUTOSAR PortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    client_servers: list[ClientServerAnnotation]
    delegated_port: Optional[DelegatedPortAnnotation]
    io_hw_abstraction_server_annotations: list[IoHwAbstractionServerAnnotation]
    mode_port_annotations: list[ModePortAnnotation]
    nv_data_port_annotations: list[NvDataPortAnnotation]
    parameter_ports: list[ParameterPortAnnotation]
    sender_receivers: list[Any]
    trigger_port_annotation_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PortPrototype."""
        super().__init__()
        self.client_servers: list[ClientServerAnnotation] = []
        self.delegated_port: Optional[DelegatedPortAnnotation] = None
        self.io_hw_abstraction_server_annotations: list[IoHwAbstractionServerAnnotation] = []
        self.mode_port_annotations: list[ModePortAnnotation] = []
        self.nv_data_port_annotations: list[NvDataPortAnnotation] = []
        self.parameter_ports: list[ParameterPortAnnotation] = []
        self.sender_receivers: list[Any] = []
        self.trigger_port_annotation_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_servers (list to container "CLIENT-SERVERS")
        if self.client_servers:
            wrapper = ET.Element("CLIENT-SERVERS")
            for item in self.client_servers:
                serialized = SerializationHelper.serialize_item(item, "ClientServerAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize delegated_port
        if self.delegated_port is not None:
            serialized = SerializationHelper.serialize_item(self.delegated_port, "DelegatedPortAnnotation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DELEGATED-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize io_hw_abstraction_server_annotations (list to container "IO-HW-ABSTRACTION-SERVER-ANNOTATIONS")
        if self.io_hw_abstraction_server_annotations:
            wrapper = ET.Element("IO-HW-ABSTRACTION-SERVER-ANNOTATIONS")
            for item in self.io_hw_abstraction_server_annotations:
                serialized = SerializationHelper.serialize_item(item, "IoHwAbstractionServerAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mode_port_annotations (list to container "MODE-PORT-ANNOTATIONS")
        if self.mode_port_annotations:
            wrapper = ET.Element("MODE-PORT-ANNOTATIONS")
            for item in self.mode_port_annotations:
                serialized = SerializationHelper.serialize_item(item, "ModePortAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize nv_data_port_annotations (list to container "NV-DATA-PORT-ANNOTATIONS")
        if self.nv_data_port_annotations:
            wrapper = ET.Element("NV-DATA-PORT-ANNOTATIONS")
            for item in self.nv_data_port_annotations:
                serialized = SerializationHelper.serialize_item(item, "NvDataPortAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize parameter_ports (list to container "PARAMETER-PORTS")
        if self.parameter_ports:
            wrapper = ET.Element("PARAMETER-PORTS")
            for item in self.parameter_ports:
                serialized = SerializationHelper.serialize_item(item, "ParameterPortAnnotation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sender_receivers (list to container "SENDER-RECEIVERS")
        if self.sender_receivers:
            wrapper = ET.Element("SENDER-RECEIVERS")
            for item in self.sender_receivers:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize trigger_port_annotation_refs (list to container "TRIGGER-PORT-ANNOTATION-REFS")
        if self.trigger_port_annotation_refs:
            wrapper = ET.Element("TRIGGER-PORT-ANNOTATION-REFS")
            for item in self.trigger_port_annotation_refs:
                serialized = SerializationHelper.serialize_item(item, "TriggerPortAnnotation")
                if serialized is not None:
                    child_elem = ET.Element("TRIGGER-PORT-ANNOTATION-REF")
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
    def deserialize(cls, element: ET.Element) -> "PortPrototype":
        """Deserialize XML element to PortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortPrototype, cls).deserialize(element)

        # Parse client_servers (list from container "CLIENT-SERVERS")
        obj.client_servers = []
        container = SerializationHelper.find_child_element(element, "CLIENT-SERVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.client_servers.append(child_value)

        # Parse delegated_port
        child = SerializationHelper.find_child_element(element, "DELEGATED-PORT")
        if child is not None:
            delegated_port_value = SerializationHelper.deserialize_by_tag(child, "DelegatedPortAnnotation")
            obj.delegated_port = delegated_port_value

        # Parse io_hw_abstraction_server_annotations (list from container "IO-HW-ABSTRACTION-SERVER-ANNOTATIONS")
        obj.io_hw_abstraction_server_annotations = []
        container = SerializationHelper.find_child_element(element, "IO-HW-ABSTRACTION-SERVER-ANNOTATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.io_hw_abstraction_server_annotations.append(child_value)

        # Parse mode_port_annotations (list from container "MODE-PORT-ANNOTATIONS")
        obj.mode_port_annotations = []
        container = SerializationHelper.find_child_element(element, "MODE-PORT-ANNOTATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mode_port_annotations.append(child_value)

        # Parse nv_data_port_annotations (list from container "NV-DATA-PORT-ANNOTATIONS")
        obj.nv_data_port_annotations = []
        container = SerializationHelper.find_child_element(element, "NV-DATA-PORT-ANNOTATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.nv_data_port_annotations.append(child_value)

        # Parse parameter_ports (list from container "PARAMETER-PORTS")
        obj.parameter_ports = []
        container = SerializationHelper.find_child_element(element, "PARAMETER-PORTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.parameter_ports.append(child_value)

        # Parse sender_receivers (list from container "SENDER-RECEIVERS")
        obj.sender_receivers = []
        container = SerializationHelper.find_child_element(element, "SENDER-RECEIVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sender_receivers.append(child_value)

        # Parse trigger_port_annotation_refs (list from container "TRIGGER-PORT-ANNOTATION-REFS")
        obj.trigger_port_annotation_refs = []
        container = SerializationHelper.find_child_element(element, "TRIGGER-PORT-ANNOTATION-REFS")
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
                    obj.trigger_port_annotation_refs.append(child_value)

        return obj



class PortPrototypeBuilder(IdentifiableBuilder):
    """Builder for PortPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PortPrototype = PortPrototype()


    def with_client_servers(self, items: list[ClientServerAnnotation]) -> "PortPrototypeBuilder":
        """Set client_servers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.client_servers = list(items) if items else []
        return self

    def with_delegated_port(self, value: Optional[DelegatedPortAnnotation]) -> "PortPrototypeBuilder":
        """Set delegated_port attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.delegated_port = value
        return self

    def with_io_hw_abstraction_server_annotations(self, items: list[IoHwAbstractionServerAnnotation]) -> "PortPrototypeBuilder":
        """Set io_hw_abstraction_server_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations = list(items) if items else []
        return self

    def with_mode_port_annotations(self, items: list[ModePortAnnotation]) -> "PortPrototypeBuilder":
        """Set mode_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations = list(items) if items else []
        return self

    def with_nv_data_port_annotations(self, items: list[NvDataPortAnnotation]) -> "PortPrototypeBuilder":
        """Set nv_data_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations = list(items) if items else []
        return self

    def with_parameter_ports(self, items: list[ParameterPortAnnotation]) -> "PortPrototypeBuilder":
        """Set parameter_ports list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameter_ports = list(items) if items else []
        return self

    def with_sender_receivers(self, items: list[any (SenderReceiver)]) -> "PortPrototypeBuilder":
        """Set sender_receivers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sender_receivers = list(items) if items else []
        return self

    def with_trigger_port_annotations(self, items: list[TriggerPortAnnotation]) -> "PortPrototypeBuilder":
        """Set trigger_port_annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations = list(items) if items else []
        return self


    def add_client_server(self, item: ClientServerAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to client_servers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.client_servers.append(item)
        return self

    def clear_client_servers(self) -> "PortPrototypeBuilder":
        """Clear all items from client_servers list.

        Returns:
            self for method chaining
        """
        self._obj.client_servers = []
        return self

    def add_io_hw_abstraction_server_annotation(self, item: IoHwAbstractionServerAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to io_hw_abstraction_server_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations.append(item)
        return self

    def clear_io_hw_abstraction_server_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from io_hw_abstraction_server_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.io_hw_abstraction_server_annotations = []
        return self

    def add_mode_port_annotation(self, item: ModePortAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to mode_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations.append(item)
        return self

    def clear_mode_port_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from mode_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.mode_port_annotations = []
        return self

    def add_nv_data_port_annotation(self, item: NvDataPortAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to nv_data_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations.append(item)
        return self

    def clear_nv_data_port_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from nv_data_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.nv_data_port_annotations = []
        return self

    def add_parameter_port(self, item: ParameterPortAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to parameter_ports list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.parameter_ports.append(item)
        return self

    def clear_parameter_ports(self) -> "PortPrototypeBuilder":
        """Clear all items from parameter_ports list.

        Returns:
            self for method chaining
        """
        self._obj.parameter_ports = []
        return self

    def add_sender_receiver(self, item: any (SenderReceiver)) -> "PortPrototypeBuilder":
        """Add a single item to sender_receivers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sender_receivers.append(item)
        return self

    def clear_sender_receivers(self) -> "PortPrototypeBuilder":
        """Clear all items from sender_receivers list.

        Returns:
            self for method chaining
        """
        self._obj.sender_receivers = []
        return self

    def add_trigger_port_annotation(self, item: TriggerPortAnnotation) -> "PortPrototypeBuilder":
        """Add a single item to trigger_port_annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations.append(item)
        return self

    def clear_trigger_port_annotations(self) -> "PortPrototypeBuilder":
        """Clear all items from trigger_port_annotations list.

        Returns:
            self for method chaining
        """
        self._obj.trigger_port_annotations = []
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


    @abstractmethod
    def build(self) -> PortPrototype:
        """Build and return the PortPrototype instance (abstract)."""
        raise NotImplementedError