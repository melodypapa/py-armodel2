"""BswImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 120)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 290)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 972)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 207)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 425)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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


class BswImplementation(Implementation):
    """AUTOSAR BswImplementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_release: Optional[RevisionLabelString]
    behavior_ref: Optional[ARRef]
    preconfigured_refs: list[Any]
    recommended_refs: list[Any]
    vendor_api_infix: Optional[Identifier]
    vendor_specific_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BswImplementation."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.behavior_ref: Optional[ARRef] = None
        self.preconfigured_refs: list[Any] = []
        self.recommended_refs: list[Any] = []
        self.vendor_api_infix: Optional[Identifier] = None
        self.vendor_specific_refs: list[ARRef] = []

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

        # Serialize ar_release
        if self.ar_release is not None:
            serialized = SerializationHelper.serialize_item(self.ar_release, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AR-RELEASE")
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

        # Serialize preconfigured_refs (list to container "PRECONFIGURED-REFS")
        if self.preconfigured_refs:
            wrapper = ET.Element("PRECONFIGURED-REFS")
            for item in self.preconfigured_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("PRECONFIGURED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize recommended_refs (list to container "RECOMMENDED-REFS")
        if self.recommended_refs:
            wrapper = ET.Element("RECOMMENDED-REFS")
            for item in self.recommended_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("RECOMMENDED-REF")
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

        # Serialize vendor_specific_refs (list to container "VENDOR-SPECIFIC-REFS")
        if self.vendor_specific_refs:
            wrapper = ET.Element("VENDOR-SPECIFIC-REFS")
            for item in self.vendor_specific_refs:
                serialized = SerializationHelper.serialize_item(item, "EcucModuleDef")
                if serialized is not None:
                    child_elem = ET.Element("VENDOR-SPECIFIC-REF")
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

        # Parse ar_release
        child = SerializationHelper.find_child_element(element, "AR-RELEASE")
        if child is not None:
            ar_release_value = child.text
            obj.ar_release = ar_release_value

        # Parse behavior_ref
        child = SerializationHelper.find_child_element(element, "BEHAVIOR-REF")
        if child is not None:
            behavior_ref_value = ARRef.deserialize(child)
            obj.behavior_ref = behavior_ref_value

        # Parse preconfigured_refs (list from container "PRECONFIGURED-REFS")
        obj.preconfigured_refs = []
        container = SerializationHelper.find_child_element(element, "PRECONFIGURED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.preconfigured_refs.append(child_value)

        # Parse recommended_refs (list from container "RECOMMENDED-REFS")
        obj.recommended_refs = []
        container = SerializationHelper.find_child_element(element, "RECOMMENDED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.recommended_refs.append(child_value)

        # Parse vendor_api_infix
        child = SerializationHelper.find_child_element(element, "VENDOR-API-INFIX")
        if child is not None:
            vendor_api_infix_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.vendor_api_infix = vendor_api_infix_value

        # Parse vendor_specific_refs (list from container "VENDOR-SPECIFIC-REFS")
        obj.vendor_specific_refs = []
        container = SerializationHelper.find_child_element(element, "VENDOR-SPECIFIC-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.vendor_specific_refs.append(child_value)

        return obj



class BswImplementationBuilder:
    """Builder for BswImplementation with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        pass
        self._obj: BswImplementation = BswImplementation()


    def with_short_name(self, value: Identifier) -> "BswImplementationBuilder":
        """Set short_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.short_name = value
        return self

    def with_short_name_fragments(self, items: list[ShortNameFragment]) -> "BswImplementationBuilder":
        """Set short_name_fragments list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = list(items) if items else []
        return self

    def with_long_name(self, value: Optional[MultilanguageLongName]) -> "BswImplementationBuilder":
        """Set long_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.long_name = value
        return self

    def with_admin_data(self, value: Optional[AdminData]) -> "BswImplementationBuilder":
        """Set admin_data attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.admin_data = value
        return self

    def with_annotations(self, items: list[Annotation]) -> "BswImplementationBuilder":
        """Set annotations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.annotations = list(items) if items else []
        return self

    def with_desc(self, value: Optional[MultiLanguageOverviewParagraph]) -> "BswImplementationBuilder":
        """Set desc attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.desc = value
        return self

    def with_category(self, value: Optional[CategoryString]) -> "BswImplementationBuilder":
        """Set category attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.category = value
        return self

    def with_introduction(self, value: Optional[DocumentationBlock]) -> "BswImplementationBuilder":
        """Set introduction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.introduction = value
        return self

    def with_uuid(self, value: Optional[String]) -> "BswImplementationBuilder":
        """Set uuid attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.uuid = value
        return self

    def with_build_action_manifest(self, value: Optional[BuildActionManifest]) -> "BswImplementationBuilder":
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

    def with_code_descriptors(self, items: list[Code]) -> "BswImplementationBuilder":
        """Set code_descriptors list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.code_descriptors = list(items) if items else []
        return self

    def with_compilers(self, items: list[Compiler]) -> "BswImplementationBuilder":
        """Set compilers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.compilers = list(items) if items else []
        return self

    def with_generateds(self, items: list[DependencyOnArtifact]) -> "BswImplementationBuilder":
        """Set generateds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.generateds = list(items) if items else []
        return self

    def with_hw_elements(self, items: list[HwElement]) -> "BswImplementationBuilder":
        """Set hw_elements list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.hw_elements = list(items) if items else []
        return self

    def with_linkers(self, items: list[Linker]) -> "BswImplementationBuilder":
        """Set linkers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.linkers = list(items) if items else []
        return self

    def with_mc_support(self, value: Optional[McSupportData]) -> "BswImplementationBuilder":
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

    def with_programming(self, value: Optional[ProgramminglanguageEnum]) -> "BswImplementationBuilder":
        """Set programming attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.programming = value
        return self

    def with_required_artifacts(self, items: list[DependencyOnArtifact]) -> "BswImplementationBuilder":
        """Set required_artifacts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_artifacts = list(items) if items else []
        return self

    def with_requireds(self, items: list[DependencyOnArtifact]) -> "BswImplementationBuilder":
        """Set requireds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.requireds = list(items) if items else []
        return self

    def with_resource(self, value: Optional[ResourceConsumption]) -> "BswImplementationBuilder":
        """Set resource attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.resource = value
        return self

    def with_swc_bsw(self, value: Optional[SwcBswMapping]) -> "BswImplementationBuilder":
        """Set swc_bsw attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.swc_bsw = value
        return self

    def with_sw_version(self, value: Optional[RevisionLabelString]) -> "BswImplementationBuilder":
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

    def with_used_code_generator(self, value: Optional[String]) -> "BswImplementationBuilder":
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

    def with_vendor_id(self, value: Optional[PositiveInteger]) -> "BswImplementationBuilder":
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

    def with_ar_release(self, value: Optional[RevisionLabelString]) -> "BswImplementationBuilder":
        """Set ar_release attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ar_release = value
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

    def with_preconfigureds(self, items: list[any (EcucModule)]) -> "BswImplementationBuilder":
        """Set preconfigureds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.preconfigureds = list(items) if items else []
        return self

    def with_recommendeds(self, items: list[any (EcucModule)]) -> "BswImplementationBuilder":
        """Set recommendeds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.recommendeds = list(items) if items else []
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

    def with_vendor_specifics(self, items: list[EcucModuleDef]) -> "BswImplementationBuilder":
        """Set vendor_specifics list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.vendor_specifics = list(items) if items else []
        return self


    def add_short_name_fragment(self, item: ShortNameFragment) -> "BswImplementationBuilder":
        """Add a single item to short_name_fragments list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments.append(item)
        return self

    def clear_short_name_fragments(self) -> "BswImplementationBuilder":
        """Clear all items from short_name_fragments list.

        Returns:
            self for method chaining
        """
        self._obj.short_name_fragments = []
        return self

    def add_annotation(self, item: Annotation) -> "BswImplementationBuilder":
        """Add a single item to annotations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.annotations.append(item)
        return self

    def clear_annotations(self) -> "BswImplementationBuilder":
        """Clear all items from annotations list.

        Returns:
            self for method chaining
        """
        self._obj.annotations = []
        return self

    def add_code_descriptor(self, item: Code) -> "BswImplementationBuilder":
        """Add a single item to code_descriptors list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.code_descriptors.append(item)
        return self

    def clear_code_descriptors(self) -> "BswImplementationBuilder":
        """Clear all items from code_descriptors list.

        Returns:
            self for method chaining
        """
        self._obj.code_descriptors = []
        return self

    def add_compiler(self, item: Compiler) -> "BswImplementationBuilder":
        """Add a single item to compilers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.compilers.append(item)
        return self

    def clear_compilers(self) -> "BswImplementationBuilder":
        """Clear all items from compilers list.

        Returns:
            self for method chaining
        """
        self._obj.compilers = []
        return self

    def add_generated(self, item: DependencyOnArtifact) -> "BswImplementationBuilder":
        """Add a single item to generateds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.generateds.append(item)
        return self

    def clear_generateds(self) -> "BswImplementationBuilder":
        """Clear all items from generateds list.

        Returns:
            self for method chaining
        """
        self._obj.generateds = []
        return self

    def add_hw_element(self, item: HwElement) -> "BswImplementationBuilder":
        """Add a single item to hw_elements list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.hw_elements.append(item)
        return self

    def clear_hw_elements(self) -> "BswImplementationBuilder":
        """Clear all items from hw_elements list.

        Returns:
            self for method chaining
        """
        self._obj.hw_elements = []
        return self

    def add_linker(self, item: Linker) -> "BswImplementationBuilder":
        """Add a single item to linkers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.linkers.append(item)
        return self

    def clear_linkers(self) -> "BswImplementationBuilder":
        """Clear all items from linkers list.

        Returns:
            self for method chaining
        """
        self._obj.linkers = []
        return self

    def add_required_artifact(self, item: DependencyOnArtifact) -> "BswImplementationBuilder":
        """Add a single item to required_artifacts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_artifacts.append(item)
        return self

    def clear_required_artifacts(self) -> "BswImplementationBuilder":
        """Clear all items from required_artifacts list.

        Returns:
            self for method chaining
        """
        self._obj.required_artifacts = []
        return self

    def add_required(self, item: DependencyOnArtifact) -> "BswImplementationBuilder":
        """Add a single item to requireds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.requireds.append(item)
        return self

    def clear_requireds(self) -> "BswImplementationBuilder":
        """Clear all items from requireds list.

        Returns:
            self for method chaining
        """
        self._obj.requireds = []
        return self

    def add_preconfigured(self, item: any (EcucModule)) -> "BswImplementationBuilder":
        """Add a single item to preconfigureds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.preconfigureds.append(item)
        return self

    def clear_preconfigureds(self) -> "BswImplementationBuilder":
        """Clear all items from preconfigureds list.

        Returns:
            self for method chaining
        """
        self._obj.preconfigureds = []
        return self

    def add_recommended(self, item: any (EcucModule)) -> "BswImplementationBuilder":
        """Add a single item to recommendeds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.recommendeds.append(item)
        return self

    def clear_recommendeds(self) -> "BswImplementationBuilder":
        """Clear all items from recommendeds list.

        Returns:
            self for method chaining
        """
        self._obj.recommendeds = []
        return self

    def add_vendor_specific(self, item: EcucModuleDef) -> "BswImplementationBuilder":
        """Add a single item to vendor_specifics list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.vendor_specifics.append(item)
        return self

    def clear_vendor_specifics(self) -> "BswImplementationBuilder":
        """Clear all items from vendor_specifics list.

        Returns:
            self for method chaining
        """
        self._obj.vendor_specifics = []
        return self


    @staticmethod
    def _coerce_to_int(value: Any) -> int:
        """Coerce value to int.

        Args:
            value: Value to coerce

        Returns:
            Integer value

        Raises:
            ValueError: If value cannot be coerced to int
        """
        if isinstance(value, int):
            return value
        if isinstance(value, str) and value.isdigit():
            return int(value)
        if isinstance(value, float):
            return int(value)
        if isinstance(value, bool):
            return int(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to int: {value}")

    @staticmethod
    def _coerce_to_float(value: Any) -> float:
        """Coerce value to float.

        Args:
            value: Value to coerce

        Returns:
            Float value

        Raises:
            ValueError: If value cannot be coerced to float
        """
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                pass
        raise ValueError(f"Cannot coerce {type(value).__name__} to float: {value}")

    @staticmethod
    def _coerce_to_bool(value: Any) -> bool:
        """Coerce value to bool.

        Args:
            value: Value to coerce

        Returns:
            Boolean value

        Raises:
            ValueError: If value cannot be coerced to bool
        """
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            return bool(value)
        if isinstance(value, str):
            if value.lower() in ("true", "1", "yes"):
                return True
            if value.lower() in ("false", "0", "no"):
                return False
        raise ValueError(f"Cannot coerce {type(value).__name__} to bool: {value}")

    @staticmethod
    def _coerce_to_str(value: Any) -> str:
        """Coerce value to str.

        Args:
            value: Value to coerce

        Returns:
            String value
        """
        return str(value)


    @staticmethod
    def _coerce_to_list(value: Any, item_type: str) -> list:
        """Coerce value to list.

        Args:
            value: Value to coerce
            item_type: Expected item type (for error messages)

        Returns:
            List value

        Raises:
            ValueError: If value cannot be coerced to list
        """
        if isinstance(value, list):
            return value
        if isinstance(value, tuple):
            return list(value)
        raise ValueError(f"Cannot coerce {type(value).__name__} to list[{item_type}]: {value}")


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