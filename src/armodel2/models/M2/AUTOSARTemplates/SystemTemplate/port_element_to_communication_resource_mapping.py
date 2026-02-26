"""PortElementToCommunicationResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 905)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.variable_data_prototype import (
    VariableDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PortElementToCommunicationResourceMapping(Identifiable):
    """AUTOSAR PortElementToCommunicationResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_server_instance_ref: Optional[ClientServerOperation]
    communication_ref: Optional[ARRef]
    mode_ref: Optional[ARRef]
    parameter_data_in_system_instance_ref: Optional[ARRef]
    trigger_ref: Optional[ARRef]
    variable_data_system_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize PortElementToCommunicationResourceMapping."""
        super().__init__()
        self.client_server_instance_ref: Optional[ClientServerOperation] = None
        self.communication_ref: Optional[ARRef] = None
        self.mode_ref: Optional[ARRef] = None
        self.parameter_data_in_system_instance_ref: Optional[ARRef] = None
        self.trigger_ref: Optional[ARRef] = None
        self.variable_data_system_instance_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PortElementToCommunicationResourceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PortElementToCommunicationResourceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_server_instance_ref
        if self.client_server_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.client_server_instance_ref, "ClientServerOperation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-SERVER-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize communication_ref
        if self.communication_ref is not None:
            serialized = SerializationHelper.serialize_item(self.communication_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_ref
        if self.mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize parameter_data_in_system_instance_ref
        if self.parameter_data_in_system_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.parameter_data_in_system_instance_ref, "ParameterDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PARAMETER-DATA-IN-SYSTEM-INSTANCE-REF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_ref
        if self.trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variable_data_system_instance_ref
        if self.variable_data_system_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.variable_data_system_instance_ref, "VariableDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIABLE-DATA-SYSTEM-INSTANCE-REF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortElementToCommunicationResourceMapping":
        """Deserialize XML element to PortElementToCommunicationResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortElementToCommunicationResourceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PortElementToCommunicationResourceMapping, cls).deserialize(element)

        # Parse client_server_instance_ref
        child = SerializationHelper.find_child_element(element, "CLIENT-SERVER-INSTANCE-REF")
        if child is not None:
            client_server_instance_ref_value = SerializationHelper.deserialize_by_tag(child, "ClientServerOperation")
            obj.client_server_instance_ref = client_server_instance_ref_value

        # Parse communication_ref
        child = SerializationHelper.find_child_element(element, "COMMUNICATION-REF")
        if child is not None:
            communication_ref_value = ARRef.deserialize(child)
            obj.communication_ref = communication_ref_value

        # Parse mode_ref
        child = SerializationHelper.find_child_element(element, "MODE-REF")
        if child is not None:
            mode_ref_value = ARRef.deserialize(child)
            obj.mode_ref = mode_ref_value

        # Parse parameter_data_in_system_instance_ref
        child = SerializationHelper.find_child_element(element, "PARAMETER-DATA-IN-SYSTEM-INSTANCE-REF-REF")
        if child is not None:
            parameter_data_in_system_instance_ref_value = ARRef.deserialize(child)
            obj.parameter_data_in_system_instance_ref = parameter_data_in_system_instance_ref_value

        # Parse trigger_ref
        child = SerializationHelper.find_child_element(element, "TRIGGER-REF")
        if child is not None:
            trigger_ref_value = ARRef.deserialize(child)
            obj.trigger_ref = trigger_ref_value

        # Parse variable_data_system_instance_ref
        child = SerializationHelper.find_child_element(element, "VARIABLE-DATA-SYSTEM-INSTANCE-REF-REF")
        if child is not None:
            variable_data_system_instance_ref_value = ARRef.deserialize(child)
            obj.variable_data_system_instance_ref = variable_data_system_instance_ref_value

        return obj



class PortElementToCommunicationResourceMappingBuilder(IdentifiableBuilder):
    """Builder for PortElementToCommunicationResourceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PortElementToCommunicationResourceMapping = PortElementToCommunicationResourceMapping()


    def with_client_server_instance_ref(self, value: Optional[ClientServerOperation]) -> "PortElementToCommunicationResourceMappingBuilder":
        """Set client_server_instance_ref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.client_server_instance_ref = value
        return self

    def with_communication(self, value: Optional[CpSoftwareCluster]) -> "PortElementToCommunicationResourceMappingBuilder":
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

    def with_mode(self, value: Optional[ModeDeclarationGroup]) -> "PortElementToCommunicationResourceMappingBuilder":
        """Set mode attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mode = value
        return self

    def with_parameter_data_in_system_instance_ref(self, value: Optional[ParameterDataPrototype]) -> "PortElementToCommunicationResourceMappingBuilder":
        """Set parameter_data_in_system_instance_ref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.parameter_data_in_system_instance_ref = value
        return self

    def with_trigger(self, value: Optional[Trigger]) -> "PortElementToCommunicationResourceMappingBuilder":
        """Set trigger attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.trigger = value
        return self

    def with_variable_data_system_instance_ref(self, value: Optional[VariableDataPrototype]) -> "PortElementToCommunicationResourceMappingBuilder":
        """Set variable_data_system_instance_ref attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.variable_data_system_instance_ref = value
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


    def build(self) -> PortElementToCommunicationResourceMapping:
        """Build and return the PortElementToCommunicationResourceMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj