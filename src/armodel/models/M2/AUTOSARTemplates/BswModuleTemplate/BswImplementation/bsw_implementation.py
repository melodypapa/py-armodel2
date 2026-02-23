"""BswImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 120)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 290)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 972)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 207)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 425)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import ImplementationBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_module_configuration_values import (
        EcucModuleConfigurationValues,
    )



from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
class BswImplementation(Implementation):
    """AUTOSAR BswImplementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_release_version: Optional[RevisionLabelString]
    behavior_ref: Optional[ARRef]
    preconfigured_configuration_refs: list[ARRef]
    recommended_configuration_refs: list[ARRef]
    vendor_api_infix: Optional[Identifier]
    vendor_specific_module_def_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BswImplementation."""
        super().__init__()
        self.ar_release_version: Optional[RevisionLabelString] = None
        self.behavior_ref: Optional[ARRef] = None
        self.preconfigured_configuration_refs: list[ARRef] = []
        self.recommended_configuration_refs: list[ARRef] = []
        self.vendor_api_infix: Optional[Identifier] = None
        self.vendor_specific_module_def_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BswImplementation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswImplementation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ar_release_version
        if self.ar_release_version is not None:
            serialized = SerializationHelper.serialize_item(self.ar_release_version, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AR-RELEASE-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize behavior_ref
        if self.behavior_ref is not None:
            serialized = SerializationHelper.serialize_item(self.behavior_ref, "BswInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize preconfigured_configuration_refs (list to container "PRECONFIGURED-CONFIGURATION-REFS")
        if self.preconfigured_configuration_refs:
            wrapper = ET.Element("PRECONFIGURED-CONFIGURATION-REFS")
            for item in self.preconfigured_configuration_refs:
                serialized = SerializationHelper.serialize_item(item, "EcucModuleConfigurationValues")
                if serialized is not None:
                    child_elem = ET.Element("PRECONFIGURED-CONFIGURATION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize recommended_configuration_refs (list to container "RECOMMENDED-CONFIGURATION-REFS")
        if self.recommended_configuration_refs:
            wrapper = ET.Element("RECOMMENDED-CONFIGURATION-REFS")
            for item in self.recommended_configuration_refs:
                serialized = SerializationHelper.serialize_item(item, "EcucModuleConfigurationValues")
                if serialized is not None:
                    child_elem = ET.Element("RECOMMENDED-CONFIGURATION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize vendor_api_infix
        if self.vendor_api_infix is not None:
            serialized = SerializationHelper.serialize_item(self.vendor_api_infix, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VENDOR-API-INFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vendor_specific_module_def_refs (list to container "VENDOR-SPECIFIC-MODULE-DEF-REFS")
        if self.vendor_specific_module_def_refs:
            wrapper = ET.Element("VENDOR-SPECIFIC-MODULE-DEF-REFS")
            for item in self.vendor_specific_module_def_refs:
                serialized = SerializationHelper.serialize_item(item, "EcucModuleDef")
                if serialized is not None:
                    child_elem = ET.Element("VENDOR-SPECIFIC-MODULE-DEF-REF")
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
    def deserialize(cls, element: ET.Element) -> "BswImplementation":
        """Deserialize XML element to BswImplementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswImplementation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswImplementation, cls).deserialize(element)

        # Parse ar_release_version
        child = SerializationHelper.find_child_element(element, "AR-RELEASE-VERSION")
        if child is not None:
            ar_release_version_value = child.text
            obj.ar_release_version = ar_release_version_value

        # Parse behavior_ref
        child = SerializationHelper.find_child_element(element, "BEHAVIOR-REF")
        if child is not None:
            behavior_ref_value = ARRef.deserialize(child)
            obj.behavior_ref = behavior_ref_value

        # Parse preconfigured_configuration_refs (list from container "PRECONFIGURED-CONFIGURATION-REFS")
        obj.preconfigured_configuration_refs = []
        container = SerializationHelper.find_child_element(element, "PRECONFIGURED-CONFIGURATION-REFS")
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
                    obj.preconfigured_configuration_refs.append(child_value)

        # Parse recommended_configuration_refs (list from container "RECOMMENDED-CONFIGURATION-REFS")
        obj.recommended_configuration_refs = []
        container = SerializationHelper.find_child_element(element, "RECOMMENDED-CONFIGURATION-REFS")
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
                    obj.recommended_configuration_refs.append(child_value)

        # Parse vendor_api_infix
        child = SerializationHelper.find_child_element(element, "VENDOR-API-INFIX")
        if child is not None:
            vendor_api_infix_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.vendor_api_infix = vendor_api_infix_value

        # Parse vendor_specific_module_def_refs (list from container "VENDOR-SPECIFIC-MODULE-DEF-REFS")
        obj.vendor_specific_module_def_refs = []
        container = SerializationHelper.find_child_element(element, "VENDOR-SPECIFIC-MODULE-DEF-REFS")
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
                    obj.vendor_specific_module_def_refs.append(child_value)

        return obj



class BswImplementationBuilder(ImplementationBuilder):
    """Builder for BswImplementation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: BswImplementation = BswImplementation()


    def with_ar_release_version(self, value: Optional[RevisionLabelString]) -> "BswImplementationBuilder":
        """Set ar_release_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ar_release_version = value
        return self

    def with_behavior(self, value: Optional[BswInternalBehavior]) -> "BswImplementationBuilder":
        """Set behavior attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.behavior = value
        return self

    def with_preconfigured_configurations(self, items: list[EcucModuleConfigurationValues]) -> "BswImplementationBuilder":
        """Set preconfigured_configurations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.preconfigured_configurations = list(items) if items else []
        return self

    def with_recommended_configurations(self, items: list[EcucModuleConfigurationValues]) -> "BswImplementationBuilder":
        """Set recommended_configurations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.recommended_configurations = list(items) if items else []
        return self

    def with_vendor_api_infix(self, value: Optional[Identifier]) -> "BswImplementationBuilder":
        """Set vendor_api_infix attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vendor_api_infix = value
        return self

    def with_vendor_specific_module_defs(self, items: list[EcucModuleDef]) -> "BswImplementationBuilder":
        """Set vendor_specific_module_defs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.vendor_specific_module_defs = list(items) if items else []
        return self


    def add_preconfigured_configuration(self, item: EcucModuleConfigurationValues) -> "BswImplementationBuilder":
        """Add a single item to preconfigured_configurations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.preconfigured_configurations.append(item)
        return self

    def clear_preconfigured_configurations(self) -> "BswImplementationBuilder":
        """Clear all items from preconfigured_configurations list.

        Returns:
            self for method chaining
        """
        self._obj.preconfigured_configurations = []
        return self

    def add_recommended_configuration(self, item: EcucModuleConfigurationValues) -> "BswImplementationBuilder":
        """Add a single item to recommended_configurations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.recommended_configurations.append(item)
        return self

    def clear_recommended_configurations(self) -> "BswImplementationBuilder":
        """Clear all items from recommended_configurations list.

        Returns:
            self for method chaining
        """
        self._obj.recommended_configurations = []
        return self

    def add_vendor_specific_module_def(self, item: EcucModuleDef) -> "BswImplementationBuilder":
        """Add a single item to vendor_specific_module_defs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.vendor_specific_module_defs.append(item)
        return self

    def clear_vendor_specific_module_defs(self) -> "BswImplementationBuilder":
        """Clear all items from vendor_specific_module_defs list.

        Returns:
            self for method chaining
        """
        self._obj.vendor_specific_module_defs = []
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


    def build(self) -> BswImplementation:
        """Build and return the BswImplementation instance with validation."""
        self._validate_instance()
        pass
        return self._obj