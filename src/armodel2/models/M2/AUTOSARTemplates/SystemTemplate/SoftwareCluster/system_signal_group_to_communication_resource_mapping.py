"""SystemSignalGroupToCommunicationResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 290)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.system_signal_group import (
    SystemSignalGroup,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SystemSignalGroupToCommunicationResourceMapping(Identifiable):
    """AUTOSAR SystemSignalGroupToCommunicationResourceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SYSTEM-SIGNAL-GROUP-TO-COMMUNICATION-RESOURCE-MAPPING"


    software_cluster_ref: Optional[ARRef]
    system_signal_group_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "SOFTWARE-CLUSTER-REF": lambda obj, elem: setattr(obj, "software_cluster_ref", ARRef.deserialize(elem)),
        "SYSTEM-SIGNAL-GROUP-REF": lambda obj, elem: setattr(obj, "system_signal_group_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SystemSignalGroupToCommunicationResourceMapping."""
        super().__init__()
        self.software_cluster_ref: Optional[ARRef] = None
        self.system_signal_group_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SystemSignalGroupToCommunicationResourceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SystemSignalGroupToCommunicationResourceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize software_cluster_ref
        if self.software_cluster_ref is not None:
            serialized = SerializationHelper.serialize_item(self.software_cluster_ref, "CpSoftwareCluster")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE-CLUSTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize system_signal_group_ref
        if self.system_signal_group_ref is not None:
            serialized = SerializationHelper.serialize_item(self.system_signal_group_ref, "SystemSignalGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SYSTEM-SIGNAL-GROUP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SystemSignalGroupToCommunicationResourceMapping":
        """Deserialize XML element to SystemSignalGroupToCommunicationResourceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SystemSignalGroupToCommunicationResourceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SystemSignalGroupToCommunicationResourceMapping, cls).deserialize(element)

        # Parse software_cluster_ref
        child = SerializationHelper.find_child_element(element, "SOFTWARE-CLUSTER-REF")
        if child is not None:
            software_cluster_ref_value = ARRef.deserialize(child)
            obj.software_cluster_ref = software_cluster_ref_value

        # Parse system_signal_group_ref
        child = SerializationHelper.find_child_element(element, "SYSTEM-SIGNAL-GROUP-REF")
        if child is not None:
            system_signal_group_ref_value = ARRef.deserialize(child)
            obj.system_signal_group_ref = system_signal_group_ref_value

        return obj



class SystemSignalGroupToCommunicationResourceMappingBuilder(IdentifiableBuilder):
    """Builder for SystemSignalGroupToCommunicationResourceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SystemSignalGroupToCommunicationResourceMapping = SystemSignalGroupToCommunicationResourceMapping()


    def with_software_cluster(self, value: Optional[CpSoftwareCluster]) -> "SystemSignalGroupToCommunicationResourceMappingBuilder":
        """Set software_cluster attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.software_cluster = value
        return self

    def with_system_signal_group(self, value: Optional[SystemSignalGroup]) -> "SystemSignalGroupToCommunicationResourceMappingBuilder":
        """Set system_signal_group attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.system_signal_group = value
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


    def build(self) -> SystemSignalGroupToCommunicationResourceMapping:
        """Build and return the SystemSignalGroupToCommunicationResourceMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj