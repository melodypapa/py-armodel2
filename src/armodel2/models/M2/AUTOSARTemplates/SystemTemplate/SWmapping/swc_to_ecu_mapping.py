"""SwcToEcuMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 197)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SWmapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import instance_ref
from armodel2.serialization.decorators import ref_conditional

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.ecu_instance import (
    EcuInstance,
)
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs.component_in_system_instance_ref import (
        ComponentInSystemInstanceRef,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SwcToEcuMapping(Identifiable):
    """AUTOSAR SwcToEcuMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SWC-TO-ECU-MAPPING"


    _component_irefs: list[ComponentInSystemInstanceRef]
    controlled_hw_element_ref: Optional[ARRef]
    ecu_instance_ref: Optional[ARRef]
    processing_unit_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "COMPONENTS-IREF": lambda obj, elem: obj._component_irefs.append(SerializationHelper.deserialize_by_tag(elem, "ComponentInSystemInstanceRef")),
        "CONTROLLED-HW-ELEMENT-REF": lambda obj, elem: setattr(obj, "controlled_hw_element_ref", ARRef.deserialize(elem)),
        "ECU-INSTANCE-REF": lambda obj, elem: setattr(obj, "ecu_instance_ref", ARRef.deserialize(elem)),
        "PROCESSING-UNIT-REF": lambda obj, elem: setattr(obj, "processing_unit_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SwcToEcuMapping."""
        super().__init__()
        self._component_irefs: list[ComponentInSystemInstanceRef] = []
        self.controlled_hw_element_ref: Optional[ARRef] = None
        self.ecu_instance_ref: Optional[ARRef] = None
        self.processing_unit_ref: Optional[ARRef] = None
    @property
    @instance_ref(flatten=True, list_type='multi')
    def component_irefs(self) -> list[ComponentInSystemInstanceRef]:
        """Get component_irefs instance reference."""
        return self._component_irefs

    @component_irefs.setter
    def component_irefs(self, value: list[ComponentInSystemInstanceRef]) -> None:
        """Set component_irefs instance reference."""
        self._component_irefs = value


    def serialize(self) -> ET.Element:
        """Serialize SwcToEcuMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcToEcuMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize component_irefs (list of instance references with multi-wrapper pattern)
        if self.component_irefs:
            irefs_container = ET.Element("COMPONENT-IREFS")
            for item in self.component_irefs:
                serialized = SerializationHelper.serialize_item(item, "ComponentInSystemInstanceRef")
                if serialized is not None:
                    # Wrap each item in its own IREF wrapper
                    iref_wrapper = ET.Element("COMPONENT-IREF")
                    # Flatten: append children of serialized element directly to iref wrapper
                    for child in serialized:
                        iref_wrapper.append(child)
                    irefs_container.append(iref_wrapper)
            elem.append(irefs_container)

        # Serialize controlled_hw_element_ref
        if self.controlled_hw_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.controlled_hw_element_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONTROLLED-HW-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize processing_unit_ref
        if self.processing_unit_ref is not None:
            serialized = SerializationHelper.serialize_item(self.processing_unit_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROCESSING-UNIT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcToEcuMapping":
        """Deserialize XML element to SwcToEcuMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcToEcuMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcToEcuMapping, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "COMPONENT-IREFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj._component_irefs.append(SerializationHelper.deserialize_by_tag(item_elem, "ComponentInSystemInstanceRef"))
            elif tag == "CONTROLLED-HW-ELEMENT-REF":
                setattr(obj, "controlled_hw_element_ref", ARRef.deserialize(child))
            elif tag == "ECU-INSTANCE-REF":
                setattr(obj, "ecu_instance_ref", ARRef.deserialize(child))
            elif tag == "PROCESSING-UNIT-REF":
                setattr(obj, "processing_unit_ref", ARRef.deserialize(child))

        return obj



class SwcToEcuMappingBuilder(IdentifiableBuilder):
    """Builder for SwcToEcuMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwcToEcuMapping = SwcToEcuMapping()


    def with_components(self, items: list[ComponentInSystemInstanceRef]) -> "SwcToEcuMappingBuilder":
        """Set components list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.components = list(items) if items else []
        return self

    def with_controlled_hw_element(self, value: Optional[HwElement]) -> "SwcToEcuMappingBuilder":
        """Set controlled_hw_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.controlled_hw_element = value
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> "SwcToEcuMappingBuilder":
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

    def with_processing_unit(self, value: Optional[HwElement]) -> "SwcToEcuMappingBuilder":
        """Set processing_unit attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.processing_unit = value
        return self


    def add_component(self, item: ComponentInSystemInstanceRef) -> "SwcToEcuMappingBuilder":
        """Add a single item to components list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.components.append(item)
        return self

    def clear_components(self) -> "SwcToEcuMappingBuilder":
        """Clear all items from components list.

        Returns:
            self for method chaining
        """
        self._obj.components = []
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


    def build(self) -> SwcToEcuMapping:
        """Build and return the SwcToEcuMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj