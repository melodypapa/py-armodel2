"""EcucModuleConfigurationValues AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 313)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 110)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 441)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCDescriptionTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RevisionLabelString,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)
from armodel2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.BswModuleTemplate.BswImplementation.bsw_implementation import (
        BswImplementation,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class EcucModuleConfigurationValues(ARElement):
    """AUTOSAR EcucModuleConfigurationValues."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ECUC-MODULE-CONFIGURATION-VALUES"


    containers: list[EcucContainerValue]
    definition_ref: Optional[ARRef]
    ecuc_def_edition: Optional[RevisionLabelString]
    implementation: Optional[Any]
    module_ref: Optional[ARRef]
    post_build_variant: Optional[Boolean]
    _DESERIALIZE_DISPATCH = {
        "CONTAINERS": lambda obj, elem: obj.containers.append(SerializationHelper.deserialize_by_tag(elem, "EcucContainerValue")),
        "DEFINITION-REF": lambda obj, elem: setattr(obj, "definition_ref", ARRef.deserialize(elem)),
        "ECUC-DEF-EDITION": lambda obj, elem: setattr(obj, "ecuc_def_edition", SerializationHelper.deserialize_by_tag(elem, "RevisionLabelString")),
        "IMPLEMENTATION": lambda obj, elem: setattr(obj, "implementation", SerializationHelper.deserialize_by_tag(elem, "any (EcucConfiguration)")),
        "MODULE-REF": lambda obj, elem: setattr(obj, "module_ref", ARRef.deserialize(elem)),
        "POST-BUILD-VARIANT": lambda obj, elem: setattr(obj, "post_build_variant", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
    }


    def __init__(self) -> None:
        """Initialize EcucModuleConfigurationValues."""
        super().__init__()
        self.containers: list[EcucContainerValue] = []
        self.definition_ref: Optional[ARRef] = None
        self.ecuc_def_edition: Optional[RevisionLabelString] = None
        self.implementation: Optional[Any] = None
        self.module_ref: Optional[ARRef] = None
        self.post_build_variant: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucModuleConfigurationValues to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucModuleConfigurationValues, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize containers (list to container "CONTAINERS")
        if self.containers:
            wrapper = ET.Element("CONTAINERS")
            for item in self.containers:
                serialized = SerializationHelper.serialize_item(item, "EcucContainerValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize definition_ref
        if self.definition_ref is not None:
            serialized = SerializationHelper.serialize_item(self.definition_ref, "EcucModuleDef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEFINITION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ecuc_def_edition
        if self.ecuc_def_edition is not None:
            serialized = SerializationHelper.serialize_item(self.ecuc_def_edition, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ECUC-DEF-EDITION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize implementation
        if self.implementation is not None:
            serialized = SerializationHelper.serialize_item(self.implementation, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize module_ref
        if self.module_ref is not None:
            serialized = SerializationHelper.serialize_item(self.module_ref, "BswImplementation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODULE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize post_build_variant
        if self.post_build_variant is not None:
            serialized = SerializationHelper.serialize_item(self.post_build_variant, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POST-BUILD-VARIANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucModuleConfigurationValues":
        """Deserialize XML element to EcucModuleConfigurationValues object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucModuleConfigurationValues object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucModuleConfigurationValues, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONTAINERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.containers.append(SerializationHelper.deserialize_by_tag(item_elem, "EcucContainerValue"))
            elif tag == "DEFINITION-REF":
                setattr(obj, "definition_ref", ARRef.deserialize(child))
            elif tag == "ECUC-DEF-EDITION":
                setattr(obj, "ecuc_def_edition", SerializationHelper.deserialize_by_tag(child, "RevisionLabelString"))
            elif tag == "IMPLEMENTATION":
                setattr(obj, "implementation", SerializationHelper.deserialize_by_tag(child, "any (EcucConfiguration)"))
            elif tag == "MODULE-REF":
                setattr(obj, "module_ref", ARRef.deserialize(child))
            elif tag == "POST-BUILD-VARIANT":
                setattr(obj, "post_build_variant", SerializationHelper.deserialize_by_tag(child, "Boolean"))

        return obj



class EcucModuleConfigurationValuesBuilder(ARElementBuilder):
    """Builder for EcucModuleConfigurationValues with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EcucModuleConfigurationValues = EcucModuleConfigurationValues()


    def with_containers(self, items: list[EcucContainerValue]) -> "EcucModuleConfigurationValuesBuilder":
        """Set containers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.containers = list(items) if items else []
        return self

    def with_definition(self, value: Optional[EcucModuleDef]) -> "EcucModuleConfigurationValuesBuilder":
        """Set definition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.definition = value
        return self

    def with_ecuc_def_edition(self, value: Optional[RevisionLabelString]) -> "EcucModuleConfigurationValuesBuilder":
        """Set ecuc_def_edition attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ecuc_def_edition = value
        return self

    def with_implementation(self, value: Optional[any (EcucConfiguration)]) -> "EcucModuleConfigurationValuesBuilder":
        """Set implementation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.implementation = value
        return self

    def with_module(self, value: Optional[BswImplementation]) -> "EcucModuleConfigurationValuesBuilder":
        """Set module attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.module = value
        return self

    def with_post_build_variant(self, value: Optional[Boolean]) -> "EcucModuleConfigurationValuesBuilder":
        """Set post_build_variant attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.post_build_variant = value
        return self


    def add_container(self, item: EcucContainerValue) -> "EcucModuleConfigurationValuesBuilder":
        """Add a single item to containers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.containers.append(item)
        return self

    def clear_containers(self) -> "EcucModuleConfigurationValuesBuilder":
        """Clear all items from containers list.

        Returns:
            self for method chaining
        """
        self._obj.containers = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "container",
        "definition",
        "ecucDefEdition",
        "implementation",
        "module",
        "postBuildVariant",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EcucModuleConfigurationValues:
        """Build and return the EcucModuleConfigurationValues instance with validation."""
        self._validate_instance()
        return self._obj