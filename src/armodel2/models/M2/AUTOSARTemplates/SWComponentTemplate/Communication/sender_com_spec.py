"""SenderComSpec AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 178)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2054)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import PPortComSpecBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    HandleOutOfRangeEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.autosar_data_prototype import (
    AutosarDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.composite_network_representation import (
    CompositeNetworkRepresentation,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transmission_acknowledgement_request import (
    TransmissionAcknowledgementRequest,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.transmission_com_spec_props import (
    TransmissionComSpecProps,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SenderComSpec(PPortComSpec, ABC):
    """AUTOSAR SenderComSpec."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    composite_network_representations: list[CompositeNetworkRepresentation]
    data_element_ref: Optional[ARRef]
    handle_out_of_range: Optional[HandleOutOfRangeEnum]
    network_representation: Optional[SwDataDefProps]
    transmission_acknowledge: Optional[TransmissionAcknowledgementRequest]
    transmission_props: Optional[TransmissionComSpecProps]
    uses_end_to_end_protection: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize SenderComSpec."""
        super().__init__()
        self.composite_network_representations: list[CompositeNetworkRepresentation] = []
        self.data_element_ref: Optional[ARRef] = None
        self.handle_out_of_range: Optional[HandleOutOfRangeEnum] = None
        self.network_representation: Optional[SwDataDefProps] = None
        self.transmission_acknowledge: Optional[TransmissionAcknowledgementRequest] = None
        self.transmission_props: Optional[TransmissionComSpecProps] = None
        self.uses_end_to_end_protection: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize SenderComSpec to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SenderComSpec, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize composite_network_representations (list to container "COMPOSITE-NETWORK-REPRESENTATIONS")
        if self.composite_network_representations:
            wrapper = ET.Element("COMPOSITE-NETWORK-REPRESENTATIONS")
            for item in self.composite_network_representations:
                serialized = SerializationHelper.serialize_item(item, "CompositeNetworkRepresentation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize data_element_ref
        if self.data_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_element_ref, "AutosarDataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize handle_out_of_range
        if self.handle_out_of_range is not None:
            serialized = SerializationHelper.serialize_item(self.handle_out_of_range, "HandleOutOfRangeEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HANDLE-OUT-OF-RANGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_representation
        if self.network_representation is not None:
            serialized = SerializationHelper.serialize_item(self.network_representation, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-REPRESENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission_acknowledge
        if self.transmission_acknowledge is not None:
            serialized = SerializationHelper.serialize_item(self.transmission_acknowledge, "TransmissionAcknowledgementRequest")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION-ACKNOWLEDGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmission_props
        if self.transmission_props is not None:
            serialized = SerializationHelper.serialize_item(self.transmission_props, "TransmissionComSpecProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMISSION-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize uses_end_to_end_protection
        if self.uses_end_to_end_protection is not None:
            serialized = SerializationHelper.serialize_item(self.uses_end_to_end_protection, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USES-END-TO-END-PROTECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderComSpec":
        """Deserialize XML element to SenderComSpec object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderComSpec object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SenderComSpec, cls).deserialize(element)

        # Parse composite_network_representations (list from container "COMPOSITE-NETWORK-REPRESENTATIONS")
        obj.composite_network_representations = []
        container = SerializationHelper.find_child_element(element, "COMPOSITE-NETWORK-REPRESENTATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.composite_network_representations.append(child_value)

        # Parse data_element_ref
        child = SerializationHelper.find_child_element(element, "DATA-ELEMENT-REF")
        if child is not None:
            data_element_ref_value = ARRef.deserialize(child)
            obj.data_element_ref = data_element_ref_value

        # Parse handle_out_of_range
        child = SerializationHelper.find_child_element(element, "HANDLE-OUT-OF-RANGE")
        if child is not None:
            handle_out_of_range_value = HandleOutOfRangeEnum.deserialize(child)
            obj.handle_out_of_range = handle_out_of_range_value

        # Parse network_representation
        child = SerializationHelper.find_child_element(element, "NETWORK-REPRESENTATION")
        if child is not None:
            network_representation_value = SerializationHelper.deserialize_by_tag(child, "SwDataDefProps")
            obj.network_representation = network_representation_value

        # Parse transmission_acknowledge
        child = SerializationHelper.find_child_element(element, "TRANSMISSION-ACKNOWLEDGE")
        if child is not None:
            transmission_acknowledge_value = SerializationHelper.deserialize_by_tag(child, "TransmissionAcknowledgementRequest")
            obj.transmission_acknowledge = transmission_acknowledge_value

        # Parse transmission_props
        child = SerializationHelper.find_child_element(element, "TRANSMISSION-PROPS")
        if child is not None:
            transmission_props_value = SerializationHelper.deserialize_by_tag(child, "TransmissionComSpecProps")
            obj.transmission_props = transmission_props_value

        # Parse uses_end_to_end_protection
        child = SerializationHelper.find_child_element(element, "USES-END-TO-END-PROTECTION")
        if child is not None:
            uses_end_to_end_protection_value = child.text
            obj.uses_end_to_end_protection = uses_end_to_end_protection_value

        return obj



class SenderComSpecBuilder(PPortComSpecBuilder):
    """Builder for SenderComSpec with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SenderComSpec = SenderComSpec()


    def with_composite_network_representations(self, items: list[CompositeNetworkRepresentation]) -> "SenderComSpecBuilder":
        """Set composite_network_representations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.composite_network_representations = list(items) if items else []
        return self

    def with_data_element(self, value: Optional[AutosarDataPrototype]) -> "SenderComSpecBuilder":
        """Set data_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_element = value
        return self

    def with_handle_out_of_range(self, value: Optional[HandleOutOfRangeEnum]) -> "SenderComSpecBuilder":
        """Set handle_out_of_range attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.handle_out_of_range = value
        return self

    def with_network_representation(self, value: Optional[SwDataDefProps]) -> "SenderComSpecBuilder":
        """Set network_representation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network_representation = value
        return self

    def with_transmission_acknowledge(self, value: Optional[TransmissionAcknowledgementRequest]) -> "SenderComSpecBuilder":
        """Set transmission_acknowledge attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmission_acknowledge = value
        return self

    def with_transmission_props(self, value: Optional[TransmissionComSpecProps]) -> "SenderComSpecBuilder":
        """Set transmission_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.transmission_props = value
        return self

    def with_uses_end_to_end_protection(self, value: Optional[Boolean]) -> "SenderComSpecBuilder":
        """Set uses_end_to_end_protection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uses_end_to_end_protection = value
        return self


    def add_composite_network_representation(self, item: CompositeNetworkRepresentation) -> "SenderComSpecBuilder":
        """Add a single item to composite_network_representations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.composite_network_representations.append(item)
        return self

    def clear_composite_network_representations(self) -> "SenderComSpecBuilder":
        """Clear all items from composite_network_representations list.

        Returns:
            self for method chaining
        """
        self._obj.composite_network_representations = []
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
    def build(self) -> SenderComSpec:
        """Build and return the SenderComSpec instance (abstract)."""
        raise NotImplementedError