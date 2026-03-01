"""DdsCpProvidedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 472)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_Dds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import (
    DdsCpServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds.dds_cp_service_instance import DdsCpServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DdsCpProvidedServiceInstance(DdsCpServiceInstance):
    """AUTOSAR DdsCpProvidedServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DDS-CP-PROVIDED-SERVICE-INSTANCE"


    local_unicast_ref: Optional[ARRef]
    minor_version: Optional[PositiveInteger]
    provided_ddses: list[DdsCpServiceInstance]
    static_remote_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "LOCAL-UNICAST-REF": lambda obj, elem: setattr(obj, "local_unicast_ref", ARRef.deserialize(elem)),
        "MINOR-VERSION": lambda obj, elem: setattr(obj, "minor_version", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PROVIDED-DDSES": ("_POLYMORPHIC_LIST", "provided_ddses", ["DdsCpConsumedServiceInstance", "DdsCpProvidedServiceInstance"]),
        "STATIC-REMOTE-REFS": lambda obj, elem: obj.static_remote_refs.append(ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize DdsCpProvidedServiceInstance."""
        super().__init__()
        self.local_unicast_ref: Optional[ARRef] = None
        self.minor_version: Optional[PositiveInteger] = None
        self.provided_ddses: list[DdsCpServiceInstance] = []
        self.static_remote_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize DdsCpProvidedServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DdsCpProvidedServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize local_unicast_ref
        if self.local_unicast_ref is not None:
            serialized = SerializationHelper.serialize_item(self.local_unicast_ref, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOCAL-UNICAST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minor_version
        if self.minor_version is not None:
            serialized = SerializationHelper.serialize_item(self.minor_version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINOR-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize provided_ddses (list to container "PROVIDED-DDSES")
        if self.provided_ddses:
            wrapper = ET.Element("PROVIDED-DDSES")
            for item in self.provided_ddses:
                serialized = SerializationHelper.serialize_item(item, "DdsCpServiceInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize static_remote_refs (list to container "STATIC-REMOTE-REFS")
        if self.static_remote_refs:
            wrapper = ET.Element("STATIC-REMOTE-REFS")
            for item in self.static_remote_refs:
                serialized = SerializationHelper.serialize_item(item, "ApplicationEndpoint")
                if serialized is not None:
                    child_elem = ET.Element("STATIC-REMOTE-REF")
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
    def deserialize(cls, element: ET.Element) -> "DdsCpProvidedServiceInstance":
        """Deserialize XML element to DdsCpProvidedServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DdsCpProvidedServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DdsCpProvidedServiceInstance, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "LOCAL-UNICAST-REF":
                setattr(obj, "local_unicast_ref", ARRef.deserialize(child))
            elif tag == "MINOR-VERSION":
                setattr(obj, "minor_version", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PROVIDED-DDSES":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "DDS-CP-CONSUMED-SERVICE-INSTANCE":
                        obj.provided_ddses.append(SerializationHelper.deserialize_by_tag(child[0], "DdsCpConsumedServiceInstance"))
                    elif concrete_tag == "DDS-CP-PROVIDED-SERVICE-INSTANCE":
                        obj.provided_ddses.append(SerializationHelper.deserialize_by_tag(child[0], "DdsCpProvidedServiceInstance"))
            elif tag == "STATIC-REMOTE-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.static_remote_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ApplicationEndpoint"))

        return obj



class DdsCpProvidedServiceInstanceBuilder(DdsCpServiceInstanceBuilder):
    """Builder for DdsCpProvidedServiceInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DdsCpProvidedServiceInstance = DdsCpProvidedServiceInstance()


    def with_local_unicast(self, value: Optional[ApplicationEndpoint]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set local_unicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.local_unicast = value
        return self

    def with_minor_version(self, value: Optional[PositiveInteger]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set minor_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minor_version = value
        return self

    def with_provided_ddses(self, items: list[DdsCpServiceInstance]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set provided_ddses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_ddses = list(items) if items else []
        return self

    def with_static_remotes(self, items: list[ApplicationEndpoint]) -> "DdsCpProvidedServiceInstanceBuilder":
        """Set static_remotes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.static_remotes = list(items) if items else []
        return self


    def add_provided_dds(self, item: DdsCpServiceInstance) -> "DdsCpProvidedServiceInstanceBuilder":
        """Add a single item to provided_ddses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_ddses.append(item)
        return self

    def clear_provided_ddses(self) -> "DdsCpProvidedServiceInstanceBuilder":
        """Clear all items from provided_ddses list.

        Returns:
            self for method chaining
        """
        self._obj.provided_ddses = []
        return self

    def add_static_remote(self, item: ApplicationEndpoint) -> "DdsCpProvidedServiceInstanceBuilder":
        """Add a single item to static_remotes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.static_remotes.append(item)
        return self

    def clear_static_remotes(self) -> "DdsCpProvidedServiceInstanceBuilder":
        """Clear all items from static_remotes list.

        Returns:
            self for method chaining
        """
        self._obj.static_remotes = []
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


    def build(self) -> DdsCpProvidedServiceInstance:
        """Build and return the DdsCpProvidedServiceInstance instance with validation."""
        self._validate_instance()
        pass
        return self._obj