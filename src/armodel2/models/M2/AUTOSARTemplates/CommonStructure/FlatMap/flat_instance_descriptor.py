"""FlatInstanceDescriptor AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 316)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 989)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 966)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_FlatMap.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.rte_plugin_props import (
    RtePluginProps,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class FlatInstanceDescriptor(Identifiable):
    """AUTOSAR FlatInstanceDescriptor."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLAT-INSTANCE-DESCRIPTOR"


    ecu_extract: Optional[AtpFeature]
    role: Optional[Identifier]
    rte_plugin_props: Optional[RtePluginProps]
    sw_data_def: Optional[SwDataDefProps]
    upstream: Optional[AtpFeature]
    _DESERIALIZE_DISPATCH = {
        "ECU-EXTRACT": ("_POLYMORPHIC", "ecu_extract", ["AtpPrototype", "AtpStructureElement"]),
        "ROLE": lambda obj, elem: setattr(obj, "role", SerializationHelper.deserialize_by_tag(elem, "Identifier")),
        "RTE-PLUGIN-PROPS": lambda obj, elem: setattr(obj, "rte_plugin_props", SerializationHelper.deserialize_by_tag(elem, "RtePluginProps")),
        "SW-DATA-DEF": lambda obj, elem: setattr(obj, "sw_data_def", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
        "UPSTREAM": ("_POLYMORPHIC", "upstream", ["AtpPrototype", "AtpStructureElement"]),
    }


    def __init__(self) -> None:
        """Initialize FlatInstanceDescriptor."""
        super().__init__()
        self.ecu_extract: Optional[AtpFeature] = None
        self.role: Optional[Identifier] = None
        self.rte_plugin_props: Optional[RtePluginProps] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.upstream: Optional[AtpFeature] = None

    def serialize(self) -> ET.Element:
        """Serialize FlatInstanceDescriptor to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlatInstanceDescriptor, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ecu_extract
        if self.ecu_extract is not None:
            serialized = SerializationHelper.serialize_item(self.ecu_extract, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECU-EXTRACT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize role
        if self.role is not None:
            serialized = SerializationHelper.serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rte_plugin_props
        if self.rte_plugin_props is not None:
            serialized = SerializationHelper.serialize_item(self.rte_plugin_props, "RtePluginProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RTE-PLUGIN-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_data_def
        if self.sw_data_def is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_def, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize upstream
        if self.upstream is not None:
            serialized = SerializationHelper.serialize_item(self.upstream, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UPSTREAM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlatInstanceDescriptor":
        """Deserialize XML element to FlatInstanceDescriptor object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlatInstanceDescriptor object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlatInstanceDescriptor, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ECU-EXTRACT":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-PROTOTYPE":
                        setattr(obj, "ecu_extract", SerializationHelper.deserialize_by_tag(child[0], "AtpPrototype"))
                    elif concrete_tag == "ATP-STRUCTURE-ELEMENT":
                        setattr(obj, "ecu_extract", SerializationHelper.deserialize_by_tag(child[0], "AtpStructureElement"))
            elif tag == "ROLE":
                setattr(obj, "role", SerializationHelper.deserialize_by_tag(child, "Identifier"))
            elif tag == "RTE-PLUGIN-PROPS":
                setattr(obj, "rte_plugin_props", SerializationHelper.deserialize_by_tag(child, "RtePluginProps"))
            elif tag == "SW-DATA-DEF":
                setattr(obj, "sw_data_def", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))
            elif tag == "UPSTREAM":
                # Check first child element for concrete type
                if len(child) > 0:
                    concrete_tag = child[0].tag.split(ns_split, 1)[1] if child[0].tag.startswith("{") else child[0].tag
                    if concrete_tag == "ATP-PROTOTYPE":
                        setattr(obj, "upstream", SerializationHelper.deserialize_by_tag(child[0], "AtpPrototype"))
                    elif concrete_tag == "ATP-STRUCTURE-ELEMENT":
                        setattr(obj, "upstream", SerializationHelper.deserialize_by_tag(child[0], "AtpStructureElement"))

        return obj



class FlatInstanceDescriptorBuilder(IdentifiableBuilder):
    """Builder for FlatInstanceDescriptor with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlatInstanceDescriptor = FlatInstanceDescriptor()


    def with_ecu_extract(self, value: Optional[AtpFeature]) -> "FlatInstanceDescriptorBuilder":
        """Set ecu_extract attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecu_extract = value
        return self

    def with_role(self, value: Optional[Identifier]) -> "FlatInstanceDescriptorBuilder":
        """Set role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.role = value
        return self

    def with_rte_plugin_props(self, value: Optional[RtePluginProps]) -> "FlatInstanceDescriptorBuilder":
        """Set rte_plugin_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.rte_plugin_props = value
        return self

    def with_sw_data_def(self, value: Optional[SwDataDefProps]) -> "FlatInstanceDescriptorBuilder":
        """Set sw_data_def attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_data_def = value
        return self

    def with_upstream(self, value: Optional[AtpFeature]) -> "FlatInstanceDescriptorBuilder":
        """Set upstream attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.upstream = value
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


    def build(self) -> FlatInstanceDescriptor:
        """Build and return the FlatInstanceDescriptor instance with validation."""
        self._validate_instance()
        pass
        return self._obj