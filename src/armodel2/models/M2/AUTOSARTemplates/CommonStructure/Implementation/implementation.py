"""Implementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 126)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 619)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2029)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 449)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Implementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    ProgramminglanguageEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RevisionLabelString,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_manifest import (
    BuildActionManifest,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.code import (
    Code,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.compiler import (
    Compiler,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.linker import (
    Linker,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_support_data import (
    McSupportData,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.resource_consumption import (
    ResourceConsumption,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.SwcBswMapping.swc_bsw_mapping import (
    SwcBswMapping,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Implementation(ARElement, ABC):
    """AUTOSAR Implementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    build_action_manifest_ref: Optional[ARRef]
    code_descriptors: list[Code]
    compilers: list[Compiler]
    generated_artifacts: list[DependencyOnArtifact]
    hw_element_refs: list[ARRef]
    linkers: list[Linker]
    mc_support: Optional[McSupportData]
    programming_language: Optional[ProgramminglanguageEnum]
    required_artifacts: list[DependencyOnArtifact]
    required_generator_tools: list[DependencyOnArtifact]
    resource_consumption: Optional[ResourceConsumption]
    swc_bsw_mapping_ref: Optional[ARRef]
    sw_version: Optional[RevisionLabelString]
    used_code_generator: Optional[String]
    vendor_id: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "BUILD-ACTION-MANIFEST-REF": lambda obj, elem: setattr(obj, "build_action_manifest_ref", ARRef.deserialize(elem)),
        "CODE-DESCRIPTORS": lambda obj, elem: obj.code_descriptors.append(SerializationHelper.deserialize_by_tag(elem, "Code")),
        "COMPILERS": lambda obj, elem: obj.compilers.append(SerializationHelper.deserialize_by_tag(elem, "Compiler")),
        "GENERATED-ARTIFACTS": lambda obj, elem: obj.generated_artifacts.append(SerializationHelper.deserialize_by_tag(elem, "DependencyOnArtifact")),
        "HW-ELEMENT-REFS": lambda obj, elem: obj.hw_element_refs.append(ARRef.deserialize(elem)),
        "LINKERS": lambda obj, elem: obj.linkers.append(SerializationHelper.deserialize_by_tag(elem, "Linker")),
        "MC-SUPPORT": lambda obj, elem: setattr(obj, "mc_support", SerializationHelper.deserialize_by_tag(elem, "McSupportData")),
        "PROGRAMMING-LANGUAGE": lambda obj, elem: setattr(obj, "programming_language", ProgramminglanguageEnum.deserialize(elem)),
        "REQUIRED-ARTIFACTS": lambda obj, elem: obj.required_artifacts.append(SerializationHelper.deserialize_by_tag(elem, "DependencyOnArtifact")),
        "REQUIRED-GENERATOR-TOOLS": lambda obj, elem: obj.required_generator_tools.append(SerializationHelper.deserialize_by_tag(elem, "DependencyOnArtifact")),
        "RESOURCE-CONSUMPTION": lambda obj, elem: setattr(obj, "resource_consumption", SerializationHelper.deserialize_by_tag(elem, "ResourceConsumption")),
        "SWC-BSW-MAPPING-REF": lambda obj, elem: setattr(obj, "swc_bsw_mapping_ref", ARRef.deserialize(elem)),
        "SW-VERSION": lambda obj, elem: setattr(obj, "sw_version", SerializationHelper.deserialize_by_tag(elem, "RevisionLabelString")),
        "USED-CODE-GENERATOR": lambda obj, elem: setattr(obj, "used_code_generator", SerializationHelper.deserialize_by_tag(elem, "String")),
        "VENDOR-ID": lambda obj, elem: setattr(obj, "vendor_id", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize Implementation."""
        super().__init__()
        self.build_action_manifest_ref: Optional[ARRef] = None
        self.code_descriptors: list[Code] = []
        self.compilers: list[Compiler] = []
        self.generated_artifacts: list[DependencyOnArtifact] = []
        self.hw_element_refs: list[ARRef] = []
        self.linkers: list[Linker] = []
        self.mc_support: Optional[McSupportData] = None
        self.programming_language: Optional[ProgramminglanguageEnum] = None
        self.required_artifacts: list[DependencyOnArtifact] = []
        self.required_generator_tools: list[DependencyOnArtifact] = []
        self.resource_consumption: Optional[ResourceConsumption] = None
        self.swc_bsw_mapping_ref: Optional[ARRef] = None
        self.sw_version: Optional[RevisionLabelString] = None
        self.used_code_generator: Optional[String] = None
        self.vendor_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize Implementation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Implementation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize build_action_manifest_ref
        if self.build_action_manifest_ref is not None:
            serialized = SerializationHelper.serialize_item(self.build_action_manifest_ref, "BuildActionManifest")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUILD-ACTION-MANIFEST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize code_descriptors (list to container "CODE-DESCRIPTORS")
        if self.code_descriptors:
            wrapper = ET.Element("CODE-DESCRIPTORS")
            for item in self.code_descriptors:
                serialized = SerializationHelper.serialize_item(item, "Code")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize compilers (list to container "COMPILERS")
        if self.compilers:
            wrapper = ET.Element("COMPILERS")
            for item in self.compilers:
                serialized = SerializationHelper.serialize_item(item, "Compiler")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize generated_artifacts (list to container "GENERATED-ARTIFACTS")
        if self.generated_artifacts:
            wrapper = ET.Element("GENERATED-ARTIFACTS")
            for item in self.generated_artifacts:
                serialized = SerializationHelper.serialize_item(item, "DependencyOnArtifact")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize hw_element_refs (list to container "HW-ELEMENT-REFS")
        if self.hw_element_refs:
            wrapper = ET.Element("HW-ELEMENT-REFS")
            for item in self.hw_element_refs:
                serialized = SerializationHelper.serialize_item(item, "HwElement")
                if serialized is not None:
                    child_elem = ET.Element("HW-ELEMENT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize linkers (list to container "LINKERS")
        if self.linkers:
            wrapper = ET.Element("LINKERS")
            for item in self.linkers:
                serialized = SerializationHelper.serialize_item(item, "Linker")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_support
        if self.mc_support is not None:
            serialized = SerializationHelper.serialize_item(self.mc_support, "McSupportData")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MC-SUPPORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize programming_language
        if self.programming_language is not None:
            serialized = SerializationHelper.serialize_item(self.programming_language, "ProgramminglanguageEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROGRAMMING-LANGUAGE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize required_artifacts (list to container "REQUIRED-ARTIFACTS")
        if self.required_artifacts:
            wrapper = ET.Element("REQUIRED-ARTIFACTS")
            for item in self.required_artifacts:
                serialized = SerializationHelper.serialize_item(item, "DependencyOnArtifact")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize required_generator_tools (list to container "REQUIRED-GENERATOR-TOOLS")
        if self.required_generator_tools:
            wrapper = ET.Element("REQUIRED-GENERATOR-TOOLS")
            for item in self.required_generator_tools:
                serialized = SerializationHelper.serialize_item(item, "DependencyOnArtifact")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize resource_consumption
        if self.resource_consumption is not None:
            serialized = SerializationHelper.serialize_item(self.resource_consumption, "ResourceConsumption")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RESOURCE-CONSUMPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_bsw_mapping_ref
        if self.swc_bsw_mapping_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_bsw_mapping_ref, "SwcBswMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-BSW-MAPPING-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_version
        if self.sw_version is not None:
            serialized = SerializationHelper.serialize_item(self.sw_version, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize used_code_generator
        if self.used_code_generator is not None:
            serialized = SerializationHelper.serialize_item(self.used_code_generator, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USED-CODE-GENERATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vendor_id
        if self.vendor_id is not None:
            serialized = SerializationHelper.serialize_item(self.vendor_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VENDOR-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Implementation":
        """Deserialize XML element to Implementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Implementation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Implementation, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "BUILD-ACTION-MANIFEST-REF":
                setattr(obj, "build_action_manifest_ref", ARRef.deserialize(child))
            elif tag == "CODE-DESCRIPTORS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.code_descriptors.append(SerializationHelper.deserialize_by_tag(item_elem, "Code"))
            elif tag == "COMPILERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.compilers.append(SerializationHelper.deserialize_by_tag(item_elem, "Compiler"))
            elif tag == "GENERATED-ARTIFACTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.generated_artifacts.append(SerializationHelper.deserialize_by_tag(item_elem, "DependencyOnArtifact"))
            elif tag == "HW-ELEMENT-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.hw_element_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "HwElement"))
            elif tag == "LINKERS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.linkers.append(SerializationHelper.deserialize_by_tag(item_elem, "Linker"))
            elif tag == "MC-SUPPORT":
                setattr(obj, "mc_support", SerializationHelper.deserialize_by_tag(child, "McSupportData"))
            elif tag == "PROGRAMMING-LANGUAGE":
                setattr(obj, "programming_language", ProgramminglanguageEnum.deserialize(child))
            elif tag == "REQUIRED-ARTIFACTS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.required_artifacts.append(SerializationHelper.deserialize_by_tag(item_elem, "DependencyOnArtifact"))
            elif tag == "REQUIRED-GENERATOR-TOOLS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.required_generator_tools.append(SerializationHelper.deserialize_by_tag(item_elem, "DependencyOnArtifact"))
            elif tag == "RESOURCE-CONSUMPTION":
                setattr(obj, "resource_consumption", SerializationHelper.deserialize_by_tag(child, "ResourceConsumption"))
            elif tag == "SWC-BSW-MAPPING-REF":
                setattr(obj, "swc_bsw_mapping_ref", ARRef.deserialize(child))
            elif tag == "SW-VERSION":
                setattr(obj, "sw_version", SerializationHelper.deserialize_by_tag(child, "RevisionLabelString"))
            elif tag == "USED-CODE-GENERATOR":
                setattr(obj, "used_code_generator", SerializationHelper.deserialize_by_tag(child, "String"))
            elif tag == "VENDOR-ID":
                setattr(obj, "vendor_id", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class ImplementationBuilder(ARElementBuilder):
    """Builder for Implementation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Implementation = Implementation()


    def with_build_action_manifest(self, value: Optional[BuildActionManifest]) -> "ImplementationBuilder":
        """Set build_action_manifest attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.build_action_manifest = value
        return self

    def with_code_descriptors(self, items: list[Code]) -> "ImplementationBuilder":
        """Set code_descriptors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.code_descriptors = list(items) if items else []
        return self

    def with_compilers(self, items: list[Compiler]) -> "ImplementationBuilder":
        """Set compilers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.compilers = list(items) if items else []
        return self

    def with_generated_artifacts(self, items: list[DependencyOnArtifact]) -> "ImplementationBuilder":
        """Set generated_artifacts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.generated_artifacts = list(items) if items else []
        return self

    def with_hw_elements(self, items: list[HwElement]) -> "ImplementationBuilder":
        """Set hw_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_elements = list(items) if items else []
        return self

    def with_linkers(self, items: list[Linker]) -> "ImplementationBuilder":
        """Set linkers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.linkers = list(items) if items else []
        return self

    def with_mc_support(self, value: Optional[McSupportData]) -> "ImplementationBuilder":
        """Set mc_support attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mc_support = value
        return self

    def with_programming_language(self, value: Optional[ProgramminglanguageEnum]) -> "ImplementationBuilder":
        """Set programming_language attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.programming_language = value
        return self

    def with_required_artifacts(self, items: list[DependencyOnArtifact]) -> "ImplementationBuilder":
        """Set required_artifacts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_artifacts = list(items) if items else []
        return self

    def with_required_generator_tools(self, items: list[DependencyOnArtifact]) -> "ImplementationBuilder":
        """Set required_generator_tools list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_generator_tools = list(items) if items else []
        return self

    def with_resource_consumption(self, value: Optional[ResourceConsumption]) -> "ImplementationBuilder":
        """Set resource_consumption attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resource_consumption = value
        return self

    def with_swc_bsw_mapping(self, value: Optional[SwcBswMapping]) -> "ImplementationBuilder":
        """Set swc_bsw_mapping attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.swc_bsw_mapping = value
        return self

    def with_sw_version(self, value: Optional[RevisionLabelString]) -> "ImplementationBuilder":
        """Set sw_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sw_version = value
        return self

    def with_used_code_generator(self, value: Optional[String]) -> "ImplementationBuilder":
        """Set used_code_generator attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.used_code_generator = value
        return self

    def with_vendor_id(self, value: Optional[PositiveInteger]) -> "ImplementationBuilder":
        """Set vendor_id attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vendor_id = value
        return self


    def add_code_descriptor(self, item: Code) -> "ImplementationBuilder":
        """Add a single item to code_descriptors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.code_descriptors.append(item)
        return self

    def clear_code_descriptors(self) -> "ImplementationBuilder":
        """Clear all items from code_descriptors list.

        Returns:
            self for method chaining
        """
        self._obj.code_descriptors = []
        return self

    def add_compiler(self, item: Compiler) -> "ImplementationBuilder":
        """Add a single item to compilers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.compilers.append(item)
        return self

    def clear_compilers(self) -> "ImplementationBuilder":
        """Clear all items from compilers list.

        Returns:
            self for method chaining
        """
        self._obj.compilers = []
        return self

    def add_generated_artifact(self, item: DependencyOnArtifact) -> "ImplementationBuilder":
        """Add a single item to generated_artifacts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.generated_artifacts.append(item)
        return self

    def clear_generated_artifacts(self) -> "ImplementationBuilder":
        """Clear all items from generated_artifacts list.

        Returns:
            self for method chaining
        """
        self._obj.generated_artifacts = []
        return self

    def add_hw_element(self, item: HwElement) -> "ImplementationBuilder":
        """Add a single item to hw_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_elements.append(item)
        return self

    def clear_hw_elements(self) -> "ImplementationBuilder":
        """Clear all items from hw_elements list.

        Returns:
            self for method chaining
        """
        self._obj.hw_elements = []
        return self

    def add_linker(self, item: Linker) -> "ImplementationBuilder":
        """Add a single item to linkers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.linkers.append(item)
        return self

    def clear_linkers(self) -> "ImplementationBuilder":
        """Clear all items from linkers list.

        Returns:
            self for method chaining
        """
        self._obj.linkers = []
        return self

    def add_required_artifact(self, item: DependencyOnArtifact) -> "ImplementationBuilder":
        """Add a single item to required_artifacts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_artifacts.append(item)
        return self

    def clear_required_artifacts(self) -> "ImplementationBuilder":
        """Clear all items from required_artifacts list.

        Returns:
            self for method chaining
        """
        self._obj.required_artifacts = []
        return self

    def add_required_generator_tool(self, item: DependencyOnArtifact) -> "ImplementationBuilder":
        """Add a single item to required_generator_tools list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_generator_tools.append(item)
        return self

    def clear_required_generator_tools(self) -> "ImplementationBuilder":
        """Clear all items from required_generator_tools list.

        Returns:
            self for method chaining
        """
        self._obj.required_generator_tools = []
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
    def build(self) -> Implementation:
        """Build and return the Implementation instance (abstract)."""
        raise NotImplementedError